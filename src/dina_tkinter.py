import tkinter as tk
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

class Application(tk.Tk):
     def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('App Dinamizacion')
        
        first_label = tk.Label(self, text = "I'm a cool App!!", font=10)
        first_label.pack(padx = 3, pady = 3)

        # first_button = tk.Button(self, text ="Hello World", command = hello)
        # first_button.pack(padx= 5, pady = 5)

        # transpuesta = tk.Button(self, text ="Transponer canales deportivos", command = lambda: transponer('canales'))
        # transpuesta.pack(padx= 15, pady = 10)

        # transpuestav = tk.Button(self, text ="Transponer mas vistos", command = lambda: transponer('masvisto'))
        # transpuestav.pack(padx= 15, pady = 10)

        live_partido = tk.Button(self, text ="live formato DEPORTES", command = live_formato)
        live_partido.pack(padx= 15, pady = 10)

        mas_visto = tk.Button(self, text ="Más vistos", command = lambda: mas_vistos('masvisto'))
        mas_visto.pack(padx= 5, pady = 5)

        canal = tk.Button(self, text ="canales", command = lambda: mas_vistos('canales'))
        canal.pack(padx= 5, pady = 5)

        destacados = tk.Button(self, text ="destacados", command = lambda: mas_vistos('destacados'))
        destacados.pack(padx= 5, pady = 5)

        partido = tk.Button(self, text ="partidos", command = deportes)
        partido.pack(padx= 5, pady = 5)
      
       
        Application.first_entry = tk.Entry(self, width = 30)
        Application.first_entry.pack(padx = 7, pady = 7)

# def hello():
#     x = Application.first_entry.get()
#     print(x)
#     Application.first_entry.delete(0,tk.END)

def mas_vistos(tipo):

    browser = _login()
    file = franja(browser,tipo)

def deportes():
    print('partidos')
    browser = _login()

    file = live(browser)
    return file

