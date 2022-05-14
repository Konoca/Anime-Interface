pipe_file_path="$(pwd)/pipe/file.txt"

watchexec -w ./pipe -e txt "if [[ -s $pipe_file_path ]]; then cat $pipe_file_path | xargs -I {} open \"{}\"; printf "" > $pipe_file_path; else echo 'File empty'; fi"
