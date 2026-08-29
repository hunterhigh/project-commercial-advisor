from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "project-commercial-advisor"


class PackageStructureTests(unittest.TestCase):
    def test_manifest_has_only_real_components(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "project-commercial-advisor")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertNotIn("mcpServers", manifest)
        self.assertNotIn("apps", manifest)
        self.assertNotIn("hooks", manifest)
        self.assertEqual(manifest["repository"], "https://github.com/hunterhigh/project-commercial-advisor")

    def test_skill_frontmatter_and_references_are_complete(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name: project-commercial-advisor$")
        self.assertRegex(text, r"(?m)^description: .{20,}$")
        self.assertNotRegex(text, r"TODO|TBD|\[TODO")
        for relative in (
            "references/evidence-and-modeling.md",
            "references/platforms/qidian.md",
            "assets/commercial-state-template.md",
        ):
            self.assertIn(relative, text)
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_skill_has_no_workspace_runtime_dependency(self) -> None:
        values = "\n".join(path.read_text(encoding="utf-8") for path in SKILL.rglob("*.md"))
        self.assertNotIn("C:/Users/", values)
        self.assertNotIn("C:\\Users\\", values)
        self.assertNotIn("v5ruwen", values.casefold())

    def test_qidian_reference_requires_query_time_verification(self) -> None:
        text = (SKILL / "references" / "platforms" / "qidian.md").read_text(encoding="utf-8")
        self.assertIn("当前咨询中重新打开", text)
        self.assertIn("https://help.yuewen.com/", text)
        self.assertIn("https://acts.qidian.com/", text)
        self.assertIn("不自动登录", text)

    def test_openai_yaml_is_utf8_and_mentions_skill(self) -> None:
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("项目商业顾问", text)
        self.assertIn("$project-commercial-advisor", text)
        self.assertNotIn("�", text)


if __name__ == "__main__":
    unittest.main()
