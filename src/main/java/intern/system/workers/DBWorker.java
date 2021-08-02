package intern.system.workers;

import com.google.protobuf.ByteString;
import intern.system.api.postgre.PostgreQuery;
import intern.system.loadbalancers.RoundRobin;
import intern.system.tasks.DBTask;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import java.io.IOException;
import java.sql.*;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import intern.system.messages.Messages.*;

public class DBWorker extends Worker {
	ThreadPoolExecutor pool;
	PostgreQuery db_connector;
	RoundRobin balancer;

	public DBWorker(String properties) throws IOException, SQLException {
		super(properties);
		db_connector = new PostgreQuery();
		pool = (ThreadPoolExecutor) Executors.newFixedThreadPool(Integer.parseInt(this.prop.getProperty("n_threads")));
	}

	@Override
	public void DoWork() {
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("receive_topic"));
		records.forEach(record -> {
			try
			{
				Request request = Request.parseFrom(record.value());
				if (request.getType() == Request.Type.SELECT)
				{
					for (Command command : request.getCommandsList())
					{
						pool.submit(new DBTask(command, this.conn));
					}
				}
				else if (request.getType() == Request.Type.UPDATE)
				{
					db_connector.Update(request);
				}
			}
			catch (Exception e)
			{
				System.out.println(e.getMessage());
			}
		});
	}
}
