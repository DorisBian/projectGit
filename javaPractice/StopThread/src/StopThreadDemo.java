/*
 * Q:如何停止线程
 * A:控制住循环，让run方法结束
 * 特殊情况：当线程处于冻结状态时，就不会读取到标记，线程也不会结束。
 * 当没有指定的方式让线程恢复到正常状态时，需对冻结进行清除。
 * interrupt方法。

 */

class StopThread implements Runnable{
	private boolean flag=true;
	public synchronized void run() {
		while (flag) {
			try {
				wait();
			} catch (InterruptedException e) {
				// TODO: handle exception
				System.out.println(Thread.currentThread().getName()+"....Exception");
			}
			System.out.println(Thread.currentThread().getName()+"....run");
		}
	}
	public void changeFlag() {
		flag=false;
	}
}

public class StopThreadDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StopThread sThread=new StopThread();
		
		Thread t1=new Thread(sThread);
		Thread t2=new Thread(sThread);
		/*
		* 当运行的线程全为守护线程时，虚拟机退出。
		* 该方法必须在启动线程前调用。
		*/	 
		t1.setDaemon(true);
		t2.setDaemon(true);

		t1.start();
		t2.start();
		
		int num=0;
		while (true) {
			if (num++==60) {
				//sThread.changeFlag();
				//t1.interrupt();
				//t2.interrupt();
				break;
			}
		System.out.println(Thread.currentThread().getName()+"...."+num);
		}
	System.out.println("over");
	}
}
