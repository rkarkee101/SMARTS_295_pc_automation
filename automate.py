import subprocess
import os
import shutil
import time



def edit_variable_in_input_file(card_to_change, variable, input_file_path):
    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if card_to_change in line:
            components = line.split()
            if len(components) >= 3:
                # Check if the variable is a string or a number
                if isinstance(variable, str):
                    # Add quotation marks for string variables
                    components[0] = f"'{variable}'"
                else:
                    components[0] = str(variable)

                lines[i] = ' '.join(components) + '\n'
                break

    with open(input_file_path, 'w') as f:
        f.writelines(lines)



def run_external_software(executable_path):
    try:
        # Use subprocess.Popen to run the external software
        process = subprocess.Popen([executable_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Capture standard output and standard error
        stdout, stderr = process.communicate()

        # Check if the process exited successfully
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, process.args, output=stdout, stderr=stderr)
    except subprocess.CalledProcessError as cpe:
        print(f"CalledProcessError: {cpe}")
        print(f"Standard Output: {cpe.output}")

    except Exception as e:
        print(f"An error occurred while running the external software: {e}")

def main():
    

    #Path of executable, input file, and output file
    executable_path = r'E:\Smarts\smarts-295-pc\SMARTS_295_PC\smarts295bat.exe'
    input_file_path = r'E:\Smarts\smarts-295-pc\SMARTS_295_PC\smarts295.inp.txt'

    card_to_change='Card 2a' #####Change this  to change other parameters in loop
    latitudes = range(10, 25, 5)
    for latitude in latitudes:
        folder_name = f"output_latitude_{latitude}"
        os.makedirs(folder_name, exist_ok=True)

        edit_variable_in_input_file(card_to_change,latitude, input_file_path)

        print(f"Running for latitude: {latitude}")

        # Executing smarts295
        run_external_software(executable_path)

        # Introduce a delay (adjust the duration as needed)
        time.sleep(0.1)
        
        ### Copying files to other folders
        shutil.copy('smarts295.inp.txt', folder_name)
        shutil.copy('smarts295.ext.txt', folder_name)
        shutil.copy('smarts295.out.txt', folder_name)
    
        os.remove('smarts295.ext.txt')
        os.remove('smarts295.out.txt')
        
    ######## For working with different atmospheres
    # atomopheres=['USSA','MLS', 'MLW','SAS'] ####Add other if needed
    # card_to_change='Card 3a'
    # for atmos in atomopheres:
    #     folder_name = f"output_atmos_{atmos}"
    #     os.makedirs(folder_name, exist_ok=True)

    #     edit_variable_in_input_file(card_to_change,atmos, input_file_path)

    #     print(f"Running for Atmosphere variable: {atmos}")

    #     # Executing smarts295
    #     run_external_software(executable_path)

    #     # Introduce a delay (adjust the duration as needed)
    #     time.sleep(0.1)
        
    #     ### Copying files to other folders
    #     shutil.copy('smarts295.inp.txt', folder_name)
    #     shutil.copy('smarts295.ext.txt', folder_name)
    #     shutil.copy('smarts295.out.txt', folder_name)
        
    #     os.remove('smarts295.ext.txt')
    #     os.remove('smarts295.out.txt')

############ For working with different aerosols parameters
    # aerosols=['S&F_RURAL','S&F_URBAN', 'S&F_MARIT','S&F_TROPO'] ### Add other if needed
    # card_to_change='Card 8'
    # for aeros in aerosols:
    #     folder_name = f"output_atmos_{aeros}"
    #     os.makedirs(folder_name, exist_ok=True)

    #     edit_variable_in_input_file(card_to_change,aeros, input_file_path)

    #     print(f"Running for Atmosphere variable: {aeros}")

    #     # Executing smarts295
    #     run_external_software(executable_path)

    #     # Introduce a delay (adjust the duration as needed)
    #     time.sleep(0.01)
        
    #     ### Copying files to other folders
    #     shutil.copy('smarts295.inp.txt', folder_name)
    #     shutil.copy('smarts295.ext.txt', folder_name)
    #     shutil.copy('smarts295.out.txt', folder_name)
        
    #     os.remove('smarts295.ext.txt')
    #     os.remove('smarts295.out.txt')


if __name__ == "__main__":
    main()
