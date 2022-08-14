import pytest
from playwright.sync_api import expect


@pytest.mark.preload_page("simple_test.html")
def test_integration(page):
    expect(page.locator("id=foo")).to_have_text("My button!")
    page.click("id=foo")
    expect(page.locator("id=foo")).to_have_text("Updated Button!")
