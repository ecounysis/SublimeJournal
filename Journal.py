import sublime
import sublime_plugin
import datetime
import random


class JournalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        right_now = datetime.datetime.now()
        time_tuple = right_now.timetuple()
        year = time_tuple.tm_year
        day_of_year = time_tuple.tm_yday
        date_string = right_now.strftime("%m/%d/%Y %H:%M:%S")
        settings = sublime.load_settings("Journal prompts.sublime-settings")
        daily_prompts = settings.get("daily_prompts")
        random_prompts = settings.get("random_prompts") + daily_prompts
        
        random_prompt = prompts[random.randint(0, len(random_prompts) - 1)]
        daily_prompt = daily_prompts[day_of_year - 1]
        if (year % 4 == 0): # leap year
            if (day_of_year == 60): # leap day
                daily_prompt = "Happy Leap Day! " + random_prompts[random.randint(0, len(random_prompts) - 1)]
            if (day_of_year > 60): # after leap day
                daily_prompt = daily_prompts[day_of_year - 2]
        header = "%s\nRandom Prompt: %s\nDaily Prompt:%s\n\n".format(date_string, random_prompt, daily_prompt)
        self.view.insert(edit, 0, header)
 