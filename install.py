import winreg
import os

# Get the directory where the install.py file is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the script
script_path = os.path.join(script_dir, "process_zip_file.py")

# create a registry key for your script
key_path = r"Software\Classes\CompressedFolder\shell\Rename Images"
key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
winreg.SetValue(key, "", winreg.REG_SZ, "AI ZIP Rename Images")

# add a command to the key to run your script
command_path = os.path.abspath(script_path) + " \"%1\""
command_key = winreg.CreateKey(key, "command")
winreg.SetValue(command_key, "", winreg.REG_SZ, command_path)

print("Context menu item added successfully!")