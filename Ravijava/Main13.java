class A 
{
	public void hello1()
	{
		int x;
		x=1;
		while(x<=10)
		{
		System.out.println("While loop :"+x);
        x++;		
		}
		
	}
}
class B 
{
	public void hello2()
	{
		int x;
		x=1;
		do
		{
		System.out.println("do-While loop :"+x);
        x++;		
		}
		while(x<=10);
	}
}
class C 
{
	public void hello3()
	{
		for(int x=1;x<=10;x++)
		{
			System.out.println("For loop:"+x);
		}
		
	}
}
class Main13
{
 public static void main(String args[])
 {
	 
	A ao=new A();
	B bo=new B();
	C co=new C();
	ao.hello1();
	bo.hello2();
	co.hello3();
	
	
 }
}