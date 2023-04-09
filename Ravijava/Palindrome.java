import java.util.*;
class Palindrome
{
    public static void main(String args[])
    {
        int n,r,sum=0;
        
        Scanner so=new Scanner(System.in);
        System.out.println("Enter the number :");
        n=so.nextInt();
        int temp=n;
        while(n>0)
        {
            r=n%10;
            sum=(sum*10)+r;
            n=n/10;



            
        }
        if(temp==sum)
        {
            System.out.println("is palindrome number");
        }
        else
        {
            System.out.println("is not palindrome number");
        }
        
    }
}