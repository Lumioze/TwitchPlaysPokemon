# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2023-04-13 11:51:16
# @Last Modified by:   user
# @Last Modified time: 2023-04-14 15:51:30

from constants import *
from download_and_extract_mgba import *
from automate import setup_mgba, press
from twitch_chat_irc import twitch_chat_irc


def callback(message):
	print(message)
	press(message['message'], hld)

def run():
	global hld
	hld = setup_mgba(mgba_executable, mgba_link)
	connection = twitch_chat_irc.TwitchChatIRC()

	connection.listen(input('Which Twitch channel would you like to join? ').lower(), on_message=callback)

