import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main{

    public static void main(String[] args) throws InterruptedException {
        
        final int dayTime = 2400;
        String characteristic;
        
        Scanner scan = new Scanner(System.in);

        System.out.println("Hello!");
        Thread.sleep(2000);
        System.out.println("Welcome to the Scheduler App!");
        Thread.sleep(2000);
        System.out.println("The objective is to find the most efficent schedule for your day.");
        Thread.sleep(2000);
        System.out.println("So, lets get started!");
        Thread.sleep(2000);

        System.out.println("First, let's see what type of person you're!");
        Thread.sleep(2000);
        System.out.println("What type of person are you?");
        Thread.sleep(2000);
        System.out.println("Are you...");
        Thread.sleep(2000);
        System.out.printf("\n1: Balanced%n2: Fronthand%n3: Backhand%n");
        Thread.sleep(2000);

        while (true) { 
            System.out.println("\nChoose by typing 1, 2, or 3.");
            int chooseChar = scan.nextInt();
            int dumbCount = 0;

            if(dumbCount == 3){
                System.out.println("Hey buddy! Are you stupid? Type in 1, 2, 3");
            }

            if(dumbCount == 5){
                System.out.println("You're clearly dumb just give up.");
                System.exit(0);
                scan.close();
            }

            if (chooseChar == 1 || chooseChar == 2 || chooseChar == 3) {
                break; 
            } 
            
            else {
                System.out.println("The option you chose doesn't exist. Try again.");
                dumbCount++;
            }
        }

    }
}

