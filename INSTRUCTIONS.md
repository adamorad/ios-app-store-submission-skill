# Portable agent instructions

If your agent does not discover `SKILL.md` automatically, read it first. It is the canonical, tool-neutral workflow for preparing, validating, uploading, testing, and submitting iOS apps through App Store Connect.

The workflow is intentionally split by capability:

- Browser/UI agents handle app creation, App Privacy, metadata, TestFlight groups, and review submission.
- macOS/Xcode agents handle signing, archiving, and uploading.
- Shell/CI agents handle repository checks, tests, URL health checks, and `xcodebuild` workflows.
- Agents without one of those capabilities must report the missing capability and provide the exact handoff step instead of pretending it completed.

Always verify the app, bundle ID, version, and build before making changes. Keep secrets private. Require explicit authorization immediately before the final App Review submission.
