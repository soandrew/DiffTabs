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

class DiffTabsCommand(sublime_plugin.WindowCommand):
    def run(self, group, index):
        window = self.window

        aview = window.active_view()
        if window.get_view_index(aview) == (group, index):
            return
        bview = window.views_in_group(group)[index]

        aname = aview.file_name() if aview.file_name() else aview.name()
        bname = bview.file_name() if bview.file_name() else bview.name()

        a = aview.substr(sublime.Region(0, aview.size())).splitlines()
        b = bview.substr(sublime.Region(0, bview.size())).splitlines()

        adate = time.ctime() if aview.is_dirty() else time.ctime(os.stat(aname).st_mtime)
        bdate = time.ctime() if bview.is_dirty() else time.ctime(os.stat(bname).st_mtime)

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

    def is_visible(self, group, index):
        window = self.window
        view = window.active_view()
        return window.get_view_index(view) != (group, index)
