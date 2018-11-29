import os
import sys
import math
import subprocess
import filecmp

temp = sys.argv[1]
submissionid = int(temp)

judge_input = sys.argv[2]
judge_output = sys.argv[3]
submitted_code = sys.argv[4]
language = sys.argv[5]

temp = sys.argv[6]
time_limit = float(temp)





where_to_output = "contestData/generatedOutput/{}.txt".format(submissionid)

if language == "C++" or language == "C":
	
	compile_submitted_file = os.system("g++ {} -o solve >/dev/null 2>&1".format(submitted_code))
	res = ""

	if compile_submitted_file == 0:
		input_for_c = open(judge_input)
		output_for_c = open(where_to_output, "w")
		proc = subprocess.Popen("./solve", stdin=input_for_c, stdout=output_for_c, stderr=subprocess.PIPE)
		

		try:
			proc.wait(time_limit)
			proc.communicate()
			if proc.returncode == 0:
				ac = filecmp.cmp(judge_output, where_to_output)

				if ac == True:
					res = "Accepted"
				else:
					res = "Wrong Answer"
			else:
				res = "Run Time Error"
		
		except subprocess.TimeoutExpired:
			proc.kill()
			res = "Time Limit Exceeded"
		input_for_c.close()
		output_for_c.close()
	else:
		res = "Compilation Error"

	judge_result_file = open("contestData/judge_result/{}.txt".format(submissionid), "w")
	judge_result_file.write(res)
	judge_result_file.close()

	
