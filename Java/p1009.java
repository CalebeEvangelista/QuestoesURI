import java.util.Locale;
import java.util.Scanner;

public class p1009 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		String nome = sc.next();
		double salario = sc.nextDouble();
		double vendas = sc.nextDouble();
		double comissao = vendas * 0.15;
		double total = salario + comissao;
		
		System.out.printf("TOTAL = R$ %.2f\n" ,total);
			
		sc.close();
	}
}
