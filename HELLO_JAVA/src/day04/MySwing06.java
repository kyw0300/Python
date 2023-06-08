package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나");
		lblMine.setBounds(12, 26, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴");
		lblCom.setBounds(12, 68, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과");
		lblResult.setBounds(12, 119, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(101, 23, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(101, 65, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(101, 116, 242, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기!!");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				game();
			}
		});
		btn.setBounds(48, 173, 126, 23);
		contentPane.add(btn);
	}

	public void game() {
		String mine = tfMine.getText();
		String com;
		String result;
		
		Random rnd = new Random();
		double rnum = rnd.nextDouble();
		
		if(rnum >= 0.5) {
			com = "짝";
		} else {
			com = "홀";
		}
		
		if(mine.equals("짝") && com.equals("짝") || mine.equals("홀") && com.equals("홀")) {
			result = "승리!!";
			tfCom.setText(com);
			tfResult.setText(result);
		} else if(mine.equals("짝") && com.equals("홀") || mine.equals("홀") && com.equals("짝")){
			result = "패배!!";
			tfCom.setText(com);
			tfResult.setText(result);
		} else {
			result = "값을 정확히 입력해주세요!";
			tfCom.setText("");
			tfResult.setText(result);
		}
		
		
	}
}
