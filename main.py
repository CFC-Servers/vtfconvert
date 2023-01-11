from io import BytesIO


from flask import Flask, request, Response, send_file
from vtf2img.buffer import Buffer
from vtf2img.header import Header
from vtf2img.image_formats import get_parser

app = Flask(__name__)


@app.route("/png", methods=["POST"])
def convert():
    image = request.get_data()

    buffer = Buffer(image)
    header = Header(buffer)
    parsed = get_parser(header.image_format)(header, buffer).read()

    output = BytesIO()
    parsed.save(output, format="PNG")
    output.seek(0)

    return send_file(output, mimetype="image/png")
