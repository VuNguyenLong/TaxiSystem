package intern.system;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.messages.Messages;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SystemApplication {

	public static void main(String[] args) throws InvalidProtocolBufferException {
		SpringApplication.run(SystemApplication.class, args);
	}

}
