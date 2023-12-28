import sublime
import sublime_plugin

class DiffTabsOpenDefaultSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command(
            'open_file',
            {
                "file": "${packages}/DiffTabs/diff_tabs.sublime-settings"
            }
        )

    def is_visible(self):
        return int(sublime.version()) < 3116

    def is_enabled(self):
        return self.is_visible()
