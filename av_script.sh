#!/bin/sh

#  av_script.sh
#  
#
#  Created by Omer Ashmaig on 1/9/20.
#  

python2 send_nlx_triggers.py &
python3 controller_log.py &
