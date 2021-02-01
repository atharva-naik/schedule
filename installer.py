import os 
bash_reqs=['at']

print("\033[43m Installing requirements \033[0m")
with open("requirements.in", "r") as f:
    for line in f:
        line=line.strip()
        print(f"installing {line} !")
        os.system(f"pip install {line}")
    f.close() 

os.system("sudo apt-get update")
for bash_req in bash_reqs:
    print(f"installing {bash_req} !")
    os.system(f"sudo apt-get install {bash_req}")
os.system("clear")
print("\033[42m Build was succesfull! \033[0m")