import java.util.PrimitiveIterator;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import javax.management.loading.PrivateClassLoader;

//多生产多消费
//描述资源。属性：商品名称和编号。  行为：对商品名称进行赋值，获取商品。
class Resource3{
	private String name;
	private int count=1;
	private boolean flag=false;
	
	private Lock lock=new ReentrantLock();
	
	private Condition condition=lock.newCondition();
	//对商品名称赋值
	public void set(String name) throws InterruptedException {
		//上锁
		lock.lock();
		try {
			while(flag) 
				condition.await();
			this.name=name+"--"+count++;
		System.out.println(Thread.currentThread().getName()+"....生产者...."+this.name);
		flag=true;
		//signal唤醒
		condition.signal();
		} finally {
			// TODO: handle finally clause
			//释放锁资源
			lock.unlock();
		}			
	}
	
	public void out() throws InterruptedException {
		lock.lock();
		try {
			while(!flag) 
				condition.await();
		//打印消费了哪个商品
		System.out.println(Thread.currentThread().getName()+"....消费者...."+this.name);
		flag=false;
		condition.signal();

		} finally {
			// TODO: handle finally clause
			lock.unlock();
		}		
	}
}

//描述生产者
class Producer3 implements Runnable{
	private Resource3 res;
	//生产者一初始化就要有资源，需要将资源传递到构造函数中
	public Producer3(Resource3 res) {
		// TODO Auto-generated constructor stub
		this.res=res;
	}
	public void run() {
		while (true) {
			try {
				res.set("面包");

			} catch (InterruptedException e) {
				// TODO: handle exception
			}
		}
	}
}
//描述消费者
class Consumer3 implements Runnable{
	private Resource3 res;
	//消费者一初始化就要有资源，需要将资源传递到构造函数中
	public Consumer3(Resource3 res) {
		// TODO Auto-generated constructor stub
		this.res=res;
	}
	public void run() {
		while (true) {
			try {
				res.out();
			} catch (InterruptedException e) {
				// TODO: handle exception
			}
		}
	}
}

public class ProducerConsumer3 {

	public static void main(String[] args) { 
		// TODO Auto-generated method stub
		Resource3 r=new Resource3();
		
		Producer3 pro=new Producer3(r);
		Consumer3 con=new Consumer3(r);
		
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





