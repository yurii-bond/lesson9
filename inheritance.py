class Page:
    """
    This is doc string of a class
    """
    counter = 0

    def __init__(self, name):
        # , url, xpath, driver):
        self.name = name
        Page.counter += 1
        # self.url = url
        # self.xpath = xpath
        # self.driver = driver
        # print('ID of object {} '.format(id(self)))

    def get_name(self):
        return f"My name is {self.name}"

    def __del__(self):
        del self
        Page.counter -= 1

    @staticmethod
    def get_counter():
        print(Page.counter)


class MainPage(Page):
    def __init__(self, name, url):
        Page.__init__(self, name)
        # super().__init__(self)
        self.url = url

    def get_url(self):
        return f'The page url is {self.url}'

    def get_name(self):
        print(self.name)


a = MainPage("MainPage", 'Https://')

a.get_name()
print(a.get_url())
Page.get_counter()
MainPage.get_counter()

print(MainPage.__mro__)
