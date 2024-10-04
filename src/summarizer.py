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
    
    def test(self, category: str, articles: str) -> str:
        prompt = """ Selecione as 10 notícias mais importantes a partir das manchetes fornecidas
        abaixo. Faça um resumo de texto corrido e fluído sobre elas, com no mínimo 10 e no máximo
        15 linhas. Retorne apenas o conteúdo do resumo.\n

        manchetes={headlines}\n
        """.format(headlines=headlines)
    
        response = self.model.generate(prompt, max_tokens=1000)
        summary = response["answer"]

        return summary
    