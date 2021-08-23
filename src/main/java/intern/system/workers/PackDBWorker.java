package intern.system.workers;

import com.google.protobuf.ByteString;
import intern.system.api.postgre.PostgreQuery;
import intern.system.messages.Messages.Command;
import intern.system.messages.Messages.Message;
import intern.system.messages.Messages.Request;
import intern.system.tasks.QueryTask;
import intern.system.tasks.UpdateTask;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import java.io.IOException;
import java.sql.SQLException;
import java.time.ZonedDateTime;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class PackDBWorker extends OnlineWorker {
	ThreadPoolExecutor pool;
	PostgreQuery db_connector;

	public PackDBWorker(String properties) throws IOException, SQLException {
		super(properties);
		db_connector = new PostgreQuery();
		pool = (ThreadPoolExecutor) Executors.newFixedThreadPool(Integer.parseInt(this.prop.getProperty("n_threads")));
	}

	@Override
	public void DoWork()
	{
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("receive_topic"));

		int update_batch_size = Integer.parseInt(this.prop.getProperty("update_batch_size"));
		Request.Builder update_builder = Request.newBuilder();

		for (ConsumerRecord<String, ByteString> record:records)
		{
			try
			{
				Message message = Message.parseFrom(record.value());
				if (message.getType() == Message.Type.SELECT)
					pool.submit(new QueryTask(message.getClient(), conn, db_connector, prop.getProperty("mode")));
				else
				{
					Command command = Command.newBuilder()
							.setDriver(message.getDriver())
							.build();
					update_builder.addCommands(command);

					if (update_builder.getCommandsCount() >= update_batch_size)
					{
						pool.submit(new UpdateTask(update_builder.build(), conn, db_connector));
						update_builder = Request.newBuilder();
					}

					System.out.println(message.getDriver().toString());
				}
			}
			catch (Exception e)
			{
				System.out.println(e.getMessage());
			}
		}

		try
		{
			pool.submit(new UpdateTask(update_builder.build(), conn, db_connector));
		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
}
