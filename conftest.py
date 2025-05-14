import pytest
from selene import browser

@pytest.fixture()
def browser():
    browser.config.window_width = 900
    browser.config.window_height = 1920
    browser.open('https://duckduckgo.com')