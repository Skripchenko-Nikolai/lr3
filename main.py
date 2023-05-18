from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    func = request.form.get('func')
    format = request.form.get('izmer')
    num_1 = float(request.form.get('num_1'))
    num_2 = int(request.form.get('num_2'))
    return render_template('index.html', ans=calculate(func, num_1, num_2, format))


def calculate(func, num, round_value, format):
    if bool(format == 'Градусы'):
        format_result = math.radians(num)
    else:
        format_result = num
    if bool(func == 'sin'):
        result = float(math.sin(format_result))
    elif bool(func == 'cos'):
        result = float(math.cos(format_result))
    elif bool(func == 'tg'):
        result = float(math.tan(format_result))
    else:
        result = float(math.atan(format_result))
    return to_fixed(float(result), round_value)


def to_fixed(num, digits=0):
    return f'{num:.{digits}f}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
