package intern.system.workers;

import java.io.IOException;

public class WorkerRunner {
	public static void main(String[] args) throws IOException {
		Worker worker;
		switch (args[0])
		{
			case "pulling": worker = new PullingWorker(args[1], args[2]); break;
			case "packing": worker = new PackingWorker(args[1], args[2]); break;
			case "db": worker = new DBWorker(args[1], args[2]); break;
			default:
				throw new IllegalStateException("Unexpected value: " + args[0]);
		}

		while (true) worker.DoWork();
	}
}
