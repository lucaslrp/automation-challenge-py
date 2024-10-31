import conftest


class BasePage:
    def __init__(self):
        self.browser = conftest.browser

    