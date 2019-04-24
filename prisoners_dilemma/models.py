from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy as np

author = 'TZ'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma'
    players_per_group = 2
    num_rounds = 30


class Subsession(BaseSubsession):
    # these two fields will be imported from the configurations you set
    # they can be set as constants, but this will allow you to change these parameters
    # without changing the code
    num_matches = models.IntegerField()
    prob_termination = models.FloatField()

    # this field keeps track of which match you are on
    match_number = models.IntegerField()

    # these fields keeps track of whether the current round is the first or last periods of a match
    last_period = models.BooleanField()
    first_period = models.BooleanField()

    def creating_session(self):

        if self.round_number == 1:

            # Fetches parameters from settings file
            num_matches = self.session.config['num_matches']
            prob_continue = self.session.config['prob_continue']
            prob_termination = 1 - prob_continue

            # Creates match length array with size equal to the number of matches and stores it in a dictionary
            self.session.vars['match_lengths'] = [None] * num_matches

            # Populates match length array with random match lengths
            for i in range(0, num_matches):
                self.session.vars['match_lengths'][i] = np.random.geometric(prob_termination)

            # Creates an array that tracks of which rounds of a session are the first period of a match
            self.session.vars['first_rounds'] = [None] * num_matches

            # Creates an array that tracks of which rounds of a session are the last period of a match
            self.session.vars['last_rounds'] = [None] * num_matches

            # The first round of the first match is the first round
            self.session.vars['first_rounds'][0] = 1

            # Populates the rest of the last_round array
            for i in range(1, num_matches):
                self.session.vars['first_rounds'][i] = self.session.vars['first_rounds'][i - 1] + \
                                                       self.session.vars['match_lengths'][i - 1]

            for i in range(0, num_matches):
                self.session.vars['last_rounds'][i] = self.session.vars['first_rounds'][i] + \
                                                      self.session.vars['match_lengths'][i] - 1

        # creates a random group structure if the current round is the first period of new matches
        if self.round_number in self.session.vars['first_rounds']:
            self.group_randomly()
            # Fills in first_period and last_period fields
            self.first_period = True
            if self.round_number+1 in self.session.vars['first_rounds']:
                self.last_period = True

        # maintains group structure match from previous round has not terminated
        else:
            self.group_like_round(self.round_number-1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
