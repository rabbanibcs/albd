from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class LiveTV(models.Model):
    objects = models.Manager()
    on_site = CurrentSiteManager()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    name = models.CharField(max_length=200)
    embedded_link = models.URLField("Embedded Link", blank=True, max_length=256)

    def __str__(self):
        return self.name
        
    # form-input: https://www.youtube.com/watch?v=2e7u6vvIIt0
    # in database save as: https://www.youtube.com/embed/2e7u6vvIIt0
    def save(self,*args,**kwargs):
        link=self.embedded_link
        link_part1,link_part2=link.split("?")
        link_part1_list=link_part1.split("/")
        link_part1_list[-1]="embed"
        link_part1=("/").join(link_part1_list)
        link_part2=link_part2.split("=")[-1]
        self.embedded_link=link_part1+"/"+link_part2
        super(LiveTV, self).save(*args, **kwargs)