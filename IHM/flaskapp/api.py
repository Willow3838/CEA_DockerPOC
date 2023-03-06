from flask import Blueprint, render_template
from pydantic.error_wrappers import ValidationError


# import request
from .models import Document, DocumentShortView
from pprint import pprint

api = Blueprint("api", __name__)


@api.post("/documents")
def api_documents():
    jsondocs = request.get_json()

    # Insert documents in db
    documents = Document.parse_obj(jsondocs)
    pprint(documents)
    return f"{len(documents)} document successfully added to the database!", 201
