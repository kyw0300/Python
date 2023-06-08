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
import java.awt.Font;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 451, 431);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫 별수");
		lblFirst.setBounds(12, 10, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝 별수");
		lblLast.setBounds(12, 35, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(81, 7, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setBounds(81, 32, 116, 21);
		contentPane.add(tfLast);
		tfLast.setColumns(10);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click();
			}
		});
		btn.setBounds(12, 60, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setFont(new Font("Monospaced", Font.PLAIN, 20));
		ta.setBounds(12, 90, 280, 257);
		contentPane.add(ta);
	}
	
	public String getStar(int cnt) {
		String ret = "";
		
		for(int i=1; i<=cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		
		return ret;
	}
	
	public void click() {
		int first = Integer.parseInt(tfFirst.getText());
		int last = Integer.parseInt(tfLast.getText());
		String result = "";
		for(int i=first; i<=last; i++) {
			result += getStar(i);
		}
		
		
		
		ta.setText(result);
	}
}
