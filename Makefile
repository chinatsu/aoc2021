%.py:
	cd $*; python prog.py

golf-%:
	wc -c < $*/prog.py