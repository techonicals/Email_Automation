import os

report_location = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
print report_location


f = open(os.path.join('Reports', 'file.txt'), 'w')
f.write('This is the new file.')
f.close()

dir = os.getcwd()
print dir