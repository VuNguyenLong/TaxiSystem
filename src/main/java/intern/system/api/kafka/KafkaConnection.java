package intern.system.api.kafka;

import com.google.protobuf.ByteString;
import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class KafkaConnection {
	Properties prop;
	KafkaProducer<String, ByteString> producer;
	KafkaConsumer<String, ByteString> consumer;

	public KafkaConnection() throws IOException
	{
		prop = new Properties();
		prop.load(new FileReader("config/kafka.properties"));

		producer = new KafkaProducer<>(this.prop);
		consumer = new KafkaConsumer<>(this.prop);
	}

	public void GetOrCreate(String name)
	{
		try
		{
			AdminClient admin = AdminClient.create(this.prop);
			NewTopic topic = new NewTopic(name, 1, (short) 1);

			admin.createTopics(Collections.singleton(topic));
			admin.close();
		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
			System.exit(0);
		}
	}

	public void send(ByteString data, String receive_topic)
	{
		ProducerRecord<String, ByteString> record = new ProducerRecord<>(receive_topic, data);
		producer.send(record);
	}

	public ConsumerRecords<String, ByteString> receive(String send_topic)
	{
		consumer.subscribe(Collections.singleton(send_topic));
		return consumer.poll(Duration.ofMillis(10000));
	}
}
