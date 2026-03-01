from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):
        # Create users
        self.admin = User.objects.create_superuser(
            username="admin",
            password="adminpass"
        )
        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        # Create tasks
        self.task1 = Task.objects.create(
            user=self.user1,
            title="Task 1",
            description="Desc 1",
            completed=False
        )

        self.task2 = Task.objects.create(
            user=self.user2,
            title="Task 2",
            description="Desc 2",
            completed=False
        )

    # Helper method for JWT authentication
    def authenticate(self, user):
        refresh = RefreshToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

    def test_regular_user_cannot_delete_others_task(self):
        self.authenticate(self.user1)
        response = self.client.delete(f"/api/tasks/{self.task2.id}/")
        # Since queryset hides other user's tasks, it returns 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_admin_can_delete_any_task(self):
        self.authenticate(self.admin)
        response = self.client.delete(f"/api/tasks/{self.task1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_list_for_user(self):
        self.authenticate(self.user1)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Only user1's task should be returned
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Task 1")

    def test_create_task(self):
        self.authenticate(self.user1)

        data = {
            "title": "New Task",
            "description": "Test task",
            "completed": False
        }

        response = self.client.post("/api/tasks/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # User1 now should have 2 tasks
        self.assertEqual(Task.objects.filter(user=self.user1).count(), 2)