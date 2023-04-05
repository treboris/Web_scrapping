import subprocess
import time


scripts = ['cvonline','it_people']
for x in scripts:
    script = f'python3 {x}.py'
    subprocess.Popen(script, shell = True)
