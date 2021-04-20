package pl.minespoko.system.client.packets.in;

import json.JSONObject;

public class LoginPatientIn extends PacketIn {

	private String login;
	private String firstname;
	private String lastname;
	private String medicines;
	private int id;
	
	public LoginPatientIn() {
	}
	
	public int getId() {
		return id;
	}
	
	public String getFirstname() {
		return firstname;
	}
	
	public String getLastname() {
		return lastname;
	}
	
	public String getLogin() {
		return login;
	}
	
	public String getMedicines() {
		return medicines;
	}

	@Override
	public JSONObject fromJson(String json) {
		JSONObject x = super.fromJson(json);
		if(isError()) return x;
		login = x.getString("login");
		firstname = x.getString("firstname");
		lastname = x.getString("lastname");
		medicines = x.getString("medicines");
		id = x.getInt("id");
		return x;
	}
	
}
