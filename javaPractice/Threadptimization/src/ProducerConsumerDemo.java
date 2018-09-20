import java.util.PrimitiveIterator;

import javax.management.loading.PrivateClassLoader;

//描述资源。属性：商品名称和编号。  行为：对商品名称进行赋值，获取商品。
class Resource{
	private String name;
	private int count=1;
	private boolean flag=false;
	//对商品名称赋值
	//加入同步synchronized来解决线程安全问题
	public synchronized void set(String name) {
		//如果标记为真
		if (flag) {
			try {
				//wait和notify：等待唤醒机制，实现生产一个消费一个，多生产多消费
				wait();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		//给成员变量赋值并加上编号，且编号自增
		this.name=name+"--"+count++;
		//打印生产了哪个商品
		System.out.println(Thread.currentThread().getName()+"....生产者...."+this.name);
		//将标记改为true
		flag=true;
		//唤醒线程池中等待的线程
		this.notify();
	}
	public synchronized void out() {
		//如果标记不为真
		if (!flag) {
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
class Producer implements Runnable{
	private Resource res;
	//生产者一初始化就要有资源，需要将资源传递到构造函数中
	public Producer(Resource res) {
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
class Consumer implements Runnable{
	private Resource res;
	//消费者一初始化就要有资源，需要将资源传递到构造函数中
	public Consumer(Resource res) {
		// TODO Auto-generated constructor stub
		this.res=res;
	}
	public void run() {
		while (true) {
			res.out();
		}
	}
}

public class ProducerConsumerDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建资源对象
		Resource r=new Resource();
		
		//创建线程任务
		Producer pro=new Producer(r);
		Consumer con=new Consumer(r);
		
		//创建线程
		Thread t1=new Thread(pro);
		Thread t2=new Thread(con);		
		
		//开始线程
		t1.start();
		t2.start();
	}

}
