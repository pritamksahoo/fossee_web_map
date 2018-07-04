from django.db import models
import uuid
import os

def get_file_path(instance, filename):
    '''To give a unique name to every file'''
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('files/', filename)

class csvfile(models.Model):
	fileobject = models.FileField(upload_to=get_file_path, null=True)
	#filename = models.CharField(max_length=255, null=True)

	def __str__(self):
		return str(self.fileobject)

