from sport_statistic_lib.sportsmen_mocker import SportsmenMocker


class Model:
    def __init__(self):
        sm = SportsmenMocker()
        sm.execute()
        self.sportsmen_list = sm.sportsmen_list
