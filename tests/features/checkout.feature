Feature: Fluxo de Compra e Checkout

  Scenario: Compra de produto com sucesso
    Given que o usuário está logado na aplicação
    And que o usuário adiciona um produto ao carrinho
    And que o usuário acessa o carrinho de compras
    When ele inicia o processo de checkout
    And ele preenche os dados de entrega com nome "Damiao", sobrenome "Barbosa" e CEP "30642"
    And ele confirma e finaliza o pedido
    Then a mensagem de sucesso "THANK YOU FOR YOUR ORDER" deve ser exibida
