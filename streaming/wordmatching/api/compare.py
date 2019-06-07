from fuzzywuzzy import fuzz
import re


class Compare:
    def __init__(self, value, whitelist):
        self.value = value
        self.whitelist = whitelist

    def regex(self, regex_list):
        for regex in regex_list:
            if regex.match(self.value) and self.value not in self.whitelist:
                result = {'source':'regex', 'input':regex.pattern, 'value': self.value}
                return result
        return None

    def fuzzy(self, fuzzy_list):
        for fuzzy in fuzzy_list:
            compare = fuzz.partial_ratio(self.value, fuzzy['value'])
            if compare >= int(fuzzy['likelihood']) and domain not in self.whitelist:
                result = {'source':'fuzzy', 'input':fuzzy['value'], 'value': self.value }
                return result
        return None
                