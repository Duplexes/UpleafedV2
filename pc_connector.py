import subprocess

# Fetches the list of all usb devices:
def get_usb():
    result = subprocess.run(['devcon', 'hwids', '=usb'],
        capture_output=True, text=True)
    print(result.stdout)

#subprocess.run(['devcon', 'disable', parsed_hwid]) # to disable
#subprocess.run(['devcon', 'enable', parsed_hwid]) # to enable