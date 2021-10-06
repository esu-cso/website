from django.db import models

class NewsArticles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to ='static/images/userupload/', null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title[:50]