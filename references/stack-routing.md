# External stack routing (opt-in)

Use this reference only when repository evidence makes a route relevant. Routing is advisory: inspect the existing stack, then recommend the matching official skill family. External source/version evidence is not an install pin.

## Evidence and negative cases

- **Cloudflare:** route when evidence includes `wrangler` configuration, a Wrangler config file, or Cloudflare bindings/workers APIs (for example `wrangler.toml`, `wrangler.json`, `cloudflare:` bindings, or Workers APIs). Do not route from generic web code, a `cloudflare` word in prose, or hosting references alone.
- **Expo/EAS:** route when `expo` is a dependency, Expo app configuration is present, or EAS configuration is present (for example `app.json`/`app.config.*` with Expo signals, `eas.json`, or Expo packages). Do not route generic React Native without Expo evidence.
- **Vercel Agent Skills:** route when React, Next.js, or React Native evidence is present **and** the task concerns UI, rendering, accessibility, performance, or related frontend implementation/review. Do not confuse Vercel guidance with Vercel deployment: a Vercel host, project setting, or deploy target alone is not a Vercel Agent Skills route.

Official mappings: Cloudflare official skills; Expo official skills; Vercel `agent-skills`. These mappings are recommendations only; inspect the repository's current dependencies, lockfile, configuration, and toolchain first.

## Source/version evidence

The official repositories were refreshed for this update through authenticated GitHub metadata. The observed `main` commits are research evidence only, not install pins:

- `cloudflare/skills` — `86505e44f87d801aa1864a3c4109e9a8ae5c409f`
- `expo/skills` — `3d1ca4e2a3c5ffc14817a85dde0bf1b188e9753d`
- `vercel-labs/agent-skills` — `063bee94c3f4df8453406c830b0a7df0f2860278`

MinimalShip does not copy these repositories, install them automatically, or claim that a current external revision is available when the network or authentication is unavailable.

## Safety boundary

Inspect and recommend only by default. Never auto-install, vendor, upgrade, change the stack, deploy, invoke paid EAS or cloud operations, or use credentials. Existing configuration, lockfiles, and toolchains are authoritative. Missing browser, native, or runtime capability is **BLOCKED**, not PASS. This reference intentionally contains no install or deployment commands.

## QA gates

- **Cloudflare:** smoke the relevant runtime, binding, and API failure paths; verify configuration and degraded/error behavior without cloud side effects.
- **Expo/EAS:** verify loading, empty, error, and content states; navigation, retry, offline, and safe-area behavior as relevant; collect device/emulator evidence. Missing device/emulator capability is BLOCKED.
- **React/Next/React Native:** collect rendered behavior plus accessibility and performance evidence where relevant. For React Native, include device/emulator evidence; missing runtime capability is BLOCKED.
- Combine applicable gates for projects matching more than one route. A recommendation is not acceptance: report PASS, FAIL, or BLOCKED evidence for each required gate.
