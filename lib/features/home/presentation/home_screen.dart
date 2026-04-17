import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/localization/app_localizations.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final t = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(t.tr('homeTitle'))),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            _HomeAction(
              label: t.tr('createVideo'),
              icon: Icons.auto_awesome,
              onTap: () => context.go('/create'),
            ),
            _HomeAction(
              label: t.tr('library'),
              icon: Icons.video_library,
              onTap: () => context.go('/library'),
            ),
            _HomeAction(
              label: t.tr('settings'),
              icon: Icons.settings,
              onTap: () => context.go('/settings'),
            ),
          ],
        ),
      ),
    );
  }
}

class _HomeAction extends StatelessWidget {
  const _HomeAction({required this.label, required this.icon, required this.onTap});

  final String label;
  final IconData icon;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: Icon(icon),
        title: Text(label),
        trailing: const Icon(Icons.chevron_left),
        onTap: onTap,
      ),
    );
  }
}
