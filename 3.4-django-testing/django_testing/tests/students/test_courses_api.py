import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.mark.django_db
class TestCoursesAPI:

    def test_retrieve_course(self, api_client, course_factory):
        """Проверка получения одного курса."""
        course = course_factory(name='Math')
        url = f'/api/v1/courses/{course.id}/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json()['id'] == course.id
        assert response.json()['name'] == 'Math'

    def test_list_courses(self, api_client, course_factory):
        """Проверка получения списка курсов."""
        course1 = course_factory(name='Math')
        course2 = course_factory(name='Physics')
        url = '/api/v1/courses/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_filter_courses_by_id(self, api_client, course_factory):
        """Проверка фильтрации курсов по ID."""
        course1 = course_factory(name='Math')
        course2 = course_factory(name='Physics')
        url = f'/api/v1/courses/?id={course1.id}'
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['id'] == course1.id

    def test_filter_courses_by_name(self, api_client, course_factory):
        """Проверка фильтрации курсов по имени."""
        course = course_factory(name='Mathematics')
        url = '/api/v1/courses/?name=Mathematics'
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == 'Mathematics'

    def test_create_course(self, api_client):
        """Проверка создания курса."""
        url = '/api/v1/courses/'
        data = {'name': 'Python'}
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert Course.objects.filter(name='Python').exists()

    def test_update_course(self, api_client, course_factory):
        """Проверка обновления курса."""
        course = course_factory(name='Math')
        url = f'/api/v1/courses/{course.id}/'
        data = {'name': 'Advanced Math'}
        response = api_client.put(url, data, format='json')
        assert response.status_code == 200
        course.refresh_from_db()
        assert course.name == 'Advanced Math'

    def test_delete_course(self, api_client, course_factory):
        """Проверка удаления курса."""
        course = course_factory(name='Math')
        url = f'/api/v1/courses/{course.id}/'
        response = api_client.delete(url)
        assert response.status_code == 204
        assert not Course.objects.filter(id=course.id).exists()
