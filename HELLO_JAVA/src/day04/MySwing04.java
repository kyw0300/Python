package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 28, 45, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(69, 31, 38, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(119, 28, 45, 21);
		contentPane.add(tf2);
		
		JButton btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(176, 27, 96, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(284, 28, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}

	public void myclick() {
		int t1 = Integer.parseInt(tf1.getText());
		int t2 = Integer.parseInt(tf2.getText());
		int sum = 0;
		
		for(int i=t1; i<=t2; i++) {
			sum += i;
		}
		
		tf3.setText(sum+"");
	}
}
