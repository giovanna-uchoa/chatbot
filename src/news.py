from newsapi import NewsApiClient
from dotenv import load_dotenv
import summarizer
import os


load_dotenv()

# Init
newsapi = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources="bbc-news",
                                          language='en',
                                          )

# /v2/everything
all_articles = newsapi.get_everything(q='apple',
                                      from_param='2024-09-27',
                                      to='2024-09-01',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sourcesBusiness = newsapi.get_sources(category='business',
                                      language='pt',
                                      country='br'
                                     )

sourcesGeneral = newsapi.get_sources(category='general',
                                      language='pt',
                                      country='br'
                                     )


sourcesAll = newsapi.get_sources(language='pt', 
                                 country='br')

print(sourcesBusiness)
print(sourcesGeneral)
print(sourcesAll)
