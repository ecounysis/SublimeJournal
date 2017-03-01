import sublime
import sublime_plugin
import datetime
import random


class JournalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        dt = datetime.datetime.now()
        dtStr = dt.strftime("%m/%d/%Y %H:%M:%S\n")
        s=sublime.load_settings("Journal prompts.sublime-settings")
        prompts = s.get("journal_prompts")
        prompt = prompts[random.randint(0, len(prompts) - 1)]
        header = prompt + '\n' + dtStr
        self.view.insert(edit, 0, header)
