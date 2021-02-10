from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):

        rating_posts_author = 0
        posts_author = Post.objects.filter(author=self)
        for post in posts_author:
            rating_posts_author += post.rating

        rating_comments_author = 0
        comments_author = Comment.objects.filter(user=self.user)
        for comment in comments_author:
            rating_comments_author += comment.rating

        rating_comments_posts = 0
        for post in posts_author:
            comments_for_post = Comment.objects.filter(post=post)
            for comment in comments_for_post:
                rating_comments_posts += comment.rating

        self.rating = rating_posts_author*3 + rating_comments_author + rating_comments_posts

    def return_best_author(self):

        best_author = Author.objects.all().order_by('-rating')[0]
        return f"Лучший пользователь - '{best_author.user.username}' с рейтингом - {best_author.rating}"

    def __str__(self):
        return f'{self.user.username}'


class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):

    article = 'AR'
    news = 'NE'

    ARTICLE_AND_NEWS = [(article, 'Статья'),
                (news, 'Новость')]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_or_news = models.CharField(max_length=2, choices=ARTICLE_AND_NEWS, default=article)
    data_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory', null=True, blank=True)
    heading = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        return self.text[:124] + '...'

    def return_best_article(self):

        best_article = Post.objects.filter(article_or_news='AR').order_by('-rating')[0]
        print(f"Лучшая статья: {best_article.heading}")
        print(f"Статья: {best_article.preview()}")
        print(f"Автор статьи: {best_article.author}")
        print(f"Рейтинг статьи: {best_article.rating}")
        print(f"Дата добавление статьи: {best_article.data_time}")

    def return_all_comment(self):

        all_comment = Comment.objects.filter(post=self)

        for comment in all_comment:
            print('--------------------')
            print(f'Дата: {comment.data_time}')
            print(f'Пользователь: {comment.user.username}')
            print(f'Рейтинг: {comment.rating}')
            print(f'Текст: {comment.text}')
        print('--------------------')

    def __str__(self):
        if self.article_or_news == 'AR':
            return f'Статья - {self.heading}'

        if self.article_or_news == 'NE':
            return f'Новость - {self.heading}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

class PostCategory(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    data_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def __str__(self):
        return f"{self.user} - '{self.text}' к посту '{self.post}'"
