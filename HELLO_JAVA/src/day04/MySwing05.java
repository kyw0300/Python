package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.Random;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(12, 10, 25, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(44, 10, 25, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(81, 10, 25, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(118, 10, 25, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(155, 10, 25, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(192, 10, 25, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(54, 69, 126, 23);
		contentPane.add(btn);
	}

	public void lotto() {
		int[] num = new int[45];
		for(int i=0; i<num.length; i++) {
			num[i] = (i+1);
		}
		
		int temp;
		for(int i=0; i<999; i++) {
			Random rnd =  new Random();
			int rnum = rnd.nextInt(45);
			
			temp = num[0];
			num[0] = num[rnum];
			num[rnum] = temp;
		}
		int r1 = num[0];
		int r2 = num[1];
		int r3 = num[2];
		int r4 = num[3];
		int r5 = num[4];
		int r6 = num[5];
		
		ArrayList<Integer> lottoList = new ArrayList<Integer>();
		lottoList.add(r1);
		lottoList.add(r2);
		lottoList.add(r3);
		lottoList.add(r4);
		lottoList.add(r5);
		lottoList.add(r6);
		
		lottoList.sort(null);
//		for (Integer integer : lottoList) {
//			System.out.println(integer);
//		}
		lbl1.setText(lottoList.get(0)+"");
		lbl2.setText(lottoList.get(1)+"");
		lbl3.setText(lottoList.get(2)+"");
		lbl4.setText(lottoList.get(3)+"");
		lbl5.setText(lottoList.get(4)+"");
		lbl6.setText(lottoList.get(5)+"");
		
		
	}
}
