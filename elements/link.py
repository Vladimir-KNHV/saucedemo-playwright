from elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'Link'
