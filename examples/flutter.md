# Flutter example

1. Run `flutter pub get` and confirm the iOS deployment target.
2. Open `ios/Runner.xcworkspace` and confirm the Runner bundle ID, team, and Release signing.
3. Run `scripts/preflight.sh ios`.
4. Archive the workspace and verify the exported archive contains the intended Flutter assets.
5. Reconcile plugin data collection with the App Privacy questionnaire.
