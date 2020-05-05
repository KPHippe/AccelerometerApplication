import subprocess
from time import sleep
    
while(1):    
    x = subprocess.run(['cat', '/sys/kernel/accel/x'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)

    print(f"x: {x.stdout} ")
    y = subprocess.run(['cat', '/sys/kernel/accel/y'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)

    print(f"y: {y.stdout} ")
    z = subprocess.run(['cat', '/sys/kernel/accel/z'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)

    print(f"z: {z.stdout} ")

    sleep(1)
