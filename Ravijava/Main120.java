class A extends Thread 
{
	public void run()
	{
		for(int i=1;i<=10;i++)
		{
			try{
			if(i==3)
			{
				Thread.sleep(5000);
			}
			}
			catch(Exception e)
			{
				
			}
			System.out.println("A.."+i);
		}
	}
}
class B extends Thread 
{
	public void run()
	{
		for(int i=1;i<=10;i++)
		{
			System.out.println("B.."+i);
		}
	}
}
class C extends Thread 
{
	public void run()
	{
		for(int i=1;i<=10;i++)
		{
			System.out.println("C.."+i);
		}
	}
}
class Main120 
{
 public static void main(String args[])
 {
	A ao=new A();
	B bo=new B();
	C co=new C();
	
	ao.start();
	bo.start();
	co.start();
 }
}

