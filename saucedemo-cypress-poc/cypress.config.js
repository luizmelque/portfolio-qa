const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://www.saucedemo.com', // URL base do site que será testado
    viewportWidth: 1280,                   // Largura da tela do navegador
    viewportHeight: 720,                   // Altura da tela do navegador

    setupNodeEvents(on, config) {
      // Aqui você pode implementar eventos personalizados se precisar
    },
  },
});
