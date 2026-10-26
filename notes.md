# PowerShell and Python Notes

1. `pwd` prints the path of the current working directory.

2. `ls -Force` shows hidden files and folders that normally do not appear with `ls`.

3. The **Mode** column tells us whether an item is a file or a directory.

4. `coding-cafe\week02` is a relative path because it starts from the current directory.

5. In the first command, `mv` moved the file to another folder. In the second command, it was used to rename the file.

6. There are **21 folders** in the `PATH` on my computer. The number can be different on other computers.

7. Python is located at the path shown in the **Source** column when using `Get-Command python`.

8. The paths may be different on different computers because Python can be installed in different locations.

9. The shell said that `pyton` was not recognized as a command because the command was typed incorrectly. Since the shell could not find a command with that name in the `PATH`, it gave an error.

10. `.venv` did not appear with the normal `ls` command because it is a hidden folder. Using `ls -Force` shows hidden items as well.

11. `(.venv)` appeared at the beginning of the prompt, which showed that the virtual environment had been successfully activated.

12. The Python path changed after activation. This means that `Activate.ps1` changed the `PATH` so that the Python inside the virtual environment is used first.

13. The second `pip list` included `requests` and its dependencies, which were not present in the first list.

14. After running `deactivate`, Python pointed back to the normal Python installation outside the virtual environment.

15. The `-Recurse` flag makes the command search through all subfolders and their contents.

16. `Ctrl + C` interrupts a running program, while `Ctrl + Z` followed by Enter sends the end-of-input signal.
