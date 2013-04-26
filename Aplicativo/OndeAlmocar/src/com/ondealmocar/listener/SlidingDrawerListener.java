package com.ondealmocar.listener;

import java.util.ArrayList;
import java.util.List;

import android.view.View;
import android.view.View.OnClickListener;
import android.widget.SlidingDrawer;

public class SlidingDrawerListener implements OnClickListener {
	
	private List<SlidingDrawer> slidings = new ArrayList<SlidingDrawer>();
	
	public SlidingDrawerListener(List<SlidingDrawer> slidings) {
		this.slidings = slidings;
	}
	
	@Override
	public void onClick(View v) {
		for (SlidingDrawer s : this.slidings)
			if (s.getId() != v.getId())
				s.animateClose();
	}

}
