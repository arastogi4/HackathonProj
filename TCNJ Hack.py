import time  # Make sure time is imported

def main():
    day_time = 2400

    print("Hello!")
    time.sleep(2)
    print("Welcome to the Scheduler App!")
    time.sleep(2)
    print("The objective is to find the most efficient schedule for your day.")
    time.sleep(2)
    print("So, let's get started!")
    time.sleep(2)

    print("First, let's see what type of person you are!")
    time.sleep(2)
    print("What type of person are you?")
    time.sleep(2)
    print("Are you...")
    time.sleep(2)
    print("\n1: Balanced\n2: Fronthand\n3: Backhand")
    time.sleep(2)

    dumb_count = 0

    while True:
        choice = input("\nChoose by typing 1, 2, or 3: ")

        if dumb_count == 3:
            print("Hey buddy! Are you stupid? Type in 1, 2, or 3.")

        if dumb_count == 5:
            print("You're clearly dumb just give up.")
            exit()

        if choice in {"1", "2", "3"}:
            break  
        else:
            print("The option you chose doesn't exist. Try again.")
            dumb_count += 1

if __name__ == "__main__":
    main()  # Ensure the function is actually called when running the script