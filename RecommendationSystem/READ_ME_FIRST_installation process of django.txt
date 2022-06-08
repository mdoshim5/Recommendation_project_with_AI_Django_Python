1. install python
2. create virtual environment for django
	i. goto any folder
	ii. run "py -m venv <foldername>" example: py -m venv virtual_env_for_django
	iii. now run "foldername\Scripts\activat.bat" example: virtual_env_for_django\Scripts\activat.bat
	iv. now run pip install Django
	v. now run django-admin

3. to store the extra libraries run command
	i. pip freeze > requirements.txt
4. to install the extra libraries from the requirements.txt file run command:
	i. pip install -r requirements.txt