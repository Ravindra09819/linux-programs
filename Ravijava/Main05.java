class A
{
	private int x,y,z;
	
	public void set(int x,int y,int z)
	{
		this.x=x;
		this.y=y;
		this.z=z;
	}
	public void show()
	{
		System.out.println(x);
		System.out.println(y);
		System.out.println(z);
	}
	
}

class Main05
{
 public static void main(String args[])
 {
	A ao=new A();
   ao.set(11,12,13);
	ao.show();
	
	
	
 }
}