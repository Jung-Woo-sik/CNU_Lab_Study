from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
driver = webdriver.Chrome("C:\\Users\\o0o0\\Desktop\\chromedriver.exe",chrome_options=chrome_options)
inputbox_list = 'search,q,p,query'

driver.get("https://www.naver.com")

for boxname in inputbox_list.split(","):
	boxname = boxname.replace('\n', '')
	try:
		search_box = driver.find_element_by_name(boxname)
		search_box.send_keys('Galaxy Note 8')
		search_box.submit()
		time.sleep(5)
		links = driver.find_element_by_xpath('//*[@href]')
		print(links)
		for link in links:
			href = link.get_attribute('href')
			print (href)
			if href.startswith('http://'):
				print (href)
	except:
		print ("error")