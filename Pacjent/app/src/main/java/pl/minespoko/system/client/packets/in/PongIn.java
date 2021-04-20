package pl.minespoko.system.client.packets.in;

import json.JSONObject;

public class PongIn extends PacketIn {

	private long id;
	
	public long getId() {
		return id;
	}
	
	@Override
	public JSONObject fromJson(String json) {
		JSONObject x = super.fromJson(json);
		id = x.getLong("time");
		return x;
	}
	
}
