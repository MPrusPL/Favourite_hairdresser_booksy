from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

a = input("Chcę skorzystać z usługi w mieście: ")

def initiate_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://booksy.com/pl-pl/')
    driver.implicitly_wait(15)
    return driver

if a.lower() == "kraków" or a== "krakow":
    print("Wyświetlam kalendarz Twojego ulubionego salonu 'ArtDream' w mieście Kraków")
    driver = initiate_driver()
    hairdresser = driver.find_element(By.XPATH, '//*[@id="page"]/header/section[3]/div/div/ul/li[1]/a')
    hairdresser.click()
    city_hairdresser = driver.find_element(By.XPATH, '//*[@id="page"]/main/div/div/section[2]/div/div/a[18]')
    city_hairdresser.click()
    chose_hairdresser = driver.find_element(By.PARTIAL_LINK_TEXT, 'ArtDream')
    chose_hairdresser.click()
    chosen_service = driver.find_element(By.XPATH, '//*[@id="service-1292361"]/div/div[2]/div/div/div[1]/div[2]/button')
    chosen_service.click()

else:
    print("Szukam dla miasta: " + a.capitalize() + ". Wybierz miasto z listy po załadowaniu się strony.")
    driver = initiate_driver()
    hairdresser = driver.find_element(By.XPATH, '//*[@id="page"]/header/section[3]/div/div/ul/li[1]/a')
    hairdresser.click()


