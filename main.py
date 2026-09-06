import subprocess
import time
import re
import sys

def run_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"ERROR: {e.stderr.strip()}"

def get_user_choice():
    """Displays a menu for the user to choose the screen mode."""
    print("\nSELECT SCRCPY DISPLAY MODE:")
    print("1. Standard Mirroring (Clones your phone screen)")
    print("2. Virtual Display (Creates a separate 1920x1080 canvas)")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("❌ Invalid input. Please enter 1 or 2.")

def find_and_run():
    # Ask the user for their preferred display mode first
    mode_choice = get_user_choice()
    
    print("\nResetting ADB server to clear stale connections...")
    run_command("adb kill-server")
    run_command("adb start-server")
    
    print("📡 Scanning Wi-Fi network for your Android device (mDNS)...")
    time.sleep(3) # Give mDNS discovery 3 seconds to catch the broadcast
    
    devices_output = run_command("adb devices")
    
    # Search for the wireless debugging mDNS signature or an IP address format
    device_match = re.search(r'([^\s]+_adb-tls-connect\._tcp|192\.168\.\d+\.\d+:\d+)\s+device', devices_output)
    
    if device_match:
        device_id = device_match.group(1)
        print(f"\nFound active wireless device: {device_id}")
        
        # Build the scrcpy base command targeting the auto-discovered device ID
        base_cmd = f"scrcpy -s {device_id}"
        
        # Append the user's specific choice flags
        if mode_choice == '1':
            print("Launching Standard Mirroring...")
            scrcpy_command = base_cmd
        
        elif mode_choice == '2':
            print("Launching 1920x1080 Virtual Display...")
            scrcpy_command = f"{base_cmd} --new-display=1920x1080"
            
        subprocess.run(scrcpy_command, shell=True)
    else:
        print("\nError: No wireless debugging device found on the network.")
        print("Please make sure 'Wireless Debugging' is turned ON in your phone's Developer Options.")

if __name__ == "__main__":
    find_and_run()
