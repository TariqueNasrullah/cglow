from __future__ import absolute_import, unicode_literals
from cglow.celery import app
from contest.models import *
from datetime import datetime, timezone, time
import math

@app.task
def contest_submission_ack(pk):
	submission = contest_submission.objects.get(pk=pk)
	problem = contest_problemset.objects.get(pk=submission.problem_id.id)
	problem.total_submit += 1
	problem.save()

	# Judge the Problem here
	# let, there was no submission of this user which was accepted
	# if there is such one just return 0
	# else do the other jobs
	
	#update penalty table

	penalty = 0
	solve = 0
	submission_list = contest_submission.objects.filter(user_id=submission.user_id, problem_id__contest_id__id=submission.problem_id.contest_id.id)
	is_there_this_contestant = contestant_point.objects.filter(user_id=submission.user_id, contest_id=submission.problem_id.contest_id).count()
	if is_there_this_contestant==0:
		instance = contestant_point(user_id=submission.user_id, contest_id=submission.problem_id.contest_id)
		instance.save()

	contestant = contestant_point.objects.get(user_id=submission.user_id, contest_id=submission.problem_id.contest_id.id)

	for i in submission_list:
		if(i.judge_result == "Accepted"):
			submission_time = i.submission_time
			contest_start_time = i.problem_id.contest_id.start_time
			pnt = submission_time.timestamp() - contest_start_time.timestamp()
			penalty += math.ceil(pnt/60);
			solve += 1
		elif i.judge_result=="Wrong Answer" or i.judge_result=="Run Time Error":
			ac_count = contest_submission.objects.filter(user_id=submission.user_id, problem_id=i.problem_id, judge_result="Accepted").count()
			if ac_count != 0:
				penalty += 20

	contestant.penalty = penalty
	contestant.solve = solve
	contestant.save()