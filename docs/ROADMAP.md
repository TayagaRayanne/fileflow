# 🗺️ Roadmap - FileFlow

Projeto de automação para organização inteligente de arquivos desenvolvido em Python.

---

## ✅ Sprint 1 - Estrutura Inicial

**Status:** Concluída

### Entregas

- [x] Estrutura do projeto
- [x] Ambiente virtual
- [x] Configuração do Git
- [x] Organização das pastas
- [x] ConfigLoader
- [x] AppConfig

---

## ✅ Sprint 2 - Sistema de Logs

**Status:** Concluída

### Entregas

- [x] Implementação do Logger
- [x] Integração com o main.py
- [x] Criação automática da pasta `logs`
- [x] Geração do arquivo `fileflow.log`
- [x] Code Review
- [x] Documentação

---

## 🚧 Sprint 3 - Organização Inteligente

**Status:** Em desenvolvimento

### Entregas concluídas

- [x] Leitura da pasta de origem
- [x] Listagem dos arquivos
- [x] Classificação por categoria
- [x] Centralização da classificação no `Classifier`
- [x] Criação automática das pastas de destino
- [x] Geração do caminho de destino
- [x] Geração automática de nomes únicos
- [x] Validação da pasta de origem
- [x] Validação da pasta de destino
- [x] Proteção contra origem e destino iguais
- [x] Proteção contra destino dentro da origem
- [x] Proteção contra origem dentro do destino
- [x] Estrutura do método `move_file()`

### Próximas entregas

- [ ] Ativar movimentação dos arquivos
- [ ] Registrar movimentações no Logger
- [ ] Testes de arquivos duplicados

---

## ⏳ Sprint 4 - Relatórios

- [ ] Relatório CSV
- [ ] Estatísticas
- [ ] Tempo de execução
- [ ] Quantidade de arquivos organizados

---

## ⏳ Sprint 5 - Monitoramento em Tempo Real

- [ ] Watchdog
- [ ] Execução contínua
- [ ] Organização automática

---

## ⏳ Sprint 6 - Arquivos Duplicados

- [ ] Estratégias de tratamento
- [ ] Relatório de duplicados
- [ ] Configuração de comportamento

---

## ⏳ Sprint 7 - Testes

- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Cenários de erro

---

## ⏳ Sprint 8 - Finalização

- [ ] Revisão geral
- [ ] Documentação final
- [ ] Release v1.0