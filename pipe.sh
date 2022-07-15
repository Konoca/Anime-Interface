#!/bin/sh
pipe_file_path="$(pwd)/pipe/file.txt"

# watchexec -w ./pipe -e txt "if [[ -s $pipe_file_path ]]; then cat $pipe_file_path | xargs -I {} open \"{}\"; printf "" > $pipe_file_path; else echo 'File empty'; fi"

while true
do
	if [[ -s $pipe_file_path ]];
	then
		if [[ "$OSTYPE" == "darwin"* ]]; then
			command='open'
		else
			command='xdg-open'
		fi
		cat $pipe_file_path | xargs -I {} $command "{}"
		printf "" > $pipe_file_path
	fi
done
