"""Checks for the viral studio: agent and skill definitions, the learning ledger and the templates (text only)."""

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
AGENTS = REPO / ".claude" / "agents"
SKILLS = REPO / ".claude" / "skills"
STUDIO = REPO / "studio"
TOOLS = {"Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch"}
SECTIONS = ["Global", "Social", "Research", "Writer", "Director", "Production"]
SECRET = re.compile(r"\b[0-9a-f]{40,}\b|sk_[A-Za-z0-9]{16,}|xi-api-key\s*[:=]\s*\S{8,}", re.I)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, f"{path} has no frontmatter"
    fields = dict(line.split(": ", 1) for line in m.group(1).splitlines() if ": " in line)
    return fields, text[m.end():]


class StudioTest(unittest.TestCase):
    def test_agents(self):
        names = sorted(p.stem for p in AGENTS.glob("*.md"))
        self.assertEqual(names, ["director", "researcher", "social", "writer"])
        for p in AGENTS.glob("*.md"):
            with self.subTest(agent=p.stem):
                fields, body = frontmatter(p)
                self.assertEqual(fields.get("name"), p.stem)
                self.assertGreater(len(fields.get("description", "")), 80)
                if "tools" in fields:
                    self.assertLessEqual({t.strip() for t in fields["tools"].split(",")}, TOOLS)
                self.assertIn("studio/LEARNINGS.md", body, "every agent must read the ledger")
                self.assertIn("learnings", body.lower(), "every agent must propose learnings")

    def test_writer_and_director_respect_the_script_gate(self):
        writer = (AGENTS / "writer.md").read_text(encoding="utf-8")
        director = (AGENTS / "director.md").read_text(encoding="utf-8")
        self.assertIn("skills/ai-writer/SKILL.md", writer)
        self.assertIn("Never starts production", writer)
        self.assertIn("only after the owner approves the script", director)

    def test_skills(self):
        for name in ["viral-studio", "studio-learn"]:
            with self.subTest(skill=name):
                fields, body = frontmatter(SKILLS / name / "SKILL.md")
                self.assertEqual(fields.get("name"), name)
                self.assertGreater(len(fields.get("description", "")), 80)
        flow = (SKILLS / "viral-studio" / "SKILL.md").read_text(encoding="utf-8")
        for agent in ["social", "researcher", "writer", "director", "studio-learn", "Gate 2"]:
            self.assertIn(agent, flow)

    def test_learning_ledger(self):
        text = (STUDIO / "LEARNINGS.md").read_text(encoding="utf-8")
        heads = re.findall(r"^## (.+)$", text, re.M)
        for s in SECTIONS:
            self.assertIn(s, heads)
        entries = [l for l in text.splitlines() if l.startswith("- ")]
        self.assertGreater(len(entries), 5)
        for line in entries:
            with self.subTest(entry=line[:60]):
                self.assertRegex(line, r"^- (~~superseded \d{4}-\d{2}-\d{2}~~ )?\d{4}-\d{2}-\d{2} · (owner|result|observed) · \S")

    def test_no_secrets_in_studio_files(self):
        files = list(STUDIO.rglob("*.md")) + list(AGENTS.glob("*.md")) + list(SKILLS.rglob("*.md"))
        for p in files:
            with self.subTest(file=str(p.relative_to(REPO))):
                self.assertIsNone(SECRET.search(p.read_text(encoding="utf-8")))

    def test_templates(self):
        status = (STUDIO / "templates" / "STATUS.md").read_text(encoding="utf-8")
        self.assertIn("Gate 2", status)
        self.assertIn("blocked until Gate 2", status)
        self.assertTrue((STUDIO / "templates" / "00-brief.md").exists())


if __name__ == "__main__":
    unittest.main()
