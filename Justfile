# Workflow on a new machine:
# 1. Initialize the virtual environment (just init-venv)
# 2. Activate the virtual environment (just activate-venv)
# 3. Install the requirements (just install)

# Initialize virtual env (once per machine)
init-venv:
  python3 -m venv .venv

# The source command to activate the python venv needs to be run in the shell
# Prompt the user with what to run
# This is basically just a reminder to the user
activate-venv:
  echo "run this:\nsource .venv/bin/activate"

# Deactivate the python venv
deactivate-venv:
  deactivate

# Install the python requirements and the npm packages
install:
  pip install -r requirements.txt

# Update the python requirements file with the current packages
freeze:
  mv requirements.txt requirements.txt.$(date +%Y%m%d%H%M%S).bak
  pip freeze > requirements.txt