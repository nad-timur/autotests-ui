from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses  # Добавили маркировку courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем, что отображается заголовок "Courses"
    courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_be_visible()
    expect(courses).to_have_text("Courses")

    # Проверить наличие и текст блока "There is no results"
    results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results).to_be_visible()
    expect(results).to_have_text("There is no results")

    # Проверить наличие и видимость иконки пустого блока
    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(text).to_be_visible()
    expect(text).to_have_text("Results from the load test pipeline will be displayed here")