def semanal_deportes(x,browser):
    #calendar = browser.find_element_by_id('element-calendar').click()
    find_element_click("/html/body/div[2]/main/header/div[2]/div[1]/div[1]/div/div[2]/input",browser)
    CANAL=x['CANAL']
    FECHA=x['FECHA2']
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
    #find_element_click('//*[@id="youbora__container"]/main/header/div[2]/button[2]',browser)
    find_element_click('//*[@id="youbora__sectionbox__sectionbox_toolbar"]',browser)

    #codigo repetido
   
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[2]/input',"Device Type"+Keys.ENTER,browser)
    find_element_click('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/ul/div/div[2]/div/li/div/p',browser)
    #Elejir STB  
    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)
    #Exclude   
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',"Exclude"+Keys.ENTER,browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[2]/input',"Title"+Keys.ENTER,browser)
    find_element_click('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/ul/div/div[2]/div[2]/li/div/p',browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/input',CANAL,browser)


    time.sleep(1)
    #click en el canal
    find_element_click('//*[@id="youbora__filters_wizard__tab_content_container"]/div[3]/div/table/tbody/div/tr[1]/td[1]/div/span/span[1]/input',browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',"Include"+Keys.ENTER,browser)
 
    #fin codigo repetido

    time.sleep(2)
    #aplicar
    find_element_click('/html/body/div[4]/div[3]/div/div[2]/div/div/button[2]',browser)
    time.sleep(3)
    suscribers = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[1]/div/div[2]/div/div/div[3]/p[1]',browser)
                                          
    hours = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[4]/div/div[2]/div/div/div[3]/p',browser)
    play = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[12]/div/div[2]/div/div/div[3]/p[1]',browser)
                                
    total = { 'canal': CANAL+' '+FECHA,'suscribers':suscribers,'hours': hours,'plays': play}
    time.sleep(1)
    return total

def live(browser):
    deportes =  pd.read_excel('live_formato.xlsx')
    deportes = deportes[['CANAL','FECHA2']]
    print(deportes)
    total_sus = []
    total_hou = []
    KPI = []
    KPI_antes = []
    time.sleep(2)

    for index,row in deportes.iterrows():
        print(row['CANAL'])
        print(row['FECHA2'])
        x ={'CANAL':row['CANAL'],'FECHA2':row['FECHA2']}    
        #week_after = datetime.strptime(x['fecha'], '%Y-%m-%d %H:%M:%S') -  timedelta(days=7)     

        #x_before = {'canal': x['canal'],'fecha':str(week_after)}

        total=semanal_deportes(x,browser)
        #clear
     
        #total_before=semanal_deportes(x_before,browser)
        KPI.append(total)
        #KPI_antes.append(total_before)
        find_element_click('//*[@id="124581"]/div[1]/div[2]/button',browser)
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

    df.to_excel("../resultados_partidos1.xlsx",index=False)
    #df2.to_excel("resultados_partidos2.xlsx",index=False)

    #path = "../resultados_partidos1.xlsx"
    #return send_file(path, as_attachment=True)
    #return df2,df


def _login():

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    prefs = {'download.default_directory' : 'C:\dina2\dina2\src\perf_filtro1'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path="C:\dina2\dina2\src\chromedriver.exe",chrome_options=options)
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

    find_element_click('//*[@id="124581"]/div[1]/div[2]/button',driver) #eliminar filtro  
    time.sleep(1)

    find_element_click('/html/body/div[4]/div[3]/div/div[3]/button[2]',driver) #confirmar eliminacion
             
    return driver

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


def semanal_franja(x,browser):
    #limpiar filtros por defecto
    #calendar = browser.find_element_by_id('element-calendar').click()
    find_element_click("/html/body/div[2]/main/header/div[2]/div[1]/div[1]/div/div[2]/input",browser)
                        
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
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA)))) #'//*[@id="date-picker-calendar"]//div[@aria-label="Tue Jul 13 2021"]'
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA))))
    find_element_click(DIA,browser)
    find_element_click(DIA,browser)
 
    time.sleep(0.5) 
    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(str(time_ini))
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input',Keys.CONTROL+"a",browser)
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input',str(time_ini),browser)
    

    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(str(time_fin))
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input',Keys.CONTROL+"a",browser)
    find_element_key('//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input',str(time_fin),browser)
    
    
    #APPLY CALENDAR
    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]').click()
    find_element_click('//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]',browser)

    #FILTER     
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__sectionbox__sectionbox_toolbar"]'))))
    find_element_click('//*[@id="youbora__sectionbox__sectionbox_toolbar"]',browser)
                  
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[2]/input',"Device Type"+Keys.ENTER,browser)
    find_element_click('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/ul/div/div[2]/div/li/div/p',browser)
    #Elejir STB  
    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)
    #Exclude         
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',"Exclude"+Keys.ENTER,browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[2]/input',"Title"+Keys.ENTER,browser)
    find_element_click('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/ul/div/div[2]/div[2]/li/div/p',browser)
    #time.sleep(2)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/input',CANAL,browser)
    #time.sleep(2)                  

    #click en el canal
    find_element_click('//*[@id="youbora__filters_wizard__tab_content_container"]/div[3]/div/table/tbody/div/tr[1]/td[1]/div/span/span[1]/input',browser)
    find_element_key('/html/body/div[4]/div[3]/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',"Include"+Keys.ENTER,browser)
    
    time.sleep(2)
    #aplicar
    find_element_click('/html/body/div[4]/div[3]/div/div[2]/div/div/button[2]',browser)
    time.sleep(3)
    
    print('--------suscribers')
    suscribers = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[1]/div/div[2]/div/div/div[3]/p[1]',browser)                                          
    
    print('hours-----------')
    hours = find_element_inner_html('/html/body/div[2]/main/div[2]/div[1]/div[4]/div/div[2]/div/div/div[3]/p',browser)

    total = { 'canal': CANAL+' '+FECHA_INIT,'suscribers':suscribers,'hours': hours }
    time.sleep(2)

    find_element_click('//*[@id="124581"]/div[1]/div[2]/button',browser)

    #confirmar borrar filtro
    find_element_click('/html/body/div[4]/div[3]/div/div[3]/button[2]',browser)
                      
    return total

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

def franja(browser,tipo):
    franja =  pd.read_csv('../FRANJAS.csv')
    franja = franja[['canal','fecha_init','fecha_fin']]
   

    total_sus = []
    total_hou = []
    KPI = []
    for index,row in franja.iterrows():       
        x ={'canal':row['canal'],'fecha_init':row['fecha_init'],'fecha_fin':row['fecha_fin']}      
        total=semanal_franja(x,browser) 
        KPI.append(total) 

    print(KPI)
    df = pd.DataFrame(data=KPI)
    print(df)
    df['suscribers']=df['suscribers'].apply(convertir_suscribers)
    df['hours']=df['hours'].apply(convertir_hours)
    df.to_csv('../RES_FRANJAS.csv', index = None)
    #path = "../RES_FRANJAS.csv"
    #return send_file(path, as_attachment=True)

    transponer(tipo)


# def live_formato():
#     df = pd.read_excel("../NOTIFICACIONESMPLAY.xlsx")
#     df.tail()

