import pytest

@pytest.fixture
def template_tier(request):
    template = request.config.getoption("--template")
    return int(template[-1])

@pytest.fixture
def context(template_tier):
    context = {
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
    if template_tier == 3 or template_tier == 4:
        context.update({
            "code_owners": "",
            "add_maintainer": False
        })
    return context

@pytest.fixture
def bakery(cookies_session, context):
    result = cookies_session.bake(extra_context={**context})
    yield result