package pl.minespoko.patient.ui.main;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.text.SpannableString;
import android.text.SpannableStringBuilder;
import android.text.style.ForegroundColorSpan;
import android.text.style.RelativeSizeSpan;
import android.text.style.StyleSpan;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputMethodManager;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.appcompat.widget.AppCompatAutoCompleteTextView;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import pl.minespoko.patient.LoginScreen;
import pl.minespoko.patient.MainActivity;
import pl.minespoko.patient.MainCache;
import pl.minespoko.patient.R;
import pl.minespoko.system.client.connection.ConnectionManager;
import pl.minespoko.system.client.objects.callback.Callback;
import pl.minespoko.system.client.objects.callback.CallbackManager;
import pl.minespoko.system.client.packets.GetDoctor;
import pl.minespoko.system.client.packets.ListLek;
import pl.minespoko.system.client.packets.LoginPatient;
import pl.minespoko.system.client.packets.in.GetDoctorIn;
import pl.minespoko.system.client.packets.in.ListLekIn;
import pl.minespoko.system.client.packets.in.LoginPatientIn;
import pl.minespoko.system.client.packets.in.PacketIn;

/**
 * A placeholder fragment containing a simple view.
 */
public class PlaceholderFragment extends Fragment {

    private static final String ARG_SECTION_NUMBER = "section_number";

    public static PlaceholderFragment newInstance(int index) {
        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle bundle = new Bundle();
        bundle.putInt(ARG_SECTION_NUMBER, index);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_main, container, false);
        int ind = getArguments().getInt(ARG_SECTION_NUMBER);
        if(ind == 1){
            root = inflater.inflate(R.layout.infofragment_main, container, false);
            String name = "błąd logowania";
            String lastname = "błąd logowania";
            String drugs = "błąd logowania";
            if(MainCache.loginPatientIn != null && !MainCache.loginPatientIn.isError()){
                name = MainCache.loginPatientIn.getFirstname();
                lastname = MainCache.loginPatientIn.getLastname();
                drugs = MainCache.loginPatientIn.getMedicines();
            }
            TextView tlab = root.findViewById(R.id.what_label);
            tlab.setText("Dane konta:");
            TextView tname = root.findViewById(R.id.name_label);
            tname.setText("Imię: "+name);
            TextView tlaname = root.findViewById(R.id.lastname_label);
            tlaname.setText("Nazwisko: "+lastname);
            TextView tdr = root.findViewById(R.id.drugs_label);
            tdr.setText("Lekarstwa: "+drugs);

        }else if(ind == 2){
            root = inflater.inflate(R.layout.doctorfragment_main, container, false);
            layout2(root);
        }
        return root;
    }

    private void layout2(View root){
        setupInfoText(root);
        AppCompatAutoCompleteTextView autoCompleteTextView = root.findViewById(R.id.contactRegionInputComplete);

        @SuppressLint("HandlerLeak") Handler done = new Handler(){
            @Override
            public void handleMessage(@NonNull Message msg) {
                autoCompleteTextView.setEnabled(true);
            }
        };


        autoCompleteTextView.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if((event != null && event.getKeyCode() == KeyEvent.KEYCODE_ENTER || (actionId == EditorInfo.IME_ACTION_DONE))){
                    if(autoCompleteTextView.getText().toString().isEmpty()) return false;
                    TextView num = root.findViewById(R.id.contactNumberShow);
                    num.setVisibility(View.VISIBLE);
                    InputMethodManager imm = (InputMethodManager)autoCompleteTextView.getContext().getSystemService(Context.INPUT_METHOD_SERVICE);
                    imm.hideSoftInputFromWindow(autoCompleteTextView.getWindowToken(), 0);
                    autoCompleteTextView.setEnabled(false);
                    search(root,done,autoCompleteTextView.getText().toString());
                }
                return false;
            }
        });
    }
    private void search(View root, Handler done, String query){
        Callback<PacketIn> callback = new Callback<PacketIn>() {
            @Override
            public void recived(PacketIn packet) {
                done.sendMessage(done.obtainMessage());
                if(packet == null || packet.isError()){
                    MainCache.displayError(null,root);
                    return;
                }
                GetDoctorIn in = (GetDoctorIn) packet;
                MainCache.displayError("Znaleziono "+in.getList().size()+" lekarzy.",root);
                for(Integer i : in.getList()){
                    szuklek(i,root);
                }
            }

            @Override
            public boolean waiting() {
                return true;
            }
        };
        CallbackManager.addCallback("getdoctor",callback);
        GetDoctor getDoctor = new GetDoctor();
        getDoctor.setSzukaj(query);
        ConnectionManager.send(getDoctor);
    }
    private void szuklek(int i, View root){
        Callback<PacketIn> callback2 = new Callback<PacketIn>() {
            @Override
            public void recived(PacketIn packet) {
                if(packet == null || packet.isError()){
                    MainCache.displayError(null,root);
                    return;
                }
                ListLekIn in = (ListLekIn) packet;
                MainCache.displayError("Znaleziono "+in.getFirstname()+" ",root);
                System.out.println("Znaleziono "+in.getFirstname()+" "+i+" =? "+in.getId());
            }

            @Override
            public boolean waiting() {
                return true;
            }
        };
        CallbackManager.addCallback("listlek",callback2);
        ListLek listLek = new ListLek();
        listLek.setId(i);
        ConnectionManager.send(listLek);
    }
    private void setupInfoText(View root){
        TextView infoText = root.findViewById(R.id.infoText);

        SpannableStringBuilder infoTextBuilder = new SpannableStringBuilder();

        SpannableString spannableString = new SpannableString(
                "Chcesz wyszukać lekarza?\n"
        );
        spannableString.setSpan(new ForegroundColorSpan(Color.BLACK), 0, spannableString.length(), 0);
        spannableString.setSpan(new RelativeSizeSpan(1.3f),0,spannableString.length(),0);
        spannableString.setSpan(new StyleSpan(Typeface.BOLD),0,spannableString.length(),0);
        infoTextBuilder.append(spannableString);

        SpannableString spannableString1 = new SpannableString(
                "Znajdź go dzięki wyszukiwarce.\n\n"
        );
        spannableString1.setSpan(new ForegroundColorSpan(Color.BLACK), 0, spannableString1.length(), 0);
        infoTextBuilder.append(spannableString1);

        SpannableString spannableString2 = new SpannableString(
                "Wprowadź imię, nazwisko, specjalizację lub nazwę placówki, w której pracuje interesujący cię lekarz. Poniżej otrzymasz listę osób pasujących do zapytania.\n"
        );
        spannableString2.setSpan(new ForegroundColorSpan(0xFF0070FE), 0, spannableString2.length(), 0);
        infoTextBuilder.append(spannableString2);

        infoText.setText(infoTextBuilder, TextView.BufferType.SPANNABLE);
    }
}