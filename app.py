from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

PAGES = [
    ("home", "الصفحة الرئيسية", "/"),
    ("assistant", "المساعد الذكي", "/assistant"),
    ("about", "من نحن", "/about"),
    ("contact", "تواصل معنا", "/contact"),
    ("article_dark_matter", "المادة المظلمة", "/articles/dark-matter"),
    ("article_nebula", "السُّدم", "/articles/nebula"),
    ("article_mars", "العيش على المريخ", "/articles/mars"),
    ("article_black_holes", "الثقوب السوداء", "/articles/black-holes"),
    ("article_exoplanets", "الكواكب الخارجية", "/articles/exoplanets"),
    ("article_supernova", "المستعرات العظمى", "/articles/supernova"),
    ("article_meteor_showers", "زخات الشهب", "/articles/meteor-showers"),
    ("article_jwst", "تلسكوب جيمس ويب", "/articles/jwst"),
]


def ai_reply(question: str) -> str:
    q = question.lower()
    if "مجرة" in q or "galaxy" in q:
        return "المجرة نظام ضخم من النجوم والغاز والغبار والمادة المظلمة مرتبط بالجاذبية."
    if "سديم" in q or "nebula" in q:
        return "السديم سحابة غازية قد تكون مهدًا لولادة النجوم أو بقايا انفجار نجمي."
    if "ثقب" in q or "black hole" in q:
        return "الثقب الأسود يملك جاذبية هائلة تمنع حتى الضوء من الهروب من أفق الحدث."
    if "شهب" in q or "meteor" in q:
        return "أفضل رصد للشهب يكون بعيدًا عن التلوث الضوئي وبعد منتصف الليل مع سماء صافية."
    if "مريخ" in q or "mars" in q:
        return "العيش على المريخ ممكن نظريًا لكنه يتطلب حماية من الإشعاع وأنظمة دعم حياة متقدمة."
    return "سؤال جميل ✨ اكتب موضوعًا فلكيًا محددًا وسأعطيك شرحًا مبسطًا وواضحًا."


@app.context_processor
def inject_nav_pages():
    return {"nav_pages": PAGES}


@app.route("/")
def home():
    featured = [
        {"title": "المادة المظلمة", "url": "/articles/dark-matter"},
        {"title": "الثقوب السوداء", "url": "/articles/black-holes"},
        {"title": "تلسكوب جيمس ويب", "url": "/articles/jwst"},
    ]
    return render_template("home.html", featured=featured)


@app.route("/assistant")
def assistant_page():
    return render_template("assistant.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/articles/dark-matter")
def article_dark_matter():
    return render_template("article_dark_matter.html")


@app.route("/articles/nebula")
def article_nebula():
    return render_template("article_nebula.html")


@app.route("/articles/mars")
def article_mars():
    return render_template("article_mars.html")


@app.route("/articles/black-holes")
def article_black_holes():
    return render_template("article_black_holes.html")


@app.route("/articles/exoplanets")
def article_exoplanets():
    return render_template("article_exoplanets.html")


@app.route("/articles/supernova")
def article_supernova():
    return render_template("article_supernova.html")


@app.route("/articles/meteor-showers")
def article_meteor_showers():
    return render_template("article_meteor_showers.html")


@app.route("/articles/jwst")
def article_jwst():
    return render_template("article_jwst.html")


@app.route("/api/assistant", methods=["POST"])
def assistant_api():
    payload = request.get_json(silent=True) or {}
    question = (payload.get("question") or "").strip()
    if not question:
        return jsonify({"error": "الرجاء كتابة سؤال."}), 400
    return jsonify({"answer": ai_reply(question)})


if __name__ == "__main__":
    app.run(debug=True)
