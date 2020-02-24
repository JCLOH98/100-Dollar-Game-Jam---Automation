import cx_Freeze
from cx_Freeze import *

exe = [Executable("Wartomation.py",base = "Win32GUI")]

setup(name="War.tomation",
      version="",
      description="War.tomation created by JCLOH",
      options={"build_exe":{"packages":["pygame","math","time","random","sys"],
                            "include_files": ["music", "sprites", "font"]}
               },
      executables=exe
      )
