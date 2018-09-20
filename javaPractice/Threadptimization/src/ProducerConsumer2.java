import java.util.PrimitiveIterator;

import javax.management.loading.PrivateClassLoader;

//多生产多消费
//描述资源。属性：商品名称和编号。  行为：对商品名称进行赋值，获取商品。
class Resource2{
	private String name;
	private int count=1;
	private boolean flag=false;
	//对商品名称赋值
	//加入同步synchronized来解决线程安全问题
	//  t1   t2
	public synchronized void set(String name) {
		//如果标记为真,
		//Q:被唤醒的线程如果没有判断标记,就会出现生产多个消费一个或者生产一个消费多个状况。
		//if换成while，多生产多消费，必须用while判断，要让被唤醒的线程再一次判断标记（出现在所有线程全部等待，只有一个线程可执行时）
		while(flag) {
			try {
				//wait和notify：等待唤醒机制，实现生产一个消费一个，多生产多消费
				wait();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		this.name=name+"--"+count++;
		System.out.println(Thread.currentThread().getName()+"....生产者...."+this.name);
		//将标记改为true
		flag=true;
		//唤醒线程池中等待的线程
		/*
		 * Q:换成while后死锁了（并非死锁，而是循环等待）
		 * 唤醒线程池中第一个等待的线程，notify唤醒了本方，改为notifyAll(),唤醒本方也唤醒对方
		 */
		this.notifyAll();
	}
	// t3    t4
	public synchronized void out() {
		//如果标记不为真
		while(!flag) {
			try {
				wait();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		//打印消费了哪个商品
		System.out.println(Thread.currentThread().getName()+"....消费者...."+this.name);
		flag=false;
		this.notify();
	}
}
//描述生产者
class Producer2 implements Runnable{
	private Resource2 res;
	//生产者一初始化就要有资源，需要将资源传递到构造函数中
	public Producer2(Resource2 res) {
		// TODO Auto-generated constructor stub
		this.res=res;
	}
	public void run() {
		while (true) {
			res.set("面包");
		}
	}
}
//描述消费者
class Consumer2 implements Runnable{
	private Resource2 res;
	//消费者一初始化就要有资源，需要将资源传递到构造函数中
	public Consumer2(Resource2 res) {
		// TODO Auto-generated constructor stub
		this.res=res;
	}
	public void run() {
		while (true) {
			res.out();
		}
	}
}

public class ProducerConsumer2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Resource2 r=new Resource2();
		
		Producer2 pro=new Producer2(r);
		Consumer2 con=new Consumer2(r);
		
		Thread t1=new Thread(pro);
		Thread t2=new Thread(con);
		Thread t3=new Thread(pro);
		Thread t4=new Thread(con);
		
		t1.start();
		t2.start();
		t3.start();
		t4.start();
	}

}
