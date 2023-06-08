package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Random;

public class MySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	public static ArrayList<Integer> ranNumList;
	public static HashSet<Integer> ranNumSet;
	int strike = 0;
	int ball = 0;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		Random random = new Random();
		ranNumSet = new HashSet<>();
		
		while (ranNumSet.size() < 3) {
			ranNumSet.add(random.nextInt(9) + 1);
		}
		ranNumList = new ArrayList<>(ranNumSet);
		Collections.shuffle(ranNumList);
		System.out.println(ranNumList);
		int count = 0;
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing11 frame = new MySwing11();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 368, 510);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("숫자야구게임!!");
		lbl.setBounds(12, 10, 97, 26);
		contentPane.add(lbl);
		
		JButton btn = new JButton("맞춰보기!!");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result();
			}
		});
		btn.setBounds(12, 46, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(12, 79, 325, 369);
		contentPane.add(ta);
		
		tf = new JTextField();
		tf.setBounds(121, 13, 216, 23);
		contentPane.add(tf);
		tf.setColumns(10);
		
		// 이 자리에 랜덤세팅 넣어주는게 좋다
	}
	
	public void result() {
		strike = 0;
		ball = 0;
		String input = tf.getText();
		String i1 = input.substring(0, 1);
		String i2 = input.substring(1, 2);
		String i3 = input.substring(2, 3);
		int ni1 = Integer.parseInt(i1);
		int ni2 = Integer.parseInt(i2);
		int ni3 = Integer.parseInt(i3);
		
		if(i1.equals(ranNumList.get(0)+"")) {
			strike++;
		} 
		if(i2.equals(ranNumList.get(1)+"")) {
			strike++;
		} 
		if(i3.equals(ranNumList.get(2)+"")) {
			strike++;
		}
		
		if(ranNumSet.contains(ni1)) {
			ball++;
		} 
		if(ranNumSet.contains(ni2)) {
			ball++;
		} 
		if(ranNumSet.contains(ni3)) {
			ball++;
		}
		
//		System.out.println(i1 + " " + i2 + " " + i3 + " ==> " + strike + "S " + (ball-strike) + "B");
		
		String result = ta.getText();
		result += (i1 + " " + i2 + " " + i3 + "\t" + strike + "S " + (ball-strike) + "B\n");
		ta.setText(result);
		
		if(strike == 3) {
			JOptionPane.showMessageDialog(null, input + " 정답!!");
		}
		tf.setText("");
	}
}
