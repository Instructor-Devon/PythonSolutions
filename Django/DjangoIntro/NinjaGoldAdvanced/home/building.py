import random
from datetime import datetime

VOWELS = ('a','e','i','o','u')

class Building:
    def __init__(self, name, min_gold, max_gold, losable=False):
        self.name = name
        self.min_gold = min_gold
        self.max_gold = max_gold
        self.losable = losable

    @property
    def description(self):
        verb = 'earns' if not self.losable else 'earns/takes'
        return f"({verb} {self.min_gold}-{self.max_gold} golds)"

    @property
    def display_name(self):
        return self.name[0].upper() + self.name[1:]

    def process(self):
        curr_gold = random.randint(self.min_gold, self.max_gold)
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")

        coin_flip = random.randint(0,1) > 0
        particle = 'an' if self.name[0] in VOWELS else 'a'

        message = f"Earned {curr_gold} from the {self.display_name}! ({now_formatted})" 
        if self.losable and not coin_flip:
            message = f"Entered {particle} {self.display_name} and lost {curr_gold} golds... Ouch... ({now_formatted})"
            curr_gold *= -1

        return (curr_gold, message)

    def __repr__(self):
        return f"<Building: {self.display_name} ({self.min_gold}-{self.max_gold})>"
