# coding: utf-8
import sublime
import sublime_plugin
import difflib
import time
import os.path

def is_st2():
    return sublime.version()[0] == '2'

def load_settings():
    return sublime.load_settings("diff_tabs.sublime-settings")

def populate_view(view, txt):
    if is_st2():
        view.set_syntax_file('Packages/Diff/Diff.tmLanguage')
        edit = view.begin_edit()
        view.insert(edit, 0, txt)
        view.end_edit(edit)
    else:
        view.assign_syntax('Packages/Diff/Diff.sublime-syntax')
        view.run_command('append', {'characters': txt})

def generate_diff_view(window, aview, bview):
    aname = aview.file_name() if aview.file_name() else aview.name()
    bname = bview.file_name() if bview.file_name() else bview.name()

    a = aview.substr(sublime.Region(0, aview.size())).splitlines()
    b = bview.substr(sublime.Region(0, bview.size())).splitlines()

    adate = time.ctime() if aview.is_dirty() or aview.is_scratch() else time.ctime(os.stat(aname).st_mtime)
    bdate = time.ctime() if bview.is_dirty() or bview.is_scratch() else time.ctime(os.stat(bname).st_mtime)

    diff = difflib.unified_diff(b, a, bname, aname, bdate, adate, lineterm='')
    difftxt = u"\n".join(line for line in diff)

    if difftxt == "":
        sublime.status_message("Files are identical")
    else:
        output_to = load_settings().get('output_to', "buffer")
        if output_to == "panel":
            v = window.get_output_panel('diff_tabs') if is_st2() else window.create_output_panel('diff_tabs')
            populate_view(v, difftxt)
            window.run_command('show_panel', {'panel': 'output.diff_tabs'})
        else:
            v = window.new_file()
            v.set_name(os.path.basename(bname) + " -> " + os.path.basename(aname))
            v.set_scratch(True)
            populate_view(v, difftxt)

class DiffTabsCommand(sublime_plugin.WindowCommand):
    def run(self, group, index):
        window = self.window

        aview = window.active_view()
        if window.get_view_index(aview) == (group, index):
            return
        bview = window.views_in_group(group)[index]

        generate_diff_view(window, aview, bview)

    def is_visible(self, group, index):
        window = self.window
        view = window.active_view()
        return window.get_view_index(view) != (group, index)

class DiffTabsPaletteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        aview = self.view
        other_views = [v for v in window.views() if v.id() != aview.id()]

        def on_select(selected_idx):
            if selected_idx == -1:
                return
            generate_diff_view(window, aview, other_views[selected_idx])

        window.show_quick_panel(
            [os.path.basename(v.file_name()) if v.file_name() else v.name() for v in other_views],
            on_select
        )
