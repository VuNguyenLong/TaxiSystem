package intern.system.tasks;

import intern.system.api.kafka.KafkaConnection;
import intern.system.api.postgre.PostgreQuery;
import intern.system.messages.Messages;

import java.io.IOException;
import java.sql.SQLException;

public class UpdateTask implements Runnable{
	Messages.Request comm;
	PostgreQuery db_connector;
	KafkaConnection conn;

	public UpdateTask(Messages.Request comm, KafkaConnection conn, PostgreQuery db_connector) throws SQLException, IOException {
		this.comm = comm;
		this.conn = conn;
		this.db_connector = db_connector;
	}

	@Override
	public void run() {
		try
		{
			this.db_connector.Update(this.comm);
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