#     df[['TIPO DE CONTENIDO','LINK / NAME','TÍTULO','FECHA','HORA']]
#     new_df=df[['TIPO DE CONTENIDO','LINK / NAME','TÍTULO','FECHA','HORA']]
#     new_df['TIPO']=new_df['TIPO DE CONTENIDO']
#     new_df.shape
#     live=new_df

#     live['TÍTULO'] = live['TÍTULO'].apply(str)
#     live['hora_mensaje'] = live['HORA'].apply(str)
#     live = live[['TIPO','LINK / NAME','TÍTULO','FECHA','HORA','hora_mensaje']]
#     live.head()
#     live['FECHA']=live['FECHA'].astype(str)+ " "+ live['HORA'].astype(str)
#     #live['HORA']=live['HORA'].astype(str)
#     live['concat'] = live['TIPO'] + "/"+live['LINK / NAME'] + " / " + live['TÍTULO'] + " / " + live['FECHA'] + " - "+ live['hora_mensaje']

#     live.to_excel("live_formato.xlsx",encoding='utf-8')
#     print('save')


def live_formato():
    live = pd.read_excel("../NOTIFICACIONESMPLAY.xlsx")
  
    live['TITULO'] = live['TITULO'].apply(str)
    live['TITULO2'] = live['TITULO2'].apply(str)
    live['TITULO3'] = live['TITULO3'].apply(str)

    live['FECHA2']=live['FECHA'].astype(str)+ " "+ live['HORA'].astype(str)
    live['HORA']=live['HORA'].astype(str)

    live['PARTIDO'] = live['TITULO'] + " "+live['TITULO2'] + " " + live['TITULO3']    
    live.to_excel("live_formato.xlsx",encoding='utf-8')
    

# def transponer():
#     df = pd.read_csv("../RES_FRANJAS.csv")
#     dr = []

#     horas = df['hours']
#     hours_csv=trasnponer_detalle(horas)
#     print(hours_csv)
#     hours_csv.to_excel('CANALES_DEPORTIVOS.xlsx',index=False)                 


    # week = ['lunes', 'martes', 'miercoles', 'jueves',
    #             'viernes', 'sabado', 'domingo']

    # hr_df = pd.DataFrame({'week': week})
    # i=1
    # j=0

    # for chunk in df['hours']:

    #     dr.append(chunk)

    #     if i%7==0:
    #         j=j+1  
    #         hh=str(j)   
            
    #         d2 = { hh: dr}
    #         gg = pd.DataFrame(d2)
    #         print(gg)
    #         hr_df = hr_df.join(gg)

    #         print(hr_df)
    #         print(hr_df.T)
    #         transponer= hr_df.T
    #         transponer.to_excel('CANALES_DEPORTIVOS.xlsx',index=False)                 
    #         dr=[]  
    #     i=i+1



def transponer_detalle(param):
    
    week = ['lunes', 'martes', 'miercoles', 'jueves',
                'viernes', 'sabado', 'domingo']

    hr_df = pd.DataFrame({'week': week})
    i=1
    j=0
    dr = []
    print(param)
    for chunk in param:

        dr.append(chunk)
        if i%7==0:
            j=j+1
       
            hh=str(j)
            print(dr)
            
            d2 = { hh: dr}
            gg = pd.DataFrame(d2)
            print(gg)
            hr_df = hr_df.join(gg)

            print(hr_df)
            print(hr_df.T)
            transponer= hr_df.T            
            dr=[]  
        i=i+1
    return transponer

def transponer(tipo):
    print('tipo')
    print(tipo)
    df = pd.read_csv("../RES_FRANJAS.csv")
    
    if tipo=='masvisto':
        df_weekend=df.tail(10)
        df=df.head(63)
        horas = df['hours']
        suscribers = df['suscribers']

        hours_csv=transponer_detalle(horas)
        suscribers_csv=transponer_detalle(suscribers)

        with pd.ExcelWriter('CUADRO_DINA.xlsx') as writer:
            hours_csv.to_excel(writer, sheet_name='HOURS', index = False)
            suscribers_csv.to_excel(writer, sheet_name='SUSCRIBE', index = False)
            df_weekend.to_excel(writer, sheet_name='FIN_SEMANA', index = False)
    elif tipo=='canales':
        #dr = []

        horas = df['hours']
        hours_csv=transponer_detalle(horas)
        print(hours_csv)
        hours_csv.to_excel('CANALES_DEPORTIVOS.xlsx',index=False) 
    else:
        print('esta opcion no es necesaria transponer')
    
app = Application()
app.mainloop()

#dt.columns = [''] * len(dt.columns)
#dt=dt[:].values