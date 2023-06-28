import subprocess
import logging

# Configure logging to write to a file
logging.basicConfig(filename='wifi_passwords.log', level=logging.INFO)

# Get the Wi-Fi profiles on the computer
profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Prompt the user to choose an option
print("Select an option: 1, 2 or 3")
print("1. Retrieve password for a specific profile/SSID")
print("2. Show Wifi password for all profile/SSID once")
print("3. Log all passwords to a file")
option = input("Option: ")

if option == "1":
    # Prompt the user to select a profile
    print("Type Wi-Fi profile to retrieve the password for:")
    for profile in profiles:
        if "All User Profile" in profile:
            profile_name = profile.split(":")[1].strip()
            print(f"- {profile_name}")
    profile_name = input("Profile name: ")

    # Get the password for the selected profile
    try:
        password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8').split('\n')
        password = [line.split(":")[1].strip() for line in password if "Key Content" in line][0]
        print(f"Profile: {profile_name}\nPassword: {password}\n")
    except subprocess.CalledProcessError:
        print(f"Profile: {profile_name}\nError: Couldn't retrieve password\n")
    except IndexError:
        print(f"Profile: {profile_name}\nPassword not found, something happened...\n")

elif option =="2":
            try:
                for profile in profiles:
                    if "All User Profile" in profile:
                        profile_name = profile.split(":")[1].strip()
                        try:
                            password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8').split('\n')
                            password = [line.split(":")[1].strip() for line in password if "Key Content" in line][0]
                            print(f"Profile: {profile_name}\nPassword: {password}\n")
                        except subprocess.CalledProcessError:
                            print(f"Profile: {profile_name}\nError Couldn't retriev password\n")
            #except Exception as e:
            except IndexError:
                logging.info(f"Profile: {profile_name}\nError: sorry, something happened\n")
                #print(f"sorry, something happened.: {str(e)}")         

elif option == "3":
    # Log all passwords for the profiles
    for profile in profiles:
        if "All User Profile" in profile:
            profile_name = profile.split(":")[1].strip()
            try:
                password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8').split('\n')
                password = [line.split(":")[1].strip() for line in password if "Key Content" in line][0]
                logging.info(f"Profile: {profile_name}\nPassword: {password}\n")
            except subprocess.CalledProcessError:
                logging.info(f"Profile: {profile_name}\nError: Couldn't retrieve password\n")
            except IndexError:
                logging.info(f"Profile: {profile_name}\nPassword not found, something happened...\n")

    print("Passwords logged to 'wifi_passwords.log' file.")

else:
    print("Invalid option.")

# Prompt the user to press Enter to exit
input("There you go!   now hit Enter to exit...")
