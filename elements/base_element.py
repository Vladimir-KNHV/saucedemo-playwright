from playwright.sync_api import Page, Locator, expect
import allure
from tools.logger import get_logger

logger = get_logger('BASE_ELEMENT')


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self._page = page
        self._locator = locator
        self._name = name

    @property
    def _type_of(self) -> str:
        return 'base element'

    def _get_locator(self, index: int | None = None) -> Locator:
        if index is None:
            step = f'Getting locator "{self._locator}"'
        else:
            step = f'Getting locator "{self._locator}" with index "{index}"'

        with allure.step(step):
            logger.info(step)
            locator = self._page.locator(self._locator)

            if index is not None:
                locator = locator.nth(index)

            return locator

    def click(self, index: int | None = None):
        step = f'Clicking {self._type_of} with name "{self._name}"'
        with allure.step(step):
            logger.info(step)
            locator = self._get_locator(index)
            locator.click()

    def check_visible(self, index: int | None = None):
        step =f'Checking {self._type_of} with name "{self._name}" is visible'
        with allure.step(step):
            logger.info(step)
            locator = self._get_locator(index)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, index: int | None = None):
        step = f'Checking {self._type_of} with name "{self._name}" have text "{text}"'
        with allure.step(step):
            logger.info(step)
            locator = self._get_locator(index)
            expect(locator).to_have_text(text)

    def check_have_contain_text(self, text: str, index: int | None = None):
        step = f'Checking {self._type_of} with name "{self._name}" have contain text "{text}"'
        with allure.step(step):
            logger.info(step)
            locator = self._get_locator(index)
            expect(locator).to_contain_text(text)

    def get_text(self, index: int | None = None) -> str:
        if index is None:
            step = f'Getting text from {self._type_of} with name "{self._name}"'
        else:
            step = f'Getting text from {self._type_of} with name "{self._name}" with index {index}'

        with allure.step(step):
            locator = self._get_locator(index)
            return locator.inner_text()

    def get_all_texts(self) -> list[str]:
        step = f'Getting all texts from {self._type_of} with name "{self._name}"'
        with allure.step(step):
            logger.info(step)
            return self._get_locator().all_inner_texts()





