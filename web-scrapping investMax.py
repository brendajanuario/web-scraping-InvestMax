import requests
import bs4
from bs4 import BeautifulSoup
import time
import datetime
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

dataFinal = datetime.date(2016,5,13)
#  Yahoo : Economia,  InfoMoney,  Último Segundo,  MoneyTimes,  Yahoo : Economia Negócios,  Portal Exame,  G1
indice = 1 #numero da pagina
indiceStr = str(indice) #numero da pagina em string
booldataLimite = 0


def saveNewsMoneyTimes(link,fonte,day, titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        div = soup.find('div',{'class':'single__text'}) #acessa a data da notícia
        p = div.find_all('p')            
        for link in p:  
            conteudoTextual = conteudoTextual + (link.text)    
        with open("Notícias MoneyTimes/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsInfoMoney(link,fonte,day, titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        scripts = soup.findAll(['script', 'style','li','ul','h2'])
        for match in scripts:
            match.decompose()
            
        div = soup.find('div',{'class':'article__content'}) #acessa a data da notícia
        conteudoTextual = div.text.strip()
        
        with open("Notícias InfoMoney/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")
            

def saveNewsUltimoSegundo(link, fonte, day, titulo):
    conteudoTextual = ""
    https = "https:"
    if link[:6] != https:
        link = https+link
    try:
        print(link)
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:

        print(e)
    except URLError:
        print("Erro foi aquie 2")
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        div = soup.find('div',{'id':'noticia'}) #acessa a data da notícia
        p = div.find_all('p')            
        for link in p:  
            conteudoTextual = conteudoTextual + (link.text)
        with open("Notícias Último Segundo/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)     
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsYahoo(link,fonte,day,titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        ps = soup.find_all('p',{'class':'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm'}) #acessa a data da notícia
        for p in ps:  
            conteudoTextual = conteudoTextual + (p.text)
        with open("Notícias Yahoo/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)  
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsG1(link,fonte,day,titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        noticias = soup.find("div",{"class": "materia-conteudo entry-content clearfix"})
        p = noticias.find_all('p')
        for el in p:
            conteudoTextual = conteudoTextual + (el.text.strip())
            
        with open("Notícias G1/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)  
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsPortalExame(link,fonte,day,titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        div = soup.find('section',{'class':'article-content'}) #acessa a data da notícia
        p = div.find_all('p')
        for el in p:
            conteudoTextual = conteudoTextual + (el.text.strip())
            
        with open("Notícias Portal Exame/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsAE(link,fonte,day,titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        div = soup.find('div',{'class':'n--noticia__content content'}) #acessa a data da notícia
        conteudoTextual = (div.find('p').text)
        with open("Notícias AE/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)   
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")

def saveNewsUOL(link,fonte,day,titulo):
    conteudoTextual = ""
    try:
        res = requests.get(link)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        section = soup.find('article',{'id':'news'}) #acessa a data da notícia
    #    print(section)
        p = section.find_all('p')            
        for link in p:  
            conteudoTextual = conteudoTextual + (link.text.strip())
        with open("Notícias UOL/"+titulo+".txt", "a", encoding="utf-8") as file: #salva o conteúdo da notícia em um .txt
            file.write ("Classificação do título: \nClassificação da notícia: \n\n"+titulo+"\n"+day+"\n\n"+conteudoTextual)
            print("Noticia salva: \n", fonte, "\n",titulo,"\n\n")
            
def OpenNew(url, fonte, day):        
    try:
        res = requests.get(url)
        res.raise_for_status()
    except HTTPError as e:
        print(e)
    except URLError:

        print("Server down or incorrect domain")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        noticias = soup.find("a",{"class": "noticiasTitContent"})
        link = noticias.get('href')
        titulo = noticias.text
        dict = str.maketrans('"\/:*<>|?,.',"'          ")
        titulo = titulo.translate(dict)#removendo caracteres especiais
        
        if fonte.strip() == "MoneyTimes":
            saveNewsMoneyTimes(link,fonte,day,titulo)
            
        if fonte.strip() == "Último Segundo":
           saveNewsUltimoSegundo(link,fonte,day,titulo)
            
        if fonte.strip() == "InfoMoney":
            saveNewsInfoMoney(link,fonte,day, titulo)

        if fonte.strip() == "Yahoo : Economia Negócios" or fonte.strip() == "Yahoo : Economia":
            saveNewsYahoo(link,fonte,day,titulo)
        
        if fonte.strip() == "G1":
            saveNewsG1(link,fonte,day,titulo)
        
        if fonte.strip() ==  "Portal Exame":
            saveNewsPortalExame(link,fonte,day,titulo)
            
        if fonte.strip() ==  "UOL":
            saveNewsUOL(link,fonte,day,titulo)    
        
        if fonte.strip() == "AE : Empresas e Negócios" or fonte.strip() =="AE : Economia" or fonte.strip() =="AE : Finanças":
            saveNewsAE(link,fonte,day,titulo)


while True:
    if booldataLimite == 1: #quando a data inicial = data final
        print("Todas noticias foram encotnradas!")
        break
    try:
        html = urlopen("https://investmax.com.br/Noticias/bradesco/"+indiceStr+"/1000/")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        i=0
        iniciando=0
        soup = BeautifulSoup(html.read(), "html5lib")
        div = soup.find("div", {"class": "conteudoD"}) #acessa os parágrafos da notícia
        links = div.find_all('h3') 
        datas = soup.find_all('p', {"class":"DataFonte"})
        if (len(links)) == 1:
            print("Todos links foram coletados!\n\n")
            break                 
        else:
            for link in links:
                if iniciando != 0: #pular o primeiro link
                    url = "https://investmax.com.br" + link.find('a').get('href')                
                    day = (datas[i].getText())[:10]
                    fonte = (datas[i].getText())[23:]   
                    dataNoticia = datetime.datetime.strptime(day, '%d/%m/%Y')
                    
                    if dataNoticia.date() < dataFinal:
                        print("Todos links foram coletados!\n\n")
                        booldataLimite = 1
                        time.sleep(5)
                        break                    

                    OpenNew(url, fonte, day)

                    i = i +1
                iniciando = 1
        
        indice = indice + 1
        indiceStr = str(indice)


################################## MONEYTIMES ######################################
"""try:
    res = requests.get('https://moneytimes.com.br/quer-entender-a-necessidade-da-reforma-da-previdencia-bradesco-explica/')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    div = soup.find('div',{'class':'single__text'}) #acessa a data da notícia
    p = div.find_all('p')            
    for link in p:  
        print(link.text)
"""
################################## Ultimo Segundo #######################################
"""try:
    res = requests.get('https://economia.ig.com.br/empresas/2019-05-06/bradesco-anuncia-compra-de-banco-da-florida-por-r-2-bilhoes.html')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    div = soup.find('div',{'id':'noticia'}) #acessa a data da notícia
    p = div.find_all('p')            
    for link in p:  
        print(link.text)
"""
################################### YAHOO ##########################################################################
"""try:
    res = requests.get('https://br.noticias.yahoo.com/presidente-bradesco-diz-que-economia-brasileira-deixou-pior-124927855--finance.html')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    ps = soup.find_all('p',{'class':'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm'}) #acessa a data da notícia
#    p = div.find_all('p')            
    for p in ps:  
        print(p.text)"""
###################################### INFOMONEY #####################################################################
"""        try:
    res = requests.get('https://www.infomoney.com.br/mercados/acoes-e-indices/noticia/5858389/santander-eleva-bradesco-venda-milhoes-acoes-gerdau-agitam-radar')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    div = soup.find('div',{'class':'article__content'}) #acessa a data da notícia
    p = div.find_all('span')            
    for link in p:  
        print(link.text)

"""
##################################### AE ##############################################################################
"""
try:
    res = requests.get('https://economia.estadao.com.br/noticias/geral,vendas-do-setor-automotivo-crescem-18-em-outubro,74211')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    div = soup.find('div',{'class':'n--noticia__content content'}) #acessa a data da notícia
    print(div.find('p').text)            
"""
##################################### UOL ###############################3
"""try:
    res = requests.get('https://www1.folha.uol.com.br/mercado/2010/10/820883-lucro-do-bradesco-cresce-39-para-r-252-bilhoes.shtml')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    section = soup.find('article',{'id':'news'}) #acessa a data da notícia
#    print(section)
    p = section.find_all('p')            
    for link in p:  
        print(link.text.strip())"""
##################################### G1 ###################################
"""        try:
    res = requests.get('http://g1.globo.com/economia-e-negocios/noticia/2010/06/bradesco-inclui-acoes-do-itau-unibanco-na-carteira-de-junho.html')
    res.raise_for_status()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    noticias = soup.find("div",{"class": "materia-conteudo entry-content clearfix"})
    p = noticias.find_all('p')
    for el in p:
        print(el.text.strip())"""