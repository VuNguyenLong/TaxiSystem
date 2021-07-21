package intern.system.loadbalancers;

import com.google.protobuf.ByteString;
import intern.system.api.kafka.KafkaConnection;

import java.io.IOException;

public class RoundRobin {
	public KafkaConnection conn;

	private int counter = 0;
	private final int size;
	public RoundRobin(String kafka_properties, int size) throws IOException {
		this.conn = new KafkaConnection(kafka_properties);
		this.size = size;
	}

	public void send(ByteString data)
	{
		conn.send(data, "pulling" + counter);
		counter = (counter + 1) % size;
	}
}
