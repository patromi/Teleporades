package pl.minespoko.system.client.connection;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicLong;

import pl.minespoko.system.client.PacketManager;
import pl.minespoko.system.client.objects.callback.Callback;
import pl.minespoko.system.client.objects.callback.CallbackManager;
import pl.minespoko.system.client.packets.Ping;
import pl.minespoko.system.client.packets.in.PacketIn;
import pl.minespoko.system.client.packets.in.PongIn;

public class ClientSocketConnection extends Thread {

	private String host;
	private int port;
	private Socket socket;
	private long lastPing = System.currentTimeMillis();
	private long lastPingRec = System.currentTimeMillis();
	private boolean connected = true;


	public ClientSocketConnection() {
		super("ConnectionThread");

	}

	public void connect(String host, int port) throws UnknownHostException, IOException {
		this.host = host;
		this.port = port;
		super.start();
	}

	private final Queue<String> toSend = new PriorityQueue<>();

	public void write(String s) {
		synchronized (toSend) {
			toSend.add(s);
		}
	}

	public boolean isConnected() {
		return connected;
	}

	public void disconnect() {
		connected = false;
		try {
			socket.close();
		} catch (Exception ignore) {}
	}

	@Override
	public void run() {
		try {
			socket = new Socket(this.host, this.port);
			PrintWriter printWriter = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true);
			new ReciveData(socket.getInputStream()).start();
			while (socket.isConnected() && connected) {
				try {
					Thread.sleep(100);
					synchronized (toSend) {
						while (!toSend.isEmpty()) {
							String s = toSend.poll();
							printWriter.println(s);
						}
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		try {
			socket.close();
		} catch (Exception ignore) {}
	}
	private class ReciveData extends Thread {

		private InputStream inputStream;

		ReciveData(InputStream inputStream) {
			this.inputStream = inputStream;
		}

		private void tryRead() throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));
			String line;
			while ((line = br.readLine()) != null) {
				try {
					PacketIn packetIn = PacketManager.getFromJson(line);
					CallbackManager.recived(packetIn);
				} catch (Exception e) {
					e.printStackTrace();
					System.err.println("Parse packet error! Line: "+line);
				}
			}
		}

		@Override
		public void run() {
			try {
				tryRead();
			} catch (IOException e) {
				e.printStackTrace();
				try {
					if(socket.isConnected()) socket.close();
				} catch (IOException ex) {
					ex.printStackTrace();
				}
				interrupt();
			}
		}
	}
}
