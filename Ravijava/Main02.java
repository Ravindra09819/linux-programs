class A 
{
	public void hello1(int x,int y)
	{
		int z=x+y;
		System.out.println("Sum is:"+z);
	}
	public void hello2(int x,int y)
	{
		int z=x-y;
		System.out.println("Subs is:"+z);
	}
	public void hello3(int x,int y)
	{
		int z=x*y;
		System.out.println("Multi is:"+z);
	}
	public void hello4(int x,int y)
	{
		int z=x/y;
		System.out.println("div is:"+z);
	}
	
}
class Main02
{
 public static void main(String args[])
 {
	 
	A ao=new A();
	ao.hello1(101,20);
	ao.hello2(102,20);
	ao.hello3(103,20);
	ao.hello4(20,5);
 }
}