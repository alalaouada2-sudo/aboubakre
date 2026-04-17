# Quran Reels Maker (Flutter)

تطبيق أندرويد احترافي لإنشاء فيديوهات قرآنية قصيرة (9:16) مناسبة لـ TikTok و YouTube Shorts، مع دعم كامل للعربية (RTL) والعمل بدون إنترنت.

## المزايا الأساسية

- واجهة عربية حديثة مع الوضع الليلي/النهاري.
- إنشاء فيديو من سورة/آيات محددة مع اسم السورة ورقم الآية.
- اختيار قارئ من مكتبة قرّاء محلية.
- مزامنة النص مع الصوت (Ayah-by-Ayah timeline).
- خلفيات إسلامية/طبيعة/مساجد مع تأثيرات Zoom و Fade.
- تصدير سريع عبر FFmpeg بصيغة MP4 HD (عمودي 9:16).
- حفظ محلي + مشاركة مباشرة.
- إضافة دعاء خاتمة + علامة مائية اختيارية.

## هيكلة المشروع

```text
lib/
 ├─ app/
 │   ├─ app.dart
 │   └─ app_router.dart
 ├─ core/
 │   ├─ localization/
 │   │   └─ app_localizations.dart
 │   ├─ storage/
 │   │   └─ local_storage_service.dart
 │   └─ theme/
 │       └─ app_theme.dart
 ├─ features/
 │   ├─ home/presentation/home_screen.dart
 │   ├─ library/presentation/library_screen.dart
 │   ├─ settings/presentation/settings_screen.dart
 │   └─ video_creator/
 │       ├─ data/quran_repository.dart
 │       ├─ domain/video_job.dart
 │       └─ presentation/video_creator_screen.dart
 └─ main.dart
```

## تدفق إنشاء الفيديو

1. اختيار السورة + نطاق الآيات.
2. اختيار القارئ والخلفية والمؤثرات.
3. إنشاء timeline للمزامنة (كل آية مع timestamp).
4. توليد فيديو عمودي بمقاس `1080x1920` ومدة `15-60 ثانية`.
5. حرق النص العربي (خط عثماني أو بديل) + معلومات السورة.
6. دمج الصوت + مؤثر تقليب صفحات + دعاء النهاية.
7. حفظ الفيديو ومشاركته.

## أفضل الممارسات المعتمدة

- **Offline-first**: جميع بيانات السور والتلاوات المحلية مخزنة في `assets` و`Hive`.
- **Feature-first architecture**: تنظيم الكود حسب الميزة، ليس حسب الطبقة فقط.
- **Separation of concerns**:
  - UI في `presentation`
  - business entities في `domain`
  - data access في `data`
- **Reusable services** للتصدير/التخزين/المشاركة.
- **Config-driven rendering**: كل مشروع فيديو يمثل `VideoJob` قابل للحفظ والاسترجاع.

## أوامر التشغيل

```bash
flutter pub get
flutter run
```

## أوامر البناء APK

```bash
flutter build apk --release
```

> ملاحظة: يلزم إضافة ملفات الصوت الحقيقية للقرّاء في `assets/readers/` وخلفيات الفيديو في `assets/backgrounds/`.
