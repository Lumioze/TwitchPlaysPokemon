# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2023-04-12 16:53:19
# @Last Modified by:   user
# @Last Modified time: 2023-04-12 19:08:19

from os.path import exists
import requests
import shutil
from pyunpack import Archive


'''
download_file(url: str) -> True if file was downloaded, or if file already exists, False


Downloads a file
'''

def download_and_extract_mgba(mgba_link):
	local_filename = mgba_link.split('/')[-1]
	if exists(local_filename) is not True:
		with requests.get(mgba_link, stream=True) as r:
			with open(local_filename, 'wb') as f:
				shutil.copyfileobj(r.raw, f)
	else:
		return False


	Archive(local_filename).extractall('.')