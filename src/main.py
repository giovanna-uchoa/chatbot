from dotenv import load_dotenv
import summarizer
import researcher
import os

def setup():
    load_dotenv()

def main():
    setup()

    maritaca = summarizer.MaritacaAdapter(os.getenv("MARITACA_KEY"))
    
    news = researcher.NewsAdapter(os.getenv("NEWS_API_KEY"), 'pt', 'br', ['blasting-news-br'])

    # print(news.get_top_headlines())

    # print(news.get_articles())
   
    '''
    teste = maritaca.run("""
    Escritor, autista e influenciador digital: quem era padre Fabrício Rodrigues, morto em acidente com cavalo no Pará. 
    
    Religioso tinha mais de 600 mil seguidores nas redes sociais. Ele estava de motocicleta e colidiu contra um cavalo na rodovia BR-230 (Transmazônica).
    Escritor, cantor e influenciador digital. Estas são algumas das funções que ajudaram ao padre Fabrício Rodrigues a cumprir com a missão de levar a palavra de Deus para o maior número possível de pessoas. Ele faleceu aos 29 anos, vítima de acidente com cavalo na rodovia BR-230, em São João do Araguaia, região sudeste do Pará, na última quinta-feira (12). (Saiba mais no vídeo ao final desta matéria)
    De todas formas com a qual ele costumava a se apresentar, uma chamava atenção: o padre Fabrício estava dentro do Transtorno do Espectro Autista (TEA).
    Somente em uma rede social, o religioso tinha mais de 600 mil seguidores e ele usava as plataformas digitais a favor da evangelização. Em um dos perfis que mantinha, ele fez questão de mostrar a carteirinha de autista.
“Para mim o autismo se tornou um dom e não um peso. Deus me concedeu esse dom para eu pudesse cuidar de uma forma muito mais humana, tivesse um olhar mais humano, para tantas almas que necessitam ter esse encontro com Jesus Cristo”, disse.
O estudante de Psicologia Elias Ferraz estudou junto com Fabrício e estagiaram juntos. Lembrou da facilidade de se comunicar que o padre tinha, mesmo com autismo.

“Ele tinha muita facilidade de se comunicar, muito carisma, sempre divertido e alegre. A gente lembra que ele sempre levava marmitas ‘fit’ para a faculdade, era um bom aluno bem dedicado”.
    """)

    print(teste)
    '''
main()