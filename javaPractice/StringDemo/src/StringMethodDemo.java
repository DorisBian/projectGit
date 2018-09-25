import java.util.Iterator;

public class StringMethodDemo {
	
	public static void methodIs() {
		String str="ArrayDemo.java";
		sop(str.startsWith("Array"));
		sop(str.endsWith(".java"));
		sop(str.contains("Demo"));
	}
	
	//把字符数组中的一部分转化成字符串
	public static void methodSwitch() {
		char[] arr={'a','b','c','d','e','f'};
		String s=new String(arr,1,3);//构造函数
		sop("s="+s);
	}
	
	public static void methodGet() {
		String str="abcdef";
		sop(str.length());
		//根据索引获取字符
		sop(str.charAt(4));
		//根据字符获取索引
		sop(str.indexOf("e"));
		sop(str.indexOf("e",1));
		sop(str.indexOf("m", 3));
	}
	
	//将字符串转化成字符数组
	public static void charToArray() {
		String s="abhwjkrj";
		char[] ch=s.toCharArray();
		for (int i = 0; i < ch.length; i++) {
			sop(ch);
		}
	}
	//替换字符串
	public static void methodReplace() {
		String s="hello java";
		String s1=s.replace('a', 'x');
		sop(s);
		sop(s1);
	}
	//切割字符串
	public static  void methodSplit() {
		String s="zhangsan,lisi,wangwu";
		String[] arr=s.split(",");
		for (int i = 0; i < arr.length; i++) {		
			sop(arr[i]);		
		}
	}
	//获取子字符串
	public static void methodGetSubString() {
		String s="bkxlvbfivnm,bvn m,bvcmvbnvjdkkd";
		String s1=s.substring(3, 18);
		sop(s1);
	}
	//转换：将字符串转换成大写
	public static void switchUpperCase() {
		String s="sdvhblvbsb mnhrnvbvbndbjxnbvhvfk  chjd nmvnmr,cjvkvjreerk";
		String s1=s.toUpperCase();
		sop(s1);
	}
	//转换：将字符串转换成小写
	public static void switchLowerCase() {
		String s="JVKBLSSTBHMMHVRJKBA.JVBFV NFMSDM NCVNBV.JF  NMSDHBDBSVSVFM,F";
		String s1=s.toLowerCase();
		sop(s1);
	}
	//将字符串两端多余空格去除
	public static void deleteBlank() {
		String s="    cghvchksvgfvv    gfksfv     nekwgfwwfjrb      jfkjf,bfd   ";
		String s1=s.trim();
		sop(s1);
	}
	//对两个字符串进行自然顺序的比较
	public static void compare() {
		String s1="jvsfvn fvbdshvsb";
		String s2="vj,hvbfb,gbeihvdhfjgsdk";
		int i=s1.compareTo(s2);//-12表示s1<s2字符串参数
		sop(i);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		methodGet();
		methodIs();
		methodSwitch();
		charToArray();
		methodReplace();
		methodSplit();
		methodGetSubString();
		switchUpperCase();
		switchLowerCase();
		deleteBlank();
		compare();
	}
	
	public static void sop(Object obj) {
		System.out.println(obj);
	}

}
