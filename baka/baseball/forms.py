from django import forms

from .models import Batter, Statline

class BatterForm(forms.ModelForm):
    class Meta:
        model = Batter
        fields = ['player', 'team','league','pos', 'blurb', 'rank', 'sp', 'rp','image', 'my_team', 'follow']
        labels = {'player': 'Player', 'league': 'league', 'team': 'team','pos': 'POS', 'blurb': 'Notes',
                  'rank': 'rank', 'my_team': 'my team', 'follow': 'follow'}

class StatlineForm(forms.ModelForm):
    class Meta:
        model = Statline
        fields = ['year', 'gp', 'ab', 'pa', 'h', 'single', 'two', 'three', 'hr', 'runs', 'rbi', 'bb', 'ibb', 'so', 'hbp',
                  'sf', 'sh', 'gdp', 'sb', 'cs', 'ba']
        labels = {'year': 'Year', 'gp': 'GP', 'ab': 'AB', 'pa': 'PA', 'h': 'H', 'single': '1B', 'two': '2B',
                  'three': '3B', 'hr': 'HR', 'runs': 'R', 'rbi': 'RBI', 'bb': 'BB', 'ibb': 'IBB', 'so': 'SO',
                  'hbp': 'HBP', 'sf': 'SF', 'sh': 'SH', 'gdp': 'GDP', 'sb': 'SB', 'cs': 'CS', 'ba': 'AVG'}













