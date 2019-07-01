from django.db import models
from django.contrib.auth.models import User

from contest.models import contest, contest_problemset

class clearifications(models.Model):
    associated_contest = models.ForeignKey(contest, on_delete=models.CASCADE)
    associated_problem = models.ForeignKey(contest_problemset, on_delete=models.CASCADE)
    declare_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    clearification_text = models.TextField(max_length=1000, null=False, blank=False)
    judge_ignored = models.BooleanField(default=False)
    judge_answer = models.TextField(max_length=4000, default="", blank=True)

class clearifications_viewed(models.Model):
    clearifications_id = models.ForeignKey(clearifications, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)