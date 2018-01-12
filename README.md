[![build status](https://travis-ci.org/wvoliveira/serint.svg?branch=master)](https://travis-ci.org/wvoliveira/serint)
# Serint

No comeco era pra procurar algum termo sobre vagas no Google, mas voce pode utilizar para outros propósitos.  

Testado:
- Python2.7 >
- Python3 


Como usar?
----------

Modifique a linha `vagas` para os termos que queira buscar no mecanismo de busca:  

vagas = ["atendente", "suporte tecnico"]

Modifique a linha `pesquisa` para qual mecanismo de busca queira utilizar para efetuar tal busca.  

Caso queira pesquisar no DuckDuckGo, ficaria assim: `pesquisa = https://duckduckgo.com/?q=vagas+de+emprego+`

No próprio Google, ficaria assim: `pesquisa = https://www.google.com.br/search?q=vagas+de+`

No yahoo: `pesquisa = https://search.yahoo.com/search?p=vagas+de+emprego+`

Instale as dependencias: `python3 -r requirements.txt`  

E rode passando o arquivo de configuracao como parametro: `python3 serint.py -c conf/example.ini` 

Parabens, voce chegou ao final do tutorial.. Seu certificado chegara no seu e-mail o mais breve possivel. 
