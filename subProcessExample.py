import subprocess

x = subprocess.run(['cat', '/sys/kernel/accel/x'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)

print(x)