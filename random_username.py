import random
import time
import sys
import os

# List of fun words to combine for usernames
adjectives = ["Crazy", "Silly", "Funny", "Epic", "Wild", "Cool", "Lucky", "Happy", "Bright", "Shiny"]
nouns = ["Panda", "Unicorn", "Ninja", "Wizard", "Dragon", "Phoenix", "Pirate", "Robot", "Samurai", "Alien"]

# Function to generate a random username
def generate_username(length):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 999)
    
    # Combine parts and truncate to desired length
    username = f"{adjective}{noun}{number}"
    return username[:length]

# Function to display colorful text
def colorful_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(colorful_text(f"Usernames saved to {filename}!", "92"))  # Green text

# Function to animate text
def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Main program
def main():
    # Welcome message with animation
    animate_text(colorful_text("🎉 Welcome to the Random Fun Username Generator! 🎉", "96"))  # Cyan text
    time.sleep(1)

    # Ask for username length
    while True:
        try:
            length = int(input(colorful_text("Enter the desired username length (6-20): ", "93")))  # Yellow text
            if 6 <= length <= 20:
                break
            else:
                print(colorful_text("Please enter a length between 6 and 20.", "91"))  # Red text
        except ValueError:
            print(colorful_text("Invalid input. Please enter a number.", "91"))  # Red text

    # Ask how many usernames to generate
    while True:
        try:
            count = int(input(colorful_text("How many usernames would you like to generate? ", "93")))  # Yellow text
            if count > 0:
                break
            else:
                print(colorful_text("Please enter a number greater than 0.", "91"))  # Red text
        except ValueError:
            print(colorful_text("Invalid input. Please enter a number.", "91"))  # Red text

    # Generate usernames
    usernames = [generate_username(length) for _ in range(count)]

    # Display generated usernames
    print(colorful_text("\nHere are your generated usernames:", "94"))  # Blue text
    for username in set(usernames):
        print(colorful_text(username, "95"))  # Purple text

    # Save usernames to file
    save_option = input(colorful_text("\nWould you like to save these usernames to a file? (y/n): ", "93")).lower()
    if save_option == "y":
        save_usernames(usernames)
        time.sleep(1)
        print(colorful_text("Thank you for using the Random Fun Username Generator! 😊", "96"))  # Cyan text
    else:
        print(colorful_text("Thank you for using the Random Fun Username Generator! 😊", "96"))  # Cyan text

# Run the program
if __name__ == "__main__":
    main()