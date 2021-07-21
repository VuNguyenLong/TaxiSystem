package intern.system.workers;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import java.io.IOException;

import intern.system.messages.Messages.*;

public class PullingWorker extends Worker {
	public PullingWorker(String properties, String kafka_properties) throws IOException {
		super(properties, kafka_properties);
	}

	@Override
	public void DoWork() throws InvalidProtocolBufferException {
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("receive_topic"));

		int select_batch_size = Integer.parseInt(this.prop.getProperty("select_batch_size"));
		Request.Builder select_builder = Request.newBuilder();
		Request.Builder update_builder = Request.newBuilder();

		for (ConsumerRecord<String, ByteString> record:records)
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
					this.conn.send(select_builder.build().toByteString(), this.prop.getProperty("send_topic"));
					select_builder = Request.newBuilder();
				}
			}
			else if (message.getType() == Message.Type.UPDATE)
			{
				Command command = Command.newBuilder()
						.setDriver(message.getDriver())
						.build();
				update_builder.addCommands(command);
			}
		}

		this.conn.send(select_builder.build().toByteString(), this.prop.getProperty("send_topic"));
		this.conn.send(update_builder.build().toByteString(), this.prop.getProperty("send_topic"));
	}
}
