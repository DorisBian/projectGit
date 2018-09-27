
/*
实现正则和字符串进行匹配，使用到字符串类的方法
String类和三个正则表达式相关的方法
boolean matches(String 正则的规则)  匹配成功返回true

String[] split(String 正则的规则） 切割字符串

String replaceAll(String 字符串，String 正则的规则)
 */
public class RegexDemo {
    //  要求：检查QQ号是否合法，0不能开头，全数字5，10位
    public static void checkQQ(){
        String QQ="123456";
        boolean b=QQ.matches("[1-9][0-9]{4,9}");//{4，9}表示除第一位外，后面最少有四位，最大有9位
        System.out.println(b);
    }

    //检查手机号码是否合法，要求：1开头，第二位可以是34578，0-9，位数固定11位
    public static void checkPhone(){
        String phoneNumber="13679764395";
        boolean b=phoneNumber.matches("1[34578][\\d]{9}");//[\\d]即[0-9]
        System.out.println(b);
    }

    //使用String类方法split()对字符串进行切割(切割后的返回值是数组)
    public static void split_1(){
        String str="21-86-92-10-95";
        String[] str_arr=str.split("-");
        System.out.println("数组的长度"+str_arr.length);
        for (int i=0;i<str_arr.length;i++){
            System.out.println(str_arr[i]);
        }
    }
    public static void split_2(){
        String str="21     8  6     92    10     95";
        String[] str_arr=str.split(" +");
        System.out.println("数组的长度"+str_arr.length);
        for (int i=0;i<str_arr.length;i++){
            System.out.println(str_arr[i]);
        }
    }

    //切割IP地址
    public static void split_3(){
        String str="192.168.106.27";
        String[] str_arr=str.split("\\.+");//让点在正则表达式中失去任意字符的含义
        System.out.println("数组的长度"+str_arr.length);
        for (int i=0;i<str_arr.length;i++){
            System.out.println(str_arr[i]);
        }
    }

    //将"helloHFH674359NDFHhsdjbfhv89250hsweveryone"里所有数字全部替换，ReplaceAll()
    public static void split_4(){
        String str="helloHFH674359NDFHhsdjbfhv89250hsweveryone";
        str=str.replaceAll("[\\d]+","#");
        System.out.println(str);
    }


    public static void main(String[] args){
        checkQQ();
        checkPhone();
        split_1();
        split_2();
        split_3();
        split_4();
    }
}
