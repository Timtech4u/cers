from django.db import models
import geocoder

class Hook(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    type = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return "{}".format(self.data)

class Report(models.Model):
    number = models.CharField(max_length=20)
    location = models.CharField(max_length=100) # Get location property value off unit
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.number

class Official(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ward = models.CharField(max_length=100, null=True, blank=True)
    lga = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Local Authority Official"
        verbose_name_plural = "Local Authority Officials"

    def __str__(self):
        return self.name


class Units(models.Model):
    # get coordinates from importer (command or xls)
    name = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lon = models.CharField(max_length=100,  blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.location = "{} {} {} {}".format(self.name, self.ward, self.lga, self.state)
        if self.location != None:
            g = geocoder.arcgis(self.location)
            g = g.latlng
            if type(g) is list and len(g)==2:
                self.lat = g[0]
                self.lon = g[1]
        super(Units, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Polling Unit"
        verbose_name_plural = "Polling Units"

    def __str__(self):
        return self.location

class Blocked(models.Model):
    number = models.CharField(max_length=20)
    reason = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.number