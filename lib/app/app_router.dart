import 'package:go_router/go_router.dart';
import '../features/home/presentation/home_screen.dart';
import '../features/video_creator/presentation/video_creator_screen.dart';
import '../features/library/presentation/library_screen.dart';
import '../features/settings/presentation/settings_screen.dart';

final appRouter = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
    GoRoute(path: '/create', builder: (context, state) => const VideoCreatorScreen()),
    GoRoute(path: '/library', builder: (context, state) => const LibraryScreen()),
    GoRoute(path: '/settings', builder: (context, state) => const SettingsScreen()),
  ],
);
