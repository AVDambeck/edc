while : 
do
	inotifywait -e modify "$1"; 
	clear;
	$2;
	sleep 1;
done;
