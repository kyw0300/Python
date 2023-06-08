package day03;

import java.util.ArrayList;

import javax.tools.Tool;

public class Human extends Animal {
	ArrayList<String> tools = new ArrayList<String>();
	
	public Human() {
		tools.add("반지");
	}
	
	public void farming(String tool) {
		tools.add(tool);
	}
	
	@Override
	public String toString() {
		String ret = "";
		for(int i=0; i<tools.size();i++) {
			ret += tools.get(i) + " ";
		}
		return ret;
		
	}
}
