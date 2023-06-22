from django.db import models


class Quote(models.Model):
    book = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book}: {self.text}'
