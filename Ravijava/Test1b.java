//Method Overriding:Same method name with same parameter.
class A 
{
	public void hello(int x,int y)
	{
	int z=x+y;
    System.out.println("sum is:"+z);	
	}
}
class B extends A 
{
    public void hello(int x,int y)
	{
	int z=x-y;
    System.out.println("subs is:"+z);	
	}	
}
class C extends A 
{
	public void hello(int x,int y)
	{
	int z=x*y;
    System.out.println("Multi is:"+z);	
	}
}
class D extends A 
{
	public void hello(int x,int y)
	{
	int z=x/y;
    System.out.println("Div is:"+z);	
	}
}
class Test1b
{
	public static void main(String args[])
  {
	  A ao=new A();
	B bo=new B();
	C co=new C();
	D d=new D();
	ao.hello(10,20);
	bo.hello(10,20);
	co.hello(10,20);
	d.hello(10,20);
	
  }
}


