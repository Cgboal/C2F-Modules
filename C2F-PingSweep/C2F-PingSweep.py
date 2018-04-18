from django.db import models
from api.lib.templates import ModelTemplate, Descriptor


class PingSweep(Descriptor):
    name = "Ping_Sweep"
    image = "cgboal/c2f-modules:PingSweep"
    args = {"network": "host"}


class PingSweepResult(ModelTemplate):
    subnet = models.TextField()
    hosts_alive = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

