package pl.minespoko.system.client.packets.in;

import json.JSONObject;

public class FindReceptionIn extends PacketIn {

	private int found;
	
	public int getFound() {
		return found;
	}
	
	@Override
	public JSONObject fromJson(String json) {
		JSONObject x = super.fromJson(json);
		found = x.getInt("found");
		return x;
	}
	
}
