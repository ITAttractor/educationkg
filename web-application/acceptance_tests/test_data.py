from lettuce.django import django_url


class Urls:
    home = django_url('/')


class Xpath:
    school_search_title_input = './/input[@name="title"]'
    school_search_titles = './/div[@data-content="schools"]//a[@class="school-name"]'
    region_checkbox_by_title = './/div[@data-content="search-block"]//span[@class="region-label"][contains(text(), "%s")]/../label'
    map = "//div[@id='map']/*[name()='svg']/*[name()='path'][@data-slug='%s']"
    total_schools = "//div[@class='map-legend']//h3"
    district_dropdown = '//div[contains(@class, "district s-filter")]'
    subject_dropdown = '//div[contains(@class, "object s-filter")]'
    district_dropdown_item_with_text = '//div[contains(@class, "district s-filter")]//ul/li[contains(text(), "%s")]'
    subject_dropdown_item_with_text = '//div[contains(@class, "object s-filter")]//ul/li[contains(text(), "%s")]'
    first_school = "//section[@id='best-schools']//table/tbody/tr[1]/td[2]/a"
    first_school_average_result = "//section[@id='best-schools']//table/tbody/tr[1]/td[3]"
    check_result_name_input = "//form[@id='search-result-form']/input[@type='text']"
    check_result_submit_button = "//form[@id='search-result-form']//button[@type='submit']"
    result_with_name_link = "//div[@class='pupil-list']/ul/li/a[contains(text(), '%s')]"
    subject_with_result = "//div[contains(@class, 'popup-person')]//table//tr/td[1][contains(text(), '%s')]/../td[2][contains(text(), '%s')]/.."
