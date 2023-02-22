from django.db import models

class Task(models.Model):

    # Specifying choices for task category
    WORK = 'WRK'
    SCHOOL = 'SCH'
    PERSONAL = 'PSL'

    CATEGORIES = [
        (WORK, 'WORK'),
        (SCHOOL, 'SCHOOL'),
        (PERSONAL, 'PERSONAL'),
    ]

    task_title = models.CharField(max_length=120)
    category = models.CharField(max_length=3, choices=CATEGORIES, default=PERSONAL)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.category}] {self.task_title} ({self.created_at.strftime("%Y-%m-%d | %H:%M:%S")})'

