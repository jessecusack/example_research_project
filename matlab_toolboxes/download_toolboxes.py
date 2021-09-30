import os
import zipfile
from urllib.request import urlretrieve

url = "https://www.eos.ubc.ca/%7Erich/m_map1.4.zip"

print(
    f"""Downloading:
{url}"""
)

urlretrieve(url, "m_map1.4.zip")

with zipfile.ZipFile("m_map1.4.zip", "r") as archive:
    archive.extractall()

os.remove("m_map1.4.zip")

url = (
    "https://github.com/jessecusack/example_matlab_toolbox/archive/refs/heads/main.zip"
)

print(
    f"""Downloading:
{url}"""
)

urlretrieve(url, "example_matlab_toolbox.zip")

with zipfile.ZipFile("example_matlab_toolbox.zip", "r") as archive:
    archive.extractall()

os.rename("example_matlab_toolbox-main", "example_matlab_toolbox")
os.remove("example_matlab_toolbox.zip")
os.remove(os.path.join("example_matlab_toolbox", ".gitignore"))
