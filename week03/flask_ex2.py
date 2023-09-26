from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def first_page():
    return """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <form method="GET" action="/gugu">
            <h2>구구단 출력하기</h2>
            <label>몇 단? => </label>
            <input type="text" name="dan">
            <button type="submit">출력</button>
        </form>

</body>
</html> """

@app.route("/hello")
def hello_world():
    #return "<p>Hello, World!</p>"
    return "<a href ='/'>첫 페이지</a> <a href =/'hello'>Hello</a> <p>Hello, World!.</p>"

# 지난주 /gugu/7
# 이번주 gugu?dan=7

@app.route("/gugu")
def gugudan():
    dan = int(request.args.get('dan'))
    resp = ""
    resp += ("<html>\n")
    resp += ('<meta charset="utf-8">\n')
    resp += ("<body>\n")
    resp += (f"<h2>구구단 {dan}단</h2>")
    resp += ("<div>\n")
    for i in range(1, 20):
        resp += (f"{dan:2d}*{i:2d} = {dan * i:3d}<br>\n")
    resp += ("</div>\n")
    resp += ("</body>\n")
    resp += ("</html>\n")
    return resp

app.run(host="0.0.0.0")