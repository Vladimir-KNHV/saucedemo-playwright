from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'Button'