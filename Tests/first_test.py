from seleniumbase import BaseCase

url = "http://www.google.com"
lucky_button = "#gbqfbb"
agree_button = "#L2AGLb > div"
search_bar = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"
top_result = "#rso > div:nth-child(1) > div > div > div > div.yuRUbf > a > h3"
search_button = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b"


class MyFirstTest(BaseCase):
    def test_old_faithful(self):
        self.open(url)
        self.click(agree_button)
        self.click(lucky_button)

    def test_search(self):
        self.open(url)
        self.click(agree_button)
        self.type(search_bar, "Banana")
        self.click(search_button)
        self.assert_text("Banana - Wikipedia", top_result)

