package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn1;
	JButton btn2;
	JButton btn3;
	JButton btn4;
	JButton btn5;
	JButton btn6;
	JButton btn7;
	JButton btn8;
	JButton btn9;
	JButton btn0;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(12, 10, 147, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		tf.setHorizontalAlignment(JTextField.RIGHT);
		
		btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn1.setBounds(12, 41, 41, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn2.setBounds(65, 41, 41, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn3.setBounds(118, 41, 41, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);;
			}
		});
		btn4.setBounds(12, 74, 41, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn5.setBounds(65, 74, 41, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);;
			}
		});
		btn6.setBounds(118, 74, 41, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn7.setBounds(12, 107, 41, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn8.setBounds(65, 107, 41, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);;
			}
		});
		btn9.setBounds(118, 107, 41, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn0.setBounds(12, 140, 41, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				call();
			}
		});
		btnCall.setBounds(65, 140, 94, 23);
		contentPane.add(btnCall);
	}

	public void call() {
		String num = tf.getText();
		String message = "Calling\n" + num;
		JOptionPane.showMessageDialog(null, message);
	}
	
	public void myclick(MouseEvent e) {
		JButton obj = (JButton) e.getSource();
		
		String num = obj.getText();
		String res = tf.getText();
		res += num;
		tf.setText(res);
	}
}
