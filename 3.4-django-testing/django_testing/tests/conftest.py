import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Фикстура для API-клиента."""
    return APIClient()


@pytest.fixture
def course_factory():
    """Фикстура для фабрики курсов."""
    return lambda **kwargs: baker.make('students.Course', **kwargs)


@pytest.fixture
def student_factory():
    """Фикстура для фабрики студентов."""
    return lambda **kwargs: baker.make('students.Student', **kwargs)
