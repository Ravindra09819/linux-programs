class A 
{
	public void hello()throws Exception
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
class Main11j
{
  public static void main(String args[])throws Exception
  {
	 A ao=new A();
	 ao.hello();
	
   
  }
 }