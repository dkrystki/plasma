from datetime import datetime

import factory

from core import models


class PhotoFactory(factory.Factory):
    class Meta:
        model = models.Photo

    name = factory.Sequence(lambda n: f"TestPhoto{n}")
    draft = False
    caption = "TestCaption"
    publish_date = datetime(2020, 3, 15, 20, 45, 40)
