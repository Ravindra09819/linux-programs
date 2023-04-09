import java.util.Scanner;
class Four
{
public static void main(String args[])
{
Scanner so=new Scanner(System.in);
int n;
double fat, snf,total,litre;
double rate=28;
	
System.out.println("how many days");
n=so.nextInt();
for(int i=1;i<=n;i++)
{
System.out.println("enter the fat");

fat=so.nextFloat();
System.out.println("enter the snf");
snf=so.nextFloat();
System.out.println("enter the liter");
litre=so.nextFloat();

while(n<0)
	
{
	System.out.println("the today rate");
	if(fat<=3.5&&snf<=8.5)
	{
		rate=24;
		System.out.print(rate);
	}
	else if(fat<=3.5&&snf<=8.6)
	{
			rate=24.50;
			System.out.print(rate);
	}
		else if(fat<=3.6&&snf<=8.6)
		{
			rate=24.60;
		}
			
		else if(fat<=4.0&&snf<=8.5)
		{
			rate=25.50;
			System.out.print(rate);
		}
			
		else if(fat<=4.2&&snf<=8.5)
			{
				rate=26.50;
				System.out.print(rate);
			}
		else if(fat<=1.5&&snf<=2.5)
			{
				rate=26.50;
				System.out.print(rate);
			}
	  else 
{
	rate=01.;
	System.out.print(rate);

}			
}

		{
			
			
		
      total=rate*litre;
System.out.println("the total amout");
System.out.println("fat\t"+"snf\t"+"litre\t"+"rate:\t"+"total RS:\t");
System.out.print(fat +" "+ snf +" "+litre+" "+ rate +" "+total);

System.out.println(total);


}

}

}
}

