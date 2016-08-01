# Database setup
import config
import datetime
from peewee import SqliteDatabase, Model, CharField, \
    BlobField, DateTimeField, ForeignKeyField


db = SqliteDatabase('db/worldtube.db',
                    threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = db


class Country(BaseModel):
    name = CharField(
        unique=True
    )


class Search(BaseModel):
    country = ForeignKeyField(
        Country,
        related_name='searches'
    )
    term = CharField(
        unique=True,
    )
    timestamp = DateTimeField(
        default=datetime.datetime.now
    )


class Video(BaseModel):
    video_id = CharField(
        unique=True,
        primary_key=True
    )
    search = ForeignKeyField(
        Search,
        related_name='videos'
    )
    title = CharField()
    thumbnail = BlobField()


def create_tables():
    db.connect()
    db.create_tables([Country,
                      Search,
                      Video])
    for country in config.COUNTRIES:
        db.Country(name=country)


def __main__():
    create_tables()
