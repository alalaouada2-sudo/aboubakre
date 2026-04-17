import 'package:flutter/material.dart';
import '../domain/video_job.dart';
import '../data/quran_repository.dart';

class VideoCreatorScreen extends StatefulWidget {
  const VideoCreatorScreen({super.key});

  @override
  State<VideoCreatorScreen> createState() => _VideoCreatorScreenState();
}

class _VideoCreatorScreenState extends State<VideoCreatorScreen> {
  final _repo = QuranRepository();
  String _reader = QuranRepository.readers.first.id;
  String _bg = QuranRepository.backgrounds.first;
  int _duration = 30;

  @override
  Widget build(BuildContext context) {
    final ayat = _repo.ayatForDemo();
    return Scaffold(
      appBar: AppBar(title: const Text('إنشاء فيديو')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text('السورة: الفاتحة (تجريبي)', style: TextStyle(fontSize: 16)),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: ayat
                .asMap()
                .entries
                .map((e) => Chip(label: Text('${e.key + 1}) ${e.value}')))
                .toList(),
          ),
          const SizedBox(height: 16),
          DropdownButtonFormField<String>(
            value: _reader,
            decoration: const InputDecoration(labelText: 'القارئ'),
            items: QuranRepository.readers
                .map((r) => DropdownMenuItem(value: r.id, child: Text(r.name)))
                .toList(),
            onChanged: (v) => setState(() => _reader = v!),
          ),
          const SizedBox(height: 16),
          DropdownButtonFormField<String>(
            value: _bg,
            decoration: const InputDecoration(labelText: 'الخلفية'),
            items: QuranRepository.backgrounds
                .map((b) => DropdownMenuItem(value: b, child: Text(b.split('/').last)))
                .toList(),
            onChanged: (v) => setState(() => _bg = v!),
          ),
          const SizedBox(height: 16),
          Text('المدة: $_duration ثانية'),
          Slider(
            value: _duration.toDouble(),
            min: 15,
            max: 60,
            divisions: 9,
            onChanged: (v) => setState(() => _duration = v.round()),
          ),
          const SizedBox(height: 20),
          FilledButton.icon(
            icon: const Icon(Icons.movie_creation_outlined),
            label: const Text('تجهيز مشروع الفيديو'),
            onPressed: _createVideoJob,
          ),
        ],
      ),
    );
  }

  void _createVideoJob() {
    final job = VideoJob(
      surahName: 'الفاتحة',
      fromAyah: 1,
      toAyah: 4,
      readerId: _reader,
      backgroundId: _bg,
      durationSeconds: _duration,
      duaText: 'اللهم اجعل القرآن ربيع قلوبنا.',
      watermark: '@quran.reels',
    );

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('تم إنشاء المشروع: ${job.toJson()}')),
    );
  }
}
