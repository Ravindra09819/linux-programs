import java.util.Scanner;
class Main3
{
 public static void main(String args[])
 {
	Scanner so=new Scanner(System.in);
	
	int roll;
	String name,city;
	System.out.println("Enter your name:");
	name=so.nextLine();
	System.out.println("Enter your Roll:");
	roll=so.nextInt();
	so.nextLine();
	System.out.println("Enter your City:");
	city=so.nextLine();
	       
	System.out.println("Entered Details are as Below:");
	System.out.println("Name is:"+name);
	System.out.println("Roll is:"+roll);
	System.out.println("City is:"+city);
 }
}