import winreg
import sys

# The name of the key to remove
key_name = "Process Images"

try:
    # Open the "Shell" key in the registry
    shell_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "Directory\\shell", 0, winreg.KEY_ALL_ACCESS)
    try:
        # Delete the key
        winreg.DeleteKey(shell_key, key_name)
        print(f"{key_name} has been removed from the Windows context menu!")
    except FileNotFoundError:
        # If the key doesn't exist, print a message
        print(f"{key_name} was not found in the Windows context menu.")
    finally:
        # Close the "Shell" key
        winreg.CloseKey(shell_key)
except Exception as e:
    # If an error occurred, print an error message
    print(f"An error occurred while removing {key_name} from the Windows context menu: {str(e)}")
