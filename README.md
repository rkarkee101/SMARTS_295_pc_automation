# SMARTS_295_pc_automation
Automates SMARTS 295 pc using python


This code automates the inputs for SMARTS (Simple Model of the Atmospheric Radiative Transfer of Sunshine) developed by Dr. Christian Gueymard (https://www.nrel.gov/grid/solar-resource/smarts.html). For how to use SMARTS, please go to the website and read the manual (input descriptions).


Here, the automate.py can change the input file and run the software. 

Download the SMARTS from https://www.nrel.gov/grid/solar-resource/smarts.html.  Download or copy automate.py into the SMARTS folder containing smarts295bat.exe 

Before running, you need to edit the path to automate.py for example (executable_path = r'E:\Smarts\smarts-295-pc\SMARTS_295_PC\smarts295bat.exe' and input_file_path = r'E:\Smarts\smarts-295-pc\SMARTS_295_PC\smarts295.inp.txt')


The current code has few examples for latitude variation, working with different atmosphere model, and aerosols parameters. User can similarly follow for other variable change.
