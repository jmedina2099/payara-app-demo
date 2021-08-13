package fish.payara.examples.amazon.aws;

import java.io.Serializable;
import java.util.concurrent.atomic.AtomicInteger;

import javax.ejb.Singleton;

import fish.payara.cluster.Clustered;

@SuppressWarnings("serial")
@Singleton
@Clustered
public class CounterService implements Serializable {

	private final AtomicInteger userCounter = new AtomicInteger(0);

	public Integer getNextValue() {
		return userCounter.incrementAndGet();
	}

	public Integer getCurrentValue() {
		return userCounter.get();
	}
}
