from django.db import models

class Paste(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150,
                             default='',
                             blank=True)
    author = models.CharField(max_length=150,
                              default='',
                              blank=False)
    content = models.TextField()

    class Meta:
        ordering=['created']

    def __unicode__(self):
        return self.title
