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
public class InfoController {
	RoundRobin balancer;

	public InfoController() throws IOException {
		balancer = new RoundRobin("src/main/resources/kafka.properties", 1);
	}

	@PostMapping("/info")
	public String info(@RequestParam(name="id") int id, @RequestBody String data) throws InvalidProtocolBufferException {
		ByteString _data = ByteString.copyFromUtf8(data);
		balancer.send(_data);

		return RestResponse.newBuilder()
				.addBrokerAddress("localhost:9092")
				.setHashedId(DigestUtils.sha256Hex(String.valueOf(id)))
				.build().toByteString().toStringUtf8();
	}

}
