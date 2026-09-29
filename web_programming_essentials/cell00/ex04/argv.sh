if [ $# -eq 0 ]; then
	echo "No arguments supplied"
	exit
fi

for arg in "$1" "$2" "$3"; do
	if [ -n "$arg" ]; then
		echo "$arg"
	fi
done
