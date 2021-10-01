# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
# ages indexing starts with 0.

class Pagination:
    def __init__(self, data: str, num_char_per_page: int):
        self.data = data
        self.num_char_per_page = num_char_per_page
        self.pages = self.page_creator()
        print(self.pages)

    def page_creator(self) -> dict:
        num_iter = 0
        temp_pages = dict()
        for i in range(0, len(self.data), self.num_char_per_page):
            temp_pages[num_iter] = self.data[i:i + self.num_char_per_page]
            num_iter += 1
        return temp_pages

    def get_page_count(self) -> int:
        return len(self.pages)

    def get_item_count(self) -> int:
        return len(self.data)

    def items_on_page(self, num_page: int) -> int:
        try:
            out = len(self.pages[num_page])
        except BaseException:
            return f'{num_page} - invalid value'
        return out

    def display_page(self, num_page: int) -> str:
        try:
            out = len(self.pages[num_page])
        except BaseException:
            return f'{num_page} - invalid value'
        return self.pages[num_page]


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)

    print(pages.get_item_count())
    print(pages.get_page_count())

    print(pages.items_on_page('d'))
    print(pages.items_on_page(-1))

    print(pages.display_page(0))
