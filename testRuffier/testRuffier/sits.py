from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    def __init__(self, total, **kwagrs):
        self.current = 0
        self.total = total
        my_text = "Залишилось присідань: " +str(self.total)
        super().__init__(text=my_text, **kwagrs)
    def next(self,*args):
        self.current += 1
        remain = max(0, self.total-self.current)
        my_text = "Залишилось присідань: " + str(remain)
        self.text=my_text