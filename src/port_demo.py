import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"

def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def score_requirement(item):
    days = item["days_until_due"]
    if days <= 14:
        return 100
    if days <= 30:
        return 85
    return 65

def build_action_plan(sailor, guidance):
    actions = []
    review_required = False

    for item in sailor["outstanding_requirements"]:
        req = item["requirement"]
        rule = guidance.get(req, {})
        score = score_requirement(item)
        source = rule.get("source", "No source found")
        guidance_text = rule.get("guidance", "No guidance available. Human review required.")

        if source == "No source found" or rule.get("requires_human_review", False):
            review_required = True

        actions.append({
            "requirement": req,
            "category": item["category"],
            "priority_score": score,
            "guidance": guidance_text,
            "source": source
        })

    actions.sort(key=lambda x: x["priority_score"], reverse=True)
    return actions, review_required

def write_plan(sailor, actions, review_required):
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / "generated_dwe_action_plan.md"

    lines = [
        "# Generated DWE Action Plan",
        "",
        f"**Sailor:** {sailor['name']}",
        f"**Unit:** {sailor['unit']}",
        f"**Next Drill Weekend:** {sailor['next_drill_weekend']}",
        "",
        "## Recommended Actions",
        ""
    ]

    for idx, action in enumerate(actions, start=1):
        lines.append(f"{idx}. **{action['requirement']}**")
        lines.append(f"   - Category: {action['category']}")
        lines.append(f"   - Priority Score: {action['priority_score']}")
        lines.append(f"   - Recommendation: {action['guidance']}")
        lines.append(f"   - Source: {action['source']}")
        lines.append("")

    lines.append("## Human Review")
    if review_required:
        lines.append("Human review is required before this plan is used for official communication.")
    else:
        lines.append("No human review trigger was detected in this synthetic demo.")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path

def main():
    sailor = load_json(DATA_DIR / "dummy_sailor_record.json")
    guidance = load_json(DATA_DIR / "dummy_readiness_guidance.json")
    actions, review_required = build_action_plan(sailor, guidance)
    output_path = write_plan(sailor, actions, review_required)

    print("PORT demo completed.")
    print(f"Generated action plan: {output_path}")

if __name__ == "__main__":
    main()
