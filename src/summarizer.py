import maritalk

class MaritacaAdapter:
    model: maritalk.MariTalk
    model_type: str = "sabia-3"

    def __init__(self, key: str) -> None:
        self.model = maritalk.MariTalk(key=key, model=self.model_type)

    def run(self, news_text: str) -> str:
        prompt = """ Resuma a notícia a seguir. Não passe de 5 linhas.
        Mencione inicialmente a manchete da notícia em negrito, por exemplo

        "*[assunto do e-mail original]*
        [Resumo do E-mail]
        "
        Notícia a ser resumido:

        \n{news}
        """.format(news=news_text)
        response = self.model.generate(
            prompt,
            max_tokens=256) # tamanho de um tweet

        summary = response["answer"]
        return summary
