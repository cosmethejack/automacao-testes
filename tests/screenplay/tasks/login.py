from screenpy import Performable
from tests.pages.login_page import LoginPage

class PerformLogin(Performable):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def perform_as(self, actor):
        page = LoginPage(actor.driver)
        
        page.open()
        page.login(self.user, self.password)
        
    @staticmethod
    def with_credentials(user, password):
        return PerformLogin(user, password)