Feature: Login

  Scenario: Login válido
    Given que o usuário acessa a página de login
    When ele realiza login com usuário válido
    Then ele deve ser redirecionado para a página de inventário

  Scenario: Login com senha inválida
    Given que o usuário acessa a página de login
    When ele realiza login com senha inválida
    Then uma mensagem de erro deve ser exibida

  Scenario: Login com usuário bloqueado
    Given que o usuário acessa a página de login
    When ele realiza login com usuário bloqueado
    Then uma mensagem de bloqueio deve ser exibida