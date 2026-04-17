# مدونة الكون (Python + Flask)

تم **جمع كل المحتوى في موقع واحد** بواجهة عربية حديثة (RTL)، مع تصميم أجمل وتجربة استخدام أوضح.

## ماذا يوجد الآن؟

- صفحة رئيسية موحدة تجمع:
  - نبذة عن المشروع
  - روابط سريعة للمساعد الذكي
  - شبكة مقالات الفضاء
  - رابط التواصل
- مساعد AI عبر API بايثون (`POST /api/assistant`).
- أكثر من 10 صفحات عبر روابط المقالات + الصفحات الأساسية.

## الصفحات

- `/`
- `/assistant`
- `/about`
- `/contact`
- `/articles/<slug>` حيث `slug` من المقالات المتاحة (مثل: `dark-matter`, `nebula`, `jwst` ...)

## التشغيل المحلي

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

ثم افتح:

- <http://127.0.0.1:5000>

## الاختبارات

```bash
python3 -m pytest -q
```
