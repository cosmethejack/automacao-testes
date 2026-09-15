from screenpy import Ability
from screenpy_selenium.abilities import BrowseTheWeb as ScreenPyBrowse

class BrowseTheWeb(Ability):
    @staticmethod

    def using(driver):
        return ScreenPyBrowse.using(driver)
