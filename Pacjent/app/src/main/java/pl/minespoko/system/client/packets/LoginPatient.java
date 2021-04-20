package pl.minespoko.system.client.packets;

public class LoginPatient extends Packet {

	private String login;
	private String password;
	
	public LoginPatient() {
		super("loginpatient");
	}
	
	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}
	
}
