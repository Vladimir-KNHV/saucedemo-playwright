from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'Image'