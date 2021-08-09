package intern.system.workers;

import intern.system.api.postgre.PostgreQuery;

import java.io.IOException;
import java.sql.SQLException;

public class UpdateWorker extends Worker{
	PostgreQuery db_connector;

	public UpdateWorker(String properties) throws IOException, SQLException {
		super(properties);

		db_connector = new PostgreQuery();
	}

	@Override
	public void DoWork() throws SQLException, InterruptedException {
		long i = this.db_connector.Refresh(Long.parseLong(this.prop.getProperty("offset")));
		this.prop.setProperty("offset", String.valueOf(i));
		Thread.sleep(Integer.parseInt(this.prop.getProperty("delay")));
	}
}
