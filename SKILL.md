---
name: ios-app-store-submission
description: Prepare, validate, upload, test, and submit iOS apps through App Store Connect, including metadata, privacy, signing, and review readiness.
---

# iOS App Store submission

Use this skill when the user asks to prepare, upload, TestFlight-test, or submit an iOS app to App Store Connect. Treat each app as a separate product: resolve the bundle ID, App Store record, version, build number, signing identity, metadata, privacy answers, and test groups for the requested app before changing anything.

## Operating rules

- Inspect the repository and the current App Store Connect record before editing. Never assume that the currently selected app, bundle ID, version, or build belongs to the requested product.
- Keep secrets out of repositories, logs, screenshots, chat messages, and generated files. Use an existing authenticated App Store Connect session or a user-provided API key through its secure local path.
- Use the App Store Connect web UI for app creation and the App Privacy questionnaire. The REST API does not provide reliable endpoints for creating an app or editing the privacy questionnaire.
- Use Xcode or Xcode Cloud for signing, archiving, and uploading. A distribution/TestFlight profile does not require a registered physical device; a development profile does.
- Treat metadata as factual product claims. Do not invent privacy practices, reviewer credentials, permissions, age-rating answers, copyright ownership, or third-party rights.
- Test the exact uploaded build, including offline behavior and all network-backed services, before submission.
- Before any external mutation, summarize the exact app, build, destination, and action. A final App Store review submission is a representational action and requires the user's explicit authorization immediately before clicking the final submit control unless the user has already explicitly authorized that exact submission in the current task.

## Workflow

### 1. Identify the app and source

Resolve:

- App Store Connect app ID and name.
- Bundle ID and Apple Developer Team ID.
- Editable App Store version and target locale.
- Build number and marketing version in the Xcode project.
- Repository commit or Xcode Cloud workflow that produced the build.

If the app record does not exist, create it manually in App Store Connect with the exact explicit bundle ID. Choose a unique App Store name; the in-app display name can remain localized separately.

### 2. Run the preflight

From the project root, inspect `Info.plist`, the Xcode project/workspace, entitlements, privacy manifests, package dependencies, and any app-store metadata files. Run the project's tests and validation scripts. Check that:

- `CFBundleIdentifier`, version, and build number match the intended App Store record.
- Release signing uses `Apple Distribution`, an App Store/TestFlight provisioning profile, and `get-task-allow` is false.
- The archive has no placeholder name, bundle ID, icons, launch assets, or missing required usage descriptions.
- Privacy manifest, App Store privacy answers, SDK data behavior, and privacy-policy text agree.
- Support and privacy URLs return HTTP 200 without authentication.
- Network endpoints used by the release build are live from outside the developer machine.
- Screenshots show the actual current build and meet Apple's required device dimensions.

Use [references/preflight.md](references/preflight.md) for the check order and common signing failures.

### 3. Prepare metadata

Complete the app-level and version-level fields for every submitted locale: name, subtitle, promotional text, description, keywords, support URL, privacy-policy URL, copyright, category, age rating, content rights, pricing/availability, export compliance, review contact, and review notes. For a first version, leave release notes/“What's New” empty unless App Store Connect explicitly requests them.

Use [references/metadata.md](references/metadata.md) for field limits, a metadata checklist, and review-note structure.

### 4. Configure privacy and compliance

Answer App Privacy from the shipped binary and backend behavior, not from assumptions. Include optional collection when the user can explicitly send it to a server. Declare whether each type is linked to identity and whether it is used for tracking. Complete age rating, content rights, encryption/export compliance, and any capability-specific declarations.

Use [references/privacy-and-compliance.md](references/privacy-and-compliance.md). Stop and ask the user when the source does not establish an answer.

### 5. Archive and upload

Use the Xcode GUI when available:

1. Select the app target, team, and Release configuration.
2. Select **Any iOS Device (arm64)**.
3. Choose **Product → Archive**.
4. In Organizer choose **Distribute App → App Store Connect → Upload**.

Alternatively use an established Xcode Cloud workflow or `xcodebuild` export with a verified `ExportOptions.plist`. Do not switch to a development profile to work around an archive error. After upload, wait for App Store Connect processing and select the processed build in the version record.

### 6. TestFlight

Internal testing can start after processing and does not require beta review. External testing requires Beta App Review before the build is distributed to external testers. Create or select the correct group, attach the intended build, fill beta app information, add testers, and test the uploaded binary on supported devices. Record any issues and fix them by uploading a new build with a higher build number.

### 7. Submit for App Review

Run the final readiness check: processed build attached, metadata complete, screenshots present, privacy published, pricing set, content rights answered, age rating complete, export compliance answered, review notes and contact details present, and no unresolved errors. Click **Add for Review**, review the submission summary, and only then perform the final **Submit for Review** after the user authorizes that exact action. Report the resulting state and submission ID/status.

### 8. Monitor and recover

Track build processing, TestFlight beta review, App Review, and release status separately. For a failed upload, inspect the Xcode Organizer log and App Store Connect processing messages before changing signing or incrementing versions. For a rejection, map each issue to the submitted binary or metadata, fix it, upload a new build only when code changed, and resubmit the corrected version.

## References

- [references/preflight.md](references/preflight.md) — project, signing, archive, URL, and build checks.
- [references/metadata.md](references/metadata.md) — App Store fields, review notes, and locale checklist.
- [references/privacy-and-compliance.md](references/privacy-and-compliance.md) — privacy labels, manifests, age rating, rights, and export compliance.
