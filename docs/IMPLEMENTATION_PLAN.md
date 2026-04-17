# خطة تنفيذ احترافية (MVP -> Production)

## 1) البيانات القرآنية والمزامنة

- استخدم مصدر نص قرآني موثوق (Uthmani) واحفظه محليًا JSON.
- أنشئ ملف مزامنة لكل تلاوة بالشكل التالي:

```json
{
  "surah": 1,
  "reader": "afasy",
  "timeline": [
    {"ayah": 1, "startMs": 0, "endMs": 5400},
    {"ayah": 2, "startMs": 5400, "endMs": 10900}
  ]
}
```

> بهذه الطريقة تظهر الآيات متسلسلة بدقة أثناء القراءة.

## 2) محرك إخراج الفيديو (FFmpeg)

اقتراح أمر FFmpeg (مبدأي):

```bash
ffmpeg -i bg.mp4 -i recitation.mp3 \
-filter_complex "[0:v]scale=1080:1920,setsar=1,zoompan=z='min(zoom+0.0008,1.08)':d=125:s=1080x1920:fps=30,format=yuv420p[v]" \
-map "[v]" -map 1:a -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 192k -shortest out.mp4
```

- أضف طبقات النص (`drawtext`) لكل آية حسب التوقيت.
- أضف شعارًا مائيًا اختياريًا في أسفل الفيديو.
- استخدم `-preset veryfast` لتوازن السرعة والجودة على الهاتف.

## 3) الأداء

- صدّر داخل Isolate لتقليل التقطيع في الواجهة.
- استخدم Caching للملفات المؤقتة.
- وفر إعدادين للتصدير:
  - Fast HD (افتراضي)
  - Ultra HD (أبطأ)

## 4) الجودة والاختبارات

- Golden tests لواجهات RTL.
- Unit tests لبناء `VideoJob` والتحقق من قواعد المدة (15-60).
- Integration test لمسار: إنشاء مشروع -> تصدير -> حفظ -> مشاركة.

## 5) النشر

- keystore خاص للتوقيع.
- Proguard/R8 مع اختبار مكتبة FFmpeg.
- صفحة خصوصية واضحة (ملفات محلية فقط + مشاركة يدوية).
