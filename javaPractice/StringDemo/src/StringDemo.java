
public class StringDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1="abc";//abc是一个对象
		String s2=new String("abc");
		
		//s1和s2区别：
		//s1在内存中有一个对象，s2在内存中有两个对象
		
		System.out.println(s1==s2);
		System.out.println(s1.equals(s2));
		

	}

}

