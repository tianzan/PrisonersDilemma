from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma'
    players_per_group = None
    num_rounds = 200


class Subsession(BaseSubsession):
    num_matches = models.IntegerField()
    prob_termination = models.IntegerField()

    def creating_session(self):
        match_lengths = []



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
