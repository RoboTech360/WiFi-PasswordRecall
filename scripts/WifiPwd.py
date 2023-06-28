import subprocess

# Get the Wi-Fi profiles on the computer
profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Loop through each profile and get the password
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
except Exception as e:
    print(f"sorry, something happened.: {str(e)}")

# Prompt the user to press Enter to exit
input("There you go!   now hit Enter to exit...harder!")