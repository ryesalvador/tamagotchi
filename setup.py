# setup.py
from distutils.core import setup
import py2exe, sys, os
from glob import glob

# The following code is a work around hack for excluded DLLs.
origIsSystemDLL = py2exe.build_exe.isSystemDLL

def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:                                                 
               return 0
       return origIsSystemDLL(pathname)

py2exe.build_exe.isSystemDLL = isSystemDLL

# This is where to put additional noncode files that are needed by the project.
data_files = [(".", [],
               "Microsoft.VC90.CRT",
               glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup_dict = dict(
    windows = [{"script": "tamagotchi.py",
                "icon_resources": [(1, "myicon.ico")],
                "dest_base": "tamagotchi"}],
    zipfile = None,
    # This tells py2exe to exclude the list.
    options = {"py2exe": { "bundle_files": 1,
                           "dll_excludes": ["AppKit",
                                            "Foundation",
                                            "Numeric",
                                            "OpenGL.GL",
                                            "_scproxy",
                                            "_sysconfigdata",
                                            "copyreg",
                                            "dummy.Process",
                                            "numpy",
                                            "pkg_resources",
                                            "queue",
                                            "winreg",
                                            "pygame.sdlmain_osx",
                                            "kernel32.dll",
                                            "libogg-0.dll",
                                            "gdi32.dll",
                                            "ws2_32.dll",
                                            "advapi32.dll",
                                            "winmm.dll",
                                            "ole32.dll",
                                            "shell32.dll",
                                            "user32.dll",
                                            "ntdll.dll",
                                            "oleaut32.dll",
                                            "shlwapi.dll",
                                            "rpcrt4.dll",
                                            "msvcrt.dll"]}},
    data_files = data_files
)

setup(**setup_dict)
setup(**setup_dict)
