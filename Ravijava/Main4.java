import java.util.Scanner;
class Main4
{
 public static void main(String args[])
 {
	 Scanner so=new Scanner(System.in);
	int n,r,sum=0;
	
	  System.out.println("Enter any digit:");
	  n=so.nextInt();
	  
	  while(n!=0)
	  {
		  r=n%10;
		  sum=sum+r;
		  n=n/10;
	  }
	  System.out.println("Sum is:"+sum);
  
 }
}