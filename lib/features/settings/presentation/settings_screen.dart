import 'package:flutter/material.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الإعدادات')),
      body: ListView(
        children: const [
          SwitchListTile(
            value: true,
            onChanged: null,
            title: Text('تفعيل الوضع الليلي تلقائيًا'),
          ),
          ListTile(
            leading: Icon(Icons.cloud_download_outlined),
            title: Text('تنزيل مكتبة التلاوات للاستخدام بدون إنترنت'),
          ),
          ListTile(
            leading: Icon(Icons.hd),
            title: Text('جودة التصدير الافتراضية: HD 1080x1920'),
          ),
        ],
      ),
    );
  }
}
