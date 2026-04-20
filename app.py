from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

ARTICLES = {
    "dark-matter": {
        "title": "المادة المظلمة",
        "summary": "مكوّن غير مرئي يشكل جزءًا ضخمًا من كتلة الكون.",
        "content": "رغم أننا لا نراها مباشرة، فإن العلماء يستدلون عليها من دوران المجرات وعدسات الجاذبية.",
    },
    "nebula": {
        "title": "السُّدم",
        "summary": "سحب غازية كونية قد تكون مهدًا لولادة النجوم.",
        "content": "تختلف ألوان السُّدم حسب العناصر الكيميائية والإشعاع الصادر من النجوم القريبة.",
    },
    "mars": {
        "title": "العيش على المريخ",
        "summary": "حلم علمي يتطلب تقنيات متقدمة للحماية والبقاء.",
        "content": "أبرز التحديات تشمل الإشعاع، البرودة الشديدة، وضرورة إنتاج الغذاء والأكسجين محليًا.",
    },
    "black-holes": {
        "title": "الثقوب السوداء",
        "summary": "أجسام فائقة الكثافة بجاذبية لا تسمح للضوء بالهروب.",
        "content": "يمكن رصدها عبر تأثيرها على النجوم القريبة والأشعة السينية الصادرة من المواد المتساقطة نحوها.",
    },
    "exoplanets": {
        "title": "الكواكب الخارجية",
        "summary": "عوالم خارج نظامنا الشمسي قد تحمل شروطًا للحياة.",
        "content": "تعتمد طرق اكتشافها على عبور الكوكب أمام النجم أو قياس اهتزاز النجم الناتج عن الجاذبية.",
    },
    "supernova": {
        "title": "المستعرات العظمى",
        "summary": "انفجارات هائلة تساهم في نشر العناصر الثقيلة في الكون.",
        "content": "هذه الانفجارات تصنع عناصر أساسية مثل الحديد وتسهم في دورة ميلاد النجوم الجديدة.",
    },
    "meteor-showers": {
        "title": "زخات الشهب",
        "summary": "مشهد سماوي جميل يحدث عند احتراق جسيمات صغيرة في الغلاف الجوي.",
        "content": "أفضل وقت للرصد يكون بعد منتصف الليل وبعيدًا عن أضواء المدن.",
    },
    "jwst": {
        "title": "تلسكوب جيمس ويب",
        "summary": "عين الكون الحديثة لرصد الأجسام البعيدة بالأشعة تحت الحمراء.",
        "content": "قدّم صورًا مذهلة كشفت تفاصيل غير مسبوقة عن المجرات الأولى وتكوّن النجوم.",
    },
}

PAGES = [
    ("home", "الصفحة الرئيسية", "/"),
    ("assistant", "المساعد الذكي", "/assistant"),
    ("about", "من نحن", "/about"),
    ("contact", "تواصل معنا", "/contact"),
    *[(f"article_{slug}", article["title"], f"/articles/{slug}") for slug, article in ARTICLES.items()],
]


def ai_reply(question: str) -> str:
    q = question.lower()
    if "مجرة" in q or "galaxy" in q:
        return "المجرة مدينة كونية ضخمة تضم مليارات النجوم والغاز والغبار والمادة المظلمة."
    if "سديم" in q or "nebula" in q:
        return "السديم سحابة كونية من الغاز والغبار، وقد يكون مهدًا لولادة نجوم جديدة."
    if "ثقب" in q or "black hole" in q:
        return "الثقب الأسود جسم فائق الكثافة، جاذبيته قوية لدرجة أن الضوء لا يهرب منه."
    if "شهب" in q or "meteor" in q:
        return "لرصد الشهب: ابتعد عن المدينة، اختر ليلة صافية، وانتظر 20 دقيقة لتأقلم العينين."
    if "مريخ" in q or "mars" in q:
        return "استيطان المريخ ممكن نظريًا، لكنه يحتاج تقنيات متقدمة للحماية من الإشعاع وتوليد الموارد."
    return "سؤال رائع ✨ اكتب موضوعًا محددًا عن الفضاء وسأجيبك بطريقة مبسطة."


@app.context_processor
def inject_nav_pages():
    return {"nav_pages": PAGES}


@app.route("/")
def home():
    return render_template("home.html", articles=ARTICLES)


@app.route("/assistant")
def assistant_page():
    return render_template("assistant.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/articles/<slug>")
def article_page(slug: str):
    article = ARTICLES.get(slug)
    if not article:
        return render_template("404.html"), 404
    return render_template("article.html", article=article)


@app.route("/api/assistant", methods=["POST"])
def assistant_api():
    payload = request.get_json(silent=True) or {}
    question = (payload.get("question") or "").strip()
    if not question:
        return jsonify({"error": "الرجاء كتابة سؤال."}), 400
    return jsonify({"answer": ai_reply(question)})


if __name__ == "__main__":
    app.run(debug=True)
