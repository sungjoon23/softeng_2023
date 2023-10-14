from flask import Flask, request, render_template

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

@app.route("/active")
def active_func():
    datasets = [
        {"title": "활동", "content": "아직까지는 능력 부족입니다."}
    ]
    return render_template("active.html", posts=datasets)

@app.route("/here")
def here_func():
    return render_template("here.html")

@app.route("/")
def first_page():
    return render_template("index.html")

@app.route("/about")
def about_me_func():
    return render_template("about_me.html")

@app.route("/blog")
def blog_list_func():
    return render_template("blog_list.html")

@app.route("/champion")
def champion_ajax_func():
    return render_template("champion_ajax.html")

@app.route("/champ")
def champion():
    champ = request.args.get('champ')

    if champ == "가렌":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/uBBKJpWc-riCOuMBmddQ3Zgcjnc5xN-fPMSwBkQS3-sH517SnWfw-ImgFAycHuP0OLY7sF_TogVdGyFFoRdg47g-jBftGjHrIFSsGpQRGFCPW-WcWa6p1B4FcM1MMkZfuIujuQvU7NriRTHhzNh15w.webp">       
        <p> 가렌은 불굴의 선봉대를 이끄는 고결하고 자긍심 강한 군인이다. 선봉대 내에서 인망이 두터울 뿐 아니라 심지어 적에게도 존경을 받지만, 
        그가 대대로 데마시아와 그 이상을 수호하는 임무를 맡은 크라운가드 가문의 자손이기 때문은 아니다. 가렌은 자신의 부모님이 마법사에 살해되어 마법을 매우혐오하면 마법 저항력을 
        갖춘 방어구와 거대한 대검으로 무장하고, 언제라도 마법사에 맞서 정의의 칼바람을 일으킬 준비가 되어 있다.</p> """

    elif champ == "갈리오":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/B-FvPOXGBwFiki3-3iR7WsxUsMJKrAj9Tf3AzmWzjRryxLZFEKIU8fCYC5FvKOxUwEgPxTsMZ-T2vr8bulcHl7LGqO6rs4JKNzjrcEQAPVgaw0YSjiKGQ0hk0AVg4t43Kb0c-RjZ3M-xWrKpM3Aa5A.webp">
        <p> 거대한 석상 갈리오는 위대한 도시 데마시아 외곽에 우뚝 선 채 경계를 늦추지 않는다. 
        마법 공격으로부터 데마시아를 수호하기 위해 만들어진 갈리오는 강력한 마법의 힘을 받아 깨어나기 전까지 수십 년간 그 자리에 미동도 하지 않고 서 있다. 
        한번 깨어나면 데마시아의 수호자로서 자부심을 안고 전투의 희열에 몸을 맡기며 전력을 다한다. 하지만 달콤한 승리의 이면에는 언제나 씁쓸한 순간이 기다리고 있다. 
        갈리오가 파괴해야 하는 마법은 곧 그를 움직이게 하는 힘의 원천이기 때문이다. 전투를 승리로 이끈 갈리오는 어김없이 다시 깊은 잠에 빠져든다.</p> """

    elif champ == "갱플랭크":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/FPaZkjDsK19zY1oQhJmR_GkkvNAvEAdah_l8QnUqRyac-uti88MU5C7n4p8E4XW6PIyERDBTDj6xkWQtsflznqrS4MO0up92ziQbygmeJFIztr3mP3boRUgj1ALiXoC7Bdtb67n6dZ6mlh8rGYG36Q.webp">
        <p> 몰락한 해적왕 갱플랭크는 잔인한 성격에다 종잡을 수 없으며 사악함은 타의 추종을 불허한다. 
        과거 항구도시 빌지워터를 힘으로 장악했으나 지금은 영향력을 잃었다. 하지만 사람들은 그렇기 때문에 오히려 갱플랭크가 더 미쳐 날뛰리라고 생각한다. 
        갱플랭크는 빌지워터를 다른 사람에게 넘기느니 다시 한 번 피바다로 만들어 버릴 인물이니까. 
        그리고 이제, 권총, 해적검, 화약통으로 무장한 갱플랭크가 잃었던 패권을 되찾기 위한 준비를 끝냈다.</p> """

    elif champ == "그라가스":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/jTM0Xvd0C19C5f5jq9r3m1qhVl9XvqPOlZkkRKOVTC1M4i97y8BMNzj7v1Nt7BrbsbOwsCoX4IE_2WbKflIDmKCnOq0FPdHucgSQFMCzmIzxiKm3kuRr92V2IHzvcDE2SrxgIzMWNvOeCghyja3GaA.webp">
        <p> 그라가스는 몸집이 크고 소란스러워서 한 번 보면 잊기 힘든 쾌활한 주조가로, 완벽한 술을 만들기 위한 여정을 떠나게 되었다. 
        그라가스가 어디서 왔는지는 아무도 모르지만, 프렐요드의 때묻지 않은 불모지를 뒤지며 희귀한 재료를 찾아 주조법을 하나씩 시험해 보고 있다. 
        대부분 술에 취해 있어 극도로 충동적인 그라가스는 소동을 일으키는 데에는 전설적인 소질이 있는데, 
        그 소동은 밤샘 파티와 엄청난 기물 파손으로 이어지기 일쑤다. 그라가스를 보게 된다면 곧 음주, 그리고 파괴가 잇따를 것이라고 생각해도 좋다</p> """

    elif champ == "그레이브즈":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/JlqlDK6ZfgtB4gXgDrs7h5rQphz0T2nW_sL4U-3aXG_Jze6Bw0Qg3iElI3cFTjNJE6pxArMNiZJqzpQDIC_BO5rkQv_LK85borI9utiHaB5ypE8J570_fxCUpNNOI4JpqMcMIV-a5RataKE1zcnsCw.webp">
        <p> 말콤 그레이브즈는 명성이 자자한 용병, 도박사, 도적으로, 그가 한 번이라도 발을 들였던 모든 도시와 제국에서 수배령이 떨어져 있을 정도다. 
        그레이브즈는 성미가 불 같지만, 범죄의 명예에 엄격한 면이 있어 자신의 이중 총열 산탄총 '운명'으로 마무리를 하는 경우가 잦다. 
        최근에는 트위스티드 페이트와 함께 바람 잘 날 없던 파트너 관계를 다시 맺고, 범죄의 냄새가 나는 빌지워터의 그늘진 곳에서 벌어지는 소동을 다시 한 번 주름잡고 있다.</p> """

    elif champ == "그웬":
        return f"""<h2>챔피언 이름 : {champ}</h2><hr/>
        <img src="https://i.namu.wiki/i/sM7QV3NtwKHTLEQPOahWgYspJmTcuiKBCEEec2CyR9hHjUJbM1r-NeBLHHkxxgBL1U9UV1o-JCj50STv6APX1YO5b5uWtJY1DmReO20y-YCP7DjW_ZhoRfPhIwyYDIE_5MMIKr0IINOr3eQLdpG0_A.webp">
        <p> 마법의 힘으로 살아나 인간이 된 인형 그웬은 한때 자신을 만들었던 도구를 휘두른다. 
        발걸음을 내디딜 때마다 자신을 만든 재봉사의 사랑을 느끼며 모든 것을 감사히 여긴다. 
        그웬이 부리는 신성한 안개는 그웬의 가위와 바늘, 실에 축복을 내린 고대의 보호 마법이다. 
        모든 게 새로운 것으로 가득하지만, 그웬은 망가진 세상에서 살아남은 선한 이들을 위해 기꺼이 싸우러 나선다.</p> """


app.run(host="0.0.0.0", debug=True)