package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;
	private JButton btn;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 10, 35, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(91, 10, 40, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(179, 10, 47, 21);
		contentPane.add(tf3);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(365, 10, 57, 21);
		contentPane.add(tf4);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(59, 13, 35, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setBounds(143, 13, 47, 15);
		contentPane.add(lbl2);
		
		btn = new JButton("배수의합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(238, 9, 115, 23);
		contentPane.add(btn);
	}

	public void myclick() {
		int t1 = Integer.parseInt(tf1.getText());
		int t2 = Integer.parseInt(tf2.getText());
		int t3 = Integer.parseInt(tf3.getText());
		int sum = 0;
		
		for(int i=t1; i<=t2; i++) {
			if(i%t3 == 0) {
				sum += i;
			}
		}
		tf4.setText(sum+"");
	}
}
