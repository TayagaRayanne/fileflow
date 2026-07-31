# 📂 FileFlow

Sistema de automação desenvolvido em Python para organizar arquivos de forma inteligente.

O FileFlow nasceu com o objetivo de automatizar uma tarefa comum do dia a dia: manter diretórios organizados automaticamente. Durante seu desenvolvimento, o projeto segue boas práticas de engenharia de software, arquitetura em camadas e Clean Code, servindo também como projeto de portfólio.

---

# 🚀 Objetivos

- Automatizar a organização de arquivos.
- Construir uma arquitetura escalável.
- Aplicar boas práticas de desenvolvimento.
- Simular um projeto utilizado em ambiente corporativo.
- Desenvolver um projeto completo para portfólio.

---

# 📌 Status do Projeto

🚧 Em desenvolvimento

Atualmente o FileFlow já é capaz de:

- Ler configurações via JSON;
- Validar pastas de origem e destino;
- Classificar arquivos por categoria;
- Criar automaticamente a estrutura de destino;
- Gerar nomes únicos para evitar sobrescritas;
- Preparar toda a estrutura necessária para organizar arquivos.

A movimentação definitiva dos arquivos será implementada na próxima sprint.

---

# ✨ Funcionalidades

| Funcionalidade | Status |
|----------------|:------:|
| Leitura do arquivo de configuração | ✅ |
| Logger da aplicação | ✅ |
| Classificação por extensão | ✅ |
| Organização por categorias | ✅ |
| Criação automática das pastas | ✅ |
| Validações de segurança | ✅ |
| Geração de nomes únicos | ✅ |
| Movimentação de arquivos | 🚧 |
| Relatórios | 🔜 |
| Watchdog | 🔜 |
| Tratamento de duplicados | 🔜 |

---

# 📁 Estrutura do Projeto

```text
fileflow/

├── config/
├── docs/
├── logs/
├── reports/
├── src/
│   ├── core/
│   └── services/
├── tests/
└── README.md

---

# 🛠️ Tecnologias

- Python 3
- Logging
- Dataclasses
- JSON
- Pathlib
- Git
- GitHub

---

# ▶️ Como executar

Clone o projeto:

```bash
git clone https://github.com/TayagaRayanne/fileflow.git
```

Entre na pasta:

```bash
cd fileflow
```

Crie a ambiente virtual:

```bash
python -m venv .venv
```

Ative:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python src/main.py
```

---

# 📅 Roadmap

- [x] Estrutura inicial
- [x] ConfigLoader
- [x] Logger
- [x] Organizador
- [x] Classificador
- [x] Movimentação segura dos arquivos
- [ ] Relatórios
- [ ] Watchdog
- [ ] Duplicados
- [ ] Testes

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto estão sendo aplicados conceitos como:

- Arquitetura em camadas
- Programação orientada a objetos (POO)
- Dataclasses
- Logging
- Manipulação de arquivos com Pathlib
- Clean Code
- Tratamento de exceções
- Organização de projetos Python
- Boas práticas de documentação
- Git e GitHub

---

# 👩‍💻 Autora

**Tayga Rayanne Rodrigues Oliveira**

Desenvolvedora Back-end | Python | Automação | RPA