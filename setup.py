import sys
from cx_Freeze import setup, Executable

build_exe_options = {}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includefiles = ['check_mark_sm.png',
				'halt_sm.png',
				'monet_sm.jpg',
				'ws_sm.png',
				'background_IMG.jpg',
				'bigbl.jpg',
				'RYB_Attendance.ico']

build_exe_options = {'include_files':includefiles, 'create_shared_zip': False}

setup(  name = "rybsms",
        version = "0.1",
        description = "RYB SMS",
        options = {"build_exe": build_exe_options},
        executables = [Executable("RYB Attendance.py",
        	targetName="RYB Teacher Attendance.exe",
        	base=base,
        	icon = "RYB_Attendance.ico")])
