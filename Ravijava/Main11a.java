class Main11a
{
  public static void main(String args[])
  {
	int x,y,z;
	x=10;
	y=0;
	try{
	z=x/y;
	System.out.println(z);
	}
	
	catch(ArithmeticException e)
	{
	  e.printStackTrace();
	}
	
	System.out.println("Program continues...");
   
  }
 }
 