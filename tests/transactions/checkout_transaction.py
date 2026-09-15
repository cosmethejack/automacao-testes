def do(self, **kwargs):
    driver = self._driver
    wait = WebDriverWait(driver, 10)

    print("URL antes do checkout:", driver.current_url)

    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )

    driver.execute_script(
        "arguments[0].click();",
        checkout_btn
    )

    time.sleep(2)

    print("URL depois do checkout:", driver.current_url)

    wait.until(
        EC.presence_of_element_located(
            (By.ID, "first-name")
        )
    )

    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys(kwargs.get("name"))

    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys(kwargs.get("last"))

    driver.find_element(
        By.ID,
        "postal-code"
    ).send_keys(kwargs.get("zip_code"))

    print(
        "Primeiro nome:",
        driver.find_element(
            By.ID,
            "first-name"
        ).get_attribute("value")
    )

    continue_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )

    driver.execute_script(
        "arguments[0].click();",
        continue_btn
    )

    time.sleep(2)

    print(
        "URL depois do continue:",
        driver.current_url
    )

    return driver.current_url