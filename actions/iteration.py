import sys

from st2common.runners.base_action import Action

class IterationAction(Action):
    def run(self, items):
        if len(items) > 0:
            return items[0], items[1:]
        else:
            raise StopIteration 
