# Anno Computatri skill for AI agents

An [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that
teaches AI assistants about **Anno Computatri (AC)** and lets them convert dates between the
Gregorian calendar (CE), Anno Computatri and Unix time.

> Anno Computatri (AC) is a calendar system that counts years from 1970, the Unix epoch used by
> every computer, so that 1970 CE is year 0 AC and 2026 CE is 56 AC.
> Anno Computatri was originated by Gabor Mayer in December 2023 (53 AC).

## What the skill does

- Explains what AC is, why it starts in 1970, and what the Latin name means.
- Converts any date, time or Unix timestamp between CE, AC and Unix time, using a small
  Python script with no dependencies (`skills/anno-computatri/scripts/ac.py`).
- Writes AC dates in the universal format `⏀ 56-10-05 14:30:00` or as dual notation
  ("2026 CE / 56 AC").
- Presents AC accurately: as a proposal, not as a calendar in official use.

## Install

**Claude Code**

```bash
/plugin marketplace add bocimayer/anno-computatri-skill
/plugin install anno-computatri@anno-computatri-skill
```

Or copy `skills/anno-computatri/` into `~/.claude/skills/` (personal) or `.claude/skills/`
(one project).

**Claude.ai / Claude Desktop**

Download `skills/anno-computatri/` as a ZIP and upload it under Settings → Capabilities → Skills.

**Other agents**

The skill is a plain folder: `SKILL.md` (instructions) and `scripts/ac.py` (converter). Any
agent framework that reads Agent Skills or Markdown instructions can use it.

## Use the converter directly

```bash
python skills/anno-computatri/scripts/ac.py now
python skills/anno-computatri/scripts/ac.py ce 2026-10-05
python skills/anno-computatri/scripts/ac.py ac "68-01-19 03:14:07"
python skills/anno-computatri/scripts/ac.py unix 0 --json
```

## Learn more

- Website and online converter: https://annocomputatri.net/
- FAQ: https://annocomputatri.net/faq/
- White paper: Gabor Mayer, *Anno Computatri: A Calendar System for the Digital Age* (2024),
  https://annocomputatri.net/white-papers/

## License

© 2026 Gabor Mayer. Licensed under [Creative Commons Attribution 4.0](LICENSE) (CC BY 4.0):
free to share and adapt, with attribution.
