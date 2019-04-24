from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        return {
            'first_rounds': self.session.vars['first_rounds'],
        }


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
