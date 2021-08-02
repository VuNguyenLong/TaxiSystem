package intern.system.controller;

import intern.system.messages.Messages;
import org.apache.commons.codec.digest.DigestUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class InfoController {

	@GetMapping("/info")
	public String info(@RequestParam(name="id", required = false, defaultValue = "-1") int id){
		String hashed_id = "";
		if (id != -1) hashed_id = DigestUtils.sha256Hex(String.valueOf(id));

		return Messages.RestResponse.newBuilder()
				.setHashedId(hashed_id)
				.addBrokerAddress("localhost:9092")
				//.addBrokerAddress("40.117.86.72:9092")
				//.addBrokerAddress("20.106.128.161:9092")
				//.addBrokerAddress("137.117.35.98:9092")
				.build().toByteString().toStringUtf8();
	}
}
