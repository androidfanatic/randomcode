while :
do
	s=`curl -s http://collegecirculars.unipune.ac.in/sites/examdocs/Results/Forms/Active%20Results.aspx | grep "Engineering" | grep -o "[0-9]*" | tail -1 |  xargs echo`
	echo "Got: $s"
	if [ $s -ge "16" ]; then
		notify-send -u critical -t 5000 "Results out."
	#else
		# notify-send -u critical -t 5000 "No results."
	fi
	# wait 1 minute
	sleep 60
done
