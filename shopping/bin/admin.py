# Author: harry.cai
# DATE: 2018/2/1

import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
from shopping.core import admin

admin.run()