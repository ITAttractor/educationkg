# coding: utf-8
from lettuce import step, world
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from acceptance_tests.test_data import Urls, Xpath


@step(u'пользователь открывает главную страницу')
def user_opens_main_page(step):
    world.browser.get(Urls.home)


@step(u'пользователь указывает в поисковой форме строку "(.*)"')
def user_fills_title_input(step, title):
    title_input = world.browser.find_element_by_xpath(Xpath.school_search_title_input)
    title_input.clear()
    for char in title:
        title_input.send_keys(char)


@step(u'пользователь видит в списке следующие школы')
def user_sees_following_schools(step):
    while True:
        try:
            schools = world.browser.find_elements_by_xpath(Xpath.school_search_titles)
            schools_titles = [school.text for school in schools]
            break
        except StaleElementReferenceException:
            pass
    for school in step.hashes:
        WebDriverWait(world.browser, 10).until(lambda driver: school['title'] in schools_titles)


@step(u'пользователь выбирает регион "(.*)"')
def user_selects_region(step, region_title):
    region_checkbox = world.browser.find_element_by_xpath(Xpath.region_checkbox_by_title % region_title)
    region_checkbox.click()
