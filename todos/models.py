from django.db import models

class TaskCategory(models.TextChoices):
    WORK = 'WRK', 'WORK'
    SCHOOL = 'SCH', 'SCHOOL'
    PERSONAL = 'PSL', 'PERSONAL'

class Task(models.Model):

    task_title = models.CharField(max_length=120, verbose_name="Task Title")
    task_description = models.TextField(blank=True, verbose_name="Description")
    category = models.CharField(max_length=3, choices=TaskCategory.choices, default=TaskCategory.PERSONAL, verbose_name="Category")
    is_done = models.BooleanField(default=False, verbose_name="Task Done")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return f'[{self.category}] {self.task_title} ({self.created_at.strftime("%Y-%m-%d | %H:%M:%S")})'

