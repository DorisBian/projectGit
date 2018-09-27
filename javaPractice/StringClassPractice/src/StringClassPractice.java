//注重每个函数实现的思想方法

public class StringClassPractice {
    //判断字符串中有多少大写小写字母和数字
    public static void getMethod(String str){
        int upper=0;
        int lower=0;
        int digit=0;
        for (int i=0;i<str.length();i++){
            char c=str.charAt(i);
            //判断字符是大写小写还是数字，利用编码表65-90 97-122 48-57
            if(c>=65&&c<=90)
                upper++;
            else if(c>=97&&c<=122)
                lower++;
            else if(c>=48&&c<=57)
                digit++;
        }
        System.out.println("在此字符串中大写字母有"+upper+"个");
        System.out.println("小写字母有"+lower+"个");
        System.out.println("数字有"+digit+"个");
    }

    //将字符串首字母转成大写，其他转小写,subString(),获取字符串的一部分
    public static String switchUpperLower(String str){
        String first=str.substring(0,1);
        String after=str.substring(1);
        first=first.toUpperCase();
        after=after.toLowerCase();
        return first+after;
    }

    //查询在一个字符串中出现关键字字符串的次数
    /*
    思想：indexOf()找到字符串中第一次出现的索引位置
         找到的索引+被找字符串的长度，截取字符串
         计数器++
     */
    public static void getStringCount(String str,String key){
        int count=0;
        int index=0;
        while ((index=str.indexOf(key))!=-1){
            //获取到的索引，和字符串长度求和，截取字符串
            str=str.substring(index+key.length());
            count++;
        }
        System.out.println("在此字符串中，出现关键字字符串"+key+"的次数为"+count+"次");
    }


    public static void main(String[] args){
        String str1="1738bdmvshfvjbgr4879ddsfGDSFDHJVbhjvj7459vnjdvbghHSJVSLFUIVEKSHEDI";
        getMethod(str1);

        String str2="jdfndFKDFFFFFFBREIRDKLSFVjsfbbbbvvsjksk";
        System.out.println(switchUpperLower(str2));

        String str3="hdjskkjavahjdvsjavajdvhfuk836842935javajksfkkuetHGFVSBJAVAjava392582java";
        getStringCount(str3,"java");


    }
}
