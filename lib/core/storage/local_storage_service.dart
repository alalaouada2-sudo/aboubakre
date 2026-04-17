import 'package:hive_flutter/hive_flutter.dart';

class LocalStorageService {
  static const _jobsBox = 'video_jobs';

  static Future<void> init() async {
    await Hive.initFlutter();
    await Hive.openBox<Map>(_jobsBox);
  }

  static Box<Map> jobsBox() => Hive.box<Map>(_jobsBox);
}
