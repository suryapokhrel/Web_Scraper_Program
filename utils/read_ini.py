# utils/read_ini.py
import configparser
import os

def read_ini_file():
    ini_folder_path = 'C:\Users\ABC\Desktop\WebScrapinG\selenium\spider_Selenium\program\ini'  # Adjust the folder path as needed

    ini_file = None
    for filename in os.listdir(ini_folder_path):
        if filename.endswith(".ini"):
            ini_file = os.path.join(ini_folder_path, filename)
            break

    if ini_file is None:
        print("No Ini file found in the directory")
        exit(1)

    config = configparser.ConfigParser()
    with open(ini_file, 'r') as ini_content:
        ini_lines = ini_content.readlines()

    ecgains = None
    base_url = None
    module_name = None

    for line in ini_lines:
        if not line.startswith('//'):
            if line.strip().startswith('ECGAINS='):
                ecgains = line.strip().split('=', 1)[1].strip(';')
            elif line.strip().startswith('BaseURL='):
                base_url = line.strip().split('=', 1)[1].strip(';')
            elif line.strip().startswith('Name='):
                module_name = line.strip().split('=', 1)[1].strip(';')

    if ecgains is None or base_url is None or module_name is None:
        print("ECGAINS, BaseURL, or Name not found in the INI file.")
        exit(1)

    return ecgains, base_url, module_name
