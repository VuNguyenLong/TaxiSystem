package intern.system.loadbalancers;

import com.google.protobuf.ByteString;

import java.io.IOException;

public class RoundRobin extends LoadBalancer{
	public RoundRobin(int size, String prefix) throws IOException {
		super(size, prefix);
	}

	@Override
	public void send(ByteString data) {
		conn.send(data, this.prefix + counter);
		counter = (counter + 1) % size;
	}
}
