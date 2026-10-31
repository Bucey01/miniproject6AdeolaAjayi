# INF601 - Advanced Programming in Python
# Adeola Ajayi
# Mini Project 6

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.task = Task.objects.create(
            user=self.user,
            title="Complete Mini Project 6",
            description="Test Django task manager"
        )

    def test_task_creation(self):
        self.assertEqual(
            self.task.title,
            "Complete Mini Project 6"
        )

    def test_task_description(self):
        self.assertEqual(
            self.task.description,
            "Test Django task manager"
        )

    def test_task_default_status(self):
        self.assertFalse(self.task.completed)

    def test_task_user(self):
        self.assertEqual(self.task.user, self.user)

    def test_task_string_representation(self):
        self.assertEqual(
            str(self.task),
            "Complete Mini Project 6"
        )
