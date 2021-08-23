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

	boolean is_benchmark = false;

	public QueryTask(Messages.Client comm, KafkaConnection conn, PostgreQuery db_connector, String mode)
	{
		this.comm = comm;
		this.conn = conn;
		this.db_connector = db_connector;

		if (mode.equals("benchmark"))
			is_benchmark = true;
	}

	@Override
	public void run() {
		try
		{
			String client_topic = DigestUtils.sha256Hex(String.valueOf(comm.getId()));
			if (is_benchmark)
				client_topic = "benchmark";
			this.conn.send(db_connector.Query(comm).toByteString(), client_topic);
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
