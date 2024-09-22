import os
import pytest

@pytest.fixture(scope="session")
def shared_data():
    return {}

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        with open('failures', mode) as f:
            if 'browser' in item.fixturenames:
                web_driver = item.funcargs['browser']
                screenshot = web_driver.get_screenshot_as_base64()
                f.write(f"FAILURE: {item.nodeid}\n")
                f.write(f"Screenshot: data:image/png;base64,{screenshot}\n")
