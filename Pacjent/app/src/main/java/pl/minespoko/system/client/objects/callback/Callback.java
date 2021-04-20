package pl.minespoko.system.client.objects.callback;

public interface Callback<T> {

	void recived(T packet);
	boolean waiting();
	
}
