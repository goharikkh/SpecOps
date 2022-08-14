#1
import os
import random
f = open('file', 'w')
while os.path.getsize("file") < 4:
    a = random.randint(0, 200)
    f.write(f'{a}\n')
f.close()
