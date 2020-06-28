import os, json, subprocess
from flask import Flask, request

app = Flask(__name__)

CPUTemp_Var = os.environ['cputemp']
CPUFan_Var = os.environ['cpufan']

SYSTemp_Var = os.environ['systemp']
SYSFan_Var = os.environ['sysfan']

GPUTemp_Var = os.environ['gputemp']


@app.route('/cputemps', methods=['GET'])
def cputempsFunc():
	cpuTemp01 = os.popen("sensors | grep '{}' | awk '{ print $2 } '| tr -d + | tr -d °C".format(CPUTemp_Var)).read()
	# cpuTemp02 = round(cpuTemp01*0.1, ndigits=1) 
	return str(cpuTemp01)

@app.route('/cpufan', methods=['GET'])
def cpuFanFunc():
	cpuTemp01 = os.popen("sensors | grep '{}' | awk '{ print $2 }'".format(CPUFan_Var)).read()
	# cpuTemp02 = round(cpuTemp01*0.1, ndigits=1) 
	return str(cpuTemp01)


@app.route('/systemps', methods=['GET'])
def systempsFunc():
	sysTemp01 = os.popen("sensors | grep '{}' | awk '{ print $2 } '| tr -d + | tr -d °C".format(SYSTemp_Var)).read()
	# cpuTemp02 = round(cpuTemp01*0.1, ndigits=1) 
	return str(sysTemp01)

@app.route('/casefan', methods=['GET'])
def caseFanFunc():
	caseTemp01 = os.popen("sensors | grep '{}' | awk '{ print $2 }'".format(SYSFan_Var)).read()
	# caseTemp02 = round(caseTemp01*0.1, ndigits=1) 
	return str(caseTemp01)


@app.route('/gputemps', methods=['GET'])
def gputempsFunc():
	gpuTemp01 = os.popen("sensors | grep '{}' | awk '{ print $2 } '| tr -d + | tr -d °C".format(GPUTemp_Var)).read()
	# gpuTemp02 = round(gpuTemp01*0.1, ndigits=1) 
	return str(gpuTemp01)


@app.route('/sensors', methods=['GET'])
def sensors():
	sensor = subprocess.check_output("sensors")
	return str(sensor)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=6969, threaded=True, debug=True) # will listen on port 6969
