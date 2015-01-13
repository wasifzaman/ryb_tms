import os
import win32com.client
ws = win32com.client.Dispatch("wscript.shell")
shortcut_ = ws.CreateShortcut('build\\RYB Teacher Attendance.lnk')
shortcut_.TargetPath = os.path.abspath('build\\bin\\ryb_teacher_attendance.exe')
shortcut_.Save()