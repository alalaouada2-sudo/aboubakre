class ReaderOption {
  const ReaderOption({required this.id, required this.name, required this.audioPath});

  final String id;
  final String name;
  final String audioPath;
}

class QuranRepository {
  static const readers = <ReaderOption>[
    ReaderOption(
      id: 'sudais',
      name: 'عبد الرحمن السديس',
      audioPath: 'assets/readers/sudais_sample.mp3',
    ),
    ReaderOption(
      id: 'afasy',
      name: 'مشاري العفاسي',
      audioPath: 'assets/readers/afasy_sample.mp3',
    ),
    ReaderOption(
      id: 'muaiqly',
      name: 'ماهر المعيقلي',
      audioPath: 'assets/readers/muaiqly_sample.mp3',
    ),
  ];

  static const backgrounds = <String>[
    'assets/backgrounds/open_book_1.mp4',
    'assets/backgrounds/mosque_ambient_1.mp4',
    'assets/backgrounds/nature_river_1.mp4',
  ];

  List<String> ayatForDemo() => const [
        'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
        'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ',
        'الرَّحْمَٰنِ الرَّحِيمِ',
        'مَالِكِ يَوْمِ الدِّينِ',
      ];
}
