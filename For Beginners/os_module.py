import os
from datetime import datetime

# Shows all attributes and methods that are available.
print(dir(os))

# Get Current Working Directory
print(os.getcwd())

# Navigate to desktop
os.chdir('/home/michael/Downloads')
print(os.getcwd())

# Lists files and folders
print(os.listdir())

# Create directory
os.mkdir('pythonFolder')

# Delete a directory
os.rmdir('pythonFolder')

# To create tree structures
os.makedirs('pythonFolder2/SubDirs')

# Delete directory and sub folders
os.removedirs('pythonFolder2/SubDirs')

# Make and rename a file
os.mkdir('rename.txt')
os.rename('rename.txt', 'demo.txt')

# Get file info
print(os.stat('demo.txt'))

# Print file size
print(os.stat('demo.txt').st_size)

# Get modified date with datetime conversion
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
os.rmdir('demo.txt')


# See entire directory tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# Use environmental variable to get the HOME path
print(os.environ.get('HOME'))

# Create file with the correct "/" placement. As soon paths will include the "/" others may not i.e. home/ and home
file_path = os.path.join(os.environ.get('HOME'), 'text.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test'))
print(os.path.splitext('/tmp/test.txt'))
