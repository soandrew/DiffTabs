import sublime
import sublime_plugin

class DiffTabsOpenUserSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command(
            'open_file',
            {
                "file": "${packages}/User/diff_tabs.sublime-settings",
                "contents": (
                    "// See Preferences > Package Settings > DiffTabs > Settings - Default\n"
                    + "// for the list of settings and valid values\n"
                    + "{\n"
                    + "\t$0\n"
                    + "}\n"
                )
            }
        )

    def is_visible(self):
        return int(sublime.version()) < 3116

    def is_enabled(self):
        return self.is_visible()
