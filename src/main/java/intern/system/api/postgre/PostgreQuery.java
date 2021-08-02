package intern.system.api.postgre;

import intern.system.messages.Messages;

import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.util.Properties;

public class PostgreQuery {
	Properties properties;
	Connection conn;

	public PostgreQuery() throws IOException, SQLException {
		properties = new Properties();
		properties.load(new FileReader("config/db.properties"));
		conn = DriverManager.getConnection(properties.getProperty("url"), this.properties);
	}

	public Messages.Response Update(Messages.Request request) throws SQLException
	{
		Statement stmt = conn.createStatement();
		for (Messages.Command command : request.getCommandsList())
		{
			stmt.addBatch(
					String.format(
							"insert into Locations(driver_id, long, lat, hash_0) " +
									"values(%d, %f, %f, %d);",
							command.getDriver().getId(),
							command.getDriver().getLong(),
							command.getDriver().getLat(),
							command.getDriver().getHash(0)
					)
			);
		}
		stmt.executeBatch();
		stmt.close();

		return Messages.Response.newBuilder()
				.setTimestamp(String.valueOf(ZonedDateTime.now().toInstant().toEpochMilli()))
				.build();
	}

	public Messages.Response Query(Messages.Command command) throws SQLException
	{
		Messages.Response.Builder builder = Messages.Response.newBuilder();
		Messages.Locations.Builder loc_builder = Messages.Locations.newBuilder();

		Statement stmt = conn.createStatement();
		ResultSet result = stmt.executeQuery(
				String.format(
						"select l.driver_id, l.long, l.lat\n" +
						"from Locations l inner join driver_view\n" +
						"on l.driver_id = driver_view.driver_id\n" +
						"where l.time_stamp = driver_view.max_time and hash_0 = %d;",
						command.getClient().getHash(0)
				)
		);

		while (result.next())
		{
			loc_builder.addDrivers(Messages.Driver.newBuilder()
					.setId(result.getInt("driver_id"))
					.setLong(result.getFloat("long"))
					.setLat(result.getFloat("lat"))
			);
		}
		builder.setClientId(command.getClient().getId());
		builder.setResponse(loc_builder.build());
		builder.setTimestamp(String.valueOf(ZonedDateTime.now().toInstant().toEpochMilli()));
		stmt.close();

		return builder.build();
	}

	public Messages.Response Query(Messages.Client command) throws SQLException
	{
		Messages.Response.Builder builder = Messages.Response.newBuilder();
		Messages.Locations.Builder loc_builder = Messages.Locations.newBuilder();

		Statement stmt = conn.createStatement();
		ResultSet result = stmt.executeQuery(
				String.format(
						"select l.driver_id, l.long, l.lat\n" +
								"from Locations l inner join driver_view\n" +
								"on l.driver_id = driver_view.driver_id\n" +
								"where l.time_stamp = driver_view.max_time and hash_0 = %d;",
						command.getHash(0)
				)
		);

		while (result.next())
		{
			loc_builder.addDrivers(Messages.Driver.newBuilder()
					.setId(result.getInt("driver_id"))
					.setLong(result.getFloat("long"))
					.setLat(result.getFloat("lat"))
			);
		}
		builder.setClientId(command.getId());
		builder.setResponse(loc_builder.build());
		builder.setTimestamp(String.valueOf(ZonedDateTime.now().toInstant().toEpochMilli()));
		stmt.close();

		return builder.build();
	}

	public void close() throws SQLException
	{
		this.conn.close();
	}
}
