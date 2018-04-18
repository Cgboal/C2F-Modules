#!/usr/bin/env python
from c2sdk import rest
from uuid import uuid4

http = rest.Rester()

print http.post("HelloWorldResult", {"random_string": "asdasdawega"}).data
