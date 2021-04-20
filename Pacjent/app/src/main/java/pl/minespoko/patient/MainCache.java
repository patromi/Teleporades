package pl.minespoko.patient;

import android.view.View;

import com.google.android.material.snackbar.Snackbar;

import pl.minespoko.system.client.packets.in.LoginPatientIn;

public class MainCache {

    public static LoginPatientIn loginPatientIn = null;

    public static void displayError(String msg, View view){
        if(msg == null){
            msg = "Błąd! Spróbuj ponownie.";
        }
        Snackbar.make(view, msg, Snackbar.LENGTH_LONG).show();
    }

}