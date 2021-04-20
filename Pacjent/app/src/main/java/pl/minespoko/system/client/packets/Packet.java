package pl.minespoko.system.client.packets;

import json.JSONObject;

public abstract class Packet {

	private String type;
	
	public Packet(String type) {
		this.type = type;
	}
	
	public String getType() {
		return type;
	}
	
	public String toJson() {
		return new JSONObject(this).toString();
	}
	
	@Override
	public String toString() {
		return toJson();
	}
	
}
