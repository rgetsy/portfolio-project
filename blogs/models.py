from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField (max_length=100)
    pubdte = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField (upload_to='images/')

#only shows 1st 100 of body
    def summary(self):
        return(self.body[:100])

#changes pubdte to display mmddyy without time for html
    def pub_date_pretty (self):
        return self.pubdte.strftime('%b %e %Y')

#changes display on admin to show title not number
    def __str__(self):
        return self.title
#def get_now():
#    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
