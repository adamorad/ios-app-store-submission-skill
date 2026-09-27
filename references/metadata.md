# App Store metadata checklist

Fill these fields for each locale supported by the release. Keep claims accurate to the binary.

## Version fields

- Name and subtitle.
- Promotional text.
- Full description.
- Keywords (comma-separated, within Apple's current character limit).
- Screenshots and optional previews for each required device family.
- Support URL and privacy-policy URL.
- Copyright, primary/secondary categories, and review contact details.
- Review notes explaining the core flow, offline limitations, optional network features, test steps, and any non-obvious behavior.

## App-level fields

- App Store name and localization.
- Age rating questionnaire.
- Content rights declaration.
- Pricing and availability.
- Export compliance/encryption answers.

## Review notes template

```text
No account is required.
Core gameplay is available offline.
<Describe the exact path to the main feature.>
<Describe optional network features and what happens when offline.>
Test contact: <support email or contact method>
```

Do not include credentials, secrets, or claims that the reviewer cannot reproduce. If a demo account is required, create a dedicated review account and provide only the minimum access information through App Store Connect's review fields.

For a first release, do not invent “What's New” text. Release notes describe changes from a previous version and are generally for subsequent updates.
