class Test07
{
	Test07()//constructor
	{
		System.out.println("Constructor");
	}
	static//static block
	{
		
		 System.out.println("Static Block");
	}
	//instance block
	{
		 System.out.println("Instance Block");
	}
	public void hello()
	{
		 System.out.println("method");
	}
	
	
  public static void main(String args[])
  {
    Test07 t=new Test07();
	t.hello();
	
  }
}