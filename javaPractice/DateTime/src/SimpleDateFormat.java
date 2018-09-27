import java.util.Date;
import java.text.DateFormat;
public class SimpleDateFormat {

    /*
    对日期进行格式化
    步骤：1.创建SimpleDateFormat对象，在类的构造方法中写入字符串的日期形式
         2.SimpleDateFormat调用format方法对日期格式化
         String format(Date date) 传递日期对象，返回字符串
         日期模式：yyyy-MM-dd:HH:mm:ss
     */

    public static void function(){
        /*StringBuilder sb=new StringBuilder();
        sb.append("yyyy年MM月dd日HH时mm分钟ss秒");
        SimpleDateFormat sdf=new SimpleDateFormat(sb.toString());
        String dateString=sdf.format(new Date());
        */
        SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd-HH:mm:ss");
        sdf.format();


    }


    public static void main(String[] args){
        function();

    }
}
