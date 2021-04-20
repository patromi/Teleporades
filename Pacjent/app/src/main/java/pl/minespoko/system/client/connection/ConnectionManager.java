package pl.minespoko.system.client.connection;

import pl.minespoko.system.client.packets.LoginPatient;
import pl.minespoko.system.client.packets.Packet;

public class ConnectionManager {

	private static String HOST = "34.105.186.206";
	private static int PORT = 20001;
	
	private static ClientSocketConnection connection;
	private static LoginPatient loginPatient;

	public static synchronized void send(Packet packet) {
		try {
			if(packet instanceof LoginPatient) {
				loginPatient = (LoginPatient) packet;
			}
			if(connection == null || !connection.isConnected()) {
				openConnection();
			}
			if(packet instanceof LoginPatient) return;
			connection.write(packet.toJson());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void openConnection() {
		try {
			connection.disconnect();
			connection = null;
		} catch (Exception ignore) {}
		try {
			connection = new ClientSocketConnection();
			connection.connect(HOST, PORT);
			connection.write(loginPatient.toJson());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
