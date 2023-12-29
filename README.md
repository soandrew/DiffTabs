# DiffTabs

Sublime Text 4/3/2 plugin that adds the option to diff the current tab with another open tab.

## Usage

![usage-1](https://gist.github.com/assets/15936962/da63a99f-9f5b-46d7-adec-9b055fe32271)

Right click another tab along the tab bar and select "DiffTabs: Diff With Current Tab…" (The tab you right click will be the from-file and the current tab will be the to-file).
Your diff results will appear in a new tab.

### Keyboard Support

![usage-2](https://gist.github.com/assets/15936962/df207285-ec09-4c02-9b7e-d0dd6cdb9093)

Open the Command Palette by pressing <kbd>&#8984;</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Linux/Windows.
Type in `DiffTabs: Diff With Current Tab…` and press <kbd>Enter</kbd>.
In the dropdown select another tab (The tab you select will be the from-file and the current tab will be the to-file).

## Configuration

- ST2:
    - Preferences > Package Settings > DiffTabs > Settings - User
- ST3/ST4:
    - Preferences > Package Settings > DiffTabs > Settings

| Key           | Possible values         | Default value | Description                                                                                                                           |
|---------------|-------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `"output_to"` | `"buffer"` \| `"panel"` | `"buffer"`    | Where to display diff output to<br>buffer: diff results will display in a new tab<br>panel: diff results will display in bottom panel |

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
