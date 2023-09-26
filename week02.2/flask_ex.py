from flask import Flask

app = Flask(__name__)


def func_a(a=1, b=0, c=0, d=0):
    pass


@app.route("/")
def first_page():
    #return "<p>첫 페이지 입니다.</p>"
    return "<a href ='/'>첫 페이지</a> <a href = 'hello'>Hello</a> <p>첫페이지입니다.</p>"

@app.route("/hello")
def hello_world():
    #return "<p>Hello, World!</p>"
    return "<a href ='/'>첫 페이지</a> <a href =/'hello'>Hello</a> <p>Hello, World!.</p>"

@app.route("/gugu/<int:dan>")
def gugudan(dan):
    return f"구구단 {dan}단"
    #return "<a href ='/'>첫 페이지</a> <a href = 'int:dan'>구구단</a> <p>구구단입니다..</p>"

    dan = int(dan)
    resp = ""
    resp += ("<html>\n")
    resp += ('<meta charset="utf-8">\n')
    resp += ("<body>\n")
    resp += (f"<h2>구구단 {dan}단</h2>\n")
    resp += ("<div>\n")
    for i in range(1, 20):
        resp += (f"{dan:2d}*{i:2d} = {dan * i:3d}<br>\n")
    resp += ("</div>\n")
    resp += ("</body>\n")
    resp += ("</html>\n")
    return resp

app.run(host="0.0.0.0")