## Jupyter Notebooks in VS Code
[Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) (formerly IPython Notebook) is an open-source project that lets you easily combine Markdown text and executable Python source code on one canvas called a notebook. Visual Studio Code supports working with Jupyter Notebooks natively, and through Python code files

## Create a virtual environment
A best practice among Python developers is to use a project-specific virtual environment. Once you activate that environment, any packages you then install are isolated from other environments, including the global interpreter environment, reducing many complications that can arise from conflicting package versions. You can create non-global environments in VS Code using Venv or Anaconda with Python: Create Environment.  

Open the Command Palette `(Ctrl+Shift+P)`, start typing the Python: Create Environment command to search, and then select the command.

Ensure your new environment is selected by using the Python: Select Interpreter command from the Command Palette.  
Or use this command to active the venv `source venv/bin/activate` and this to stop `deactivate`

## Set Type Checking Level in VSCode GUI 

* Step 1: Install Pyright (or Pylance) Extension
  * Recommended — Pylance (includes Pyright) - Pylance is Microsoft's extension for Python that uses Pyright under the hood for type checking.
* Option 2: Install Pyright directly
  * You can install both, but Pylance is better integrated with the Python extension.

## By running makemigrations

* `python manage.py makemigrations polls`
* `python manage.py sqlmigrate polls 0001`
* `python manage.py migrate`
* `python manage.py shell`

# Creating an admin user
`python manage.py createsuperuser`