import pytest
from allure_commons._allure import step
from dotenv import load_dotenv
import os



def pytest_addoption(parser):
    parser.addoption(
        "--test-rail-result",
        dest="test-rail-result",
        type=bool,
        default=False,
        help="Add the result to Testrail.",
    )
    parser.addoption(
        "--run",
        dest="run",
        type=str,
        default="local",
        help="Run tests locally or in CI/CD.",
    )


def pytest_configure(config):
    load_dotenv()  # Load environment variables from a .env file if present

    # Load environment variables from pytest.ini
    env_vars = config.inicfg.get('env', '')
    for env_var in env_vars.split('\n'):
        if env_var.strip():
            key, value = env_var.split('=', 1)
            os.environ[key.strip()] = value.strip()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="session", autouse=True)
def get_config(request):
    pytest.testrail_result = request.config.getoption("--test-rail-result")
    pytest.run_type = request.config.getoption("--run")

