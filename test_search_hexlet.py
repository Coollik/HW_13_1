from selene import browser, be, have

def test_find_hexlet(browser):

    browser.element('[name="q"]').should(be.blank).type('hexlet').press_enter()
    browser.element('#r1-0 [class~="CXMyPcQ6nDv47DKFeywM"]').should(have.text('Хекслет — онлайн-школа программирования, онлайн-обучение ИТ-профессиям'))