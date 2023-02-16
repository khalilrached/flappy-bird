import os
import pip
import platform


package_list = ["neat-python","pygame"]

PYTHON_PATH = ""

for path in os.get_exec_path():
    if path.lower().find("python") != -1:
        PYTHON_PATH = path
print(PYTHON_PATH)

if platform.system().lower() == "windows":
    for package in package_list:
        os.system(PYTHON_PATH + f"\\python.exe -m pip install {package}")
else:
    for package in package_list:
        os.system(PYTHON_PATH+f"/python -m pip {package}")