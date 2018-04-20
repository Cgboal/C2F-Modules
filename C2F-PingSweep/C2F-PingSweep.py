# Import required base classes and Django models
from django.db import models
from api.lib.templates import ModelTemplate, Descriptor


# Define Module Descriptor
class PingSweep(Descriptor):
    name = "Ping_Sweep"
    image = "cgboal/c2f-modules:PingSweep"
    args = {"network": "host"}


# Define Model used to store Agent results
class PingSweepResult(ModelTemplate):
    subnet = models.TextField()
    hosts_alive = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)



