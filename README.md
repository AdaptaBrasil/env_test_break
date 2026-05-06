# env_test_break

> Repositório de experimentação para testes e validação de novas tecnologias, bibliotecas e configurações de ambiente.

## 📋 Sobre

Este repositório é dedicado exclusivamente a:
- ✅ Experimentação com novas tecnologias e bibliotecas
- ✅ Validação de configurações de ambiente
- ✅ Testes de integração contínua
- ✅ Prototipagem rápida

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clonar o repositório
git clone <url-repositorio>
cd env_test_break

# Instalar dependências
pip install -e .
```

### Execução

```bash
# Executar testes unitários
pytest

# Executar com cobertura
pytest --cov=src
```

## 📁 Estrutura do Projeto

```
env_test_break/
├── src/                    # Código fonte principal
│   ├── __init__.py
│   └── util/              # Utilitários
│       ├── __init__.py
│       └── utilities.py
├── tests/                 # Testes
│   ├── __init__.py
│   └── unit/             # Testes unitários
│       ├── __init__.py
│       └── test_utilities.py
├── pyproject.toml        # Configuração do projeto
└── README.md
```

## ⚙️ Integração Contínua

### Status de Testes

| Plataforma | Status |
|-----------|--------|
| Linux | ✅ Funcionando |
| Windows | ⏳ Em desenvolvimento |

### Configuração do GitHub Actions

- **Linux**: Ambiente testado e validado (`ubuntu-latest`)
- **Windows**: Versão `windows-2024` em testes

## 📝 Licença

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.