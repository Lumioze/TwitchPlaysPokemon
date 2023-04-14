# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2023-04-12 16:51:52
# @Last Modified by:   user
# @Last Modified time: 2023-04-14 13:16:16


import sys

mgba_version = input("mGBA version (as of writing 0.10.1): ")

bitness = 64 if sys.maxsize > 2**32 else 32
mgba_link = f"https://github.com/mgba-emu/mgba/releases/download/{mgba_version}/mGBA-{mgba_version}-win{bitness}.7z"
mgba_folder = f"mGBA-{mgba_version}-win{bitness}"

mgba_executable = mgba_folder + r"\mgba-sdl.exe"