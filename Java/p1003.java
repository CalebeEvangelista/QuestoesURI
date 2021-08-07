import java.util.Scanner;

public class p1003 {
	public static void main (String[] args) {
	Scanner garotinho = new Scanner(System.in);
	
	int A,B,SOMA;
	
	A = garotinho.nextInt();
	B = garotinho.nextInt();
	SOMA = A + B;
	
	System.out.println("SOMA = " + SOMA);

	garotinho.close();
}
}