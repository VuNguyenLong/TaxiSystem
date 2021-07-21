package intern.system.messages.deserializers;

import com.google.protobuf.ByteString;
import org.apache.kafka.common.header.Headers;
import org.apache.kafka.common.serialization.Deserializer;

import java.util.Map;

public class ByteStringDeserializer implements Deserializer<ByteString>
{
	@Override
	public void configure(Map<String, ?> configs, boolean isKey) {
		Deserializer.super.configure(configs, isKey);
	}

	@Override
	public ByteString deserialize(String s, byte[] bytes) {
		return ByteString.copyFrom(bytes);
	}

	@Override
	public ByteString deserialize(String topic, Headers headers, byte[] data) {
		return Deserializer.super.deserialize(topic, headers, data);
	}

	@Override
	public void close() {
		Deserializer.super.close();
	}
}
