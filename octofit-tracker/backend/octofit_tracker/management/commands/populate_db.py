from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all collections
        Team.objects.all().delete()
        User.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-12-24')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2025-12-23')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2025-12-22')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date='2025-12-21')

        # Create workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout', suggested_for='Marvel')
        Workout.objects.create(name='Strength Builder', description='Strength training routine', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750)
        Leaderboard.objects.create(team=dc, points=800)


        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
        self.stdout.write('To ensure unique email index, run the following in mongosh:')
        self.stdout.write('db.users.createIndex({ "email": 1 }, { unique: true })')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
