# coding=utf-8
from lettuce import step, world
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from acceptance_tests.test_data import Urls, Xpath

@step(u'пользователь выбирает район "(?P<district>.+)"')
def user_select_district(step, district):
    district_dropdown = world.browser.find_element_by_xpath(Xpath.district_dropdown)
    district_dropdown.click()
    district_dropdown_item = world.browser.find_element_by_xpath(Xpath.district_dropdown_item_with_text % district)
    district_dropdown_item.click()


@step(u'пользователь выбирает предмет "(?P<subject>.+)"')
def user_select_subject(step, subject):
    subject_dropdown = world.browser.find_element_by_xpath(Xpath.subject_dropdown)
    subject_dropdown.click()
    subject_dropdown_item = world.browser.find_element_by_xpath(Xpath.subject_dropdown_item_with_text % subject)
    subject_dropdown_item.click()


@step(u'пользователь видит в списке школу "(?P<school>.+)" на первом месте')
def user_sees_first_school(step, school):
    element = world.browser.find_element_by_xpath(Xpath.first_school)
    assert school in element.text


@step(u'пользователь видит средний результат "(?P<average_result>.+)"')
def user_sees_average_result_fro_first_schools(step, average_result):
    element = world.browser.find_element_by_xpath(Xpath.first_school_average_result)
    assert average_result in element.text