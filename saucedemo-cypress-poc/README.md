# Cypress SauceDemo Automation 🛒

![Node.js Version](https://img.shields.io/badge/Node-18+-green)
![Cypress Version](https://img.shields.io/badge/Cypress-12+-blue)
![Status dos Testes](https://img.shields.io/badge/Testes-Passando-brightgreen)

---

## 📌 Objetivo
Prova de conceito (POC) de automação de testes web para validar o fluxo de login, adição de produtos ao carrinho e checkout no site público de e-commerce fictício [SauceDemo](https://www.saucedemo.com/).

---

## 🛠 Ferramentas e Tecnologias
- **Linguagem:** JavaScript  
- **Framework de Teste:** Cypress  
- **Arquitetura:** Page Object Model (POM)  
- **Controle de Versão:** Git / GitHub  
- **Execução Contínua (CI):** GitHub Actions (opcional)

---

## 📂 Estrutura do Projeto

cypress-project/
├── cypress/
│ ├── e2e/
│ │ ├── tests/
│ │ │ └── checkoutComplete.cy.js
│ │ └── pages/
│ │ ├── inventoryPage.js
│ │ ├── loginPage.js
│ │ ├── cartPage.js
│ │ └── checkoutPage.js
├── cypress.config.js
├── package.json
├── .gitignore
└── README.md

yaml
Copiar código

---

## ⚙ Configuração do Ambiente

### Pré-requisitos
- Node.js v18+  
- Git  
- VS Code (opcional)

### Instalação
```bash
npm install
🚀 Execução dos Testes
Modo interativo:

bash
Copiar código
npm run test
Modo headless:

bash
Copiar código
npm run test:run
Evidências:
Screenshots e vídeos são gerados automaticamente em cypress/screenshots/ e cypress/videos/.

🔄 Fluxo de Teste Automatizado
Etapa	Descrição
Login	Acessa o site com standard_user / secret_sauce.
Navegação	Acessa a listagem de produtos (inventory).
Validação	Seleciona um produto e valida nome, preço e descrição.
Carrinho & Checkout	Adiciona produto ao carrinho e inicia checkout.
Finalização	Preenche dados do checkout e valida mensagem de sucesso.

💡 Decisões Técnicas
Decisão	Justificativa
Cypress	Framework moderno, confiável e integrado a CI/CD.
JavaScript	Linguagem de fácil integração com Cypress.
POM	Facilita manutenção, reutilização e clareza do código.
GitHub Actions	Permite execução automática dos testes.
Evidências	Screenshots e vídeos gerados automaticamente.

⚙ Execução Contínua – GitHub Actions
Exemplo de workflow: .github/workflows/cypress.yml

yaml
Copiar código
name: Cypress Tests

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 18
      - run: npm ci
      - run: npx cypress install
      - run: npm run test:run
      - name: Upload Artifacts
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: cypress-results
          path: |
            cypress/screenshots
            cypress/videos
🔑 Credenciais Padrão
Usuário: standard_user

Senha: secret_sauce

📌 Como Reproduzir
bash
Copiar código
git clone https://github.com/SEU-USUARIO/cypress-saucedemo-tests.git
cd cypress-saucedemo-tests
npm install
npm run test
Em modo headless:

bash
Copiar código
npm run test:run
✅ Resultado Esperado
Testes executam com sucesso validando todo o fluxo de compra.

Relatórios, screenshots e vídeos gerados automaticamente.

Estrutura POM clara e modular.

Execução automática via GitHub Actions funcionando.

🏗 Desenvolvido por
Luiz Melque Almeida
Analista de Testes e Qualidade de Software | Automação | QA | Cypress | JavaScript