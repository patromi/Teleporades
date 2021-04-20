package pl.minespoko.system.client.packets.in;

import json.JSONObject;

public class ListLekIn extends PacketIn {

	private String firstname;
	private String lastname;
	private String specjalizacja;
	private int idkliniki;
	private String klinika;
	private int id;

	public String getFirstname() {
		return firstname;
	}

	public String getLastname() {
		return lastname;
	}

	public String getSpecjalizacja() {
		return specjalizacja;
	}

	public int getIdkliniki() {
		return idkliniki;
	}

	public String getKlinika() {
		return klinika;
	}

	public int getId() {
		return id;
	}

	@Override
	public JSONObject fromJson(String json) {
		JSONObject x = super.fromJson(json);
		firstname = x.getString("firstname");
		lastname = x.getString("lastname");
		specjalizacja = x.getString("specjalizacja");
		idkliniki = x.getInt("idkliniki");
		klinika = x.getString("clinic");
		id = x.getInt("id");
		return x;
	}
}

