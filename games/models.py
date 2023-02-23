from django.db import models

class MHYGameManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(game_publisher='miHoYo')

class Game(models.Model):

    game_title = models.CharField(max_length=255)
    game_publisher = models.CharField(max_length=60)
    
    # Game Platforms Field (Boolean Values)
    is_pc = models.BooleanField(default=False)
    is_mobile = models.BooleanField(default=False)
    is_xbox = models.BooleanField(default=False)
    is_ps4 = models.BooleanField(default=False)
    is_switch = models.BooleanField(default=False)

    game_objects = models.Manager()
    mhy_game_objects = MHYGameManager()


    def __str__(self):
        return f'{self.game_title} ({self.game_publisher})'


