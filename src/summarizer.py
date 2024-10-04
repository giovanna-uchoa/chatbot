import maritalk

class MaritacaAdapter:
    model: maritalk.MariTalk
    model_type: str = "sabia-3"

    def __init__(self, key: str) -> None:
        self.model = maritalk.MariTalk(key=key, model=self.model_type)

    def run(self, headlines: str) -> str:
        prompt = """ Selecione as 10 notícias mais importantes a partir das manchetes fornecidas
        abaixo. Faça um resumo de texto corrido e fluído sobre elas, com no mínimo 10 e no máximo
        15 linhas. Retorne apenas o conteúdo do resumo.\n

        manchetes={headlines}\n
        """.format(headlines=headlines)
    
        response = self.model.generate(prompt, max_tokens=1000)
        summary = response["answer"]

        return summary
    
    def filter(self, category: str, articles: str) -> None:
        prompt = """ Selecione no máximo 10 das manchetes fornecidas abaixo que 
        entre as categorias [educação, meio ambiente, esporte, economia, saúde, política]
        você classificaria como {category} e relevante para a categoria.
        Retorne somente a lista contendo essas notícias.\n

        Exemplo de resposta caso não haja categorias para o tema:
        []

        Exemplo de resposta caso haja notícias para a categoria:
        ['noticia1', 'noticia2', ...]

        manchetes={articles}\n
        """.format(category=category, articles=articles)
    
        response = self.model.generate(prompt, max_tokens=500)
        filtered_news = response["answer"]


        prompt = """ Faça um resumo de texto corrido e fluído sobre as manchetes fornecidadas
        abaixo com no máximo 15 linhas.
        Retorne apenas o conteúdo do resumo (não cite a estrutura da pergunta).\n

        Se machetes=[], emite uma mensagem lamentando que não há notícias sobre o tema. \n
        
        manchetes={headlines}\n
        """.format(headlines=filtered_news)


        response = self.model.generate(prompt, max_tokens=1000)
        summary = response["answer"]

        return summary
    