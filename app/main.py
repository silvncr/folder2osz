import contextlib, os, re, sys, zipfile
from colorama import init as colorama_init, Fore, Style

colorama_init(convert=True)

class c:
	cyan = '\033[96m'
	green = '\033[92m'
	grey = '\033[90m'
	red = '\033[91m'
	reset = '\033[0m'
	yellow = '\033[93m'

mode = ''
try:
	mode = sys.argv[1]
except IndexError:
	mode_valid = False
else:
	mode_valid = True
	print(f'\n\tMode set to [{mode}]\n')
finally:
	if not any(mode.lower().startswith(char) for char in ['c', 'e']):
		print(f'\n\tMode: {c.cyan}[c]{c.reset}ompile or {c.cyan}[e]{c.reset}xtract\n')
		while not mode_valid:
			mode = input('\t> ')
			if any(mode.lower().startswith(char) for char in ['c', 'e']):
				mode_valid = True
				print('')

found_valid_files = False

try:
	for dir in os.walk(sys.path[0]):
		try:
			fn = dir[0]
			print(f' {c.grey}[RUNNING]{c.reset} | Checking folder:', fn.replace(sys.path[0], '') or '(root)')

			if mode.lower().startswith('c') and any(
				filename.endswith('.osu') for filename in os.listdir(fn)
			):
				try:
					with zipfile.ZipFile(os.path.join(sys.path[0], f'{fn}.osz'), 'x') as zf:
						for dirname, subdirs, files in os.walk(os.path.join(sys.path[0], fn)):
							for filename in files:
								zf.write(os.path.join(sys.path[0], fn, filename), filename)
							print(f' {c.green}[SUCCESS]{c.reset} | Created {c.cyan}[{fn.replace(sys.path[0], "")}.osz]{c.cyan}!')

				except FileExistsError:
					with contextlib.suppress(NameError):
						if filename.endswith('.osz'):
							print(f' {c.yellow}[NOTICE]{c.reset}  | {c.cyan}[{filename}]{c.reset} already exists.')

				except Exception as e:
					print(f' {c.red}[ERROR-1]{c.reset} | {e}')

				else:
					found_valid_files = True

			elif mode.lower().startswith('e') and any(
				filename.endswith('.osz')
				for filename in os.listdir(os.path.join(sys.path[0], fn))
			):

				for dirname, subdirs, files in os.walk(os.path.join(sys.path[0], fn)):
					for filename in subdirs + files:
						if filename.endswith('.osz'):
							try:
								with zipfile.ZipFile(os.path.join(sys.path[0], dirname, f'{filename}'), 'r') as zf:
									os.makedirs(os.path.join(sys.path[0], fn, dirname, filename[:filename.rfind('.')]), exist_ok=True)
									zf.extractall(os.path.join(sys.path[0], fn, dirname, filename[:filename.rfind('.')]))
								print(f' {c.green}[SUCCESS]{c.reset} | Extracted {c.cyan}[{filename}]{c.reset}!')

							except zipfile.BadZipFile:
								print(f' {c.red}[ERROR-2]{c.reset} | {c.cyan}[{filename}]{c.reset} is corrupted and could not be extracted.')

							except PermissionError:
								pass

							except Exception as e:
								print(f' {c.red}[ERROR-3]{c.reset} | {e}')

							else:
								found_valid_files = True

			found_valid_files = True

		except Exception as e:
			print(f' {c.red}[ERROR-4]{c.reset} | {e}')

except KeyboardInterrupt:
	print(f' {c.yellow}[NOTICE]{c.reset}  | Interrupted by user.')

except Exception as e:
	print(f' {c.red}[ERROR-5]{c.reset} | {e}')

if not found_valid_files:
	print(f' {c.yellow}[NOTICE]{c.reset}  | No valid files/folders found.')

input('\n\tFinished! Press Enter to exit.')
