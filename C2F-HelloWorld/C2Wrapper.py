#!/usr/bin/env python
from c2sdk import rest
from uuid import uuid4

http = rest.Rester()

http.post("HelloWorldResult", {"random_string": "hahahahaha fucking uuid"})