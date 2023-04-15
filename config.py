import requests
import sys
from configparser import ConfigParser
from os import path


class Config:
	__emulator_header = "emulator"
	__mgba_version_key = "mgba_version"

	def mgba_version_value():
		return Config.parser[Config.__emulator_header][Config.__mgba_version_key]

	__mgba_scaling_key = "mgba_scaling"

	def mgba_scaling_value():
		return Config.parser[Config.__emulator_header][Config.__mgba_scaling_key]

	__mgba_executable_key = "mgba_executable"

	def mgba_executable_value():
		return Config.parser[Config.__emulator_header][Config.__mgba_executable_key]

	__rom_file_key = "rom_file"

	def rom_file_value():
		return Config.parser[Config.__emulator_header][Config.__rom_file_key]

	__chat_header = "chat"
	__twitch_channel_key = "twitch_channel"

	def twitch_channel_value():
		return Config.parser[Config.__emulator_header][Config.__twitch_channel_key]

	parser = ConfigParser()
	"""
	Parses and stores the configuration.
	"""

	__bitness = 64 if sys.maxsize > 2**32 else 32

	def mgba_link():
		return (
			"https://github.com/mgba-emu/mgba/releases/download/"
			+ f"{Config.mgba_version_value()}/mGBA-{Config.mgba_version_value()}-win{Config.__bitness}.7z"
		)

	def mgba_folder():
		return f"mGBA-{Config.mgba_version_value()}-win{Config.__bitness}"

	def mgba_executable_file_path():
		return path.join(Config.mgba_folder(), Config.mgba_executable_value())

	def load_settings():
		"""
		Reads settings, and if the setting doesn't exist,
		prompt the user for them. Afterward, save it into
		a config.ini file.
		"""

		Config.parser.read("config.ini")

		if not Config.parser.has_section(Config.__emulator_header):
			Config.parser.add_section(Config.__emulator_header)

		if not Config.parser.has_option(
			Config.__emulator_header, Config.__mgba_version_key
		):
			mgba_version = (
				input(
					"Type an mGBA version (ex. 0.10.1) to use.\n"
					+ "Leave empty to use the current latest version of mGBA: "
				)
				or requests.get(
					"https://api.github.com/repos/mgba-emu/mgba/releases"
				).json()[0]["tag_name"]
			)
			Config.parser.set(
				Config.__emulator_header, Config.__mgba_version_key, mgba_version
			)

		if not Config.parser.has_option(
			Config.__emulator_header, Config.__mgba_scaling_key
		):
			Config.parser.set(Config.__emulator_header, Config.__mgba_scaling_key, "3")

		if not Config.parser.has_option(
			Config.__emulator_header, Config.__mgba_executable_key
		):
			Config.parser.set(
				Config.__emulator_header, Config.__mgba_executable_key, "mgba-sdl.exe"
			)

		if Config.mgba_executable_value() == "mgba.exe":
			print(
				"\033[1;33mNote: Inputs may not work properly with mgba.exe,"
				+ "with ROM autoloading!\033[0m"
			)

		if not Config.parser.has_option(
			Config.__emulator_header, Config.__rom_file_key
		):
			rom_file = input(
				"Enter the file path to the ROM you wish to automatically load: "
			).strip('" ')
			Config.parser.set(Config.__emulator_header, Config.__rom_file_key, rom_file)

		if not Config.parser.has_section(Config.__chat_header):
			Config.parser.add_section(Config.__chat_header)

		if not Config.parser.has_option(
			Config.__chat_header, Config.__twitch_channel_key
		):
			twitch_channel = (
				input(
					"Enter the Twitch channel you wish to check inputs from"
					+ " (default: argoniumcodes): "
				).lower()
				or "argoniumcodes"
			)
			Config.parser.set(
				Config.__chat_header, Config.__twitch_channel_key, twitch_channel
			)

		with open("config.ini", "w") as file:
			Config.parser.write(file)
