import java.util.Locale;
import java.util.Scanner;

public class p1008 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		int funcNum = sc.nextInt();
		int hrsTrb = sc.nextInt();
		double valorHrs = sc.nextDouble();
		double salary = hrsTrb * valorHrs;
		
		System.out.println("NUMBER = " + funcNum);
		System.out.printf("SALARY = U$ %.2f\n" ,salary);
			
		sc.close();
	}
}
