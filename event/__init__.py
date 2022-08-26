from flask import Blueprint

app = Blueprint("Event API", __name__)

import event.views