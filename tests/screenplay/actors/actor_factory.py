from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb

from tests.fixtures.driver import driver_func


def create_actor(name="Usuário"):
    driver = driver_func()

    actor = Actor.named(name).who_can(
        BrowseTheWeb.using(driver)
    )

    actor.driver = driver

    return actor