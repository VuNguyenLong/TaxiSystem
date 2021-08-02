package intern.system.loadbalancers;

import com.google.protobuf.ByteString;
import intern.system.api.kafka.KafkaConnection;

import java.io.IOException;

public abstract class LoadBalancer {
	public KafkaConnection conn;
	public String prefix;

	protected int counter = 0;
	protected final int size;

	public LoadBalancer(int size, String prefix) throws IOException
	{
		this.conn = new KafkaConnection();
		this.size = size;
		this.prefix = prefix;
	}

	public abstract void send(ByteString data);
}
