#importação  request com o  get
from requests import get

# importação da beutifulshop
from bs4 import BeautifulSoup

# modulo re, ajuda com as expressões regulares.
import re

#modulo json
import json

# link do site
url = "https://..."
link= get(url="https://..."")

# utilizamos o argumeto html.parser para que o python possa analisar
soup = BeautifulSoup(link.text,'html.parser')

# função de capturar o nome do autor
def author():
    if re.search('ted.com',url):
        autor = soup.find("meta",{"name":"author"}).get("content")
        return autor
    elif re.search('olhardigital.com.br',url):
        autor = soup.find("span", {'class':'meta-item'}).text
        return autor
    elif re.search('startse.com',url):
        autor = soup.find('h4').text
        return autor
    else:
        autor ='Desconhecido'
        return autor

#função de capturar a descrição do artigo ou video
def description():
    if re.search('ted.com',url):
        # Pegando cada tag p e colocando ela dentro de uma lista
        descricao = ""
        d = soup.find_all("p")
        for d in d :
        # replace para retirar quebra de  .strip() não funcionou
            descricao+=(d.text.replace("\n",""))
        # replace para retirar os espacos
            descricao = descricao.replace("\t","")
        return descricao
    elif re.search('olhardigital.com.br',url):
        descricao = ''
        # procuramos todas as tags para paragrafo, se tiver separado é só colocar a class da materia escolhida
        d = soup.find_all("p")
        # a cada interção ele vai conctenar com o text e dar um replace no espaço
        for d in d :
            descricao += (d.text.replace('\n',''))
        return descricao
    else:
        descricao = ''
        d = soup.find_all('span', {"style": "font-weight: 400;"})
        for d in d:
            descricao += (d.text)
        return descricao


# titulo pegando o title da pagina
# replace utilizado para retirar partes desnecessarias
def title():
    if re.search('ted.com',url):
        titulo = (soup.find("title").text).replace(author(),"").replace(": ","").replace(" | TED Talk Subtitles and Transcript | TED","")
        return titulo
    elif re.search('olhardigital.com.br',url):
        titulo = (soup.find("title").text)
        return titulo
    elif re.search('startse.com',url):
        titulo = soup.find('h2').text
        return titulo
    else:
        if re.search('noticia',url):
            titulo = soup.find("h1",{'class':'mat-tit'}).text
            return titulo



# re.search utilizado para procurar caracteres
#condicional especifica para o desafio 3
if re.search('talks',url):
    tipo = "Video"
else:
    tipo = "Artigo"

# ordenação de dados que ficará no json
df = {
  "author": author(),
  "body": description(),
  "title": title(),
  "type": tipo,
  "url": url
}
#criando o arquivo json
with open(f'{author()}.json','w',encoding='utf-8') as json_file:

    json.dump(df,json_file,indent=4,ensure_ascii=False)
