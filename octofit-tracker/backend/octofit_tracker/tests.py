from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        user = User.objects.create(name='Test User', email='testuser@example.com', team=team)
        self.assertEqual(user.email, 'testuser@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        user = User.objects.create(name='Test User', email='testuser@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-12-24')
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='A workout for testing', suggested_for='Test Team')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
