class A 
{
	public void hello()
	{
		for(int i=1;i<=10;i++)
		{
			if(i==5)
			{
				Thread.sleep(5000);
			}
		System.out.println(i);
		}
	}
}
class Main11h
{
  public static void main(String args[])
  {
	 A ao=new A();
	 ao.hello();
	
   
  }
 }