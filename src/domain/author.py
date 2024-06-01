import datetime


class Goalscorers:
    date: str = ""
    home_team: str = ""
    away_team: str = ""
    team: str = ""
    scorer: str = ""
    minute: int = 00
    own_goal: bool = False
    penalty: bool = False

    def __init__(self, date: str, home_team: str, away_team: str, team: str, scorer: str, minute: int, own_goal: bool,
                 penalty: bool):
        self._date: str = date
        self._home_team: str = home_team
        self._away_team: str = away_team
        self._team: str = team
        self._scorer: str = scorer
        self._minute: int = minute
        self._own_goal: bool = own_goal
        self._penalty: bool = penalty

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def home_team(self):
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        self._home_team = home_team

    @property
    def away_team(self):
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        self._away_team = away_team

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        self._team = team

    # Getter and Setter for team
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def scorer(self):
        return self._scorer

    @scorer.setter
    def scorer(self, value):
        self._scorer = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if isinstance(value, int) and value >= 0:
            self._minute = value
        else:
            raise ValueError("Minute must be a non-negative integer")

    @property
    def own_goal(self):
        return self._own_goal

    @own_goal.setter
    def own_goal(self, value):
        if isinstance(value, bool):
            self._own_goal = value
        else:
            raise ValueError("Own goal must be a boolean")

    @property
    def penalty(self):
        return self._penalty

    @penalty.setter
    def penalty(self, value):
        if isinstance(value, bool):
            self._penalty = value
        else:
            raise ValueError("Penalty must be a boolean")