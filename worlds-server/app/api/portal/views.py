from flask import jsonify
from . import blueprint
from .data import generate


@blueprint.route('/', methods=['GET'])
def portal():
    text = """
You {names[1]} forward through the {names[2]} portal {names[3]}.
You're immediately met by {names[4]} world. {names[5]}.
{names[6]}.        

{names[7]}{names[8]}.
This world is {names[9]}{names[10]}.

{names[11]} you {names[12]} of {names[13]}.
{names[14]}, {names[15]}.
{names[16]} {names[17][0]} creatures, {names[17][1]} creatures,
and what you think might be {names[17][2]} creatures of some sort.

{names[18]} as {names[19]}.
But, with {names[20][0]}, {names[20][1]}, and {names[20][2]}, {names[21]}.
    """.format(names=generate())

    return jsonify({
        'status': 'success',
        'portal': text,
    })
