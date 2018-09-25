class ThreadTest implements Runnable{
	public void run() {
		
	}
}
public class ThreadTestDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(){
			public void run() {
				for(int x=0;x<100;x++)
				{
					System.out.println(Thread.currentThread().getName()+"...."+x);
				}
			}
		}.start();
		
		
				for(int x=0;x<100;x++)
		{
			System.out.println(Thread.currentThread().getName()+"...."+x);
		}
			
		Runnable r=new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				for(int x=0;x<100;x++)
				{
					System.out.println(Thread.currentThread().getName()+"...."+x);
				}
			}
		};
		new Thread(r).start();	
	}
}
