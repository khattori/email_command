import sys
import email.utils

from st2common.runners.base_action import Action

class ParseAddressAction(Action):
    def run(self, address):
        _, ret = email.utils.parseaddr(address)
        return ret
