import sys

from st2common.runners.base_action import Action

class SplitTextAction(Action):
    def run(self, text):
        print(text)
        lines = text.splitlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line]
        return lines
