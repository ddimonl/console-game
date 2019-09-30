## Run a Python script under Windows with the Command Prompt
Windows users must pass the path of the program as an argument to the Python interpreter. Such as follows:


`C:\Python27\python.exe C:\Users\Username\Desktop\my_python_script.py`

Note that you must use the full path of the Python interpreter. If you want to simply type python.exe `C:\Users\Username\Desktop\my_python_script.pyc` you must add python.exe to your PATH environmental variable.

## Run a Python Script Under Mac, Linux, BSD, Unix, etc
On platforms like Mac, BSD or Linux (Unix) you can put a "shebang" line as first line of the program which indicates the location of the Python interpreter on the hard drive. It's in the following format:

`!/path/to/interpreter`
A common shebang line used for the Python interpreter is as follows:

`!/usr/bin/env python`
You must then make the script executable, using the following command:


`chmod +x my_python_script.py`

Unlike Windows, the Python interpreter is typically already in the $PATH environmental variable, so adding it is un-necessary.

You can then run a program by invoking the Python interpreter manually as follows:

`python firstprogram.py`
