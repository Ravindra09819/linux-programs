import java.util.Scanner;
class A1
{
public static void main(String args[])
{
Scanner so=new Scanner(System.in);
int n,r,sum=0;
System.out.println("enter any digit:");
n=so.nextInt();
while(n!=0)
{
r=n%10;//153%10 3 5 1
sum=sum+r;//0+3 3+5 8+1
n=n/10;//153/10; 153 15 1 
}
System.out.println("sum is:"+sum);
}
}
