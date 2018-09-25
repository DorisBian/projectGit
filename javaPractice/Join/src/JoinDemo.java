

class Demo implements Runnable{
    public void run() {
        for(int x=0;x<70;x++)
            //System.out.println(Thread.currentThread().getName()+"...."+x);
            System.out.println(Thread.currentThread().toString()+"...."+x);

    }
}

public class JoinDemo {


    public static void main(String[] args) throws InterruptedException {
        // TODO Auto-generated method stub
        Demo d=new Demo();

        Thread t1=new Thread(d);
        Thread t2=new Thread(d);

        t1.start();

        //t1.join();//t1抢夺cpu执行权，主线程等待t1结束才开始运行
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.start();

        //t1.join();

        for(int x=0;x<80;x++)
            System.out.println("main....."+x);
        System.out.println("over");
    }

}

