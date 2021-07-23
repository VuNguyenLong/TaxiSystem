package intern.system;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import intern.system.messages.Messages;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SystemApplication {

	public static void main(String[] args) throws InvalidProtocolBufferException {
		//Messages.Message a = Messages.Message.newBuilder().setClient(Messages.Client.newBuilder().setId(128).addHash(1).build()).build();
		//Messages.Message.parseFrom(a.toByteString());
		//System.out.println(a.toByteString());
		SpringApplication.run(SystemApplication.class, args);
	}

}
