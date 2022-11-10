# save this as app.py
from flask import Flask, request, render_template
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import datetime
from datetime import datetime, timedelta
import os
from flask import send_file

app = Flask(__name__,template_folder='../template')

def find_element_key(path,sendkey,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).send_keys(sendkey)
            break
        except Exception as e:
            print(e)

    return browser

def find_element_key_enter(path,sendkey,browser):
    while True:
        try:
            b=browser.find_element(By.XPATH,path).send_keys(sendkey).send_keys('Keys.ENTER')
            time.sleep(1)
            b.click()
            break
        except Exception as e:
            print(e)

    return browser

def find_element_click(path,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).click()
            break
        except Exception as e:
            print(e)

    return browser

def find_element_cc(path,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path)
            break
        except Exception as e:
            print(e)

    return browser

def find_element_inner_html(path,browser):
    while True:
        try:
            data = browser.find_element(By.XPATH,path).get_attribute("innerHTML")
            break
        except Exception as e:
            print(e)

    return data

def _login():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    #driver = webdriver.Chrome(executable_path="./chromedriver")
    driver = webdriver.Chrome(executable_path="C:\dina2\dina2\src\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://suite.npaw.com/MainKPIsPeru/Phantasia-DINA")   
    time.sleep(3)
  
    find_element_key('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input',"PeruOps",driver)
    find_element_key('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input',"P3ru0ps",driver)
    find_element_click('//*[@id="youbora__login_submit"]',driver)
    

    time.sleep(2)

    find_element_click('//*[@id="youbora__home__app__analytics"]',driver)

    time.sleep(1)

    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 2)
    actions.perform()
    actions.click()
    time.sleep(5)

    find_element_click('//*[@id="sidebar-pinner"]',driver)
    find_element_key('//*[@id="sidebar"]/div[2]/div[1]/div/div/input',"Phantasia",driver)    
    find_element_click('//*[@id="sidebar"]//span[text()="Main KPIs Peru"]',driver)
    find_element_click('//*[@id="sidebar"]/div[1]/div/div[1]/div/div//span[text()="Phantasia - DINA"]',driver)

    time.sleep(3)
    find_element_click('//*[@id="124581"]/div[1]/button',driver) #eliminar filtro     
    find_element_click('/html/body/div[4]/div[3]/div/div[3]/button[2]',driver) #confirmar eliminacion

    return driver

#def my_form():
#    return render_template('form.html')

def convertir_suscribers(x):

    x1= str(x).replace(",","")
    print(x1)
    return float(x1)


def convertir_hours(x):
    a= str(x).split(" ")
    aa= str(a[0]).replace("h", "")
    aa1 = float(aa.replace(",",""))

    if len(a)>1:
        bb= str(a[1]).replace("m", "")
        a_hours = float(bb)/60
    else:
        a_hours=0

    return aa1+a_hours

