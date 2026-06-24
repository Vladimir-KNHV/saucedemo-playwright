from elements.base_element import BaseElement
from enums.sort_option import SortOption
from playwright.sync_api import expect
import allure
from tools.logger import get_logger
logger = get_logger("DROPDOWN_ELEMENT")

class Dropdown(BaseElement):

    @property
    def _type_of(self) -> str:
        return 'Dropdown'


    def sort(self, option: SortOption):
        step = f'{self._type_of} sort with value {option.name}'
        with allure.step(step):
            locator = self._get_locator()
            logger.info(step)
            locator.select_option(value=option.value)

    def check_selected_option(self, option: SortOption = SortOption.NAME_AZ):
        step = f'Check {self._type_of} selected option is "{option.name}"'
        with allure.step(step):
            locator = self._get_locator()
            logger.info(step)
            expect(locator).to_have_value(option.value)
