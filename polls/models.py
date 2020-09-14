from tortoise import models, fields
import datetime


class Question(models.Model):
    question_text = fields.CharField(max_length=200)
    pub_date = fields.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= datetime.datetime.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = fields.ForeignKey('models.Question',)
    choice_text = fields.CharField(max_length=200)
    votes = fields.IntegerField(default=0)
