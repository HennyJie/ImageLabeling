import sys

missingTk = False
missingIdle = False
if sys.version_info.major == 2:
    try:
        import Tkinter as tk
        import ttk
        import tkMessageBox as MessageBox
    except ImportError:
        missingTk = True

    try:
        from idlelib.ToolTip import ToolTip
    except ImportError:
        missingIdle = True

elif sys.version_info.major == 3:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
        from tkinter import messagebox as MessageBox
    except ImportError:
        missingTk = True

    try:
        from idlelib.tooltip import ToolTip
    except ImportError:
        missingIdle = True
else:
    raise EnvironmentError("You version of Python (%d) is not supported." % sys.version_info.major)

if missingTk:
    raise ImportError("Missing tkinter. Please install tkinter. On Ubuntu/Debian you can do apt-get install python-tk.")

if missingIdle:
    raise ImportError("Missing idlelib. Please install idle. On Ubuntu/Debian you can do apt-get install idle.")
