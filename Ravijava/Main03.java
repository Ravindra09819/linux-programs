class A
{
	public void hello(int x,int y)
	{
		int z=x+y;
		System.out.println("Sum is:"+z);
	}
}
class Main03
{
 public static void main(String args[])
 {
	 
	A ao=new A();
	ao.hello(101,20);
	ao.hello(102,20);
	ao.hello(103,20);
	ao.hello(104,20);
 }
}