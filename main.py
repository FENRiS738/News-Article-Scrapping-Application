import nltk
from newspaper import Article
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Text Summarizer API"}
 
@app.get("/news")
def get_news(url: str):
    try: 
        article = Article(url) 
        article.download()
        article.parse()
        nltk.download('punkt')
        article.nlp()
        return {
            "title": article.title,
            "text": article.text,
            "summary": article.summary,
            "keywords": article.keywords,
            "authors": article.authors,
            "publish_date": article.publish_date,
            "top_image": article.top_image,
            "movies": article.movies,
            "url": article.url,
            "images": article.images
        }
    except Exception as ex:
        return {"error": str(ex)}
