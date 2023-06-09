# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2023-04-13 11:51:16
# @Last Modified by:   user
# @Last Modified time: 2023-04-15 16:54:09

import time
from config import Config
# from constants import *
from download_and_extract_mgba import *
from automate import setup_mgba, press
from twitch_chat_irc import twitch_chat_irc


def callback(message):
	print(message)
	hex_color = message["color"]
	if hex_color != '':
		rgb_color = tuple(int(ip[i:i+2],16) for i in (0, 2, 4))
	else:
		rgb_color = (255, 255, 255)

	twitch_color = f"\033[38;2;{rgb_color[0]};{rgb_color[1]};{rgb_color[2]}m"
	reset = "\033[0m"
	print(f"{twitch_color}{message['display-name']}{reset}: {message['message']}")

	press(message, handle)


def run():
	print("=======================================")
	print("Welcome to the Twitch Plays Pokémon Bot")
	print("=======================================")
	Config.load_settings()

	global handle
	handle = setup_mgba()
	connect()


def connect(connection_delay=2):
	try:
		twitch_channel = Config.twitch_channel_value()
		connection = twitch_chat_irc.TwitchChatIRC()
		connection.listen(twitch_channel, on_message=callback)
	except Exception as e:
		print(e)
		print(f"Attempting to connect in {connection_delay} seconds...")
		connection_delay = connection_delay * 2 + 2
		time.sleep(connection_delay)
		connect(connection_delay)
