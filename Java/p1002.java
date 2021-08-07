import java.util.Scanner;
import java.util.Locale;
public class p1002 {

	public static void main (String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		double raio,n,area;
		
		raio = sc.nextDouble();
		n = 3.14159;	
		area = n * Math.pow(raio, 2);
		
		System.out.printf("A=%.4f%n" ,area);
		
		
	}
}
