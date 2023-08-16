import csv
import os
import sys
import requests
import re
import slackweb
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
#-----------------------------------------------
UId = "*********************************************************"
GId = "**********************************************************************************"
LineAPI_Token = "***************************************************************************************"
Channel_seacret = "**********************************************************"
#-----------------------------------------------


def send_message(text):
    
    line_bot_api = LineBotApi(LineAPI_Token)

    try:
        line_bot_api.push_message(GId, TextSendMessage(text=text))
    except LineBotApiError as e:
        print(e.message)


def scraping_update():
    url = '****************************************************************************' 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    return soup.text



def output_txt(result):
    with open('log.txt', 'w',encoding='utf_8') as f:
        
        f.write(result)
            
def read_txt():
    
    f = open('log.txt', 'r', encoding='UTF-8')

    data = f.read()

    f.close()
    
    return data
   


def main():
    
    check = ""
    
    while True:
        
        check_update = scraping_update()
        
        check_read_update = read_txt()
        
        if check_update == check_read_update:
            
            pass
        
        else:
            
            send_message("更新がありました")
            
            output_txt(check_update)
            
        sleep(43200)
        
if __name__ == '__main__':
    
    main()     
        
        