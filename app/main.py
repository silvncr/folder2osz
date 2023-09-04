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
	red = '\033[91m'
	reset = '\033[0m'
	yellow = '\033[93m'

# determine working mode
mode = ''

# if mode is set as an argument
try:
	mode = sys.argv[1]

# if mode is not set as an argument
except IndexError:
	mode_valid = False

# alert user if mode is set
else:
	mode_valid = True
	print(f'\n\tMode set to [{mode}]\n')

# if mode is not set as an argument
finally:

	# alert user of mode options and get user input
	if not any(mode.lower().startswith(char) for char in ['c', 'e']):
		print(f'\n\tMode: {c.blue}[c]{c.reset}ompile or {c.blue}[e]{c.reset}xtract\n')
		while not mode_valid:
			mode = input('\t> ')
			if any(mode.lower().startswith(char) for char in ['c', 'e']):
				mode_valid = True
				print('')

# determine whether actions were performed
found_valid_files = False

# failsafe
try:

	# alert user of working directory
	print(f' {c.yellow}[NOTICE]{c.reset}  | Working directory: {app_path}')

	# for every path
	for dir in os.walk(app_path):

		# failsafe
		try:

			# get folder name
			fn = dir[0]

			# alert user of current directory
			print(f' {c.grey}[RUNNING]{c.reset} | Checking folder:', fn.replace(app_path, '') or '(root)')

			# if folder contains .osu files and mode is set to compile
			if mode.lower().startswith('c') and any(
				filename.endswith('.osu') for filename in os.listdir(os.path.join(app_path, fn)) + os.listdir(os.getcwd())
			):

				# failsafe
				try:

					# create .osz file
					with zipfile.ZipFile(os.path.join(app_path, f'{fn}.osz'), 'x') as zf:
						for dirname, subdirs, files in os.walk(os.path.join(app_path, fn)):
							for filename in files:
								zf.write(os.path.join(app_path, fn, filename), filename)
							print(f' {c.green}[SUCCESS]{c.reset} | Created {c.blue}[{fn.replace(app_path, "")}.osz]{c.reset}!')

				# alert user if file already exists
				except FileExistsError:
					with contextlib.suppress(NameError):
						if filename.endswith('.osz'):
							print(f' {c.yellow}[NOTICE]{c.reset}  | {c.blue}[{filename}]{c.reset} already exists.')

				# catch errors
				except Exception as e:
					print(f' {c.red}[ERROR-1]{c.reset} | {e}')

				# if no errors were caught
				else:
					found_valid_files = True

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
								print(f' {c.green}[SUCCESS]{c.reset} | Extracted {c.blue}[{filename}]{c.reset}!')

							# alert user is file is corrupted
							except zipfile.BadZipFile:
								print(f' {c.red}[ERROR-2]{c.reset} | {c.blue}[{filename}]{c.reset} is corrupted and could not be extracted.')

							# alert user if access is denied
							except PermissionError:
								pass

							# catch errors
							except Exception as e:
								print(f' {c.red}[ERROR-3]{c.reset} | {e}')

							# if no errors were caught
							else:
								found_valid_files = True

		# catch errors
		except Exception as e:
			print(f' {c.red}[ERROR-4]{c.reset} | {e}')

# if actions are interrupted
except KeyboardInterrupt:
	print(f' {c.yellow}[NOTICE]{c.reset}  | Interrupted by user.')

# catch errors
except Exception as e:
	print(f' {c.red}[ERROR-5]{c.reset} | {e}')

# alert user if no actions were performed
if not found_valid_files:
	print(f' {c.yellow}[NOTICE]{c.reset}  | No valid files/folders found.')

# alert user of completion
input('\n\tFinished! Press Enter to exit.')
