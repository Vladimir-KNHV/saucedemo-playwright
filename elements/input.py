from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure
from tools.logger import get_logger
logger = get_logger("INPUT_ELEMENT")


class Input(BaseElement):

    @property
    def _type_of(self) -> str:
        return 'Input'

    def fill(self, value: str):
        step = f'Fill {self._type_of} with name "{self._name}" to value "{value}"'
        with allure.step(step):
            locator = self._get_locator()
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str):
        step = f'Checking {self._type_of} with name "{self._name}" have value "{value}"'
        with allure.step(step):
            locator = self._get_locator()
            logger.info(step)
            expect(locator).to_have_value(value)



