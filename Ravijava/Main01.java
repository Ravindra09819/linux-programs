




class A
{
	public void hello()
	{
		System.out.println("Hello I m in class A..");
	}
	public void hello1(int a,int b)
	{
		int c;
		c=a+b;
		System.out.println(c);

		//System.out.println("Hello I m in class A..");
	}

	public void hello2(int a,int b)
	{
		int c;
		c=a-b;
		System.out.println(c);

		//System.out.println("Hello I m in class A..");
	}

	
}
class Main01
{
 public static void main(String args[])
 {
	A ao=new A();
	ao.hello();
	ao.hello1(12,8);
	ao.hello2(12,8);
 }
}
