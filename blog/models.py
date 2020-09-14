from tortoise.models import Model
from tortoise import fields


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    body = fields.TextField()
    image = fields.CharField(max_length=250)
    author = fields.ForeignKeyField(
        'accounts.models.User', related_name='author')
    created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title
