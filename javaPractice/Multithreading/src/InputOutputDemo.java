/*
 * 线程间通讯其实就是多个线程在操作同一资源，但操作的动作不同
 * 不加同步会出现控制台输出错误,加锁要加同一把锁
 */

class Resource{
	String name;
	String sex;
	boolean flag=false;
}
class Input implements Runnable{
	private Resource r;
	Object obj=new Object();
	Input(Resource r){
		this.r=r;
	}
	public void run() {
		int x=0;
		while(true)
		{
			//参数写obj不对，与下面的那个同步不是同一个obj，不是同一把锁，参数里可写一个唯一的类，譬如Input.class，实际上参数写r就可以了，因为r唯一
			synchronized (r) {
				if(r.flag)
					try {
						wait();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				if (x==0) {
					r.name="mike";
				    r.sex="male";
				}
				else {
					r.name="doris";
					r.sex="female";
				}
				x=(x+1)%2;
				r.flag=true;
				notify();
			}
		}
	}
}
class Output implements Runnable{
	private Resource r;
	Object obj=new Object();
	Output(Resource r) {
		// TODO Auto-generated constructor stub
		this.r=r;
	}
	public void run() {
		while(true){
			synchronized (r) {
				if(!r.flag)
					try {
						wait();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				System.out.println(r.name+"....."+r.sex);
				r.flag=false;
				notify();
			}
		}
	}
}
public class InputOutputDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Resource r=new Resource();  //有一堆煤
		Input in=new Input(r);    //有两个卡车
		Output out=new Output(r);   
		
		Thread t1=new Thread(in);   //把两个卡车放在高速公路上
		Thread t2=new Thread(out);
		
		t1.start();   //两卡车启动
		t2.start();
	}

}
