package intern.system.workers;

import java.io.IOException;
import java.sql.SQLException;

public class WorkerRunner {
	public static void main(String[] args) throws IOException, SQLException, InterruptedException {
		Worker worker;
		switch (args[0])
		{
			case "pulling": worker = new PullingWorker(args[1]); break;
			case "packing": worker = new PackingWorker(args[1]); break;
			case "db": worker = new DBWorker(args[1]); break;
			case "packdb": worker = new PackDBWorker(args[1]); break;
			case "updatedb": worker = new UpdateWorker(args[1]); break;
			default:
				throw new IllegalStateException("Unexpected value: " + args[0]);
		}

		while (true) worker.DoWork();
	}
}
