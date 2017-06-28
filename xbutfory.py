import os
from random import randint
from flask import Flask, render_template
app = Flask(__name__)


class ElevatorPitch(object):
    def __init__(self):
        def _read_list(filename):
            datadir = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "data"
            )
            with open(os.path.join(datadir, filename)) as f:
                return f.read().splitlines()

        self.companies = _read_list("companies.txt")
        self.nouns = _read_list("nouns.txt")

    def generate(self):
        x_row = randint(0, len(self.companies) - 1)
        y_row = randint(0, len(self.nouns) - 1)
        x = self.companies[x_row]
        y = pluralize(self.nouns[y_row])

        return "{} but for {}".format(x, y)


def pluralize(noun):
    if len(noun) > 1:
        if noun.endswith('s'):
            return noun
        if any(noun.endswith(s) for s in ['sh', 'x', 'o', 'ch']):
            return noun + 'es'
        if noun.endswith('y'):
            if noun[-2] not in "aeoui":
                return noun[:-1] + 'ies'
    return noun + 's'


def get_pitch():
    elevator_pitch = ElevatorPitch()
    return elevator_pitch.generate()


@app.route('/')
def index():
    result = get_pitch()
    return render_template("index.html", result=result)
