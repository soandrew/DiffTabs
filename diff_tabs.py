# coding: utf-8
import sublime_plugin

class DiffTabsCommand(sublime_plugin.WindowCommand):
    def run(self, group, index):
        window = self.window
        view = window.active_view()

        if window.get_view_index(view) == (group, index):
            return

        this_file = view.file_name()
        other_file = window.views_in_group(group)[index].file_name()

        window.run_command("diff_files", {"files": [this_file, other_file]})

    def is_visible(self, group, index):
        window = self.window
        view = window.active_view()
        return window.get_view_index(view) != (group, index)
