package pl.minespoko.patient;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;

import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import pl.minespoko.system.client.connection.ConnectionManager;
import pl.minespoko.system.client.objects.callback.Callback;
import pl.minespoko.system.client.objects.callback.CallbackManager;
import pl.minespoko.system.client.packets.LoginPatient;
import pl.minespoko.system.client.packets.in.LoginPatientIn;
import pl.minespoko.system.client.packets.in.PacketIn;


public class LoginScreen extends AppCompatActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.loginscreen);

        final EditText usernameEditText = findViewById(R.id.username);
        final EditText passwordEditText = findViewById(R.id.password);
        final Button loginButton = findViewById(R.id.login);
        final ProgressBar loadingProgressBar = findViewById(R.id.loading);

        @SuppressLint("HandlerLeak") final Handler handler = new Handler() {
            @Override
            public void handleMessage(Message msg) {
                loginButton.setEnabled(true);
                loadingProgressBar.setVisibility(View.GONE);

                boolean error = msg.getData().getBoolean("error");
                if(error){
                    passwordEditText.getText().clear();
                    Toast.makeText(getApplicationContext(), "Błąd! Spróbuj ponownie.", Toast.LENGTH_LONG).show();
                }else{
                    Intent launchActivity = new Intent(LoginScreen.this, MainActivity.class);
                    startActivity(launchActivity);
                    finish();
                    Toast.makeText(getApplicationContext(), "Zalogowano!", Toast.LENGTH_LONG).show();
                }
            }
        };

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                loginButton.setEnabled(false);
                loadingProgressBar.setVisibility(View.VISIBLE);

                LoginPatient p = new LoginPatient();
                p.setLogin(usernameEditText.getText().toString());
                p.setPassword(passwordEditText.getText().toString());
                long start = System.currentTimeMillis();
                CallbackManager.addCallback("loginpatient", new Callback<PacketIn>() {
                    public boolean waiting() {
                        return System.currentTimeMillis()-start < 10000;
                    }
                    public void recived(PacketIn packet) {
//                        System.out.println("REcived: "+packet);
                        Message msg = handler.obtainMessage();
                        Bundle bun = new Bundle();
                        if(packet == null || packet.isError()) {
                            bun.putBoolean("error", true);
                        }else{
                            LoginPatientIn loginPatientIn = (LoginPatientIn) packet;
                            MainCache.loginPatientIn = loginPatientIn;
                            bun.putBoolean("error", false);
//                            bun.putString("name",loginPatientIn.getFirstname());
                        }
                        msg.setData(bun);
                        handler.sendMessage(msg);
                    }
                });
                ConnectionManager.send(p);
            }
        });


    }

}