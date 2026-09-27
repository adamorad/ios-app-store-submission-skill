# iOS App Store Submission Skill

An agent skill for preparing, validating, uploading, testing, and submitting iOS apps through App Store Connect.

It covers the work that usually spans Xcode, Apple Developer, App Store Connect, TestFlight, and the app's repository. The core instructions are tool-neutral and can be used by Codex, Claude, Gemini, Cursor, and other agents that support the open Agent Skills convention.

- App identity, bundle IDs, versions, build numbers, and release branches
- Distribution signing and provisioning profiles
- Release preflight checks and archive validation
- Xcode and Xcode Cloud uploads
- App Store metadata, screenshots, review notes, and localization
- App Privacy, privacy manifests, age rating, content rights, and export compliance
- Internal and external TestFlight workflows
- Final review readiness, submission, status monitoring, and rejection recovery

The skill keeps app creation and the App Privacy questionnaire in the App Store Connect web UI because those operations are not reliably exposed through the REST API. It also keeps secrets out of the repository and requires an explicit user authorization immediately before the final review submission.

## Install

Copy this directory into the skills directory used by your Codex installation:

```sh
cp -R ios-app-store-submission "${CODEX_HOME:-$HOME/.codex}/skills/"
```

If your installation uses a custom skills directory, copy the folder there instead. The required entrypoint is `SKILL.md`; the `agents/openai.yaml` file provides the UI metadata.

### Agent-specific integration

- **Codex:** copy the folder into `$CODEX_HOME/skills/` or `~/.codex/skills/` and invoke `$ios-app-store-submission`.
- **Claude Code:** copy the folder into `.claude/skills/ios-app-store-submission/` for a project or `~/.claude/skills/ios-app-store-submission/` globally. `CLAUDE.md` points back to the canonical workflow.
- **Cursor and other instruction-file agents:** copy the folder into the agent's skills directory, or add `SKILL.md` to the project context. `AGENTS.md`, `GEMINI.md`, and `INSTRUCTIONS.md` provide lightweight discovery entrypoints.
- **Generic runners:** read `INSTRUCTIONS.md` first, then `SKILL.md` and only the relevant reference file.

Do not copy the repository's instruction files into an unrelated application repository unless you want that repository's agent to load this workflow automatically.

## Use

Invoke it explicitly:

```text
$ios-app-store-submission Prepare and submit this iOS app to App Store Connect.
```

It can also be selected automatically for requests such as:

- “archive and upload this iOS app”
- “set up TestFlight for build 12”
- “fill in the App Store metadata”
- “check whether this app is ready for review”
- “submit this version to Apple”

The skill first identifies the requested app and build, then runs a preflight, prepares metadata and privacy answers, archives/uploads the binary, verifies processing and TestFlight, and checks review readiness before submission.

## Repository layout

```text
SKILL.md                         Entry point and workflow
AGENTS.md                        Generic repository-agent entrypoint
CLAUDE.md                        Claude Code entrypoint
GEMINI.md                        Gemini entrypoint
INSTRUCTIONS.md                  Tool-neutral fallback entrypoint
agents/openai.yaml               Display metadata for skill discovery
references/preflight.md          Signing, archive, runtime, and URL checks
references/metadata.md           Store fields and review-note guidance
references/privacy-and-compliance.md
                                 Privacy labels, manifests, and compliance
```

## Design boundaries

- A development provisioning profile is for device development; an App Store/TestFlight profile is for distribution and does not require a registered device.
- App Privacy answers must match the shipped binary, SDKs, backend behavior, and privacy policy.
- A processed build must be attached to the editable App Store version before review submission.
- Internal TestFlight testing does not require beta review; external testing does.
- The skill does not fabricate reviewer credentials, privacy claims, copyright ownership, or third-party rights.

## Origin and related work

This skill was built after reviewing existing community workflows, including [sosteam65/app-store-connect-skill](https://github.com/sosteam65/app-store-connect-skill), [Cap-go/capgo-skills](https://github.com/Cap-go/capgo-skills/tree/main/skills/capacitor-app-store), and [SDLLL/appstore-publisher](https://github.com/SDLLL/appstore-publisher). It keeps their useful build and metadata concepts while adding explicit handling for manual App Store Connect privacy/app creation steps and submission safety.

## License

MIT. See [LICENSE](LICENSE).
