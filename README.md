# Automação de Testes e QAOps

Projeto de automação de testes E2E para o [SauceDemo](https://www.saucedemo.com/) utilizando múltiplos padrões de arquitetura e pipeline contínuo de QAOps com relatórios executivos no **Allure Report** e publicação no **GitHub Pages**:

- **PyTest**: Testes funcionais e Page Objects.
- **Guará (PTP)**: Page Transactions Pattern.
- **Screenplay**: Arquitetura orientada a Atores, Habilidades, Tarefas e Questões via ScreenPy.
- **Behave (BDD)**: Especificação em linguagem Gherkin com cenários executáveis e rastreamento de cada passo no Allure.

---

## 🚀 QAOps & Relatórios Dinâmicos

O projeto conta com uma esteira automatizada no **GitHub Actions** que:
1. Executa a suíte de testes de interface (PyTest, Screenplay e Behave BDD).
2. Captura **automaticamente screenshots** de falhas (com destaque para o fluxo de checkout/compra).
3. Agrega todos os resultados no formato **Allure Report** com histórico de tendências de execuções anteriores.
4. Faz o deploy contínuo do dashboard interativo no **GitHub Pages**.

> 📊 **Acesse o Dashboard Online**:
> `https://<seu-usuario>.github.io/<seu-repositorio>/` *(configurado após a primeira execução da branch `gh-pages`)*.

---

## 🛠️ Instalação de Dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧪 Execução dos Testes

### 1. PyTest Specs (Page Objects & PTP) com Allure
```bash
python -m pytest tests/specs --alluredir=reports/allure-results
```

### 2. Screenplay Tests com Allure
```bash
python -m pytest tests/screenplay/tests --alluredir=reports/allure-results
```

### 3. Behave (BDD) com Allure
```bash
python -m behave tests/features -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### 4. Executar Toda a Suíte Unificada
```bash
# Executa PyTest (Specs + Screenplay) e Behave gerando todos os resultados no Allure
python -m pytest tests/specs tests/screenplay/tests --alluredir=reports/allure-results
python -m behave tests/features -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

---

## 📊 Visualização do Allure Report Localmente

Se você possui o CLI do Allure instalado na sua máquina:
```bash
# Inicia um servidor local e abre o dashboard automaticamente no navegador:
allure serve reports/allure-results
```

Para gerar a pasta estática do relatório:
```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

## 📸 Evidências e Screenshots Automáticos em Falhas

- Em caso de falha em qualquer cenário (Behave ou PyTest), um screenshot em alta resolução é capturado automaticamente do navegador.
- O screenshot é:
  - **Anexado diretamente ao relatório do Allure**, permitindo que Desenvolvedores e Product Owners analisem a causa da quebra visualmente no passo exato onde ocorreu o erro.
  - **Salvo no diretório `reports/screenshots/`** com carimbo de data/hora para arquivamento e inspeção.
