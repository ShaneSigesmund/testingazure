%USERPROFILE%\AppData\Local\Programs\Python\Python310\python -m venv venv
venv\Scripts\python -m pip --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install wheel
venv\Scripts\python -m pip --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install -r requirements.txt