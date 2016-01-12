from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=128)
    comment = models.TextField()
    country = models.CharField(max_length=128, blank=True)
    url = models.CharField(max_length=128, blank=True)
    ignores = models.ManyToManyField(User, related_name='ignore_set',
                                     blank=True, null=True)

    def __str__(self):
        return "%s" % self.user

    def get_ignorelist(self):
        ignores = []
        for k in self.ignores.all():
            ignores.append(k.id)
        return ignores

    def set_ignorelist(self, ignores):
        self.ignores = []
        for k in ignores:
            try:
                ignore = User.objects.ger(id=k)
                self.ignores.add(ignore)
                self.save()
            except:
                pass

    def serialize(self):
        data = {
            'user': self.user_id,
            'username': self.user.username,
            'nickname': self.nickname,
            'comment': self.comment,
            'country': self.country,
            'url': self.url,
            'ignores': self.get_ignorelist(),
        }
        return data


class Message(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        data = {
            'id': self.id,
            'user': self.user_id,
            'username': self.user.username,
            #'liked': self.like_set_count(),
            'message': self.message,
            'created': self.created.ctime(),
        }
        return data


class Like(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey('Message')


