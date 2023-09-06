import colorama, contextlib, os, sys, zipfile

# determine application path (working directory)
app_path = (
	os.path.dirname(sys.executable)
	if getattr(sys, 'frozen', False)
	else sys.path[0]
)

# initialise colour conversion
colorama.init(convert=True)

# set text colour values
class c:
	blue = '\033[96m'
	green = '\033[92m'
	grey = '\033[90m'
	purple = '\033[35m'
	red = '\033[91m'
	reset = '\033[0m'
	yellow = '\033[93m'

# define error function
def alert(
	alert_colour: str,
	alert_type: str,
	alert_body: str,
	filenames: list[str]
) -> str:
	for filename in filenames:
		alert_body = alert_body.replace('[]', f'{c.blue}[{filename}]{c.reset}', 1)
	return f' {alert_colour}[{alert_type.upper()}]{c.reset}' + (' ' * (8 - len(alert_type))) + f'| {alert_body}'

# if mode is set as an argument
try:
	mode = sys.argv[1]

# if mode is not set as an argument
except IndexError:
	mode = ''

# check mode
finally:

	# alert user of mode options and get user input
	print('')
	if not any(mode.lower().startswith(char) for char in ['c', 'e']):
		print(alert(c.yellow, 'NOTICE', 'Mode is not set.', []))
		while not any(mode.lower().startswith(char) for char in ['c', 'e']):
			mode = input(alert(c.purple, 'INPUT', 'Set mode to []ompile or []xtract. > ', ['c', 'e']))
			if any(mode.lower().startswith(char) for char in ['c', 'e']):
				mode_valid = True

# alert user of which mode was selected
print(alert(c.grey, 'RUNNING', 'Mode is set to [].', [mode]))

# determine whether actions were performed
found_valid_files = False

# failsafe
try:

	# alert user of working directory
	print(alert(c.grey, 'RUNNING', f'Working directory: {app_path}', []))

	# for every path
	for dir in os.walk(app_path):

		# failsafe
		try:

			# get folder name
			fn = dir[0]

			# alert user of current directory
			print(alert(c.grey, 'RUNNING', 'Checking folder: ' + (fn.replace(app_path, '') or '(root)'), []))

			# if folder contains .osu files and mode is set to compile
			if mode.lower().startswith('c') and any(
				filename.endswith('.osu') for filename in os.listdir(os.path.join(app_path, fn)) + os.listdir(os.getcwd())
			):
				c_name = (fn.replace(app_path, '') + '.osz')[1:]
				# failsafe
				try:

					# failsafe
					try:

						# create .osz file
						with zipfile.ZipFile(os.path.join(app_path, f'{fn}.osz'), 'x') as zf:
							for dirname, subdirs, files in os.walk(os.path.join(app_path, fn)):
								for file in files:
									zf.write(os.path.join(app_path, fn, file), file)
								print(alert(c.green, 'SUCCESS', 'Created []!', [c_name]))

					# alert user if file already exists
					except FileExistsError:
						with contextlib.suppress(NameError):
							print(alert(c.yellow, 'NOTICE', '[] already exists.', [c_name]))

					# alert user if access is denied
					except PermissionError:
						with contextlib.suppress(NameError):
							print(alert(c.red, 'ERROR', 'Access is denied to [].', [c_name]))

					# found valid file
					found_valid_files = True

				# catch errors
				except Exception as e:
					print(alert(c.red, 'ERROR', e, []))

			# if folder contains .osz files and mode is set to extract
			elif mode.lower().startswith('e') and any(
				filename.endswith('.osz') for filename in os.listdir(os.path.join(app_path, fn)) + os.listdir(os.getcwd())
			):

				# for every .osz file
				for dirname, subdirs, files in os.walk(os.path.join(app_path, fn)):
					for filename in subdirs + files:
						if filename.endswith('.osz'):

							# failsafe
							try:

								# extract .osz file
								with zipfile.ZipFile(os.path.join(app_path, dirname, f'{filename}'), 'r') as zf:
									os.makedirs(os.path.join(app_path, fn, dirname, filename[:filename.rfind('.')]), exist_ok=True)
									zf.extractall(os.path.join(app_path, fn, dirname, filename[:filename.rfind('.')]))
								print(alert(c.green, 'SUCCESS', 'Extracted []!', [filename]))

							# alert user is file is corrupted
							except zipfile.BadZipFile:
								print(alert(c.red, 'ERROR', '[] is corrupted and could not be extracted.', [filename]))

							# alert user if access is denied
							except PermissionError:
								print(alert(c.red, 'ERROR', 'Access is denied to [].', [filename]))

							# catch errors
							except Exception as e:
								print(alert(c.red, 'ERROR', e, []))

							# if no errors were caught
							else:
								found_valid_files = True

		# catch errors
		except Exception as e:
			print(alert(c.red, 'ERROR', e, []))

# if actions are interrupted
except KeyboardInterrupt:
	print(alert(c.yellow, 'NOTICE', 'Interrupted by user.', []))

# catch errors
except Exception as e:
	print(alert(c.red, 'ERROR', e, []))

# alert user if no actions were performed
if not found_valid_files:
	print(alert(c.yellow, 'NOTICE', 'No valid files/folders found.', []))

# alert user of completion
input('\n\tFinished! Press Enter to exit.')
