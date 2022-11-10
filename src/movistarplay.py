from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from datetime import datetime, timedelta
import pandas as pd

serie = str(input("escribe URL de la serie: "))
capitulos = int(input("escribe el numero de capitulos: "))
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
   

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#browser = webdriver.Chrome(executable_path="./chromedriver")
browser = webdriver.Chrome(executable_path="C:\dina2\src\chromedriver.exe")

browser.get("https://www.movistarplay.com.pe/")
browser.maximize_window()
time.sleep(5)

#browser.find_element_by_xpath("/html/body/go-cmp-main-upper/header/div[2]/div/div/div/form/input").send_keys(serie)

#browser.get("https://www.movistarplay.com.pe/details/serie/al-fondo-hay-sitio-190883")
browser.get(serie)

print('data1')
time.sleep(5)

browser.execute_script("window.scrollTo(0, 500)")
time.sleep(5)


def es_multiplo(numero, multiplo):
    return numero % multiplo == 0

serieid=[]

def find_element_click(path,browser):
    c=0
    while True:
        try:
            browser.find_element(By.XPATH,path).click()
           
            break
        except Exception as e:
            print(e)
            c=c+1
        if c==10:
            break
    return browser
data=[]

for i in range(4):
	c=i+1
	print(c)

	#time.sleep(2)
	find_element_click('/html/body/main/div/go-mdl-details-cmp-serie/data-go-mdl-details-cmp-serie-uniapi/div/data-go-mdl-details-cmp-serie-tabs/div/go-cmp-episode-carousel/section/div/div[1]/div['+str(c)+']',browser)
	print(browser.current_url)
	a= str(browser.current_url)
	b=a.split('-')
	json = {'url': str(browser.current_url)}#, 'capitulo':b[1] ,'id_serie':b[2]}
	data.append(json)
	#if es_multiplo(c,4):
	#print('next')
find_element_click('/html/body/main/div/go-mdl-details-cmp-serie/data-go-mdl-details-cmp-serie-uniapi/div/data-go-mdl-details-cmp-serie-tabs/div/go-cmp-episode-carousel/section/div/div[3]',browser)
time.sleep(2)
print('next ->11')

count= 0
limite = capitulos#-4
while True:
	try:
		#capitulo=[]
		for i in [5,6,7,8]:
			
			#print("c: "+str(c))
			find_element_click('/html/body/main/div/go-mdl-details-cmp-serie/data-go-mdl-details-cmp-serie-uniapi/div/data-go-mdl-details-cmp-serie-tabs/div/go-cmp-episode-carousel/section/div/div[1]/div['+str(i)+']',browser)
			print(browser.current_url)

			a= str(browser.current_url)
			b=a.split('-')
			#print(b[0])
			#print(b[1])
			#print(b[2])
			#idserie=b[2]
			#capitulo=b[1]
			json = {'url': str(browser.current_url)}
			data.append(json)
			print("count: "+ str(count))

			if count==limite: break
			count=count+1
			print("count: "+ str(count))

			if es_multiplo(i,4):				
				a = find_element_click('/html/body/main/div/go-mdl-details-cmp-serie/data-go-mdl-details-cmp-serie-uniapi/div/data-go-mdl-details-cmp-serie-tabs/div/go-cmp-episode-carousel/section/div/div[3]',browser)
				print('next')
				time.sleep(2)
			#else:
			#	print('no next')				
				break
		
		#print(capitulo)
		if count==limite: break
		#if int(capitulo)==limite: 
		#	break			
	except Exception as e:
		print(e)

df = pd.DataFrame(data=data)
df=df.drop_duplicates()
print(df)

def reverse(url):
	#tmp = "a,b,cde"
	tmp2 = url.split('-')[::-1]
	print(tmp2[0])

	return tmp2[0]

df['contentid']=df['url'].apply(reverse)
df.to_excel("serie.xlsx",index=False)

