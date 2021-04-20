package pl.minespoko.system.client.packets;

public class ListLek extends Packet {

	private int id;

	public ListLek() {
		super("listlek");
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
}