def semanal_deportes(x,browser):
    calendar = browser.find_element_by_id('element-calendar').click()

    CANAL=x['canal']
    FECHA=x['fecha']
    time_ini= datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S').time()
    time_tuple =  datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S') +  timedelta(hours=1,minutes=59,seconds=59)
    time_2horas = time_tuple.time()
    time.sleep(0.5) 

    print(time_2horas)
    print(time_ini)
    
    d = datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S')
    dia  = str(d.strftime('%a %b %d %Y'))
 

    DIA='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia+'"]'
    driver = browser
    time.sleep(0.5) 
  
    find_element_click(DIA,browser)
    find_element_click(DIA,browser)


    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input',Keys.CONTROL+"a",browser)
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input',str(time_ini),browser)

    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input',Keys.CONTROL+"a",browser)
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input',str(time_2horas),browser)
    

    find_element_click('//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]',browser)

    find_element_click('//*[@id="youbora__container"]/main/header/div[2]/button[2]',browser)

    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Device Type"+Keys.ENTER,browser)
    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)
    #Exclude   
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Exclude"+Keys.ENTER,browser)

    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Title"+Keys.ENTER,browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/input',CANAL,browser)

 
    # DEVICE=browser.find_elements_by_xpath('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td/div/p')
    # for option in DEVICE:
    #     print('-----------------option----------->')
    #     print(option.text)
    #     print('-----------------option----------->')
    #     if option.text == CANAL:
    #         option.click() # select() in earlier versions of webdriver
    #         break

    time.sleep(1)
    #click en el canal
 
    find_element_click('//*[@id="youbora__filters_wizard__tab_content_container"]/div[3]/div/table/tbody/div/tr[1]/td[1]/div/span/span[1]/input',browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Include"+Keys.ENTER,browser)
    
   
    time.sleep(2)
    #aplicar
    find_element_click('/html/body/div[4]/div[3]/div/div[2]/div/div/button[2]',browser)
    time.sleep(2)

    suscribers = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[13]/div/div[2]/div/div[1]/p',browser)
    hours = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/p',browser)
    play = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[12]/div/div[2]/div/div[1]/p',browser)

    total = { 'canal': CANAL+' '+FECHA,'suscribers':suscribers,'hours': hours,'plays': play}
    time.sleep(1)

    return total

def semanal_franja(x,browser):
    #limpiar filtros por defecto
    calendar = browser.find_element_by_id('element-calendar').click()

    CANAL=x['canal']
    FECHA_INIT=x['fecha_init']
    FECHA_FIN=x['fecha_fin']
    time_ini= datetime.strptime(FECHA_INIT, '%Y-%m-%d %H:%M:%S').time()
    time_fin= datetime.strptime(FECHA_FIN, '%Y-%m-%d %H:%M:%S').time()   
         
    d = datetime.strptime(FECHA_INIT, '%Y-%m-%d %H:%M:%S')
    dia  = str(d.strftime('%a %b %d %Y'))
    #'Tue Jul 13 2021'
    DIA='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia+'"]'
    driver = browser
    time.sleep(0.5) 
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA)))) #'//*[@id="date-picker-calendar"]//div[@aria-label="Tue Jul 13 2021"]'
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA))))
 
    time.sleep(0.5) 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(str(time_ini))
 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(str(time_fin))
    #APPLY CALENDAR
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]').click()
    #FILTER     
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/header/div[2]/button[2]'))))
      


    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Device Type"+Keys.ENTER,browser)
    #Elejir STB  

    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)
 
    #Exclude   
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Exclude"+Keys.ENTER,browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Title"+Keys.ENTER,browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/input',CANAL,browser)

    #find_element_key('/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Exclude"+Keys.ENTER,browser)
    #find_element_key('/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Title"+Keys.ENTER,browser)
    #find_element_key('//*[@id="youbora__filters_wizard__tab_content_container"]/div[2]/div[2]/input',CANAL,browser)


    #click en el canal
    find_element_click('//*[@id="youbora__filters_wizard__tab_content_container"]/div[3]/div/table/tbody/div/tr[1]/td[1]/div/span/span[1]/input',browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Include"+Keys.ENTER,browser)
    
    time.sleep(2)
    #aplicar
    find_element_click('/html/body/div[4]/div[3]/div/div[2]/div/div/button[2]',browser)
    time.sleep(2)

    #find_element_click('//*[@id="youbora__filters_wizard__tab_content_container"]/div[3]/div/table/tbody/div/tr[1]/td[1]/div/span/span[1]/input',browser)
    #find_element_key('/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/input',"Include"+Keys.ENTER,browser)
    
   
    #find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div/div[2]/div/div/button[2]',browser)
    #time.sleep(2)
    

    suscribers = find_element_inner_html('//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p',browser)
    print('--------suscribers')
    print(suscribers)  
    hours = find_element_inner_html('//*[@id="52194ecc-0755-44a7-b329-3e2775623aa4"]/div/div[2]/div/div[1]/p',browser)

    print('hours-----------')
    print(hours)
    total = { 'canal': CANAL+' '+FECHA_INIT,'suscribers':suscribers,'hours': hours }
 
    time.sleep(2)

    find_element_click('//*[@id="youbora__container"]/main/div[1]/button',browser)
    #confirmar borrar filtro
    find_element_click('/html/body/div[4]/div[3]/div/div[3]/button[2]',browser)
    
    return total


def vod_det(browser,titulo):

    print(titulo)
    print('-->')

    CONTENTID=titulo
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Content ID"+Keys.ENTER,browser)


    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/input',str(CONTENTID),browser)
                      
    find_element_click('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/table/tbody/div/tr/td[1]/div/span/span[1]/input',browser)
    
   

                 

    #return browser
        

def vod(browser):

    # find_element_click('//*[@id="sidebar-pinner"]',browser)
    # find_element_key('//*[@id="sidebar"]/div[2]/div[1]/div/div/input',"Phantasia",browser)    
    # find_element_click('//*[@id="sidebar"]//span[text()="Dinamización"]',browser)
    # find_element_click('//*[@id="sidebar"]/div[1]/div/div[1]/div/div//span[text()="Phantasia-DINA-series"]',browser)
    browser.get("https://suite.npaw.com/analytics/Dinamizaci%C3%B3n/Phantasia-DINA-series") 
    time.sleep(3) 

    #browser.find_element_by_id('element-calendar').click()
    #find_element_click('//*[@id="element-calendar"]',browser)
    

    FECHA_INI='2022-03-20 00:00:00'
    FECHA_FIN='2022-03-31 23:59:59'

    time_ini= datetime.strptime(FECHA_INI, '%Y-%m-%d %H:%M:%S').time()
    time_ini= datetime.strptime(FECHA_FIN, '%Y-%m-%d %H:%M:%S').time()
 
     
    d1 = datetime.strptime(FECHA_INI, '%Y-%m-%d %H:%M:%S')
    dia_ini  = str(d1.strftime('%a %b %d %Y'))

    d2 = datetime.strptime(FECHA_FIN, '%Y-%m-%d %H:%M:%S')
    dia_fin  = str(d2.strftime('%a %b %d %Y'))

    #'Tue Jul 13 2021'
    #r1='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia_ini+'"]'
    #r2='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia_fin+'"]'

    time.sleep(2) 
    #find_element_click(r1,browser)
    #find_element_click(r2,browser)
    #find_element_click('//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]',browser)
    #find_element_click('//*[@id="youbora__container"]/main/header/div[2]/div[3]/div/button[1]',browser)
   

    #DAYS VOD SELECT
    find_element_click('//*[@id="youbora__container"]/main/header/div[2]/div[2]/div/div/div/div[2]',browser)

    find_element_key('/html/body/div[2]/main/header/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',"Days"+ Keys.ARROW_DOWN + Keys.ENTER,browser)

    #find_element_key('/html/body/div[2]/main/header/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',keys.ARROW_DOWN,browser)
    #find_element_key('/html/body/div[2]/main/header/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/input',keys.ENTER,browser)
   
    find_element_click('/html/body/div[2]/main/header/div[2]/button[2]',browser)    
    #find_element_click('//*[@id="youbora__sectionbox__sectionbox_toolbar"]',browser)

    df =  pd.read_csv('VOD.csv',encoding='latin-1')
    #print(df)
    for index,row in df.iterrows():
        print(row['titulo'])
        titulo= row['titulo']
        vod_det(browser,titulo)
        
    time.sleep(2)
    #aplicar
    find_element_click('/html/body/div[4]/div[3]/div/div[2]/div/div/button[2]',browser)


    #browser.find_element(By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]').click()
    #find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]',browser)

    

 

def franja(browser):
    franja =  pd.read_csv('FRANJAS.csv')
    franja = franja[['canal','fecha_init','fecha_fin']]

    total_sus = []
    total_hou = []
    KPI = []
    #time.sleep(2)

    for index,row in franja.iterrows():
       
        x ={'canal':row['canal'],'fecha_init':row['fecha_init'],'fecha_fin':row['fecha_fin']} 
      
        total=semanal_franja(x,browser)
 
        KPI.append(total) 

    #df = pd.read_json(KPI)
    print(KPI)
    df = pd.DataFrame(data=KPI)
    print(df)
    df['suscribers']=df['suscribers'].apply(convertir_suscribers)
    df['hours']=df['hours'].apply(convertir_hours)
    df.to_csv('RES_FRANJAS.csv', index = None)
    path = "../RES_FRANJAS.csv"
    return send_file(path, as_attachment=True)

def live(browser):
    deportes =  pd.read_csv('DEPORTES.csv')
    deportes = deportes[['canal','fecha']]
    print(deportes)
    total_sus = []
    total_hou = []
    KPI = []
    KPI_antes = []
    time.sleep(2)

    for index,row in deportes.iterrows():
        print(row['canal'])
        print(row['fecha'])
        x ={'canal':row['canal'],'fecha':row['fecha']}    
        #week_after = datetime.strptime(x['fecha'], '%Y-%m-%d %H:%M:%S') -  timedelta(days=7)     

        #x_before = {'canal': x['canal'],'fecha':str(week_after)}

        total=semanal_deportes(x,browser)
        #clear
     
        #total_before=semanal_deportes(x_before,browser)
        KPI.append(total)
        #KPI_antes.append(total_before)
        find_element_click('//*[@id="youbora__container"]/main/div[1]/button',browser)
        find_element_click('/html/body/div[4]/div[3]/div/div[3]/button[2]',browser)

    print(KPI)
    df = pd.DataFrame(data=KPI)
    print(df)
    df['suscribers']=df['suscribers'].apply(convertir_suscribers)
    df['hours']=df['hours'].apply(convertir_hours)
    #df2 = pd.DataFrame(data=KPI_antes)
    #print(df2)
    #df2['suscribers']=df2['suscribers'].apply(convertir_suscribers)
    #df2['hours']=df2['hours'].apply(convertir_hours)

    df.to_excel("resultados_partidos1.xlsx",index=False)
    #df2.to_excel("resultados_partidos2.xlsx",index=False)

    path = "../resultados_partidos1.xlsx"
    return send_file(path, as_attachment=True)
    #return df2,df


def inc(x):
    return x + 1

@app.route('/')
def index():
    #"hello "
    return render_template(
        'index.html',
        data=[{'name':'VOD'}, {'name':'LIVE'}, {'name':'FRANJA'}])

@app.route("/test" , methods=['GET', 'POST'])
def test():

    select = request.form.get('comp_select')
    # options = webdriver.ChromeOptions()
    # #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument('--headless') 
    # #options.add_argument('--ignore-certificate-errors')
    # #options.add_argument('--incognito')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    #driver.get("https://youbora.nicepeopleatwork.com/")
   
    browser = _login()

    if select == 'LIVE':
        file = live(browser)
       
    elif select == 'FRANJA':
        file = franja(browser)
    else:
        vod(browser)
    #return(str(select))
    return file

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        print(f)
        data_xls = pd.read_csv(f)
        return data_xls.to_html()
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/export", methods=['GET'])
def export_records():
    return 


@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "../resultados_partidos1.xlsx"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)

    #web gunicorn --pythonpath src app:app
