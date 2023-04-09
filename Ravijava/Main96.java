abstract class A 
{
	abstract public void hello();//abstract method
	
	public void hello2()//Non-abstract method
	{
		System.out.println("non-abstract method..");
	}
	public A()
	{
		System.out.println("Its parent constructor..");
	}
	
}
class B extends A 
{
	public void hello()
	{
	  System.out.println("Hello B..");	
	}
	public B()
	{
	System.out.println("Its child constructor..");	
	}
}

class Main96 
{
  public static void main(String[] args)
 {
	A ao=new B();
	ao.hello();
	ao.hello2();
	
 }
}