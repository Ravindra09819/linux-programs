import java.util.Scanner;
class AB
{
	public static void main(String args[])
	{
		Scanner so=new Scanner(System.in);
		int rows,cols,sum=0;
		System.out.println("Enter the no.of rows:");
		rows=so.nextInt();
		System.out.println("Enter the no.of cols:");
		cols=so.nextInt();
	int x[][]=new int[rows][cols];
	
	System.out.println("Enter "+(rows*cols)+" values");
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<cols;j++)
		{
		x[i][j]=so.nextInt();
		}
	}
	System.out.println("Entered values are as below:");
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<cols;j++)
		{
		System.out.print(" "+x[i][j]);
		sum=sum+x[i][j];
		}
		System.out.println("\n");
	}
	System.out.println("sum is:"+sum);
	}
}