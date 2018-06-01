from django.contrib import admin
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class ConditionsCourseHomeInline(admin.TabularInline):
    model = ConditionsCourseHome


@admin.register(CourseHome)
class CourseHomeAdmin(admin.ModelAdmin):
    inlines = [ConditionsCourseHomeInline]


# Register your models here.
admin.site.register(Review)
admin.site.register(PostStudy)
