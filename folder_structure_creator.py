import os
import time
from datetime import date

def get_files_content(layer_name= "Layer_Name", module_name= "Module_Name"):
    files_content = []
    current_date = date.today().strftime("%B %d, %Y")

    source_file        = open(file= "Files Content\\1- Source File Content.txt", mode= "r")
    interface_file     = open(file= "Files Content\\2- Interface File Content.txt", mode= "r")
    configuration_file = open(file= "Files Content\\3- Configuration File Content.txt", mode= "r")
    private_file       = open(file= "Files Content\\4- Private File Content.txt", mode= "r")

    source_file_content        = source_file.read()
    interface_file_content     = interface_file.read()
    configuration_file_content = configuration_file.read()
    private_file_content       = private_file.read()

    source_file_content = source_file_content.format(User_Name= user_name, Module_Name= module_name.replace("_"," "), module_name= module_name.lower(), Date= current_date)
    interface_file_content = interface_file_content.format(User_Name= user_name, Module_Name= module_name.replace("_"," "), module_name= module_name.lower(), MODULE_NAME= module_name.upper(), Date= current_date, LAYER_NAME= layer_name)
    configuration_file_content = configuration_file_content.format(User_Name= user_name, Module_Name= module_name.replace("_"," "), module_name= module_name.lower(), MODULE_NAME= module_name.upper(), Date= current_date, LAYER_NAME= layer_name)
    private_file_content = private_file_content.format(User_Name= user_name, Module_Name= module_name.replace("_"," "), module_name= module_name.lower(), MODULE_NAME= module_name.upper(), Date= current_date, LAYER_NAME= layer_name)

    files_content.append(source_file_content)
    files_content.append(interface_file_content)
    files_content.append(configuration_file_content)
    files_content.append(private_file_content)

    return files_content

def create_new_module(layer_name, module_name, module_path):
    os.system(f"cd {module_path}")
    os.system(f"mkdir {module_name}\\SOURCE")
    os.system(f"mkdir {module_name}\\INCLUDES")

    source_file        = open(file= f"{module_path}\\{module_name}\\SOURCE\\{module_name.lower()}.c", mode= "w")
    interface_file     = open(file= f"{module_path}\\{module_name}\\INCLUDES\\{module_name.lower()}.h", mode= "w")
    configuration_file = open(file= f"{module_path}\\{module_name}\\INCLUDES\\{module_name.lower()}_cfg.h", mode= "w")
    private_file       = open(file= f"{module_path}\\{module_name}\\INCLUDES\\{module_name.lower()}_prv.h", mode= "w")

    files_content = get_files_content(layer_name, module_name)
    
    source_file.write(files_content[0])
    interface_file.write(files_content[1])
    configuration_file.write(files_content[2])
    private_file.write(files_content[3])

if __name__ == "__main__":
    user_name = os.getenv("USERNAME").title()
    print(f"Welcome, {user_name}.", end= "\n\n")

    layer_name  = input("Layer name [MCAL - HAL]: ").strip().upper()
    module_name = input("Module name: ").strip().replace(" ","_")
    module_path = input("Module Path: ").strip('\"')

    create_new_module(layer_name, module_name, module_path)

    print("\n" + "\033[92m" + "Module created successfully." + "\033[0m")
    time.sleep(4)
