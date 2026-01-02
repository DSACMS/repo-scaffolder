import pytest

@pytest.fixture
def context():
    return {
        "project_name": "Web Dashboard",
        "project_slug": "web_dashboard",
        "project_org": "DSACMS",
        "project_repo_name": "web-dashboard",
        "project_description": "This is a web dashboard.",
        "project_visibility": "private",
        "create_repo": False,
        "receive_updates": False,
        "add_team": False
    }

@pytest.fixture
def result(cookies, context):
    return cookies.bake(extra_context={**context})