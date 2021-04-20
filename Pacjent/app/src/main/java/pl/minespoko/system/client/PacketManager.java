package pl.minespoko.system.client;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

import json.JSONObject;

import pl.minespoko.system.client.packets.in.ListLekIn;
import pl.minespoko.system.client.packets.in.GetDoctorIn;
import pl.minespoko.system.client.packets.in.LoginPatientIn;
import pl.minespoko.system.client.packets.in.PacketIn;
import pl.minespoko.system.client.packets.in.PongIn;

public class PacketManager {

	private static Map<String, Class<? extends PacketIn>> packetsin = new HashMap<String, Class<? extends PacketIn>>();
	static{
		packetsin.put("listlek", ListLekIn.class);
		packetsin.put("getdoctor", GetDoctorIn.class);
		packetsin.put("loginpatient", LoginPatientIn.class);
		packetsin.put("pong", PongIn.class);
	}
	
	public static PacketIn getFromJson(String json) {
		PacketIn find = null;
		JSONObject o = new JSONObject(json);
		String type = o.getString("type");
		try {
			find = Objects.requireNonNull(packetsin.get(type)).newInstance();
			find.fromJson(json);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return find;
	}
	
}
