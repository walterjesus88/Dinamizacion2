#!/usr/bin/env python
# coding: utf-8

# In[15]:


# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
import pandas as pd
import time



df = pd.read_excel("NOTIFICACIONESMPLAY.xlsx")
df.tail()




#df[['TIPO DE CONTENIDO','LINK / NAME','TÍTULO','FECHA','HORA']]
#new_df=df[['TIPO DE CONTENIDO','LINK / NAME','TÍTULO','FECHA','HORA']]
#new_df['TIPO']=new_df['TIPO DE CONTENIDO']
new_df.shape



#live =new_df[new_df.TIPO == 'LIVE']
live=new_df


def versus(msg):
    vs = msg.find(" vs ")
    VS = msg.find(" VS ")
    if vs>=0 or VS>=0:
        titulo = 1
    else:
        titulo = 0
    return titulo


# In[21]:


def hora_mensaje(msg):
    msg = msg.strip()
    texto = msg[-7:]
    cc = texto.find(" ")
    print('inicio')
    print(texto)
    print(cc)
    
    if cc>=0:
        text = texto[cc:]  
        print(text)
        #text='llego'
        #text =time.strptime(text,'%H')
        #text = time.strftime("%H:%M:%S", '00:03:38')        
    elif cc==-1:
        print('es -1')
        text = texto
        #text=time.strptime(text,'%H')
        #time.strptime("30 Nov 00", "%d %b %y") 
    print(text)
    print('fin')
    return text




def hora_mensaje2(msg):
    texto = msg[-7:]    
    return texto




#def concatenar(texto)
live['TÍTULO'] = live['TÍTULO'].apply(str)
live['TÍTULO2'] = live['TÍTULO2'].apply(str)
live['TÍTULO3'] = live['TÍTULO3'].apply(str)
#live['title'] = live['TÍTULO'].apply(versus)
#lives = live[live['title']==1]
#live['hora_mensaje'] = live['HORA'].apply(str)
#.apply(hora_mensaje)
#lives
#lives['hora_mensaje2'] = lives['MENSAJE'].apply(hora_mensaje2)




#live = live[['TIPO','LINK / NAME','TÍTULO','FECHA','HORA','hora_mensaje']]
live.head()
live['FECHA']=live['FECHA'].astype(str)+ " "+ live['HORA'].astype(str)
live['HORA']=live['HORA'].astype(str)


# In[26]:


#live['concat'] = live['TIPO'] + "/"+live['LINK / NAME'] + " / " + live['TÍTULO'] + " / " + live['FECHA'] + " - "+ live['hora_mensaje']
live['TÍTULO'] = live['TÍTULO'] + " "+live['TÍTULO2'] + " " + live['TÍTULO3']
 
live.to_excel("live_formato.xlsx",encoding='utf-8')


# In[ ]:


def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "am" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "am": 
        return str1
        #[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "pm" and str1[:2] == "12": 
        return str1
        #[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 







