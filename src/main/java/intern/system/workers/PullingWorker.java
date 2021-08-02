package intern.system.workers;

import com.google.protobuf.ByteString;
import intern.system.loadbalancers.LoadBalancer;
import intern.system.loadbalancers.RoundRobin;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import java.io.IOException;

import intern.system.messages.Messages.*;

public class PullingWorker extends Worker {
	LoadBalancer balancer;
	public PullingWorker(String properties) throws IOException {
		super(properties);
		balancer = new RoundRobin(1, "db");
	}

	@Override
	public void DoWork(){
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("receive_topic"));

		int select_batch_size = Integer.parseInt(this.prop.getProperty("select_batch_size"));
		int update_batch_size = Integer.parseInt(this.prop.getProperty("update_batch_size"));
		Request.Builder select_builder = Request.newBuilder();
		Request.Builder update_builder = Request.newBuilder();

		for (ConsumerRecord<String, ByteString> record:records)
		{
			try
			{
				Message message = Message.parseFrom(record.value());
				if (message.getType() == Message.Type.SELECT)
				{
					Command command = Command.newBuilder()
							.setClient(message.getClient())
							.build();
					select_builder.addCommands(command);

					if (select_builder.getCommandsCount() >= select_batch_size)
					{
						balancer.send(select_builder.build().toByteString());
						select_builder = Request.newBuilder();
					}
				}
				else if (message.getType() == Message.Type.UPDATE)
				{
					Command command = Command.newBuilder()
							.setDriver(message.getDriver())
							.build();
					update_builder.addCommands(command);

					if (update_builder.getCommandsCount() >= update_batch_size)
					{
						balancer.send(update_builder.build().toByteString());
						update_builder = Request.newBuilder();
					}
				}
			}
			catch (Exception e)
			{
				System.out.println(e.getMessage());
			}
		}
		if (select_builder.getCommandsCount() > 0)
			balancer.send(select_builder.build().toByteString());

		if (update_builder.getCommandsCount() > 0)
			balancer.send(update_builder.build().toByteString());
	}
}
