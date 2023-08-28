import os, sys, zipfile

# Set this to true so that the first directory is skipped
first = True

# Walk through all directories and subdirectories
for dir in os.walk(sys.path[0]):

	# Skip the first directory (the one this script is in)
	if not first:

		# Get the relative path of the directory
		fn = dir[0].replace(sys.path[0], '')[1:]
		try:

			# If there is an osu file in this directory
			if any(filename.endswith('.osu') for filename in os.listdir(os.path.join(sys.path[0], fn))):

				# Create a zip file with the same name as the directory
				with zipfile.ZipFile(os.path.join(sys.path[0], f'{fn}.osz'), 'x') as zf:

					# Walk through all files in the directory
					for dirname, subdirs, files in os.walk(os.path.join(sys.path[0], fn)):

						# Write each file to the zip file
						for filename in files:
							zf.write(os.path.join(sys.path[0], fn, filename), filename)
						print(f'Created [{fn}.osz]')

		# If the zip file already exists, print a message
		except FileExistsError:
			print(f'File [{fn}.osz] already exists')

	# Set first to false so that the first directory is skipped
	first = False
