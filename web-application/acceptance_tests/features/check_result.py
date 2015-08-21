# coding=utf-8
from time import sleep
from lettuce import step, world
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from acceptance_tests.test_data import Urls, Xpath

@step(u'пользователь вводит имя "(.*)"')
def user_input_name(step, name):
    element = world.browser.find_element_by_xpath(Xpath.check_result_name_input)
    element.send_keys(name)
    world.browser.find_element_by_xpath(Xpath.check_result_submit_button).click()


@step(u'нажимает кликает по ссылке "(.*)"')
def user_click_on_link_with_name(step, name):
    element = world.browser.find_element_by_xpath(Xpath.result_with_name_link % name)
    element.click()


@step(u'видит результат "(.*)" по предмету "(.*)"')
def user_sees_result_for_subject(step, result, subject):
    assert world.browser.find_element_by_xpath(Xpath.subject_with_result % (subject, result))