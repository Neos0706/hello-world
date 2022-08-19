from django.test import TestCase,Client
from .models import Student
# Create your tests here.


class StudentsModelTests(TestCase):
    def test_get_students(self):
        """
        测试获取所有学生
        """
        client = Client()
        response = client.get('http://127.0.0.1:8000/api/students/3/')
        print(response)
        print(response.text)
        self.assertIs(response.status_code, 200)