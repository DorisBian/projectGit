public class RegexDemo2 {
    /*
    检查邮箱格式是否合法
    规则：@前面数字字母不能少于一个
         @后面数字或字母不少于一个
         .后面可以是字母
     */
    public static void checkEmail(){
        String email="12675386@sina.com.cn.org";
        boolean b=email.matches("[a-zA-Z0-9_]+@+[a-zA-Z0-9]+(\\.+[a-z]+)+");//加号表示前面的内容出现一次或多次，不是传统意义的加号
        System.out.println(b);
    }
    public static void main(String[] args){
        checkEmail();
    }
}
