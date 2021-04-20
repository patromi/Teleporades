package pl.minespoko.system.client.objects.callback;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Stack;

import pl.minespoko.system.client.packets.in.PacketIn;

public class CallbackManager {

	private static final Map<String, Stack<Callback<PacketIn>>> callbacks = new HashMap<String, Stack<Callback<PacketIn>>>();
	
	static {
		new Thread(new Runnable() {
			@RequiresApi(api = Build.VERSION_CODES.N)
			@Override
			public void run() {
				while (true) {
					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					checkWait();
				}
			}
		}).start();
	}

	@RequiresApi(api = Build.VERSION_CODES.N)
	public static void checkWait() {
		synchronized (callbacks) {
			callbacks.forEach((type, stack) -> {
				Iterator<Callback<PacketIn>> it = stack.iterator();
				while (it.hasNext()) {
					Callback<PacketIn> call = it.next();
					try {
						if(!call.waiting()) {
							call.recived(null);
							it.remove();
						}
					} catch (Exception e) {
						e.printStackTrace();
						it.remove();
					}
				}
			});
		}
	}
	
	public static void recived(PacketIn packetIn) {
		Stack<Callback<PacketIn>> stack = callbacks.get(packetIn.getType());
		if(stack == null) {
			return;
		}
		while (!stack.isEmpty()) {
			try {
				stack.pop().recived(packetIn);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		callbacks.remove(packetIn.getType());
	}
	
	public static <T> void addCallback(String type, Callback<PacketIn> callback) {
		if(!callbacks.containsKey(type)) {
			callbacks.put(type, new Stack<>());
		}
		callbacks.get(type).push(callback);
	}
	
}
