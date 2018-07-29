from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):
    def is_displayed(self):
        return self.round_number == 1


class Agreements(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroandData(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'
    form_fields = ['age', 'sex', 'education', 'income']


class GameInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
        }


class GameKLevel1(Page):

    def is_displayed(self):
        return self.round_number <= 3

    form_model = 'player'
    form_fields = ['flags_remaining_player_1', 'flags_remaining_player_2', 'flags_remaining_player_3',
                   'flags_remaining_player_4', 'flags_remaining_player_5', 'flags_remaining_player_6',
                   'flags_remaining_player_7', 'flags_remaining_player_8', 'flags_remaining_player_9',
                   'flags_remaining_player_10', 'flags_remaining_player_11', 'is_winner', 'moves']


    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'current_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'round_number': self.round_number,

        }

    def before_next_page(self):
        p = self.player
        if p.is_winner:
            if p.incentivized:
                p.endowment = p.endowment + c(100)
            else:
                p.endowment = p.endowment + c(0)
        else:
            if p.incentivized:
                p.endowment = p.endowment - c(0)
            else:
                p.endowment = p.endowment - c(100)

        if self.round_number == Constants.num_rounds:
            self.player.total_endowment = sum([p.endowment for p in self.player.in_all_rounds()])
            self.player.total_wins = sum([p.is_winner for p in self.player.in_all_rounds()])


class GameKLevel2(Page):

    def is_displayed(self):
        return (self.round_number >= 4) & (self.round_number <= 8)

    form_model = 'player'
    form_fields = ['flags_remaining_player_1', 'flags_remaining_player_2', 'flags_remaining_player_3',
                   'flags_remaining_player_4', 'flags_remaining_player_5', 'flags_remaining_player_6',
                   'flags_remaining_player_7', 'flags_remaining_player_8', 'flags_remaining_player_9',
                   'flags_remaining_player_10', 'flags_remaining_player_11', 'is_winner', 'moves']


    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'current_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'round_number': self.round_number,

        }

    def before_next_page(self):
        p = self.player
        if p.is_winner:
            if p.incentivized:
                p.endowment = p.endowment + c(100)
            else:
                p.endowment = p.endowment + c(0)
        else:
            if p.incentivized:
                p.endowment = p.endowment - c(0)
            else:
                p.endowment = p.endowment - c(100)

        if self.round_number == Constants.num_rounds:
            self.player.total_endowment = sum([p.endowment for p in self.player.in_all_rounds()])
            self.player.total_wins = sum([p.is_winner for p in self.player.in_all_rounds()])


class GameKLevel3(Page):

    def is_displayed(self):
        return (self.round_number >= 9) & (self.round_number <= 14)
    form_model = 'player'
    form_fields = ['flags_remaining_player_1', 'flags_remaining_player_2', 'flags_remaining_player_3',
                   'flags_remaining_player_4', 'flags_remaining_player_5', 'flags_remaining_player_6',
                   'flags_remaining_player_7', 'flags_remaining_player_8', 'flags_remaining_player_9',
                   'flags_remaining_player_10', 'flags_remaining_player_11', 'is_winner', 'moves']

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'current_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'round_number': self.round_number,
        }

    def before_next_page(self):
        p = self.player
        if p.is_winner:
            if p.incentivized:
                p.endowment = p.endowment + c(100)
            else:
                p.endowment = p.endowment + c(0)
        else:
            if p.incentivized:
                p.endowment = p.endowment - c(0)
            else:
                p.endowment = p.endowment - c(100)

        if self.round_number == Constants.num_rounds:
            self.player.total_endowment = sum([p.endowment for p in self.player.in_all_rounds()])
            self.player.total_wins = sum([p.is_winner for p in self.player.in_all_rounds()])


class GamePerfect(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['flags_remaining_player_1', 'flags_remaining_player_2', 'flags_remaining_player_3',
                   'flags_remaining_player_4', 'flags_remaining_player_5', 'flags_remaining_player_6',
                   'flags_remaining_player_7', 'flags_remaining_player_8', 'flags_remaining_player_9',
                   'flags_remaining_player_10', 'flags_remaining_player_11', 'is_winner', 'moves']

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'current_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'round_number': self.round_number,

        }

    def before_next_page(self):
        p = self.player
        if p.is_winner:
            if p.incentivized:
                p.endowment = p.endowment + c(100)
            else:
                p.endowment = p.endowment + c(0)
        else:
            if p.incentivized:
                p.endowment = p.endowment - c(0)
            else:
                p.endowment = p.endowment - c(100)

        if self.round_number == Constants.num_rounds:
            self.player.total_endowment = sum([p.endowment for p in self.player.in_all_rounds()])
            self.player.total_wins = sum([p.is_winner for p in self.player.in_all_rounds()])



class Results(Page):
    form_model = 'player'
    form_fields = ['understanding', 'desire']

    def is_displayed(self):
        return self.round_number < Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'player_in_all_rounds': self.player.in_all_rounds(),
        }


class ExitQuestions(Page):
    form_model = 'player'
    form_fields = ['understanding', 'desire']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
            'total_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
            'total_wins': sum([p.is_winner for p in self.player.in_all_rounds()]),
        }


class Debrief(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'player_treatment': self.player.in_rounds(1,1),
        }


class Test(Page):
    form_model = 'player'
    form_fields = ['flags_remaining_player_1', 'flags_remaining_player_2','flags_remaining_player_3',
                   'flags_remaining_player_4', 'flags_remaining_player_5', 'flags_remaining_player_6',
                   'flags_remaining_player_7', 'flags_remaining_player_8', 'flags_remaining_player_9',
                   'flags_remaining_player_10', 'flags_remaining_player_11', 'is_winner', 'moves']

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'current_endowment': sum([p.endowment for p in self.player.in_all_rounds()]),
        }


page_sequence = [
    StartPage,
    Agreements,
    IntroandData,
    GameInstructions,
    GameKLevel1,
    GameKLevel2,
    GameKLevel3,
    GamePerfect,
    Results,
    ExitQuestions,
    Debrief,


]
