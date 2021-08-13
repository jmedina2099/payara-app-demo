package fish.payara.examples.amazon.aws;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/pod")
public class PodServlet extends HttpServlet {

	private static final Logger LOG = Logger.getLogger(PodServlet.class.getName());

	private static final long serialVersionUID = -1555408311258177419L;

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {

		try {
			resp.getWriter().println(getServerInfo());
		} catch (IOException exception) {
			LOG.log(Level.SEVERE, "Error retrieving instance name", exception);
		}
	}

	private String getServerInfo() {
		try {
			return String.format("Executed From Server: %s", InetAddress.getLocalHost().getHostName());
		} catch (UnknownHostException exception) {
			LOG.log(Level.SEVERE, "Error retrieving instance name", exception);
			return null;
		}
	}

}
