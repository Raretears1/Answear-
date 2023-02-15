import pytest
from base_vars.bv_for_reg import *
from playwright.sync_api import Page


@pytest.fixture
def open_link(page: Page):
    page.goto(ANSWEAR_URL)
    if page.get_by_role("button", name="погодитися з усім").is_visible():
        page.get_by_role("button", name="погодитися з усім").click()
    page.locator("[data-test=\"my_account_icon\"]").click()
    page.locator("[id=\"_username\"]").click()
    page.locator("[id=\"_username\"]").fill(USERNAME)
    page.locator("[id=\"_password\"]").click()
    page.locator("[id=\"_password\"]").fill(PASSWORD)
    page.get_by_role("button", name="Увійдіть").click()
    return page
