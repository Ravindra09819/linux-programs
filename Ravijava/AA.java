import java.util.Scanner;
class AA
{
	public static void main(String args[])
	{
		Scanner so=new Scanner(System.in);
		int size,sum=0;
		System.out.println("Enter the size of array:");
		size=so.nextInt();
	    int x[]=new int[size];
	
	System.out.println("Enter "+size+" values");
	for(int i=0;i<size;i++)
	{
		x[i]=so.nextInt();
	}
	System.out.println("Entered values are as below:");
	for(int i=0;i<size;i++)
	{
		System.out.println(x[i]);
		sum=sum+x[i];
	}
	System.out.println("sum is:"+sum);
	}
}