from __future__ import absolute_import, unicode_literals
from cglow.celery import app
from offlineProblemSolve.models import *
from datetime import datetime, timezone, time
import math
import os
import subprocess
import filecmp

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

	

	where_to_output = os.path.join(BASE_DIR, "offlineProblemData/generatedOutput/{}.txt".format(submissionid))
	
	if language == "C++" or language == "C":
		compile_submitted_file = os.system("g++ {} -o solve >/dev/null 2>&1".format(os.path.join(BASE_DIR, uploadedfile)))

		if compile_submitted_file == 0:
			input_for_c = open(os.path.join(BASE_DIR, inputfile))
			output_for_c = open(where_to_output, "w")
			proc = subprocess.Popen("./solve", stdin=input_for_c, stdout=output_for_c, stderr=subprocess.PIPE)

			try:
				proc.wait(timelimit)
				proc.communicate()
				if proc.returncode == 0:
					ac = filecmp.cmp(os.path.join(BASE_DIR, outputfile), where_to_output)
					if ac == True:
						print("Accepted")
						this_submission.judge_result = "Accepted"
					else:
						print("Wrong Answer")
						this_submission.judge_result = "Wrong Answer"
				else:
					print("Run Time Error")
					this_submission.judge_result="Run Time Error"
			except subprocess.TimeoutExpired:
				proc.kill()
				print("Time Limit Exceeded")
				this_submission.judge_result = "Time Limit Exceeded"
			
			input_for_c.close()
			output_for_c.close()
			
		else:
			print("Compilation Error")
			this_submission.judge_result = "Compilation Error"

		this_submission.save()
	return 0