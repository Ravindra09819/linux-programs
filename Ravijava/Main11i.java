class Main
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
	catch(Exception e)
	{
	
	System.out.println("Its not possible.."+e);
	}
	
	System.out.println("Program continues...");
   
  }
 }
 