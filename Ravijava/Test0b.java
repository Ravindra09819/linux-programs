//Method Overloading:same name with different parameter

class A 
{
	public void hello()
	{
		System.out.println("No parameter..");
	}
	public void hello(int x)
	{
		System.out.println(x);
	}
	public void hello(int x,int y)
	{
		int z=x+y;
		System.out.println("sum is:"+z);
	}
	public double hello(double x)
	{
		return x*x;
	}
	
}
class Test0b
{
  public static void main(String args[])
  {
     A ao=new A();
	 ao.hello(11);
	 System.out.println(ao.hello(12.36));
	 ao.hello();
	 ao.hello(12,45);
	 
 
	
  }
}