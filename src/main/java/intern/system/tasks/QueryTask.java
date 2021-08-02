package intern.system.tasks;

import intern.system.api.kafka.KafkaConnection;
import intern.system.api.postgre.PostgreQuery;
import intern.system.messages.Messages;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.sql.SQLException;

public class QueryTask implements Runnable {
	Messages.Client comm;
	PostgreQuery db_connector;
	KafkaConnection conn;

	public QueryTask(Messages.Client comm, KafkaConnection conn) throws SQLException, IOException {
		this.comm = comm;
		this.conn = conn;
		db_connector = new PostgreQuery();
	}

	@Override
	public void run() {
		try
		{
			String client_topic = DigestUtils.sha256Hex(String.valueOf(comm.getId()));
			this.conn.send(db_connector.Query(comm).toByteString(), "benchmark");
			this.db_connector.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
