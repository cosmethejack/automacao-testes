# Automação de Testes e QAOps

Projeto de automação de testes E2E para o [SauceDemo](https://www.saucedemo.com/) utilizando múltiplos padrões de arquitetura:
- **PyTest**: Testes funcionais e Page Objects.
- **Guará (PTP)**: Page Transactions Pattern.
- **Screenplay**: Arquitetura orientada a Atores, Habilidades, Tarefas e Questões via ScreenPy.
- **Behave (BDD)**: Especificação em linguagem Gherkin com cenários executáveis.

## Instalação de Dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Execução dos Testes

### PyTest Specs (Page Objects, PTP)
```bash
python -m pytest tests/specs -v
```

### PyTest com Relatório HTML
```bash
python -m pytest tests/specs --html=reports/report.html --self-contained-html
```

### Screenplay Tests
```bash
python -m pytest tests/screenplay/tests -v
```

### Behave (BDD)
```bash
python -m behave tests/features
```
