#!/bin/python3

import os

MIDBRANCH='├'
VERTBRANCHEXTEND='|'
ENDBRANCH='└'
HORZBRANCHEXTEND='─'

while(True):
	# Grab input or Q to quit.
	inp = input('\nEnter path to directory or Q to quit (if your path IS "Q", screw you!): ')
	if inp == 'Q':
		break

	# Scan the path and notify on path errors.
	try:
		# scandir returns an iterator of os.DirEntry objects.
		scangen = os.scandir(inp)
	except FileNotFoundError:
		print(f"Path \"{inp}\" was not found. Check the name for errors.")
		continue
	except NotADirectoryError:
		print(f"Path \"{inp}\" does not point to a directory. We may support files in a later release.")
		continue

	# Organize the scanned directory.
	current_dir_directories = []
	current_dir_files = []
	current_dir_symlinks = []
#	current_dir_junctions = []

	for item in scangen:
		if item.is_dir():
			current_dir_directories.append(f"{item.name}/")
		elif item.is_file():
			current_dir_files.append(item.name)
		elif item.is_symlink():
			current_dir_symlinks.append(item.name)

	current_dir_directories.sort()
	current_dir_files.sort()
	current_dir_symlinks.sort()

	total_dir = current_dir_directories + current_dir_files + current_dir_symlinks

	# Print items in directory.
	print(f"{inp}/")
	for item in total_dir:
		if item == total_dir[-1]:
			print(f"{ENDBRANCH}{HORZBRANCHEXTEND} {item}")
		else:
			print(f"{MIDBRANCH}{HORZBRANCHEXTEND} {item}")


	# Close the scanned directory iterator.
	scangen.close()
