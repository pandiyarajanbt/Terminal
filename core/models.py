from django.db import models

class Terminal(models.Model):
    commands = models.CharField(max_length=240, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> None:
        return self.commands