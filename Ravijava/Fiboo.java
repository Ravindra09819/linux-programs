class Fiboo
{
public static void main(String args[])
{
int n1=0,n2=1,n3;
System.out.println(n1);
System.out.println(n2);
for(int c=1;c<=10;c++)
{
n3=n1+n2;
System.out.println(n3);
n1=n2;
n2=n3;
}
}
}