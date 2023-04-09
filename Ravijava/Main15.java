class A 
{
	public void hello(int x,int y)
	{
		int z=x+y;
		System.out.println("Sum is:"+z);
	}
}
class Main15
{
 public static void main(String args[])
 {
	 
	A ao=new A();
	ao.hello(10,20);
 }
}