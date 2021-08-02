package intern.system.workers;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.messages.Messages.*;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;

public class PackingWorker extends Worker {
	public PackingWorker(String properties) throws IOException {
		super(properties);
	}

	@Override
	public void DoWork(){
		ConsumerRecords<String, ByteString> records = this.conn.receive(this.prop.getProperty("response_topic"));
		records.forEach(record -> {
			try
			{
				Response response = Response.parseFrom(record.value());
				String client_topic = DigestUtils.sha256Hex(String.valueOf(response.getClientId()));
				System.out.println("Client " + response.getClientId());
				System.out.println(response);

				//this.conn.GetOrCreate(client_topic);
				this.conn.send(response.getResponse().toByteString(), client_topic);
				//this.conn.send(response.getResponse().toByteString(), String.valueOf(response.getClientId()));
			}
			catch (Exception e)
			{
				System.out.println(e.getMessage());
			}
		});
	}
}
