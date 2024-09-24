import subprocess
import shutil
import json
from cookiecutter.main import cookiecutter


if shutil.which('scc') is not None:
    try:
        #Run scc and load results into a dictionary
        #assuming we are in the .git directory of the repo
        d = json.loads(subprocess.run(["scc","..", "--format","json2"],check=True, capture_output=True).stdout)
        
        #inject a default value for labor hours calculated from scc
        cookiecutter(
            '.',
            extra_context={'labor_hours': d['estimatedScheduleMonths'] * 730.001}
        )
    except subprocess.CalledProcessError as e:
        print(e)
else:
    print("scc (https://github.com/boyter/scc) not found on system")

    #Otherwise just use previous value as a default value.
    cookiecutter(
        '.',
        extra_context={'labor_hours': 0}
    )