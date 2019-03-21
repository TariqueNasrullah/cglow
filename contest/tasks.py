from __future__ import absolute_import, unicode_literals
from cglow.celery import app
from contest.models import *
from datetime import datetime, timezone, time
import math
import os
import subprocess
import filecmp
import docker

import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core import serializers

@app.task
def contest_submission_ack(pk):
	submission = contest_submission.objects.get(pk=pk)
	problem = contest_problemset.objects.get(pk=submission.problem_id.id)
	problem.total_submit += 1
	problem.save()

	websocket_send_submission_verdict_change(submission.pk, "Submitted")
	# Judge the Problem here
	# let, there was no submission of this user which was accepted
	# if there is such one just return 0
	# else do the other jobs
	
	#update penalty table

	haveAc = contest_submission.objects.filter(problem_id__contest_id__id=submission.problem_id.contest_id.id, problem_id=submission.problem_id, user_id=submission.user_id, judge_result="Accepted").count()
	
	if haveAc == 0:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

		submissionid = submission.id
		uploadedfile = str(submission.uploaded_file)
		language = submission.language
		timelimit = submission.problem_id.problem_time_limit
		inputfile = str(submission.problem_id.problem_input)
		outputfile = str(submission.problem_id.problem_out)

		res = "Running"
		websocket_send_submission_verdict_change(submissionid, res)
		
		judge_pera = "{} {} {} {} {} {}".format(submissionid, inputfile, outputfile, uploadedfile, language, timelimit)
		client = docker.from_env()
		volume_dir = os.path.join(BASE_DIR, 'contestData/')
		ans = client.containers.run("contestjudger", judge_pera, volumes={volume_dir : {'bind': '/contestData', 'mode': 'rw'}})

		fp = open("contestData/judge_result/{}.txt".format(submissionid), "r")
		fp_content = fp.read()
		res = str(fp_content)

		submission.judge_result = res
		submission.save()

		fp.close()
		websocket_send_submission_verdict_change(submissionid, res)

	else:
		submission.judge_result = "Passed"
		submission.save()
		websocket_send_submission_verdict_change(submission.pk, "Passed")
		return 0


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
			problem.total_solve += 1
			problem.save()
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

@app.task
def websocket_send_submission(pk):
	submitted_code = contest_submission.objects.get(pk=pk)

	contest_name = submitted_code.problem_id.contest_id.pk
	group_name = 'judge_%s' % contest_name
	message = 'submission'

	sub_code = contest_submission.objects.filter(pk=pk)
	submitted_code_json = serializers.serialize('json', sub_code)

	async_to_sync(send_submission)(group_name, message, submitted_code_json)


@app.task
def websocket_send_submission_verdict_change(pk, verdict):
	submissoin = contest_submission.objects.get(pk=pk)
	contest_name = submissoin.problem_id.contest_id.pk
	group_name = 'judge_%s' % contest_name

	submission_id = pk
	message = 'verdict_change'
	new_verdict = verdict

	async_to_sync(send_submission_verdict_change)(group_name, message, submission_id, new_verdict)

async def send_submission(group_name, message, submitted_code_json):
	channel_layer = get_channel_layer()
	await channel_layer.group_send(
		'{}'.format(group_name),
		{
			'type': 'send_submission',
			'message': message,
			'submitted_code': submitted_code_json
		}
	)

async def send_submission_verdict_change(group_name, message, submission_id, new_verdict):
	channel_layer = get_channel_layer()
	await channel_layer.group_send(
		'{}'.format(group_name),
		{
			'type': 'send_submissoin_verdict_change',
			'message': message,
			'submission_id': submission_id,
			'new_verdict': new_verdict
		}
	)