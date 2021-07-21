package intern.system.workers;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.api.kafka.KafkaConnection;

public abstract class Worker {
	Properties prop;
	KafkaConnection conn;

	public Worker(String properties, String kafka_properties) throws IOException
	{
		prop = new Properties();
		prop.load(new FileReader(properties));

		conn = new KafkaConnection(kafka_properties);
	}

	public abstract void DoWork() throws InvalidProtocolBufferException;
}
