package intern.system.workers;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.tasks.DBTask;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import java.io.IOException;
import java.sql.*;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import intern.system.messages.Messages.*;

public class DBWorker extends Worker {
	ThreadPoolExecutor pool;

	public DBWorker(String properties, String kafka_properties) throws IOException {
		super(properties, kafka_properties);

		pool = (ThreadPoolExecutor) Executors.newFixedThreadPool(Integer.parseInt(this.prop.getProperty("n_threads")));
	}

	@Override
	public void DoWork() throws InvalidProtocolBufferException {
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("receive_topic"));
		records.forEach(record -> {
			try
			{
				Request request = Request.parseFrom(record.value());
				System.out.println(request);
				if (request.getType() == Request.Type.SELECT)
				{
					for (Command command : request.getCommandsList())
					{
						pool.submit(new DBTask(command, this.conn, this.prop.getProperty("send_topic")));
					}
				}
				else if (request.getType() == Request.Type.UPDATE)
				{
					// do some update
				}
			}
			catch (Exception e)
			{
				System.out.println(e.getMessage());
			}
		});
	}
}
