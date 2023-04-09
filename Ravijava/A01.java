
class A
{
	public void hello()
	{
		System.out.println("Hello I m in class A..");
	}
	public void hello1(int a,int b)
	{
int c=0;
c=a+b;
System.out.println(c);
	}
}
class A01
{
 public static void main(String args[])
 {
	A ao=new A();
	ao.hello();
ao.hello1(9,8);
ao.hello1(99,1);
 }
}
