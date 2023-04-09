import java.util.*;
class Reverse
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
            sum=(sum*10)+r;
            n=n/10;
            
        }
        
        System.out.println("Rev is:"+sum);
    }
}