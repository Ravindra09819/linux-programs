class A
{
	private int x,y;
	
	public void set(int x,int y)
	{
		this.x=x;
		this.y=y;
	}
	public void show()
	{
		System.out.println(x);
		System.out.println(y);
	}
	
}

class Main08
{
 public static void main(String args[])
 {
	A ao=new A();
   ao.set(11,12);
	ao.show();
	
	
	
 }
}