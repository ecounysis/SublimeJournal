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
        
        #school_prompts = []
        #school_prompts_list = settings.get("school_prompts_list")
        #for pr in school_prompts_list:
        #    school_prompts += settings.get(pr)
        #school_prompt = school_prompts[random.randint(0, len(school_prompts) - 1)]

        random_prompts = []
        random_prompts_list = settings.get("random_prompts_list")
        for pr in random_prompts_list:
            random_prompts += settings.get(pr)
        random_prompt = random_prompts[random.randint(0, len(random_prompts) - 1)]
        
        daily_prompts = settings.get("daily_prompts")
        daily_prompt = daily_prompts[day_of_year - 1]
        

        if (year % 4 == 0): # leap year
            if (day_of_year == 60): # leap day
                daily_prompt = "Happy Leap Day! " + random_prompts[random.randint(0, len(random_prompts) - 1)]
            if (day_of_year > 60): # after leap day
                daily_prompt = daily_prompts[day_of_year - 2]
        header = "{}\n\nRandom Prompt:\n{}\n\nDaily Prompt:\n{}\n\n\n\n".format(date_string, random_prompt, daily_prompt)

        self.view.insert(edit, 0, header)
 