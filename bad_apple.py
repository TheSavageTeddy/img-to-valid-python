from strategies import Strategy
from frames_to_array import frame_to_array
import subprocess, time


target_string = "Bad Apple!!"
decimals = list(map(ord, target_string))


for framenumber in range(1, 6572 + 1):
    image_array = [[i for i in a] for a in frame_to_array(f"./frames/{framenumber}.jpg" ,1/7, 2/7)]
    strats = Strategy(target_string, image_array)
    bad_apple = strats.inlineFormat2()
    print(bad_apple)
    #print(framenumber, end="")
    #exec(bad_apple)
    #time.sleep(1)

# goddamn it actually works