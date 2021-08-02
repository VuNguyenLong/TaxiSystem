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

	public UpdateTask(Messages.Request comm, KafkaConnection conn) throws SQLException, IOException {
		this.comm = comm;
		this.conn = conn;
		db_connector = new PostgreQuery();
	}

	@Override
	public void run() {
		try
		{
			db_connector.Update(this.comm);
			this.db_connector.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
