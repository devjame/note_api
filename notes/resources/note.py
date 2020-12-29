from flask import request
from flask_restful import Resource
from http import HTTPStatus

from api.notes.note_schemas import NoteSchema
from notes.models import Notes

note_schema = NoteSchema()
note_list_schema = NoteSchema(many=True)


class NoteListResource(Resource):

    def get(self):
        notes = Notes.query.all()

        return note_list_schema.dump(notes), HTTPStatus.OK

    def post(self):
        json_data = request.get_json()

        data, errors = note_schema.load(data=json_data)

        if errors:
            return {"message": "Validations errors", 'errors': errors}, HTTPStatus.BAD_REQUEST

        note = Notes(**data)
        note.save()

        return note_schema.dump(note).data, HTTPStatus.OK


class NoteResource(Resource):

    def get(self, note_id):
        note = Notes.get_by_id(note_id=note_id)

        if note is None:
            return {"message": "Note not found"}, HTTPStatus.NOT_FOUND

        return note_schema.dump(note), HTTPStatus.OK

    def patch(self, note_id):

        json_data = request.get_json()

        data, errors = note_schema.load(data=json_data, partial=('title',))

        if errors:
            return {"message": "Validation errors", "errors": errors}, HTTPStatus.BAD_REQUEST

        note = Notes.get_by_id(note_id=note_id)

        if note is None:
            return {"message": "Note not found"}, HTTPStatus.NOT_FOUND

        note.title = data.get('title') or note.title
        note.body = data.get('body') or note.body

        note.save()

        return note_schema.dump(note).data, HTTPStatus.OK

    def delete(self, note_id):
        note = Notes.get_by_id(note_id=note_id)

        if note is None:
            return {"message": "Note not found"}, HTTPStatus.NOT_FOUND

        note.delete()

        return {}, HTTPStatus.NO_CONTENT
