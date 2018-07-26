from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Daniel Saxon'

doc = """
Your app description
"""




import itertools



class Constants(BaseConstants):
    name_in_url = 'my_21Flags'
    #Single player game, dictates that we indicate 'none' in the Players per
    #group command
    players_per_group = None
    #I believe that 10 rounds should be a good amount in order to "learn"
    #strategy
    num_rounds = 15






class Subsession(BaseSubsession):

    def creating_session(self):
        incentivized = itertools.cycle([True, False])
        for p in self.get_players():
            if 'incentivized' in self.session.config:
                # demo mode
                p.incentivized = self.session.config['incentivized']
            else:
                #live experiment mode
                p.incentivized = next(incentivized)

            if p.incentivized:
                p.endowment = c(0)
            else:
                if self.round_number == 1:
                    p.endowment = c(1500)




class Group(BaseGroup):
        pass

class Player(BasePlayer):
    incentivized = models.BooleanField()

    endowment = models.CurrencyField(initial=0)

    total_endowment = models.CurrencyField()

    total_wins = models.IntegerField()

    is_winner = models.BooleanField(
        choices=[True, False]
    )

    flags_remaining_player_1 = models.LongStringField()

    flags_remaining_player_2 = models.StringField()

    flags_remaining_player_3 = models.StringField()

    flags_remaining_player_4 = models.StringField()

    flags_remaining_player_5 = models.StringField(blank=True)

    flags_remaining_player_6 = models.StringField(blank=True)

    flags_remaining_player_7 = models.StringField(blank= True)

    flags_remaining_player_8 = models.StringField(blank=True)

    flags_remaining_player_9 = models.StringField(blank=True)

    flags_remaining_player_10 = models.StringField(blank=True)

    flags_remaining_player_11 = models.StringField(blank=True)

    flags_remaining_player_12 = models.StringField(blank=True)

    moves = models.IntegerField()

    age = models.IntegerField(min=18)

    sex = models.StringField(
        choices=['Male', 'Female', 'I Choose to Define Differently']

    )
    education = models.StringField(
        choices=['GED', 'High School', 'Some College', 'Associates Degree', 'Bachelors Degree', 'Masters Degree',
                 'Professional degree','Doctorate degree', 'Choose not to respond']
    )
    income = models.StringField(
        choices=[ 'Less than $10,000','$10,000 to $19,999','$20,000 to $29,999','$30,000 to $39,999',
                  '$40,000 to $49,999','$50,000 to $59,999','$60,000 to $69,999','$70,000 to $79,999',
                  '$80,000 to $89,999','$90,000 to $99,999','$100,000 to $149,999','$150,000 or more', 'Choose not to respond']
    )

    understanding = models.StringField(
        choices=[ '1','2','3','4','5','6','7']

    )
    desire = models.StringField(
        choices=[ '1','2','3','4','5','6','7']
    )

