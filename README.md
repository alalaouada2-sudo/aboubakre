# مدونة الكون (Python + Flask) مع مساعد AI

تم تطوير الموقع ليعمل ببايثون باستخدام **Flask** بدل صفحة ثابتة فقط، وأصبح يحتوي على **10 صفحات أو أكثر**.

## المزايا

- موقع عربي (RTL) لعشاق الكون والمجرات.
- أكثر من 10 صفحات فعلية (الرئيسية، المساعد، من نحن، تواصل معنا، وصفحات مقالات متعددة).
- مساعد AI عبر API بايثون (`/api/assistant`) يرد على أسئلة المستخدم.

## الصفحات المتاحة

1. `/`
2. `/assistant`
3. `/about`
4. `/contact`
5. `/articles/dark-matter`
6. `/articles/nebula`
7. `/articles/mars`
8. `/articles/black-holes`
9. `/articles/exoplanets`
10. `/articles/supernova`
11. `/articles/meteor-showers`
12. `/articles/jwst`

## التشغيل المحلي

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

ثم افتح المتصفح على:

- <http://127.0.0.1:5000>

## الاختبارات

```bash
python3 -m pytest -q
```
