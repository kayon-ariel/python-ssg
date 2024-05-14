
# Python Server Side Rendering

Gerando páginas estáticas atualizadas dinamicamente com python.

Esse projeto é apenas um passatempo feito em poucas horas, não deve ser interpretado como algo para produção.
Ficarei feliz em receber sugestões ou implementações de melhorias!
## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/kayon-ariel/Python-SSR.git
```

Inicie o servidor de mock (Somente se for rodar para testes, sem ter alterado o config.json)

```bash
  python mock_api.py
```

Em outro terminal rode o gerador de páginas

```bash
  python watch.py
```
## Declaração das páginas: config.json

```javascript
{
    "pages": {
        "index": {
            "api": {
                "url": "http://127.0.0.1:5000/api/index",
                "method": "GET"
            },
            "render_interval": 5
        },
        "blog": {
            "api": {
                "url": "http://127.0.0.1:5000/api/blog",
                "method": "GET"
            },
            "render_interval": 1
        }
    }
}
```
- As chaves de ```pages``` como index ou blog, devem coresponder ao nome de um arquivo de template dentro de html, por exemplo /html/blog.html que irá gerar ```/dist/blog.html```.
- O json retornado pela API definida no json em pages->blog->api será passado como parâmetro para montar o template.
- O render_interval define de quanto em quanto tempo a página será regenerada, com um novo consumo de API.