from lettuce.django import django_url


class Urls:
    home = django_url('/')


class Xpath:
    school_search_title_input = './/input[@name="title"]'
    school_search_titles = './/div[@data-content="schools"]//a[@class="school-name"]'
    region_checkbox_by_title = './/div[@data-content="search-block"]//span[@class="region-label"][contains(text(), "%s")]/../label'
