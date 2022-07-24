# DiffTabs

Sublime Text 2/3/4 plugin that adds the option to diff the current tab with another open tab.

## Usage

![usage-1](https://user-images.githubusercontent.com/15936962/180658183-5ae16438-1cce-4062-86cb-9a23fddfd113.gif)

Right click another tab along the tab bar and select "Diff with current tab…" (The tab you right click will be the from-file and the current tab will be the to-file).
Your diff results will appear in a new tab.

## Installation

**Package Control:** 

1. Install [Package Control](https://packagecontrol.io/installation) if necessary.
2. Open the Command Palette by pressing <kbd>&#8984;</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Linux/Windows.
3. Type in `Package Control: Install Package` and press <kbd>Enter</kbd>
4. Type `DiffTabs` and hit <kbd>Enter</kbd>

**Without Git:** Download the latest source from [GitHub](https://github.com/soandrew/DiffTabs) and extract archive to your Sublime Text "Packages" directory.

**With Git:** Clone the repository to your Sublime Text "Packages" directory:

- `git clone https://github.com/soandrew/DiffTabs.git`

The "Packages" directory is located at:

- ST2: 
    - OS X: `~/Library/Application Support/Sublime Text 2/Packages`
    - Linux: `~/.config/sublime-text-2/Packages`
    - Windows: `%APPDATA%\Sublime Text 2\Packages`
- ST3/ST4:
    - OS X: `~/Library/Application Support/Sublime Text 3/Packages`
    - Linux: `~/.config/sublime-text-3/Packages`
    - Windows: `%APPDATA%\Sublime Text 3\Packages`
