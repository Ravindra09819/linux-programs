import java.util.Scanner;
class A 
{
	public int hello1(int x,int y)
	{
		return x+y;
		
	}
	
}

class Main11
{
 public static void main(String args[])
 {
	 Scanner so=new Scanner(System.in);
	 int a,b;
	 System.out.println("Enter two values:");
	 a=so.nextInt();
	 b=so.nextInt();
	A ao=new A();
	System.out.println("sum is:"+ao.hello1(a,b));
	
 }
}