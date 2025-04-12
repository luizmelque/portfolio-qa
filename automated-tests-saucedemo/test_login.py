
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador (você pode mudar para Firefox, Edge etc.)
driver = webdriver.Chrome()

# Acessa o site
driver.get("https://www.saucedemo.com/")

# Preenche os campos de login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Espera e verifica se o login deu certo (título da página muda)
time.sleep(2)
assert "inventory" in driver.current_url

# Fecha o navegador
driver.quit()
