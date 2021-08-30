package intern.system.api.postgre;

import intern.system.messages.Messages;

import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.util.Arrays;
import java.util.Properties;

public class PostgreQuery {
	Properties properties;
	Connection conn;
	String sql = "insert into Locations(driver_id, long, lat, hash_0, available, vehicle_type) values (?, ?, ?, ?, ?, ?)";

	public PostgreQuery() throws IOException, SQLException {
		properties = new Properties();
		properties.load(new FileReader("config/db.properties"));
		conn = DriverManager.getConnection(properties.getProperty("url"), this.properties);
	}

	public Messages.Response Update(Messages.Request request) throws SQLException
	{
		if (request.getCommandsCount() <= 0)
			return null;

		PreparedStatement stmt = conn.prepareStatement(this.sql);
		conn.setAutoCommit(false);
		for (Messages.Command command : request.getCommandsList())
		{
			stmt.setLong(1, command.getDriver().getId());
			stmt.setFloat(2, command.getDriver().getLong());
			stmt.setFloat(3, command.getDriver().getLat());
			stmt.setLong(4, command.getDriver().getHash(0));
			stmt.setBoolean(5, command.getDriver().getAvailable());
			stmt.setInt(6, command.getDriver().getVehicleType());
			stmt.addBatch();
		}

		stmt.executeLargeBatch();
		conn.commit();
		conn.setAutoCommit(true);
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
						"from Locations l inner join driver_table_view\n" +
						"on l.driver_id = driver_table_view.driver_id\n" +
						"where l.time_stamp = driver_table_view.max_time and hash_0 = %d" +
						"and available and vehicle_type = %d;",
						command.getClient().getHash(0),
						command.getClient().getVehicleType()
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
						"from Locations l inner join driver_table_view\n" +
						"on l.driver_id = driver_table_view.driver_id\n" +
						"where l.time_stamp = driver_table_view.max_time and hash_0 = %d" +
						"and available and vehicle_type = %d;",
						command.getHash(0),
						command.getVehicleType()
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

	public long Refresh(long n) throws SQLException
	{
		Statement stmt = conn.createStatement();
		ResultSet result = stmt.executeQuery(String.format("select update_driver_view(%d)", n));
		long i = 0;
		while (result.next())
			i = result.getLong("update_driver_view");

		result.close();
		stmt.close();

		return i;
	}

	public void close() throws SQLException
	{
		this.conn.close();
	}
}
