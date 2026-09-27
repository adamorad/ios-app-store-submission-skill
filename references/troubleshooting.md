# Troubleshooting

| Symptom | Likely cause | Next check |
| --- | --- | --- |
| No profiles for bundle identifier | App ID, team, or signing mode mismatch | Confirm exact bundle ID, team, Release configuration, and distribution profile |
| Selected signing certificate not included | Provisioning profile was created for another certificate | Regenerate/download a profile containing the selected distribution certificate |
| Project does not exist | CI path or repository layout is stale | Check the committed `.xcodeproj`/`.xcworkspace` path and CI project setting |
| No supported iOS devices | Xcode is targeting a physical device only | Select a simulator for development or Any iOS Device for archive |
| App record creation failed | App Store name is already taken | Create the record manually with an available unique name |
| Build is processing | App Store Connect is validating the upload | Wait for processing; inspect the build's activity and processing messages |
| Unable to add for review | Required metadata or compliance field is missing | Follow every item in the App Store Connect error panel |
| Privacy answers do not match | Binary, SDK, backend, and questionnaire disagree | Re-audit actual collection and update the policy/questionnaire |

Do not solve signing errors by switching a distribution archive to a development profile.
