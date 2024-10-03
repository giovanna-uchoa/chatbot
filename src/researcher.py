from newsapi import NewsApiClient
from datetime import date, datetime
from datetime import timedelta

class NewsAdapter:


    def __init__(self, key: str, language: str, country: str, ignoreSources : list = []) -> None:
        self.model = NewsApiClient(api_key=key)
        self.language = language
        self.country = country

        self.sources = self.get_sources(ignoreSources)
        self.set_everything()

    def get_sources(self, ignore : list = []) -> str:
        sources = ''
        for source in self.model.get_sources(language=self.language, country=self.country).get('sources'):
            if source.get('id') not in ignore:
                sources = f'{sources}{source.get('id')}, '  
        return sources


    def set_everything(self) -> list:
        all_articles = self.model.get_everything(q='',
                                                 sources=self.sources,
                                                 from_param=date.today() - timedelta(days = 1),
                                                 to=date.today(),
                                                 language=self.language,
                                                 sort_by='relevancy',
                                                ).get('articles')

        top_headlines = self.model.get_top_headlines(sources=self.sources, 
                                                     language=self.language
                                                    ).get('articles')
    
        self.articles = self.get_titles(all_articles)
        self.headlines = self.get_titles(top_headlines)
        self.updated = datetime.now()
        

    def get_articles(self) -> list:
        if (self.updated - datetime.now() > timedelta(hours = 8)):
            set_everything() 
        return self.articles


    def get_top_headlines(self) -> list:
        if (self.updated - datetime.now() > timedelta(hours = 8)):
            set_everything() 
        return self.headlines
        

    def get_titles(self, articles):
        titles = []
        for article in articles:
            titles.append(article.get('title'))
        return titles
