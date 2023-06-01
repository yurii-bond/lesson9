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


class MainPage:
    """
    This is doc string of a class
    """
    counter = 0

    def __init__(self, name, url):
        # , url, xpath, driver):
        self.name = name
        self.url = url
        Page.counter += 1
        # self.url = url
        # self.xpath = xpath
        # self.driver = driver
        # print('ID of object {} '.format(id(self)))

    def get_name(self):
        return f"My name is {self.name}"

    def get_url(self):
        return f'The page url is {self.url}'

    def __del__(self):
        del self
        Page.counter -= 1

    @staticmethod
    def get_counter():
        print(Page.counter)

Page.get_counter()
a = Page('main')
Page.get_counter()
# a.

mp = MainPage('Main', 'https://')

# mp.

# print("Page class objects counter {}".format(Page.counter.__str__()))
# a = Page('Yurii')
#
# print("Page class objects counter {}".format(Page.counter.__str__()))
# b = Page('Alex')
#
# print("Page class objects counter {}".format(Page.counter.__str__()))
#
# # print(dir(Page))
# # print(a.__str__())
# print(a)
# print(a.get_name())
# print('ID of object a {} '.format(id(a)))
# print(b)
# print(b.get_name())
# print('ID of object b {} '.format(id(b)))
# print(Page.__doc__)
# print(a.__doc__)
# print(a.get_name().__doc__)

