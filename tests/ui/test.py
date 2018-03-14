from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select


def main():
    DesiredCapabilities.CHROME["unexpectedAlertBehaviour"] = "accept"
    chrome = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    chrome.get('http://prototyper:8000/')
    chrome.find_elements_by_css_selector('.nav a')[2].click()

    def invalid_input(input_field, btn_field, inputs=None):
        if inputs is None:
            inputs = ["", "_a", "12aa", "@dsa", "-ee", "~aqq", "as "]
        for input in inputs:
            input_field.send_keys(input)
            assert 'disabled' in btn_field.get_attribute('class')
            input_field.clear()

    def same_object(input_field, btn_field, name):
        input_field.send_keys(name)
        btn_field.click()
        chrome.switch_to.alert.accept()

    def test_project_add():
        try:
            project = chrome.find_element_by_xpath(
                '//div[contains(@class,"card-header") and contains(text(),"test_project")]')
            delete_btn = project.find_element_by_xpath('.//button')
            delete_btn.click()
        except NoSuchElementException:
            print('not found')
            pass
        sleep(0.1)

        input_field = chrome.find_element_by_xpath('//div[contains(@class,"input-group")]//input')
        field_add_btn = chrome.find_element_by_xpath('//div[contains(@class,"input-group")]//button')
        project_name = 'test_project'
        invalid_input(input_field, field_add_btn)
        input_field.send_keys(project_name)
        field_add_btn.click()
        same_object(input_field, field_add_btn, project_name)
        sleep(0.1)

    test_project_add()

    def test_model_add():
        project_header = chrome.find_element_by_xpath(
            '//div[contains(@class,"card-header") and contains(text(),"test_project")]')

        model_input = project_header.find_element_by_xpath('./following-sibling::div//input')
        model_add_btn = project_header.find_element_by_xpath('./following-sibling::div//button')
        model_name = 'test_model'
        model_input.send_keys(model_name)
        model_add_btn.click()

        same_object(model_input, model_add_btn, model_name)

        invalid_input(model_input, model_add_btn)

    test_model_add()

    def test_field_add():

        model_href = chrome.find_element_by_xpath('//a[text()="test_model"]')
        model_href.click()
        field_input = chrome.find_element_by_xpath('//div[@class="input-group"]/input')
        field_add_btn = chrome.find_element_by_xpath('//div[contains(@class,"input-group")]//button')
        invalid_input(field_input, field_add_btn)

        field_name = 'text'
        field_input.send_keys(field_name)
        field_add_btn.click()

        same_object(field_input, field_add_btn, field_name)
        field_tr = chrome.find_elements_by_xpath('//td//input/ancestor::tr')[0]
        type_field = field_tr.find_element_by_xpath('.//select')
        assert "TextField" == type_field.get_attribute('value')
        select = Select(type_field)
        select.select_by_visible_text("CharField")
        assert "CharField" == type_field.get_attribute('value')

        null_span = field_tr.find_element_by_xpath('.//span[contains(text(),"N")]')
        blank_span = field_tr.find_element_by_xpath('.//span[contains(text(),"B")]')
        unique_span = field_tr.find_element_by_xpath('.//span[contains(text(),"U")]')
        index_span = field_tr.find_element_by_xpath('.//span[contains(text(),"I")]')
        spans = [null_span, blank_span, unique_span, index_span]
        for span in spans:
            span.click()

        null_select = chrome.find_element_by_xpath(
            '//tr[contains(@class,"field-attr")]/td[contains(text(),"null")]/parent::tr//select')
        blank_select = chrome.find_element_by_xpath(
            '//tr[contains(@class,"field-attr")]/td[contains(text(),"blank")]/parent::tr//select')
        unique_select = chrome.find_element_by_xpath(
            '//tr[contains(@class,"field-attr")]/td[contains(text(),"unique")]/parent::tr//select')
        db_index_select = chrome.find_element_by_xpath(
            '//tr[contains(@class,"field-attr")]/td[contains(text(),"db_index")]/parent::tr//select')
        selects = [null_select, blank_select, unique_select, db_index_select]
        for select in selects:
            assert "true" in select.get_attribute('value').lower()
        for span in spans:
            span.click()
        for select in selects:
            assert not "true" in select.get_attribute('value').lower()

    test_field_add()
    chrome.save_screenshot('/tmp/screen.png')


main()
