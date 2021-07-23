package intern.system.controller;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.SystemApplication;
import intern.system.messages.Messages;
import org.apache.commons.codec.digest.DigestUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

@RestController
public class InfoController {

	@GetMapping("/info")
	public String info(@RequestParam(name="id") int id){
		return Messages.RestResponse.newBuilder()
				.setHashedId(DigestUtils.sha256Hex(String.valueOf(id)))
				.addBrokerAddress("localhost:9092")
				.build().toByteString().toStringUtf8();
	}
}
