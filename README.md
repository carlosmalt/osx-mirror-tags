osx_mirror_tags
===============

Mirror Finder tags in OS X from src directory tree to dst directory tree (assuming all paths in src also exist in dst). 

*Installation:* Requires a Python installation that allows adding new modules

`./setup.py install`

*Command line use:* Create a symbolic link to `osx_mirror_tags/__init__.py` using a name of your choice. Then run that name as command with source and destination paths as arguments. Use absolute paths.

*Example use:* When switching from the old version of Google Drive to Google File Stream's "My Drive", this program copies all Finder tags from files and directories in Google Drive to My Drive (Tip: use "/Volumes/GoogleDrive/My Drive" as destination). This also works when none of My Drive's files are actually downloaded.
