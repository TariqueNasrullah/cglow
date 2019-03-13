from django.db import models
from django.contrib.auth.models import User

class contest(models.Model):
	name = models.CharField(max_length=200)
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.name

class contest_problemset(models.Model):
	problem_title = models.CharField(max_length=5)
	problem_name = models.CharField(max_length=300)
	problem_file = models.FileField(upload_to='contestData/problemset/', blank=True)
	problem_time_limit = models.FloatField(default=2.0)
	problem_input = models.FileField(upload_to='contestData/problemset_input/', blank=True)
	problem_out = models.FileField(upload_to='contestData/problemset_output/', blank=True)
	total_submit = models.IntegerField(default=0)
	total_solve = models.IntegerField(default=0)
	contest_id = models.ForeignKey(contest, on_delete=models.CASCADE)
	special_judge = models.BooleanField(default=False)

	def __str__(self):
		return self.problem_name

class contest_submission(models.Model):
	problem_id = models.ForeignKey(contest_problemset, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	judge_result = models.CharField(max_length=50, default="Submitted")
	submission_time = models.DateTimeField(auto_now_add=True)
	uploaded_file = models.FileField(upload_to='contestData/user_submission/')
	language = models.CharField(max_length=50)

	def __str__(self):
		return self.problem_id.contest_id.name + "  " + self.user_id.username + "  " + self.judge_result

class contestant_point(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	contest_id = models.ForeignKey(contest, on_delete=models.CASCADE)
	penalty = models.IntegerField(default=0)
	solve = models.IntegerField(default=0)