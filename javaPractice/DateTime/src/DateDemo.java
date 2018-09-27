import java.util.Date;

public class DateDemo {
    /*
    时间和日期类：
    java.util.date
    毫秒的0点：System.currentTimeMillis()  返回long类型参数
    重点：时间和日期的计算，必须依赖毫秒值
    xxx-xxx-xx=毫秒值
     */

    //Date类空参数构造方法
    public static void function(){
        Date date=new Date();
        //获取到当前操作系统的时间和日期
        System.out.println(date);
    }

    public static void function_1(){
        Date date=new Date(4684392831943L);
        System.out.println(date);
    }

    /*
    Date类方法getTime()，返回值long
     */
    public static void function_2(){
        Date date=new Date();
        System.out.println(date.getTime());
    }

    public static void function_3() {
        Date date = new Date();
        System.out.println(date);
        date.setTime(0);
        System.out.println(date);
        //System.out.println(date.setTime(0));
    }




    public static void main(String[] args){
        long time=System.currentTimeMillis();
        System.out.println(time);

        function();
        function_1();
        function_2();
        function_3();
    }
}
