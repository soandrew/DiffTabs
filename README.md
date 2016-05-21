# DiffTabs

Sublime Test 2/3 plugin that adds the option to diff the current tab with another open tab.

## Usage

Just right click another tab along the tab bar and select "Diff with current tab…" (The tab you right click will be the from-file and the current tab will be the to-file).
Your diff results will appear in a new tab.

## Dependencies

DiffTabs serves as a wrapper around the built in Diff package, so if for any reason your installation did not come with this core package, this plugin will not work. This also limits the diff to unified format.

## Installation

### Manual

Clone the repository to your Sublime Text "Packages" folder:

`git clone https://github.com/soandrew/DiffTabs.git`

The "Packages" folder is located at:

* ST2: 
    * OS X: `~/Library/Application Support/Sublime Text 2/Packages`
    * Linux: `~/.config/sublime-text-2/Packages`
    * Windows: `%APPDATA%\Sublime Text 2\Packages`
* ST3:
    * OS X: `~/Library/Application Support/Sublime Text 3/Packages`
    * Linux: `~/.config/sublime-text-3/Packages`
    * Windows: `%APPDATA%\Sublime Text 3\Packages`

You can also download and extract the archive to the folder.
