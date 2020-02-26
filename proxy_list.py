from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import os
os.system(r'nul > proxy_list.txt')




def parse_proxy(tr):
    list_ip = tr.find_all('td',class_='tdl')
    for td in list_ip:
        if len(td.text) > 4:
            return td.text.strip()
def parse_port(tr):
    list_ip = tr.find_all('td')
    for td in list_ip:
        if td.text.isdigit():
            return td.text.strip()






def main():
    url = 'https://hidemy.name/en/proxy-list/'
    opts = Options()
    # opts.set_headless()
    # assert opts.headless   #без графического интерфейса.    
    browser = webdriver.Chrome(r'C:\Users\mkura\Downloads\chromedriver_win32\chromedriver.exe',options=opts)
    browser.get(url)
    sleep(7)
    
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    list_columns = soup.find('tbody').find_all('tr')
    list_proxy =[]
    
    for tr in list_columns:
        file_txt = open('proxy_list.txt','a')
        proxy_ip = parse_proxy(tr)
        proxy_port = parse_port(tr)
        if proxy_ip and proxy_port:
            stroka = proxy_ip +':'+proxy_port
            stroka = stroka.replace(' ','')
            file_txt.write(stroka+'\n')
            file_txt.close()
            list_proxy.append(stroka)
    browser.close()
    return list_proxy
    
            

    


if __name__ == "__main__":
    main()
