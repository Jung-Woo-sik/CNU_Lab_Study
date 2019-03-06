#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scapy.all import *

def find_str(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport
 
 
        if (pkt[TCP].dport == 80):
                if(str(pkt[TCP].payload).find(".mp3") > 0) or str(pkt[TCP].payload).find(".mpeg") > 0) or str(pkt[TCP].payload).find("lyric") > 0) or or str(pkt[TCP].payload).find("title") > 0) :
                        print("테스팅한 음원 사이트에서 정보노출의 가능성이 있습니다.")


if __name__ == "__main__":					
	
	print ("test 하고자하는 음원사이트를 선택")
	print ("1. melon")
	print ("2. genie")
	print ("3. bugs")
	print ("4. Mnet")
	print ("5. naver")
	num = input()
	
	if num == '1':
		site = "https://www.melon.com/"
		boxname = 'top_search'
	elif num =='2':
		site = "http://www.genie.co.kr/"
		boxname =  'sc-fd'
	elif num == '3':
		site = "https://music.bugs.co.kr/"
		boxname = 'headerSearchInput' 
	elif num == '4':
		site = "http://www.mnet.com/chart/TOP100/"
		boxname = 'search' 
	elif num =='5':
		site = "https://music.naver.com/"
		boxname = 'query'
	else:
		exit()

	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument("--incognito")

	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument("--incognito")
	#chrome_options.add_argument('headless')
	chrome_options.add_argument('window-size=1920x1080')
	chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
	driver = webdriver.Chrome("C:\\Users\\o0o0\\Desktop\\chromedriver.exe",chrome_options=chrome_options)

	driver.get(site)
	
	
	#boxname = 'top_search' #melon
	#boxname =  'sc-fd' #genie
	#boxname = 'headerSearchInput' # bugs
	#boxname = 'search' #mnet
	#boxname = 'query' #naver
	
	search_box = driver.find_element_by_id(boxname)
	search_box.send_keys('동화 멜로망스')
	#search_box.submit()
	search_box.send_keys(Keys.ENTER)
	
	#elem = driver.find_element_by_class_name('chart').click()
	
	if num =='1' or num =='3' or num == '4' or num =='5':
		driver.find_element_by_link_text("동화").click() # melon bugs mnet naver
	elif num =='2':
		elem = driver.find_element_by_class_name('t_point').click() #genie



	p = sniff(timeout=45)
	wrpcap('C:\\Users\\o0o0\\Desktop\\temp.pcap',p)

	sniff(offline='C:\\Users\\o0o0\\Desktop\\temp.pcap',prn=find_str)



