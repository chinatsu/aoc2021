%.py:
	cd $*; python prog.py < in

golf-%:
	wc -c < $*/prog.py