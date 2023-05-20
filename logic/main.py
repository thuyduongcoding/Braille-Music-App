import subprocess
import os
import converted
from music21 import *

def convert(image_file, mxl_path, output_path):
    try:
        
        # Converting image to musicXML file
        mxl_file = converted.convert_to_mxl(image_file, mxl_path)

        # Converting musicXML file to Braille format (.brf)
        subprocess.run(["python", "converted.py", "convert_to_braille(mxl_file)"], 
                       stdout=open(output_path + "/file.brf", "w"))
                
    except subprocess.CalledProcessError as e:
        print("Error invoking Audiveris.")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")

# Always use png file
image_file = "input/testing2.png"
mxl_path = "mxl"
output_path = "output"

convert(image_file, mxl_path, output_path)
