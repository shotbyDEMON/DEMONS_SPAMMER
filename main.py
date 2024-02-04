import os
import time
import pyautogui
import keyboard
from colorama import Fore, Style, init

# Global variable to store the selected GUI color
selected_color = Fore.RED

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(selected_color + r"""
  ╔══════════════════════════════════════╗
  ║           Welcome to the            ║
  ║      🌟  𝗗𝗲𝗺𝗼𝗻 𝗦𝗽𝗮𝗺𝗺𝗲𝗿  🌟      ║
  ║            😈😄😈😄😈               ║
  ║                                     ║
  ║  Main Features:                     ║
  ║   - FAST and FURIOUS spamming       ║
  ║   - GUI color change                ║
  ║   - Malevolent elegance              ║
  ║                                     ║
  ║  Press Enter to unleash the chaos!  ║
  ╚════════════════════════════════════╝
    """ + Style.RESET_ALL)

def main_menu():
    input(selected_color + "Press Enter to continue..." + Style.RESET_ALL)
    clear_screen()

def spam_menu():
    print(selected_color + "╔════════════════════════════════════╗" + Style.RESET_ALL)
    print(selected_color + "║               Spam Menu               ║" + Style.RESET_ALL)
    print(selected_color + "╠══════════════════════════════════════╣" + Style.RESET_ALL)
    print(selected_color + "║ Options:                             ║" + Style.RESET_ALL)
    print(selected_color + "║   1. Spammer                         ║" + Style.RESET_ALL)
    print(selected_color + "║   2. Change GUI color                ║" + Style.RESET_ALL)
    print(selected_color + "╚══════════════════════════════════════╝" + Style.RESET_ALL)

def choose_color():
    global selected_color

    clear_screen()  # Clear the command panel before changing the GUI color
    print(selected_color + "Choose a color from the rainbow:")
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for index, color in enumerate(rainbow_colors, start=1):
        print(f"{index}. {color}Sample text{Style.RESET_ALL}")
    
    while True:
        try:
            option = int(input(selected_color + "Option> " + Style.RESET_ALL))
            if 1 <= option <= len(rainbow_colors):
                selected_color = rainbow_colors[option - 1]
                print(f"{selected_color}GUI color has been changed!{Style.RESET_ALL}")
                break
            else:
                print(selected_color + "Invalid option. Please choose a valid color." + Style.RESET_ALL)
        except ValueError:
            print(selected_color + "Invalid input. Please enter a number." + Style.RESET_ALL)

def spam_message(message):
    print(selected_color + f"shotbyDEMON: Note - To stop the spam, press Alt key." + Style.RESET_ALL)
    
    try:
        while True:
            # Send the message using pyautogui
            pyautogui.write(message, interval=0.005)  # Faster interval for faster spamming
            pyautogui.press('enter')
            
            # Check if Alt key is pressed to stop spamming
            if keyboard.is_pressed('alt'):
                break

    except KeyboardInterrupt:
        print(selected_color + f"\n{Fore.RESET} {Style.RESET_ALL}{Style.BRIGHT} {selected_color}shotbyDEMON: {Style.RESET_ALL}Interrupted by the user. Quitting gracefully." + Style.RESET_ALL)

# Discord bypass function
def discord_bypass():
    try:
        # JavaScript to disable Discord chill zone message
        js_script = '''
        setTimeout(() => {
            document.querySelector('form.form_a88d78 button.primaryButton__78ebb').removeAttribute('disabled');
            document.querySelector('form.form_a88d78 button.primaryButton__78ebb div.contents_fb6220').innerText = '';
        }, 1000);
        '''
        pyautogui.press('f12')  # Open browser console (DevTools)
        pyautogui.write(js_script)  # Inject the JavaScript code
        pyautogui.press('enter')  # Execute the code
        pyautogui.press('f12')  # Close the browser console
        print(f"{selected_color}EvLGPT: Chill zone disabled on Discord tab.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{selected_color}EvLGPT: An error occurred while attempting Discord bypass: {e}{Style.RESET_ALL}")

# Password function
def check_password():
    password_attempt = input(selected_color + "Enter the password: " + Style.RESET_ALL)
    if password_attempt.lower() == "shotbydemon":
        print(Fore.GREEN + "Password correct and accepted" + Style.RESET_ALL)
        input(selected_color + "Press Enter to continue..." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Incorrect password. Exiting..." + Style.RESET_ALL)
        exit()

# Initialize colorama for colored text in the console
init()

# Check password before entering the tool
check_password()

# Clear the screen
clear_screen()

# Display the enhanced home page
print_banner()

# Display the main menu
main_menu()

# Display the options menu
spam_menu()

# Prompt user for option
while True:
    try:
        option = int(input(selected_color + "Option> " + Style.RESET_ALL))
        if option == 1:
            clear_screen()
            spam_input = input(f"{selected_color}shotbyDEMON: {Style.RESET_ALL}What message do you want to spam? ")
            discord_bypass()  # Call Discord bypass before spamming starts in Discord
            spam_message(spam_input)
            break
        elif option == 2:
            choose_color()
            clear_screen()
            print_banner()
            main_menu()
            spam_menu()
        else:
            print(selected_color + "Invalid option. Please choose a valid option." + Style.RESET_ALL)
    except ValueError:
        print(selected_color + "Invalid input. Please enter a number." + Style.RESET_ALL)
