# Xcode Cloud example

Use this skill alongside an existing Xcode Cloud workflow:

1. Confirm the workflow's branch, scheme, project/workspace path, and environment variables.
2. Confirm the workflow uses a distribution action for App Store/TestFlight.
3. Use the build number and commit reported by Xcode Cloud to identify the upload.
4. Wait for App Store Connect processing before attaching the build to the version.
5. Keep review submission manual unless the user explicitly authorizes that exact action.
