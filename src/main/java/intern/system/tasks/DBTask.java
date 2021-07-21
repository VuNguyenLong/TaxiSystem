package intern.system.tasks;

import intern.system.api.kafka.KafkaConnection;
import intern.system.messages.Messages;
import java.sql.*;

public class DBTask implements Runnable{
	Messages.Command comm;
	KafkaConnection conn;
	String topic;

	public DBTask(Messages.Command comm, KafkaConnection conn, String topic)
	{
		this.comm = comm;
		this.conn = conn;
		this.topic = topic;
	}

	@Override
	public void run() {
		// query part

		Messages.Locations.Builder builder = Messages.Locations.newBuilder();
		builder.addDrivers(Messages.Driver.newBuilder().setId(1).setLat(10).setLong(10));

		Messages.Response response = Messages.Response.newBuilder()
				.setClientId(this.comm.getClient().getId())
				.setResponse(builder.build()).build();
		this.conn.send(response.toByteString(), this.topic);
	}
}
