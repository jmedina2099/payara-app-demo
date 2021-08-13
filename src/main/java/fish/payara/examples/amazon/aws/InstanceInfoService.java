package fish.payara.examples.amazon.aws;

import javax.enterprise.context.ApplicationScoped;
import java.net.InetAddress;
import java.util.Optional;
import java.util.logging.Level;
import java.util.logging.Logger;

@ApplicationScoped
public class InstanceInfoService {

    private static final Logger LOG = Logger.getLogger(InstanceInfoService.class.getName());
    private static final String DEFAULT_NAME = "payara-app-demo-2";

    public String getName() {
        String instanceName = null;
        try {
            instanceName = InetAddress.getLocalHost().getHostName();
        } catch (Exception exception) {
            LOG.log(Level.SEVERE, "Error retrieving instance name", exception);
        }
        return Optional.ofNullable(instanceName).orElse(DEFAULT_NAME);
    }
}
