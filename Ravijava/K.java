import java.util.Scanner;
class K
{
 public static void main(String args[])
 {
	 int n,i,j,sum=0;
	
	 Scanner so=new Scanner(System.in);
	                                                          
	                         
 System.out.println("enter the no of rows");
 i=so.nextInt();
   
   
	   System.out.println("enter the no of rows");
 j=so.nextInt();
 int x[][]= new int [i][j];
 {
	 for(i=0;i<=2;i++)
	   {
		   for(j=0;j<=5;j++){
			System.out.print(" "+x[i][j]); 
           sum=sum+x[i][j];		
		   }
		
	   }
	   
	   System.out.println("\n");
   }
   System.out.println("==================");
   System.out.println("sum is:"+sum);
    
 }
}
