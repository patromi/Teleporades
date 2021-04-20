package pl.minespoko.system.client.packets.in;

import json.JSONObject;

public abstract class PacketIn {

	private String type;
	private int error;
	
	public String getType() {
		return type;
	}

	public int getError() {
		return error;
	}
	
	public boolean isError() {
		if(error == -1) return false;
		if(error >= 200 && error < 300) return false;
		return true;
	}
	
	public JSONObject fromJson(String json) {
		JSONObject x = new JSONObject(json);
		type = x.getString("type");
		if(x.has("error")) {
			error = x.getInt("error");
		}else {
			error = -1;
		}
		return x;
	}
	
	@Override
	public String toString() {
		return new JSONObject(this).toString();
	}
	
}
