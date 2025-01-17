import zipfile
import os
from termcolor import colored
from pyfiglet import figlet_format

def print_banner():
    banner = figlet_format("Zip Cracker")
    print(colored(banner, "cyan"))
    print(colored("Advanced Zip File Brute Force Tool", "yellow", attrs=["bold"]))
    print(colored("--------------------------------------------------", "cyan"))
    print(colored("Create By: Secure Horizon [ M.R.C005 ]", "green"))
    print(colored("YouTube  : https://www.youtube.com/@chamidunimsara20052", "yellow"))
    print(colored("Telegram : https://t.me/hackingword24", "blue"))
    print(colored("--------------------------------------------------", "cyan"))

def generate_password_list():
    print(colored("\nGenerating a default password list...", "yellow"))
    passwords = ["123456", "password", "admin", "letmein", "welcome"]
    with open("password_list.txt", "w") as file:
        file.write("\n".join(passwords))
    print(colored("Default password list generated: password_list.txt", "green"))

def create_custom_password_list():
    print(colored("\nCreating a custom password list...", "yellow"))
    passwords = []
    while True:
        password = input(colored("Enter a password (or type 'done' to finish): ", "blue"))
        if password.lower() == "done":
            break
        passwords.append(password)
    with open("custom_password_list.txt", "w") as file:
        file.write("\n".join(passwords))
    print(colored("Custom password list saved as: custom_password_list.txt", "green"))
    return "custom_password_list.txt"

def main():
    print_banner()

    while True:
        print(colored("\nOptions:", "magenta"))
        print(colored("1. Use your own password list", "magenta"))
        print(colored("2. Generate and use a default password list", "magenta"))
        print(colored("3. Create a custom password list", "magenta"))
        choice = input(colored("\nEnter your choice (1, 2, or 3): ", "blue"))

        if choice == "1":
            pwd_file = input(colored("\nEnter the path to your password file: ", "blue"))
            if not os.path.exists(pwd_file):
                print(colored("Password file not found. Please try again.", "red"))
                continue
        elif choice == "2":
            generate_password_list()
            pwd_file = "password_list.txt"
        elif choice == "3":
            pwd_file = create_custom_password_list()
        else:
            print(colored("Invalid choice. Please enter 1, 2, or 3.", "red"))
            continue
        break

    zip_file = input(colored("\nEnter the path to the zip file: ", "blue"))
    if not os.path.exists(zip_file):
        print(colored("Zip file not found. Exiting...", "red"))
        return

    try:
        zip_file_obj = zipfile.ZipFile(zip_file)
        with open(pwd_file, "r") as pwd_file_obj:
            for password in pwd_file_obj:
                password = password.strip()  # Remove any extra whitespace or newlines
                try:
                    zip_file_obj.extractall(pwd=password.encode())
                    print(colored(f"\nPassword found: {password}", "green"))
                    return
                except (RuntimeError, zipfile.BadZipFile):
                    continue
        print(colored("\nPassword not found in the list.", "red"))
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))

if __name__ == "__main__":
    main()
