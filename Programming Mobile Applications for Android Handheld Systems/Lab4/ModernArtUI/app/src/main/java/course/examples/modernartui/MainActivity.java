package course.examples.modernartui;

import android.app.DialogFragment;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.FrameLayout;
import android.widget.SeekBar;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        final FrameLayout mask1 = (FrameLayout) findViewById(R.id.mask1);
        final FrameLayout mask2 = (FrameLayout) findViewById(R.id.mask2);
        final FrameLayout mask3 = (FrameLayout) findViewById(R.id.mask3);
        final FrameLayout mask4 = (FrameLayout) findViewById(R.id.mask4);

        SeekBar seekBar = (SeekBar) findViewById(R.id.seekBar);
        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                mask1.setAlpha(1 - (float) progress / seekBar.getMax());
                mask2.setAlpha(1 - (float) progress / seekBar.getMax());
                mask3.setAlpha(1 - (float) progress / seekBar.getMax());
                mask4.setAlpha(1 - (float) progress / seekBar.getMax());
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_more) {
            DialogFragment dialogFragment = new MoreInfoDialogFragment();
            dialogFragment.show(getFragmentManager(), "dialog");
        }

        return super.onOptionsItemSelected(item);
    }
}
