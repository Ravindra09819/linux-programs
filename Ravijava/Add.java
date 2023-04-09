import java.util.*;
class Add
{
    public static void main(String args[])
    {
        int n,r,sum=0;
        Scanner so=new Scanner(System.in);
        System.out.println("Enter the number");
        n=so.nextInt();
        while(n>0)
        {
            r=n%10;
            sum=sum+r;
            n=n/10;

          //sum=sum+x[i][j];
            

        }
        System.out.println("Sum is:"+sum);
    }
}