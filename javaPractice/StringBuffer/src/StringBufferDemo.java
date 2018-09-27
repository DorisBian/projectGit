public class StringBufferDemo {

    public static void function(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1.5).append(7).append('c').append("djskbchj");
        System.out.println(sBuffer);
    }
    public static void function_1(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1.5).append(7).append('c').append("djskbchj");
        sBuffer.delete(0,9);
        System.out.println(sBuffer);
    }
    public static void function_2(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1.5).append(7).append('c').append("djskbchj");
        sBuffer.insert(3,"HELLO");
        System.out.println(sBuffer);
    }
    public static void function_3(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1.5).append(7).append('c').append("djskbchj");
        sBuffer.replace(2,6,"worldxxxxxxxxxx");
        System.out.println(sBuffer);
    }
    public static void function_4(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1.5).append(7).append('c').append("djskbchj");
        sBuffer.reverse();
        System.out.println(sBuffer);
    }
    public static void function_5(){
        StringBuffer sBuffer=new StringBuffer();
        sBuffer.append("hdsvkevitgth").append(1234567789).append(7).append('c').append("djskbchj");
        //将可变的字符串缓冲区对象，编变成了不可变的String对象
        sBuffer.toString();
        System.out.println(sBuffer);
    }

    //将数组转换成字符串形式
    public static String toString(int[] arr){
        //创建字符串缓冲区
        StringBuffer stringBuffer=new StringBuffer();
        stringBuffer.append("[");
        //数组遍历
        for (int i=0;i<stringBuffer.length();i++){
            //判断是不是数组最后一个元素
            if(i!=arr.length-1)
                stringBuffer.append(arr[i]).append(",");
            else
                stringBuffer.append(arr[i]).append("]");
        }
        return stringBuffer.toString();
    }


    public static void main(String[] args){
        function();
        function_1();
        function_2();
        function_3();
        function_4();
        function_5();

        int[] arr={1,2,3,7,0,9};
        System.out.println(toString(arr));
    }
}
