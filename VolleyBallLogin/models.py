from django.db import models

class Matches(models.Model):
    match_id = models.AutoField(primary_key=True)
    teamA = models.CharField(max_length=100)
    teamB = models.CharField(max_length=100)
    date = models.DateTimeField()
    points_teamA = models.IntegerField(default=0)
    points_teamB = models.IntegerField(default=0)
    sets_teamA = models.IntegerField(default=0)
    sets_teamB = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.teamA} vs {self.teamB} on {self.date.strftime('%Y-%m-%d %H:%M')}"