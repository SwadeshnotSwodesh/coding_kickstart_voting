from django.db import models

# Create your models here.

class Team(models.Model):
    CATEGORY_CHOICES = [
        ('scratch', 'Scratch'),
        ('app_inventor', 'App Inventor'),
        ('robotics', 'Robotics'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['category', '-votes']


class VotingPasscode(models.Model):
    """Single model to store the admin passcode for voting"""
    passcode = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Passcode: {self.passcode}"

    class Meta:
        verbose_name = "Voting Passcode"
        verbose_name_plural = "Voting Passcode"

    @staticmethod
    def get_passcode():
        """Get the current admin passcode"""
        passcode_obj = VotingPasscode.objects.first()
        return passcode_obj.passcode if passcode_obj else None


class UserVote(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    voter_name = models.CharField(max_length=100, blank=False, null=False, default="")
    scratch_votes = models.ManyToManyField(Team, related_name='scratch_voters', blank=True)
    app_inventor_votes = models.ManyToManyField(Team, related_name='app_inventor_voters', blank=True)
    robotics_votes = models.ManyToManyField(Team, related_name='robotics_voters', blank=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Voter: {self.voter_name} - {self.created_at}"

    def save(self, *args, **kwargs):
        """Ensure voter_name is not empty before saving (except on initial creation)"""
        # Only enforce non-empty voter_name if this is an update (pk exists) or if voter_name was explicitly set
        if self.pk is not None and (not self.voter_name or not self.voter_name.strip()):
            raise ValueError("Voter name is required and cannot be empty.")
        super().save(*args, **kwargs)

    def get_scratch_count(self):
        return self.scratch_votes.count()

    def get_app_inventor_count(self):
        return self.app_inventor_votes.count()

    def get_robotics_count(self):
        return self.robotics_votes.count()

    def is_all_complete(self):
        return (self.get_scratch_count() == 5 and 
                self.get_app_inventor_count() == 5 and 
                self.get_robotics_count() == 5)
