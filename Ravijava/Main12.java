import java.util.Scanner;
class A 
{
	public void hello1(int x,int y)
	{
		int z=x+y;
		
		System.out.println("sum is:"+z);
        		
		
		
	}
}

class Main12
{
 public static void main(String args[])
 {
	 Scanner so=new Scanner(System.in);
	 int a,b;
	 System.out.println("Enter two values:");
	 a=so.nextInt();
	 b=so.nextInt();
	A ao=new A();
	ao.hello1(a,b);
	
 }
}