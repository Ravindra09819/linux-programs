
class Main11d
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
	
	System.out.println("Program continues...");
   
  }
 }
 