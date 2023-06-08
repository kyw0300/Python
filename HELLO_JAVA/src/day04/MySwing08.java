package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(12, 10, 31, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(59, 7, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugu();
			}
		});
		btn.setBounds(78, 50, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(230, 5, 192, 246);
		contentPane.add(ta);
	}
	
	public void gugu() {
		int dan = Integer.parseInt(tf.getText());
		String result = "";
		
		for(int i=1; i<=9; i++) {
			if(i != 1) {
				result += "\n";
			}
			result += dan + " * " + i + " = " + dan*i;
		}
		
		ta.setText(result);
	}
}
