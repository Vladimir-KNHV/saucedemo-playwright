from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.image import Image
from elements.text import Text
from test_data.models.product_data import ProductItem
from elements.container import Container
import allure

class ItemViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._item = Container(page, '[data-test="inventory-item"]', 'item card')
        self._title = Text(page, '[data-test="inventory-item-name"]', 'item name')
        self._description = Text(page, '[data-test="inventory-item-desc"]', 'item description')
        self._price = Text(page, '[data-test="inventory-item-price"]', 'item price')
        self._image = Image(page, '[data-test="inventory-item"] > [class*="inventory"][class*="img"]', 'item image')
        self._add_cart_button = Button(page, 'button.btn_small', 'add to cart button')


    def check_visible(
            self,
            indexes: int | list[int] | None = None,
            added: bool = False,
            has_image: bool = True,
            has_button: bool = True
    ):

        if indexes is None:
            step_name = 'Check visible all items containers'
        else:
            step_name = f'Check visible item container at index "{indexes}"'

        with allure.step(step_name):
            if indexes is None:
                indexes = range(0, self._item.count())
            elif isinstance(indexes, int):
                indexes = [indexes]
            for index in indexes:
                self._item.check_visible(index)
                self._title.check_visible(index)
                self._description.check_visible(index)
                self._price.check_visible(index)

                if has_image:
                    self._image.check_visible(index)
                if has_button:
                    self._add_cart_button.check_visible(index)

                    if not added:
                        self._add_cart_button.check_have_text('Add to cart', index)
                    if added:
                        self._add_cart_button.check_have_text('Remove', index)

    @allure.step('Click add item to cart at index "{indexes}"')
    def click_add_to_cart_button(self, indexes: int | list[int]):
        if isinstance(indexes, int):
            self._add_cart_button.click(indexes)
            return
        for i in indexes:
            self._add_cart_button.click(i)

    @allure.step('Click remove item from cart at index "{indexes}"')
    def click_remove_button(self, indexes: int | list[int]):
        if isinstance(indexes, int):
            self._add_cart_button.click(indexes)
            return

        for i in indexes:
            self._add_cart_button.click(i)


    def get_item_data(self, indexes: int | list[int] | None = None) -> list[ProductItem]:
        if indexes is None:
            step_name = 'Get all items data'
        else:
            step_name = f'Get item data for indexes "{indexes}"'

        with allure.step(step_name):

            if indexes is None:
                indexes = range(0, self._item.count())
            elif isinstance(indexes, int):
                indexes = [indexes]

            return [
                ProductItem(
                    name=self._title.get_text(index),
                    description=self._description.get_text(index),
                    price=float(
                        self._price.get_text(index).replace('$', '')
                    ),
                )
                for index in indexes
            ]

    @allure.step('Get all prices')
    def get_all_prices(self) -> list[float]:
        return [float(p.replace('$', '')) for p in self._price.get_all_texts()]

    @allure.step('Get all names')
    def get_all_names(self) -> list[str]:
        return self._title.get_all_texts()

    @allure.step('Click remove button by name')
    def click_remove_by_name(self, names: list):
        for name in names:
            with allure.step(f"Click remove: {name}"):
                name = name.lower().replace(' ', '-')
                locator = f'//*[@data-test="remove-{name}"]'
                self._page.locator(locator).click()

    def open_item_page(self, index: int):
        with allure.step(f'Open item page at index "{index}"'):
            self._title.click(index)

