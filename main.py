from strategies import Strategy
from frames_to_array import frame_to_array
import subprocess, time


target_string = input("Enter your target string (must be less than height of image)")
decimals = list(map(ord, target_string))

height_scaling = float(input("Enter height scaling: "))
width_scaling = float(input("Enter width scaling: "))

image_path = input("Enter image path: ")

image_array = [[i for i in a] for a in frame_to_array(image_path ,height_scaling, width_scaling)]
strats = Strategy(target_string, image_array)
valid_code = strats.inlineFormat2()
print(valid_code)