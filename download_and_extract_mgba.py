# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2023-04-12 16:53:19
# @Last Modified by:   user
# @Last Modified time: 2023-04-12 19:08:19

from os.path import exists
import requests
import shutil
import subprocess


def download_and_extract_mgba(mgba_link: str):
	"""
	Downloads and extracts mGBA.

	:param str mgba_link: The GitHub link to a 7-Zip archive.
	:return: True if file was downloaded, or if file already exists, False
	"""
	local_filename = mgba_link.split("/")[-1]
	if exists(local_filename) is not True:
		with requests.get(mgba_link, stream=True) as response:
			with open(local_filename, "wb") as file:
				shutil.copyfileobj(response.raw, file)
	else:
		return False

	subprocess.run(["7z", "e", "-y", local_filename, "-o*"])
