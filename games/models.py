from django.db import models

class GameManager(models.Manager):
    def for_platform(self, platform):
        return self.get_queryset().filter(**{f'is_{platform}': True})

class Game(models.Model):
    PLATFORMS = [
        ('pc', 'PC'),
        ('mobile', 'Mobile'),
        ('xbox', 'Xbox'),
        ('ps4', 'PS4'),
        ('switch', 'Switch'),
    ]

    game_title = models.CharField(max_length=255)
    game_publisher = models.CharField(max_length=60)

    # Game Platforms Field (Boolean Values)
    is_pc = models.BooleanField(default=False)
    is_mobile = models.BooleanField(default=False)
    is_xbox = models.BooleanField(default=False)
    is_ps4 = models.BooleanField(default=False)
    is_switch = models.BooleanField(default=False)

    objects = GameManager()

    def __str__(self):
        return f'{self.game_title} ({self.game_publisher})'

    def for_platform(self, platform):
        return getattr(self.objects, f'{platform}_game_objects')()