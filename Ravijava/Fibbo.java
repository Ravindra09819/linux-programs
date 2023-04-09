class Fibbo
{
    public static void main(String args[])
    {
        //Scanner so=new Scanner(System.in);
        int n1=0,n2=1,n3,sum=0;
        System.out.println(n1);
        System.out.println(n2);
        for(int c=1;c<=10;c++)
        {
            n3=n1+n2;
            System.out.println(n3);
            sum=sum+n3;
            n1=n2;
            n2=n3;
    }
     System.out.print("Sum is:"+sum);
        }
        
}