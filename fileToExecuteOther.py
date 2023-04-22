""" Test 1 : Failed
import file

exec(open('/sayHelloTestExec.py').read())
"""

""" Test 2 : failed
import os
import time

os.system('python3 ./sayHelloTestExec.py')

print("Héhé")
time.sleep(5)
print("Hoho")
"""

# Code fonctionnel par chat GPT
import subprocess
import time

# Exécuter le programme secondaire
process = subprocess.Popen(['python', './sayHelloTestExec.py'])

# Continuer à exécuter le programme principal
print("Héhé")
time.sleep(5)
print("Hoho")

# Attendre que le programme secondaire se termine
process.wait()
