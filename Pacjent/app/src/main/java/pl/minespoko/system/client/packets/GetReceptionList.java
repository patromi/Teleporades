package pl.minespoko.system.client.packets;

public class GetReceptionList extends Packet {

	private int begin;
	private int end;
	private String query;
	
	public GetReceptionList() {
		super("getreceptionlist");
	}
	
	public int getBegin() {
		return begin;
	}
	
	public void setBegin(int begin) {
		this.begin = begin;
	}
	
	public int getEnd() {
		return end;
	}
	
	public void setEnd(int end) {
		this.end = end;
	}
	
	public String getQuery() {
		return query;
	}
	
	public void setQuery(String query) {
		this.query = query;
	}
	
}
