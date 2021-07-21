package intern.system.messages.serializers;

import com.google.protobuf.ByteString;
import org.apache.kafka.common.header.Headers;
import org.apache.kafka.common.serialization.Serializer;

import java.util.Map;

public class ByteStringSerializer implements Serializer<ByteString>
{
	@Override
	public void configure(Map configs, boolean isKey) {
		Serializer.super.configure(configs, isKey);
	}

	@Override
	public byte[] serialize(String s, ByteString bytes) {
		return bytes.toByteArray();
	}

	@Override
	public byte[] serialize(String topic, Headers headers, ByteString data) {
		return Serializer.super.serialize(topic, headers, data);
	}

	@Override
	public void close() {
		Serializer.super.close();
	}
}
