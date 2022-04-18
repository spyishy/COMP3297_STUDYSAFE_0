from django.db import models

class Venue(models.Model):
    venue_code = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.IntegerField()
    def __str__(self):
        return f'{self.venue_code}'

class HKUMember(models.Model):
    hku_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)
    entered_venue = models.ManyToManyField(Venue, through='Entry', related_name='entered_venue')
    exited_venue = models.ManyToManyField(Venue, through='Exit', related_name='exited_venue')
    def __str__(self):
        return f'{self.hku_id}'

class Entry(models.Model):
    entry_venue_code = models.ForeignKey(Venue, to_field='venue_code', on_delete=models.CASCADE)
    entry_hku_id = models.ForeignKey(HKUMember, to_field='hku_id', on_delete=models.CASCADE)
    entry_date = models.DateField()
    entry_time = models.TimeField()
    def __str__(self):
        return f'{self.entry_date} {self.entry_time}: {self.entry_hku_id} {self.entry_venue_code}'

class Exit(models.Model):
    exit_venue_code = models.ForeignKey(Venue, to_field='venue_code', on_delete=models.CASCADE)
    exit_hku_id = models.ForeignKey(HKUMember, to_field='hku_id', on_delete=models.CASCADE)
    exit_date = models.DateField()
    exit_time = models.TimeField()
    def __str__(self):
        return f'{self.exit_date} {self.exit_time}: {self.exit_hku_id} {self.exit_venue_code}'
