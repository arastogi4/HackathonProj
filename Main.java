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

                if(chooseChar == 1){
                    characteristic = "Balanced";
                }
        
                else if(chooseChar == 2){
                    characteristic = "Fronthand";
                }
        
                else if(chooseChar == 3){
                    characteristic = "Fronthand";
                }

                break; 
            } 
            
            else {
                System.out.println("The option you chose doesn't exist. Try again.");
                dumbCount++;
            }
        }

        System.out.println("Nice! Now let's start with your important events.");
        System.out.println("How many important events do you have today? (Type the number of events)");
        int importantEvents = scan.nextInt();
        scan.nextLine(); 
        String[][] iEvents = new String[importantEvents][2];

        System.out.println("How many extracurriculars are you doing today? (Type the number of events)");
        int extraEvents = scan.nextInt();
        scan.nextLine(); 
        String[][] exEvents = new String[extraEvents][2];

        System.out.println("What fun events are you doing today such as hanging out with friends? (Type the number)");
        int funEvents = scan.nextInt();
        scan.nextLine(); 
        String[][] fEvents = new String[funEvents][2];

        System.out.println("Lastly, what is the day today?");
        String weekDay = scan.nextLine();

        // important events
        System.out.println("For important events such as classes, meetings, etc., what are the events called?");
        for (int i = 0; i < iEvents.length; i++) {
            System.out.print("Event " + (i + 1) + ": ");
            iEvents[i][0] = scan.nextLine();
        }

        System.out.println("Now input the time for each event in minutes (e.g., 80 minutes is one hour and twenty minutes)");
        for (int i = 0; i < iEvents.length; i++) {
            System.out.print("Time for " + iEvents[i][0] + ": ");
            iEvents[i][1] = scan.nextLine();
        }

        System.out.println("Now enter the time this will be at. (Enter a number such as 5 to indictate the hour of day)");
        for (int i = 0; i < iEvents.length; i++) {
            System.out.print("Time of day for " + iEvents[i][0] + ": ");
            iEvents[i][2] = scan.nextLine();
        }

        // extracul
        System.out.println("Now, enter the names of your extracurricular events:");
        for (int i = 0; i < exEvents.length; i++) {
            System.out.print("Extracurricular " + (i + 1) + ": ");
            exEvents[i][0] = scan.nextLine();
        }

        System.out.println("Enter the duration (in minutes) for each extracurricular event:");
        for (int i = 0; i < exEvents.length; i++) {
            System.out.print("Time for " + exEvents[i][0] + ": ");
            exEvents[i][1] = scan.nextLine();
        }

        System.out.println("Now enter the time this will be at. (Enter a number such as 5 to indictate the hour of day)");
        for (int i = 0; i < iEvents.length; i++) {
            System.out.print("Time of day for " + exEvents[i][0] + ": ");
            iEvents[i][2] = scan.nextLine();
        }

        // fun events
        System.out.println("Now, enter the names of your fun events:");
        for (int i = 0; i < fEvents.length; i++) {
            System.out.print("Fun Event " + (i + 1) + ": ");
            fEvents[i][0] = scan.nextLine();
        }

        System.out.println("Enter the duration (in minutes) for each fun event:");
        for (int i = 0; i < fEvents.length; i++) {
            System.out.print("Time for " + fEvents[i][0] + ": ");
            fEvents[i][1] = scan.nextLine();
        }

        System.out.println("Now enter the time this will be at. (Enter a number such as 5 to indictate the hour of day)");
        for (int i = 0; i < iEvents.length; i++) {
            System.out.print("Time of day for " + fEvents[i][1] + ": ");
            iEvents[i][2] = scan.nextLine();
        }

        System.out.println("Schedule input complete!");
        Thread.sleep(2000);
        System.out.println("Let's see how your schedule looks!");


    }

    String TCNJCourseReader(String lol){
        return lol;
    }

    void PersonalityTest(){
        System.out.println("Do you prefer");
    }
}

