# Prompt to Explainer

A Codex skill for turning a topic into a narrated MP4. Choose dark metallic or isometric visuals, or describe a new style in your prompt. The default is a 30-second vertical short with English narration and animated captions.

## Install

Clone the skill into your personal Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/drawrs/prompt-to-explainer.git "${CODEX_HOME:-$HOME/.codex}/skills/prompt-to-explainer"
```

Start a new Codex chat and try:

> Use $prompt-to-explainer to make a 90-second isometric video explaining how an elevator decides which floor to visit next. Use English narration and animated captions. Show me the 30-second pilot.

## Production workflow

The [skill](SKILL.md) guides Codex through nine stages: scaffold, research, narration and word timing, storyboard, shared visual elements, pilot review, parallel shot production, render, and quality checks. You can review the pilot before the remaining shots are built or request autonomous delivery.

The local rendering workflow uses Node.js and npm, Python 3, FFmpeg and ffprobe, a compatible browser, and a local speech engine with word timing or alignment. A [macOS speech recipe](references/local-speech.md) is included. Check [Remotion's license](https://www.remotion.dev/license) for your use case. Multi-agent production requires an environment with delegation enabled.

Style briefs live in [styles](styles/). Add a brief covering camera, lighting, palette, typography, and motion to introduce another style.

Workflow inspiration: [anything2explainer](https://github.com/Vincentwei1021/anything2explainer).
