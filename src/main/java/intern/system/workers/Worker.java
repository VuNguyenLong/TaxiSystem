package intern.system.workers;

import java.io.FileReader;
import java.io.IOException;
import java.sql.SQLException;
import java.util.Properties;

import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.api.kafka.KafkaConnection;

public abstract class Worker {
	Properties prop;

	public Worker(String properties) throws IOException
	{
		prop = new Properties();
		prop.load(new FileReader(properties));
	}

	public abstract void DoWork() throws InterruptedException, SQLException;
}
