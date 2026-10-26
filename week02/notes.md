# lab1

1. **`pwd`** prints the path of the current working directory, showing exactly where the terminal is currently located.  
   It helps identify the current folder before running commands that depend on the working location.

2. **`ls -Force`** displays all files and folders, including hidden items that normal `ls` does not show.  
   This is useful for finding hidden folders such as `.venv` or hidden configuration files.

3. The **Mode** column indicates whether an item is a file or a directory and provides information about its type.  
   It helps distinguish folders from individual files when viewing the contents of a directory.

4. **`coding-cafe\week02`** is a relative path because it starts from the current working directory rather than the root location.  
   A relative path depends on the directory from which the command is being executed.

5. In the first command, **`mv`** moved the file from one folder to another specified location.  
   In the second command, `mv` was used with a different name, so it renamed the file instead.

6. The number of folders listed in the **PATH** environment variable depends on the computer and its installed programs.  
   Different software installations add different directories to PATH so their commands can be used from the terminal.

7. Python is installed at the location shown in the **Source** column when running `Get-Command python`.  
   This command searches the PATH and identifies which Python executable will be used by the shell.

8. The Python paths can be different on different computers because Python may be installed in different directories.  
   The installation method, user account, Python version, and computer configuration can all affect its location.

9. The shell reported that **`pyton`** was not recognized because the command was typed incorrectly.  
   Since there was no command with that name available through PATH, the shell could not execute it.

10. **`.venv`** did not appear when using normal `ls` because it is a hidden directory.  
    Running **`ls -Force`** displays hidden files and folders, making `.venv` visible.

11. **`(.venv)`** appeared at the beginning of the terminal prompt after activation.  
    This indicates that the Python virtual environment named `.venv` was successfully activated.

12. The Python path changed after activating the virtual environment because **`Activate.ps1`** modified the PATH.  
    It places the virtual environment's Python directory first, so its Python executable is used before the system Python.

13. The second **`pip list`** contained `requests` and its required dependencies, which were missing from the first list.  
    This happened because those packages were installed inside the virtual environment rather than the global Python environment.

14. After running **`deactivate`**, the terminal stopped using the virtual environment's Python installation.  
    Python then pointed back to the normal Python installation available outside the virtual environment.

15. The **`-Recurse`** flag tells a command to process not only the current directory but also its subdirectories.  
    It allows the command to search through the complete folder structure and include files inside nested folders.

16. **Ctrl + C** interrupts and stops a currently running program or command in the terminal.  
    **Ctrl + Z followed by Enter** sends an end-of-input signal, indicating that no more input is being provided.
