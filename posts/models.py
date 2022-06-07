from django.db import models

#models are tables in db and class based

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        #index slice for title
        return self.text[:50]

    