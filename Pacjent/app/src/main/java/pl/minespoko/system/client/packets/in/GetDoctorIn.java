package pl.minespoko.system.client.packets.in;

import java.util.ArrayList;
import java.util.List;

import json.JSONArray;
import json.JSONObject;

public class GetDoctorIn extends PacketIn {

	private String squery;
	private List<Integer> list;

	public String getSquery() {
		return squery;
	}

	public List<Integer> getList() {
		return list;
	}

	@Override
	public JSONObject fromJson(String json) {
		JSONObject x = super.fromJson(json);
		squery = x.getString("squery");
		JSONArray list = x.getJSONArray("ID");
		this.list = new ArrayList<Integer>();
		for (int i = 0; i < list.length(); i++) {
			try {
				JSONObject jo = list.getJSONObject(i);
				this.list.add(jo.getInt("ID"));
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return x;
	}
	
}
