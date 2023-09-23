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
    <script
  src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
        <form id="form_id" action="javascript:post_query()">
            <h2>구구단 출력하기</h2>
            <label>몇 단? => </label>
            <input type="text" name="dan">
            <button type="submit">출력</button>
        </form>
        <div id="results"></div> 
        
<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/gugu",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}
function update_result(data) {
    $("#results").html(data);
}
</script>
</body>
</html> """

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