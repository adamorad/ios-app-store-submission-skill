# Privacy and compliance

App Privacy is a manual App Store Connect questionnaire. Derive every answer from the shipped app, SDKs, server code, and privacy policy.

For each collected data type, decide:

1. Whether the app or a third-party partner transmits it off-device.
2. Whether it is linked to a user or account.
3. Whether it is used for tracking as Apple defines tracking.
4. The purpose: app functionality, analytics, advertising/marketing, personalization, or another purpose.

Optional user-submitted data that is sent to a backend on an ongoing basis should normally be disclosed. Do not mark a data type as optional merely because the user can avoid the feature if the app collects it when the feature is used.

Check consistency across:

- `PrivacyInfo.xcprivacy` and any extension/framework manifests.
- App Store privacy answers.
- Permission usage descriptions and entitlements.
- Third-party SDK behavior.
- Privacy policy and review notes.

Also complete:

- Age rating.
- Content rights for third-party material.
- Export compliance/encryption questionnaire.
- Required capability disclosures and reviewer instructions.

If the app has no collection, select “Data Not Collected” only after confirming the binary and all SDKs do not transmit data. If the answer is uncertain, inspect the code and dependency documentation or ask the user; never guess.
