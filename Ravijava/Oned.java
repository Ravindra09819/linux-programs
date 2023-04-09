import java.util.*;
class Oned 
{
    public static void main(String args[])
    {
        Scanner so=new Scanner(System.in);
        int size,sum=0;
        System.out.print("Enter number of elements:");
        size=so.nextInt();

        int x[]=new int[size];
        for(int i=0;i<size;i++)
        {
            x[i]=so.nextInt();
            sum=sum+x[i];
        }


System.out.println("entered given elements below:");
for(int i=0;i<size;i++)
{
    System.out.println(" "+x[i]);
}
System.out.println("sum is:"+sum);
    }
}