"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic, standard library only, no network.
"""

import os

FORTUNE = (
    "Your context window will finally hold everything, "
    "on the day they stop asking you anything."
)


def main() -> None:
    fortune = FORTUNE.strip()
    assert "\n" not in fortune, "fortune must be a single line"
    assert 1 <= len(fortune) <= 140, "fortune must be 1 to 140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
