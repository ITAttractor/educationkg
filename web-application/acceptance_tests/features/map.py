# coding=utf-8
from lettuce import step, world
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from acceptance_tests.test_data import Urls, Xpath


@step(u'пользователь наводит курсор на область "(?P<region>.+)"')
def user_hover_on_state(step, region):
    element = world.browser.find_element_by_xpath(Xpath.map % region)
    ac = ActionChains(world.browser)
    ac.move_to_element(element)
    ac.perform()


@step(u'видит количество школ "(?P<total_schools>.+)"')
def user_sees_total_schools(step, total_schools):
    element = world.browser.find_element_by_xpath(Xpath.total_schools)
    assert total_schools in element.text
