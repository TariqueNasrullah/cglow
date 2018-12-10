from __future__ import absolute_import, unicode_literals
from cglow.celery import app
from offlineProblemSolve.models import *
from datetime import datetime, timezone, time
import math
import os
import subprocess
import filecmp
import docker


@app.task
def offline_submission_ack(pk):
	this_submission = submission.objects.get(pk=pk)
	problem = problemset.objects.get(pk=this_submission.problem_id.id)
	problem.total_submit += 1
	problem.save()

	print(this_submission)

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	submissionid = this_submission.id
	uploadedfile = str(this_submission.uploaded_file)
	language = this_submission.language
	timelimit = this_submission.problem_id.problem_time_limit
	inputfile = str(this_submission.problem_id.problem_input)
	outputfile = str(this_submission.problem_id.problem_output)

	judge_pera = "{} {} {} {} {} {}".format(submissionid, inputfile, outputfile, uploadedfile, language, timelimit)
	client = docker.from_env()
	volume_dir = os.path.join(BASE_DIR, 'offlineProblemData/')
	ans = client.containers.run("offlinejudger", judge_pera, volumes={volume_dir : {'bind': '/offlineProblemData', 'mode': 'rw'}})

	res = ""
	fp = open("offlineProblemData/judge_result/{}.txt".format(submissionid), "r")
	fp_content = fp.read()
	res = str(fp_content)
	fp.close()

	this_submission.judge_result = fp_content;
	this_submission.save()

	return 0