import pytest
from selene import browser

@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 900
    yield
    browser.quit()