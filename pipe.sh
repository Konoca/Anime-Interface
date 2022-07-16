pipe_file_path="$(pwd)/pipe/file.txt"

printf "" > $pipe_file_path
while true
do
	if [[ -s $pipe_file_path ]];
	then
		if [[ "$OSTYPE" == "darwin"* ]]; then
			command='open'
		elif [ $(uname -r | sed -n 's/.*\( *Microsoft *\).*/\1/ip') ]; then
			command='wslview'
		else
			command='xdg-open'
		fi
		cat $pipe_file_path | xargs -I {} $command "{}"
		printf "" > $pipe_file_path
	fi
done
