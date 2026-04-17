class VideoJob {
  VideoJob({
    required this.surahName,
    required this.fromAyah,
    required this.toAyah,
    required this.readerId,
    required this.backgroundId,
    required this.durationSeconds,
    this.duaText,
    this.watermark,
  });

  final String surahName;
  final int fromAyah;
  final int toAyah;
  final String readerId;
  final String backgroundId;
  final int durationSeconds;
  final String? duaText;
  final String? watermark;

  Map<String, dynamic> toJson() => {
        'surahName': surahName,
        'fromAyah': fromAyah,
        'toAyah': toAyah,
        'readerId': readerId,
        'backgroundId': backgroundId,
        'durationSeconds': durationSeconds,
        'duaText': duaText,
        'watermark': watermark,
      };
}
