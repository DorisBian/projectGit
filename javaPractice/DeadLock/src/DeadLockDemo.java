import java.security.PublicKey;

/*死锁
 * 死锁出现情况在；同步中嵌套同步
 */
class Ticket implements Runnable{
	private int ticket=1000;
	Object obj=new Object();
	boolean flag=true;
	public void run() {
		if(flag)
		{
			while (true) {
				synchronized (obj) 
				{
					show();			
				}
			}
		}
		else 
		{
			while (true) {
				show();
				}				
			}
		}
		public synchronized void show(){//this
			synchronized (obj) {
				if (ticket>0)
			{
				try {
					Thread.sleep(10);
				} catch (Exception e) {
					// TODO: handle exception
				}
				System.out.println(Thread.currentThread().getName()+"...code:"+ticket--);
			}
		}			
	}
}


public class DeadLockDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Ticket t=new Ticket();
		
		Thread t1=new Thread(t);
		Thread t2=new Thread(t);
		t1.start();
		try {
			Thread.sleep(10);
		} catch (Exception e) {
			// TODO: handle exception
		}
		t.flag=false;
		t2.start();
				
	}

}
