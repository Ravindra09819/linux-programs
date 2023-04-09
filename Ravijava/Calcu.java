import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class Calcu extends JFrame implements ActionListener {
JButton b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,plus,min,div,mul,eq,mod,clear;
JTextField t1;
Font f;
 
int n1,n2,n3,n4;
String op;
Calcu()
{
	setSize(500,400);
	setVisible(true);
	setLayout(new FlowLayout());
	f=new Font(Font.MONOSPACED,Font.BOLD,20);
	b0=new JButton("0");
	b1=new JButton("1");
	b2=new JButton("2");
	b3=new JButton("3");
	b4=new JButton("4");
	b5=new JButton("5");
	b6=new JButton("6");
	b7=new JButton("7");
	b8=new JButton("8");
	b9=new JButton("9");
	b9=new JButton("9");
t1=new JTextField(20);


	plus=new JButton("+");
	min=new JButton("-");
	div=new JButton("/");
	mul=new JButton("*");
	eq=new JButton("=");
	mod=new JButton("%");
	clear=new JButton("AC");
t1.setFont(f);

	b0.setFont(f);
	b1.setFont(f);
	b2.setFont(f);
	b3.setFont(f);
	b4.setFont(f);
	b5.setFont(f);
	b6.setFont(f);
	b7.setFont(f);
	b8.setFont(f);
	b9.setFont(f);
	
	plus.setFont(f);
	min.setFont(f);
	div.setFont(f);
	mul.setFont(f);
	eq.setFont(f);
	mod.setFont(f);
	clear.setFont(f);

	add(t1);
	
	add(b0);
	add(b1);
	add(b2);
	add(b3);
	add(b4);
	add(b5);
	add(b6);
	add(b7);
	add(b8);
	add(b9);

	
	add(plus);
	add(min);
	add(div);
	add(mul);
	add(eq);
	add(mod);
	add(clear);
	
	
    t1.setBackground(Color.white); 
    
	b0.addActionListener(this);
	b1.addActionListener(this);
	b2.addActionListener(this);
	b3.addActionListener(this);
	b4.addActionListener(this);
	b5.addActionListener(this);
	b6.addActionListener(this);
	b7.addActionListener(this);
	b8.addActionListener(this);
	b9.addActionListener(this);
	plus.addActionListener(this);
	min.addActionListener(this);
	div.addActionListener(this);
	mul.addActionListener(this);
	clear.addActionListener(this);
	mod.addActionListener(this);
	eq.addActionListener(this);
	
	}
	
	public static void main(String[] args) {
		new Calcu();

	}

	@Override
	public void actionPerformed(ActionEvent ae) {
		if(ae.getSource()==b0)
		{
	t1.setText(t1.getText()+"0");
		}
		
		
		if(ae.getSource()==b1)
		{
			
	t1.setText(t1.getText()+"1");
		}
		if(ae.getSource()==b2)
		{
	t1.setText(t1.getText()+"2");
		}
		if(ae.getSource()==b3)
		{
	t1.setText(t1.getText()+"3");
		}
		if(ae.getSource()==b4)
		{
	t1.setText(t1.getText()+"4");
		}
		if(ae.getSource()==b5)
		{
	t1.setText(t1.getText()+"5");
		}
		if(ae.getSource()==b6)
		{
	t1.setText(t1.getText()+"6");
		}
		if(ae.getSource()==b7)
		{
	t1.setText(t1.getText()+"7");
		}
		if(ae.getSource()==b8)
		{
	t1.setText(t1.getText()+"8");
		}
		if(ae.getSource()==b9)
		{
	t1.setText(t1.getText()+"9");
		}
		if(ae.getSource()==plus)
		{
			n1=Integer.parseInt(t1.getText());
			
			t1.setText("");
			
			op="+";
		}
		if(ae.getSource()==eq)
		{
			if(op.equals("+"))
			{
		n2=Integer.parseInt(t1.getText());
		
		n3=n2+n1;
		t1.setText(""+n3);
		}
		}
			
			if(ae.getSource()==min)
			{
				n1=Integer.parseInt(t1.getText());
				
				t1.setText("");
				
				op="-";
			}
			if(ae.getSource()==eq)
			{
				if(op.equals("-"))
				{
			n2=Integer.parseInt(t1.getText());
			
			n3=n1-n2;
			t1.setText(""+n3);
			}
			}
				
				if(ae.getSource()==mul)
				{
					n1=Integer.parseInt(t1.getText());
					
					t1.setText("");
					
					op="*";
				}			
				if(ae.getSource()==eq)
				{
					if(op.equals("*"))
					{
				n2=Integer.parseInt(t1.getText());
				
				n3=n2*n1;
				t1.setText(""+n3);
				}
				}
					
					
					
					if(ae.getSource()==div)
				{
					n1=Integer.parseInt(t1.getText());
					
					t1.setText("");
					
					op="/";
				}
				if(ae.getSource()==eq)
				{
					if(op.equals("/"))
					{
				n2=Integer.parseInt(t1.getText());
				
				double n4=n1/n2;
				t1.setText(""+n4);
				}
				}
					
				if(ae.getSource()==mod)
				{
					n1=Integer.parseInt(t1.getText());
					
					t1.setText("");
					
					op="%";
				}
				if(ae.getSource()==eq)
				{
					if(op.equals("%"))
					{
				n2=Integer.parseInt(t1.getText());
				
				n3=n2%n1;
				t1.setText(""+n3);
				}
				}
					
		if(ae.getSource()==clear)
		
	t1.setText("");
	}
		
			}
		

	




