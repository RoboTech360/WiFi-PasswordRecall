import subprocess
import logging

# Configure logging to write to a file
logging.basicConfig(filename='wifi_passwords.log', level=logging.INFO)

# Get the Wi-Fi profiles on the computer
profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Loop through each profile and get the password
for profile in profiles:
    if "All User Profile" in profile:
        profile_name = profile.split(":")[1].strip()
        try:
            password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8').split('\n')
            password = [line.split(":")[1].strip() for line in password if "Key Content" in line][0]
            message = f"Profile: {profile_name}\nPassword: {password}\n"
            print(message)
            logging.info(message)
        except subprocess.CalledProcessError:
            message = f"Profile: {profile_name}\nError couldn't retriev password, Oppsie Daisy\n"
            print(message)
            logging.warning(message)