//Polymorphism: many Form
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
class Test1d
{
	public static void main(String args[])
  {
	A ao=new A();
	B bo=new B();
	C co=new C();
	D d=new D();
	
	
	A ref;
	ref=ao;
	
	ref.hello(10,20);
	
	ref=bo;
	ref.hello(10,20);
	
	ref=co;
	ref.hello(10,20);
	
	ref=d;
	ref.hello(10,20);
	
	
	
  }
}


