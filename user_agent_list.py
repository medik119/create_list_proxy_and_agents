import requests as req
from bs4 import BeautifulSoup

def get_req(url,browse):
    try:
        r = req.get(url+browse)
    except:
        return None
    if r.status_code == 200:
        return r.text

def soup_obj(agent):
    list_agent = []
    url = 'http://www.useragentstring.com/pages/useragentstring.php?name='
    html = get_req(url,agent)
    if html:
        soup =  BeautifulSoup(html,'lxml')
        div_teg = soup.find('div',{'id':'liste'})
        lnk_teg = div_teg.find_all('a')
        for i in lnk_teg:
            try:
                list_agent.append(i.text.strip())
            except:
                continue
        return list_agent

def main():
    work_list_agent = ['Firefox','Chrome']
    list_user_agent = []
    for i in work_list_agent:
        list_user_agent += soup_obj(i)
    return list_user_agent




if __name__ == "__main__":
    main()
