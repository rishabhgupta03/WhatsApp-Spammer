from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)

song = "highest in the room"
browser.get("https://genius.com") #opens genius.com
searchbox = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/input") #search box
searchbox.send_keys(song) #enter song name in search box
searchbox.submit() #press enter key

song_card = browser.find_element_by_xpath('/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div[2]/search-result-section/div/div[2]/search-result-items/div[1]/search-result-item/div/mini-song-card/a/div[2]')
song_card.click() #clicks on song card to open lrics

lyrics = browser.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/div[2]/div[1]/div/defer-compile[1]/lyrics/div/div/section/p')
content = lyrics.text   #captures lyrics of song in  content variable

file = open(f'C:\\Users\Rishabh\\Desktop\\{song}.txt', 'w+' , errors='ignore')
file.write(content)
file.close()

browser.quit()

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
name = input("enter the name of user:")
user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()

file  = open(f'c:\\Users\\Rishabh\\Desktop\\{song}.txt', 'r')
content = file.read()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
for word in content.split():
    msg_box.send_keys(word)
    msg_send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    msg_send.click()

driver.quit()
