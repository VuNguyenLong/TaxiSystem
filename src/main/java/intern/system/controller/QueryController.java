package intern.system.controller;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.api.kafka.KafkaConnection;
import intern.system.loadbalancers.RoundRobin;
import org.apache.commons.codec.digest.DigestUtils;
import org.springframework.web.bind.annotation.*;

import intern.system.messages.Messages.*;

import java.io.IOException;

@RestController
public class QueryController {
	RoundRobin balancer;

	public QueryController() throws IOException {
		balancer = new RoundRobin("src/main/resources/kafka.properties", 1);
	}

	@PostMapping("/query")
	public String query(@RequestBody byte[] data) throws InvalidProtocolBufferException {
		ByteString _data = ByteString.copyFrom(data);
		balancer.send(_data);

		return "";
	}

}
