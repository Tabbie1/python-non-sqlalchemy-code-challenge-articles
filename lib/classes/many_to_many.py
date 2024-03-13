class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title  
        self.author = author
        self.magazine = magazine
        self.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return [article.magazine for article in Article.all if article.author == self]

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        contributing_authors = []
        articles_by_authors = {}
        for article in self.articles():
            if article.author in articles_by_authors:
                articles_by_authors[article.author] += 1
            else:
                articles_by_authors[article.author] = 1
        
        for author, count in articles_by_authors.items():
            if count > 2:
                contributing_authors.append(author)
        
        return contributing_authors
author_1 = Author("Carry Bradshaw")
magazine_1 = Magazine("Vogue", "Fashion")

article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
article_2 = Article(author_1, magazine_1, "Dating life in NYC")
article_3 = Article(author_1, magazine_1, "2023 Eccentric Design Trends")

author_1.add_article(magazine_1, "How to wear a tutu with style")
author_1.add_article(magazine_1, "Dating life in NYC")
author_1.add_article(magazine_1, "2023 Eccentric Design Trends")

titles = magazine_1.article_titles()  
print("Article titles in magazine:", titles)
