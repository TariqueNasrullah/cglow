from __future__ import absolute_import, unicode_literals
from cglow.celery import app
from offlineProblemSolve.models import *
from datetime import datetime, timezone, time
import math

@app.task
def offline_submission_ack(pk):
	this_submission = submission.objects.get(pk=pk)
	problem = problemset.objects.get(pk=this_submission.problem_id.id)
	problem.total_submit += 1
	problem.save()

	print(this_submission)
	return 0