import os
import re
from pathlib import Path

from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)
print(os.getcwd(), "hi")

# Source: https://github.com/cookiecutter/cookiecutter-django/blob/f8897bfdff9681a28bc07b3361ab51bddb71a27c/tests/test_cookiecutter_generation.py
def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        print(str(path), "hi")
        path_obj = Path(path)

        if is_binary(str(path)) or ".git" in path_obj.parts:
            print("SKIP BINARY")
            continue

        if ".github" in path_obj.parts:
            print("SKIP .github")
            continue

        print("OPEN FILE")
        for line in path.open("r", encoding="utf-8"):
            match = RE_OBJ.search(line)
            assert match is None, f"cookiecutter variable not replaced in {path}"


# Source: https://github.com/cookiecutter/cookiecutter-django/blob/f8897bfdff9681a28bc07b3361ab51bddb71a27c/tests/test_cookiecutter_generation.py
def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        Path(dirpath) / file_path
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]


def check_temp_paths_are_removed(result):
    temp_paths = [
        result.project_path / "templates",
    ]

    for temp_path in temp_paths:
        assert not temp_path.exists()


# Source: https://github.com/cookiecutter/cookiecutter-django/blob/f8897bfdff9681a28bc07b3361ab51bddb71a27c/tests/test_cookiecutter_generation.py
def test_project_generation(context, result):
    """Test that project is generated and fully rendered."""

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()

    check_temp_paths_are_removed(result)

    paths = build_files_list(result.project_path)
    assert paths
    check_paths(paths)