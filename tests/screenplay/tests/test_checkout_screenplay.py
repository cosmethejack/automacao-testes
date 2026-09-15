from tests.screenplay.actors.actor_factory import create_actor

from tests.screenplay.tasks.login import PerformLogin
from tests.screenplay.tasks.add_to_cart import AddItemToCart
from tests.screenplay.tasks.checkout import ProceedToCheckout
from tests.screenplay.tasks.finish_order import FinishOrder

from tests.screenplay.questions.order_completed import OrderCompleted


def test_checkout_com_sucesso():

    actor = create_actor()

    try:

        actor.attempts_to(
            PerformLogin.with_credentials(
                "standard_user",
                "secret_sauce"
            )
        )

        actor.attempts_to(
            AddItemToCart.the_first_item()
        )

        actor.attempts_to(
            ProceedToCheckout.with_customer_data(
                "Damiao",
                "Timoteo",
                "35180-000"
            )
        )

        actor.attempts_to(
            FinishOrder.now()
        )

        assert OrderCompleted().resolve(actor)

    finally:
        actor.driver.quit()