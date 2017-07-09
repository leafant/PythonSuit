import os
import time



source = ['D:'+ os.sep +'Gloria'+ os.sep +'IDE'+ os.sep, 'D:'+ os.sep +'Gloria'+ os.sep +'Photo'+ os.sep]

today_dir = 'd:'+ os.sep +'Sumbline'+ os.sep + time.strftime('%Y%m%d')

now_time = time.strftime('%H%M%S')

if not os.path.exists(today_dir):
	os.mkdir(today_dir)

target_file = today_dir + os.sep + now_time + '.zip'

zip_command = "7z a %s %s -r" % (target_file, ' '.join(source))

print zip_command

if(os.system(zip_command) == 0):
	print 'Successfully back up to' + target_file
else:
	print 'Failed to backup!'