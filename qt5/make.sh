#!/bin/sh

pyuic5="/usr/bin/pyuic5"

# for i in new popup_alert popup_input dialog_search dialog_output; do
for i in dialog_edit; do
	{
		echo '#!/bin/python'
		${pyuic5} -x ${i}.ui
	} > ${i}.py
	chmod +x ${i}.py
done
