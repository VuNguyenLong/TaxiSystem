package intern.system.workers;

import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.api.kafka.KafkaConnection;

import java.io.IOException;

public abstract class OnlineWorker extends Worker{
	KafkaConnection conn;

	public OnlineWorker(String properties) throws IOException {
		super(properties);
		conn = new KafkaConnection();
	}
}
