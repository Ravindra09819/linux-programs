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
	public void hello3()
	{
		for(int x=1;x<=10;x++)
		{
			System.out.println("For loop:"+x);
		}
		
	}
}
class Main14
{
 public static void main(String args[])
 {
	 
	A ao=new A();
	ao.hello1();
	ao.hello2();
	ao.hello3();
	ao.hello3();
	ao.hello3();
	ao.hello3();
	
 }
}