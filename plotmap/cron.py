import time
import os
import sys
from django_cron import CronJobBase, Schedule
from django.conf import settings

class MyCronJob(CronJobBase):
	RUN_EVERY_MINS = 1 # every 1 mins
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'plotmap.cron.remove'
	#code = 'my_app.my_cron_job' # a unique code
	
	def do(self):
		print('Done')
		one_day_ago = time.time() - 3600
		path = "files/"
		for f in os.listdir(path):
			f = os.path.join(path, f)
			if os.stat(f).st_mtime < one_day_ago:
				if os.path.isfile(f):
					os.remove(f)
	
def remove():
	print('Done')
	one_minute_ago = time.time() - 60
	path = "files/"
	for f in os.listdir(path):
		f = os.path.join(path, f)
		if os.stat(f).st_mtime < one_minute_ago:
			if os.path.isfile(f):
				os.remove(f)
