package pl.minespoko.system.client.packets;

public class Ping extends Packet {

	private long time;
	
	public Ping() {
		super("ping");
	}
	
	public long getTime() {
		return time;
	}

	public void setTime(long id) {
		this.time = id;
	}
	
}
