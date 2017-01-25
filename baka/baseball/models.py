
from __future__ import unicode_literals
from django.db import models

from django.core.urlresolvers import reverse

class Batter(models.Model):
    player = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    league = models.CharField(max_length=50, blank=True)
    team = models.CharField(max_length=50, blank=True)
    tright = models.BooleanField(default=True)
    bright = models.BooleanField(default=True)
    bleft = models.BooleanField(default=False)
    pos = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    sp = models.BooleanField(default=False)
    rp = models.BooleanField(default=False)
    util = models.BooleanField(default=False)
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)
    catch = models.BooleanField(default=False)
    short = models.BooleanField(default=False)
    outf = models.BooleanField(default=False)
    ci = models.BooleanField(default=False)
    mi = models.BooleanField(default=False)
    my_team = models.BooleanField(default=False)
    follow = models.BooleanField(default=False)
    blurb = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.player

    def get_absolute_url(self):
        return reverse("baseball:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.player

class Statline(models.Model):
    batter = models.ForeignKey(Batter, on_delete=models.CASCADE)
    year = models.CharField(max_length=50)
    gp = models.IntegerField(default=0)
    ab = models.IntegerField(default=0)
    pa = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    single = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    hr = models.IntegerField(default=0)
    tb = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    bb = models.IntegerField(default=0)
    ibb = models.IntegerField(default=0)
    so = models.IntegerField(default=0)
    hbp = models.IntegerField(default=0)
    sf = models.IntegerField(default=0)
    sh = models.IntegerField(default=0)
    gdp = models.IntegerField(default=0)
    sb = models.IntegerField(default=0)
    cs = models.IntegerField(default=0)
    ba = models.DecimalField(max_digits=3,decimal_places=3, default=0)
    obp = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    slg = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    ops = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    iso = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    babip = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    ubr = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    wgdp = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    wsb = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    wrc = models.IntegerField(default=0)
    wraa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    woba = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    wrcp = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    era = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    g = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    cg = models.IntegerField(default=0)
    sho = models.IntegerField(default=0)
    sv = models.IntegerField(default=0)
    hld = models.IntegerField(default=0)
    bs = models.IntegerField(default=0)
    ip = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tbf = models.IntegerField(default=0)
    ha = models.IntegerField(default=0)
    ra = models.IntegerField(default=0)
    er = models.IntegerField(default=0)
    hra = models.IntegerField(default=0)
    bba = models.IntegerField(default=0)
    ibba = models.IntegerField(default=0)
    k = models.IntegerField(default=0)
    knine = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    bbnine = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    kbb = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    hrnine = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    kpercent = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    bbpercent = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    kbbpercent = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    avaga = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    whip = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    babip = models.DecimalField(max_digits=3, decimal_places=3, default=.0)
    lob = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fip = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return str(self.year)





