package intern.system.controller;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.loadbalancers.RoundRobin;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class QueryController {
	RoundRobin balancer;

	public QueryController() throws IOException {
		balancer = new RoundRobin(3, "pulling");
	}

	@PostMapping("/query")
	public String query(@RequestBody byte[] data) throws InvalidProtocolBufferException {
		ByteString _data = ByteString.copyFrom(data);
		balancer.send(_data);
		return "";
	}

}
