class A 
{
	public int x;
	public void show()
	{
		System.out.println(x);
	}
	
}

class Main06
{
 public static void main(String args[])
 {
	A ao=new A();
    ao.x=10;
	ao.show();
	
	A ao2=new A();
    ao2.x=20;
	ao2.show();
	
	
	A ao3=new A();
    ao3.x=9819;
	ao3.show();
	
 }
}