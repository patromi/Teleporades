package pl.minespoko.system.client.packets;

public class GetDoctor extends Packet {

	private String szukaj;
	
	public GetDoctor() {
		super("getdoctor");
	}

	public String getSzukaj() {
		return szukaj;
	}

	public void setSzukaj(String szukaj) {
		this.szukaj = szukaj;
	}
}
