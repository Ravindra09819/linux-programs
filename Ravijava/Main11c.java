class Main11c
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
	catch(ArrayIndexOutOfBoundsException e)
	{
	
	System.out.println("Array Exception"+e);
	}
	catch(NullPointerException e)
	{
	
	System.out.println("Null pointer."+e);
	}
	catch(ArithmeticException e)
	{
	
	System.out.println("Divide by zero."+e);
	}
	
	System.out.println("Program continues...");
   
  }
 }
 