import os.path
import pickle


class Article:
    def __init__(self, title, genre, director, year_release, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year_release = year_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title} ({self.genre})'


class ArticleModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'название фильма': article.title,
            'жанр': article.genre,
            'режиссер': article.director,
            'год выпуска': article.year_release,
            'длительность': article.duration,
            'студия': article.studio,
            'актеры': article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)
