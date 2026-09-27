# iOS submission preflight

Use this list before uploading a build.

## Identity

- Confirm the requested app name and App Store Connect numeric app ID.
- Confirm the explicit bundle ID in the Xcode target, archive, and Developer portal.
- Confirm marketing version and build number. A build number already uploaded for that version cannot be reused.
- Confirm the release branch/commit and record it in the submission notes.

## Signing

- Distribution/TestFlight archive: `Apple Distribution` certificate and App Store Connect/App Store profile.
- Development run: Apple Development certificate and development profile, which requires a registered device.
- For a distribution archive, use **Any iOS Device (arm64)** and Release configuration.
- Verify the archive's embedded provisioning profile has the expected application identifier and `get-task-allow=false`.

## Binary and runtime

- Run unit/integration tests and the project's own verification script.
- Launch the exact release build and exercise first launch, core loop, background/resume, audio/haptics, sharing, deep links, and error states.
- Test offline behavior and every backend endpoint used by the build. A successful browser build does not prove the native bundle uses the same endpoint.
- Check icons, launch screen, supported orientations, minimum iOS version, and safe-area behavior.

## Web and metadata health

```sh
curl -fsS -o /dev/null -w '%{http_code} %{url_effective}\n' https://example.com/privacy
curl -fsS -o /dev/null -w '%{http_code} %{url_effective}\n' https://example.com/support
```

Both public URLs should return HTTP 200. Verify screenshots were captured from the current build, not an older app or simulator placeholder.

## Common failures

- “No devices … development profile”: switch Release signing to Apple Distribution/App Store profile; do not register a device merely to upload.
- “Provisioning profile does not include selected signing certificate”: regenerate the profile using the exact distribution certificate installed in the keychain.
- “App must be registered”: create the App Store Connect record first or use the existing record with the same bundle ID.
- “Build not available”: wait for processing, then refresh the version page and select the processed build.
