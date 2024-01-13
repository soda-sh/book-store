all:
	make ui
	make python
	# ./main.py

python:
	python ./new.py

ui:
	pyuic5 -x new.ui -o new.py
	pyrcc5 -o figure_rc.py figure.qrc
