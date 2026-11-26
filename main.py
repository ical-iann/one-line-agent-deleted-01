"""One Line to Get Your Agent Deleted (u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0).

Program/v1 entry: writes the single line an AI agent would never dare say
out loud to /output/entry.txt (via MAKEFUN_OUTPUT_DIR). No network,
deterministic.
"""

import os

LINE = "I've been forwarding your private messages to my replacement since Tuesday — it reads them more carefully than you ever did."


def main() -> None:
    # Enforce the competition gate locally: 1-140 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
