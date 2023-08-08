[![Python application to learn Git hub Actions](https://github.com/sumathikotthuri/python-learnings/actions/workflows/dev-continous-integration.yml/badge.svg)](https://github.com/sumathikotthuri/python-learnings/actions/workflows/dev-continous-integration.yml)


# python-learnings


1. Create a Python Virtual Environment using 'virtualenv ~/.venv'
2. Setting venv in bashfile using 'vim ~/.bashrc' . This will open the bash file. In the end of the add below:
    # Sourcing Python Virtual Environment
    source ~/.venv/bin/activate
3. To check the virtual env, you will see a + icon next to bash, if we click the +. you will see .venv activated with (.venv) as a before to username
4. Creating the required empty files :Make file, Requirements file, main.py for micro services, Docker File, Project related Library folder and files like __init__.py
    1. touch requirements.txt
    2. touch Dockerfile
    3. touch Makefile
    4. mkdir projectlib
    5. touch projectlib/__init__.py
    6. touch projectlib/api.py
    7. touch main.py
5. Populate the Make file
6. Popuate the Requirements file with all install details required.
7. Run 'make install'
8. Then attach the versions to requirements file. First list the versions of install using 'pip freeze | less' . This command will list all installations with versions.
9. Go to Git Hub actions, then write work flow yaml file. You can get the sample workflow file python from git hub searck workflow bar.
10. Check out this project workflow file, which execution on push to this repository.
11. Configured pre-commit hooks file , How to configure pre-hooks ? Details here : https://github.com/sumathikotthuri/github-learnings
12.
