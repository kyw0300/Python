package day03;

public class OopTest {
	public static void main(String[] args) {

		Human hum = new Human();
		System.out.println(hum.age);
		System.out.println(hum);
		hum.birthHappy();
		hum.farming("gun");
		System.out.println(hum.age);
		System.out.println(hum);
	}
}
