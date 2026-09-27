# Release status monitoring

Track these states separately:

1. **Archive/upload** — Xcode Organizer or Xcode Cloud reports whether the upload succeeded.
2. **Processing** — App Store Connect's TestFlight build list reports `Processing`, `Complete`, or an error.
3. **Beta review** — external TestFlight groups may require Beta App Review.
4. **App Review** — the version page reports `Prepare for Submission`, `Waiting for Review`, `In Review`, `Pending Developer Release`, or a rejection state.
5. **Release** — the app version page reports the production release state.

For an authenticated API integration, use an Apple App Store Connect API key stored outside the repository and a dedicated client such as Fastlane. Never put the issuer ID, key ID, private key, or JWT in this repository or in logs. When an API client is unavailable, use the App Store Connect web UI and record the build number, version, and timestamp in the release notes.
