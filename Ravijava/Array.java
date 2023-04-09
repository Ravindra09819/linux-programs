import java.util.*;
import java.io.*;

class Array
{
    public static void main(String args[])
    {
        Scanner so=new Scanner(System.in);
        int rows,cols,sum=0;
    
        System.out.println("Enter number of rows:");
           rows=so.nextInt();
           System.out.println("Enter number of cols:");
           cols=so.nextInt();
           int x[][]=new int [rows][cols];
           System.out.println("Enter "+(rows*cols)+" values:");

           for(int i=0;i<rows;i++)
           {
               for(int j=0;j<cols;j++)
               {
                   x[i][j]=so.nextInt();
               }
           }
           System.out.println("Entered values are below");
           for(int i=0;i<rows;i++)
           {
               for(int j=0;j<cols;j++)
               {
               System.out.print(" "+x[i][j]);
               sum=sum+x[i][j];
               }
               System.out.println("  ");
           }
           System.out.println("Sum is: "+sum);
               }
}