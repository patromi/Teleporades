package pl.minespoko.system.client.packets;

public class FindReception extends Packet {

	private String query;
	
	public FindReception() {
		super("findreception");
	}
	
	public String getQuery() {
		return query;
	}
	
	public void setQuery(String query) {
		this.query = query;
	}
	
}
