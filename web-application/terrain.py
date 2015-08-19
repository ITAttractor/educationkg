from datetime import datetime

from django.conf import settings
from django.core.management import call_command
from lettuce import before, after, world
from selenium import webdriver


def reinitialize_db():
    fixtures = ['geo', 'schools']
    call_command('reset_db', interactive=False, verbosity=1)
    call_command('migrate', interactive=False, verbosity=1)
    for fixture in fixtures:
        call_command('loaddata', fixture, interactive=False, verbosity=1)


@before.all
def init():
    reinitialize_db()
    world.browser = webdriver.Firefox()
    world.browser.maximize_window()
    world.browser.implicitly_wait(1)
    world.cache = {}


@after.all
def teardown(total):
    world.browser.quit()


@before.each_scenario
@before.outline
def clear_cookies_and_db(scenario, *args, **kwargs):
    world.browser.delete_all_cookies()
    world.cache = {}


@after.each_scenario
@after.outline
def take_screenshot(scenario, *args, **kwargs):
    if scenario.failed:
        date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        world.browser.get_screenshot_as_file('/tmp/%s-%s.png' % (date, scenario.name.replace(' ', '-')))
