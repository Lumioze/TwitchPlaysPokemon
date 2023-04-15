# For Maintainers

If you're not a maintainer, check out the [README.md](./README.md) instead!

This project is only maintained for Windows, as it relies on Windows APIs for inputs.

## Building

First, download these pre-requsites:

- [7-Zip](https://www.7-zip.org/) - Used for extracting mGBA
- [Git](https://git-scm.com/) - For cloning the repository
- [Python 3.9](https://python.org) - At the time of writing, `pydle` only supports up to 3.9.

<details>
<summary>Install Pre-requisites via CLI</summary>

Notes:

- The following commands are untested, and may not properly work (ex. may not add these programs to your PATH).
- Note from 7-Zip choco package:
  > The installer for 7-Zip is known to close the Explorer process. This means you may lose current work. If it doesn't automatically restart explorer, type explorer on the command shell to restart it.

```
# Via chocolatey:
cinst 7zip python39 git
RefreshEnv.cmd
```

```
# Via winget (built-in):
winget install 7zip.7zip
winget install Python.Python.3.9
winget install Git.Git
```

You may need to restart your terminal in order for the PATH to update. At this point, all these tools should be in your PATH, which is important for this app to work properly.

</details>
<br />

After installing your pre-requisites, run the following commands:

```powershell
git clone https://github.com/Lumioze/TwitchPlaysPokemon
cd TwitchPlaysPokemon

# Create a new virtual environment and activate it.
# The environment will be in the "env" folder
python -m venv env
.\env\Scripts\activate

# Install requirements inside our new virtual environment
pip install -r requirements.txt
```

To run the application, run the following command:
```
python main.py
```
