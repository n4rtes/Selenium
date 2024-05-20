from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

class CursoAutomacao:
  def __init__(self):
    chrome_options = Options()
    chrome_options.add_argument('--lang=pt-BR')
    self.driver = webdriver.Chrome(
      executable_path=r'./chromedriver.exe', options=chrome_options)

  def Iniciar(self, sites):
    for site in sites:
      self.driver.get(site)
      self.SalvarScreenshot()
      time.sleep(5)

  def SalvarScreenshot(self):
    nome_arquivo = str(round(time.time() *1000)) + ".png"
    nome_arquivo_com_diretorio = os.path.join("fotos", nome_arquivo)
    self.driver.save_screenshot(nome_arquivo_com_diretorio)

sites = [
  "https://www.facebook.com",
  "https://www.instagram.com",
  "https://www.youtube.com",
  "https://www.google.com"
]    

curso = CursoAutomacao()
curso.Iniciar(sites)