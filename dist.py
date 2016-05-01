version = '1'

import os
import shutil
import subprocess

# configure.ac

with open('configure.ac') as f:
	xs = f.readlines()

xs[0] = 'AC_INIT([memtest], [%s], [russell.wallace@gmail.com], [memtest], [https://github.com/russellw/memtest])\n' % version

with open('configure.ac', 'wb') as f:
	f.writelines(xs)

# Makefile.am

with open('Makefile.am') as f:
	xs = f.readlines()

i = 0
while not xs[i].startswith('memtest_SOURCES '):
	i += 1
i += 1

j = i
while xs[j].startswith('\t'):
	j += 1
del xs[i:j]

ys = []
for root, dirs, files in os.walk('.'):
	for filename in files:
		if os.path.splitext(filename)[1] in ('.c', '.h'):
			ys.append('\t' + filename)
for j in xrange(len(ys) - 1):
	ys[j] += '\\'
for j in xrange(len(ys)):
	ys[j] += '\n'
xs[i:i] = ys

with open('Makefile.am', 'wb') as f:
	f.writelines(xs)

# memtest.c

with open('memtest.c') as f:
	xs = f.readlines()

for i in xrange(len(xs)):
	if xs[i].startswith('#define version '):
		xs[i] = '#define version "%s"\n' % version

with open('memtest.c', 'wb') as f:
	f.writelines(xs)

# build

subprocess.check_call('build.bat')

# zip

d = 'memtest-' + version
if os.path.exists(d):
	shutil.rmtree(d)
os.mkdir(d)

subprocess.check_call('copy *.bat ' + d, shell=1)
subprocess.check_call('copy *.c ' + d, shell=1)
subprocess.check_call('copy *.exe ' + d, shell=1)
subprocess.check_call('copy *.md ' + d, shell=1)
subprocess.check_call('copy LICENSE ' + d, shell=1)

subprocess.check_call('del *.zip', shell=1)
subprocess.check_call('7z a ' + d + '.zip ' + d)

shutil.rmtree(d)
