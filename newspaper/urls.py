"""
URL configuration for newspaper_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorsListView,
    NewspaperDetailView,
    RedactorsDetailView,
    TopicCreateView,
    NewspaperCreateView,
    RedactorsCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorsDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    path(
        "topics/",
        TopicListView.as_view(),
        name="topics-list"
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topics-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),

    path(
        "newspaper/",
        NewspaperListView.as_view(),
        name="newspapers-list"
    ),
    path(
        "newspaper/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspaper/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspaper/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspaper/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),

    path(
        "redactors/",
        RedactorsListView.as_view(),
        name="redactors-list"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorsDetailView.as_view(),
        name="redactors-detail"
    ),
    path(
        "redactors/create/",
        RedactorsCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/delete",
        RedactorsDeleteView.as_view(),
        name="redactors-delete"
    ),

]

app_name = "newspaper"
