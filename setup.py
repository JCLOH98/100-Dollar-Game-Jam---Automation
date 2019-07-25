import cx_Freeze
from cx_Freeze import *

exe = [Executable("Wartomation.py")]

setup(name="War.tomation",
      version="",
      description="War.tomation created by JCLOH",
      options={"build_exe":{"packages":["pygame"]}},
      executables=exe
      )
