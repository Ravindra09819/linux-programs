class A 
{
	private int x,y;
	
	public void set(int a,int b)
	{
		x=a;
		y=b;
	}
	public void show()
	{
		System.out.println(x);
		System.out.println(y);
	}
	
}

class Main09
{
 public static void main(String args[])
 {
	A ao=new A();
   ao.set(11,12);
	ao.show();
	
	
	
 }
}