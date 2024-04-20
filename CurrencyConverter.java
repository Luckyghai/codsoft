 import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double fromCurrency, toCurrency;
        double exchangeRate = 0.85; // 1 USD = 0.85 EUR, update this value as needed

        System.out.println("Enter amount in USD:");
        fromCurrency = input.nextDouble();

        toCurrency = fromCurrency * exchangeRate;

        System.out.println(fromCurrency + " USD is equivalent to " + toCurrency + " EUR.");
        input.close();
    }
}
 
    

