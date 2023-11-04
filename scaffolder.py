from cookiecutter.main import cookiecutter

import os

def my_function(A,B,C):
    return A + B + C

cookiecutter(
    'https://github.com/DSACMS/repo-scaffolder.git',
    extra_context={'secret': my_function}, checkout='add-nested'
)