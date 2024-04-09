class Article:
    # Class variable to store all instances of Article
    all = []

    # Initialization
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    # Properties
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine


class Author:
    # Class variable to store all instances of Author
    all = []

    # Initialization
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # Properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 50 and not hasattr(self,'name'):
            self._name = name

    # Methods
    def articles(self):
        return [article for article in Article.all if article.author is self]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        articles = self.articles()
        if articles:
            return list(set([article.magazine.category for article in articles]))
        else:
            return None


class Magazine:
    # Class variable to store all instances of Magazine
    all = []

    # Initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # Properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category

    # Methods
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        else:
            return None

    def contributing_authors(self):
        # Dictionary to store counts of articles contributed by each author
        author_counts = {}
        
        # Iterate through all articles associated with the magazine
        for article in self.articles():
            author = article.author
            # Increment count for the author if already in dictionary, otherwise initialize count to 1
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        # Filter authors who have contributed more than 2 articles
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        # Return the list of contributing authors if it is not empty, otherwise return None
        if contributing_authors:
            return contributing_authors
        else:
            return None

