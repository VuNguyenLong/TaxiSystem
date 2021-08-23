package intern.system.workers;

import intern.system.api.postgre.PostgreQuery;

import java.io.FileWriter;
import java.io.IOException;
import java.sql.SQLException;

public class UpdateWorker extends Worker{
	PostgreQuery db_connector;
	String properties_file;

	public UpdateWorker(String properties) throws IOException, SQLException {
		super(properties);
		this.properties_file = properties;
		db_connector = new PostgreQuery();
	}

	@Override
	public void DoWork() throws SQLException, InterruptedException {
		long offset = Long.parseLong(this.prop.getProperty("offset"));
		long i = this.db_connector.Refresh(offset);
		this.prop.setProperty("offset", String.valueOf(offset + i));
		Thread.sleep(Integer.parseInt(this.prop.getProperty("delay")));

		try
		{
			FileWriter file = new FileWriter(this.properties_file);
			this.prop.store(file, "");
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}
