from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=200, unique=True, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik",)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now_add=True, verbose_name="Güncellenme Tarihi")
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    active = models.BooleanField(default=False, verbose_name="Onay")
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = "Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name = "İsim")
    comment_content = models.CharField(max_length=200, verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name = "Tarih")
    active = models.BooleanField(default=False, verbose_name="Onay")
    email = models.EmailField()
    class Meta:
        ordering = ["comment_date"]
    
    def __str__(self):
        return "Comment {} by {}".format(self.comment_content, self.comment_author)
