# models.py

from datetime import datetime
from config import db, ma


class Note(db.Model):

    __table_name__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Person(db.Model):

    __table_name__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        Note,
        backref="person",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.timestamp)"
    )

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        include_fk = True
        load_instance = True
        sqla_session = db.session

class PersonSchema(ma.SQLAlchemyAutoSchema):

    notes = ma.Nested(NoteSchema, many=True)

    class Meta:
        model = Person
        include_relationships = True
        load_instance = True
        sqla_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

note_schema = NoteSchema()

