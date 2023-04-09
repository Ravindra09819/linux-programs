 import java.io.*;
import java.lang.String.*;

class text extends Thread
{
 String msg="";
 int  n;
 text(String msg,int n)
 {
  this.msg=msg;
  this.n=n;
 }
 public void run()
 {
  try
  { for(int i=1;i<=n;i++)
   {
    System.out.println(msg+" "+i+" times");
   }
  }
  catch(Exception e)
  {
	  System.out.println("not a initilized..");
  }
 }
}

public class Ravi10
{
 public static void main(String a[])
 {
	 int n=Integer.parseInt(a[0]);
  Ass_seta3 t1=new Ass_seta3("I am in FY",n);
  t1.start();
  Ass_seta3 t2=new Ass_seta3("I am in SY",n+10);
  t2.start();
  Ass_seta3 t3=new Ass_seta3("I am in TY",n+20);
  t3.start();
 }
}
