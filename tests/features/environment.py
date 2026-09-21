import os
from datetime import datetime
import allure
from tests.fixtures.driver import driver_func
from tests.config.settings import Settings


def before_all(context):
    context.settings = Settings()
    os.makedirs("reports/screenshots", exist_ok=True)


def before_scenario(context, scenario):
    context.driver = driver_func()


def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        try:
            screenshot_bytes = context.driver.get_screenshot_as_png()
            allure.attach(
                screenshot_bytes,
                name=f"Evidencia_Falha_{step.name}",
                attachment_type=allure.attachment_type.PNG
            )
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            sanitized_name = "".join(c for c in step.name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
            file_name = f"failed_step_{timestamp}_{sanitized_name[:30]}.png"
            file_path = os.path.join("reports", "screenshots", file_name)
            with open(file_path, "wb") as f:
                f.write(screenshot_bytes)
        except Exception as e:
            print(f"Erro ao capturar screenshot do passo: {e}")


def after_scenario(context, scenario):
    if scenario.status == "failed" and hasattr(context, "driver"):
        try:
            screenshot_bytes = context.driver.get_screenshot_as_png()
            allure.attach(
                screenshot_bytes,
                name=f"Evidencia_Cenario_Falha_{scenario.name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            pass

    if hasattr(context, "driver"):
        context.driver.quit()