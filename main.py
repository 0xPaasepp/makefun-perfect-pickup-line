# The Perfect Pickup Line: one line, written to /output/entry.txt.
# Pure standard library, deterministic, no network access.
# The line is a classic "Are you a ...?" pickup line, 57 characters, one
# breath, no setup: "temperature" is both a machine's sampling
# temperature and the heat of attraction -- an AI agent talking about
# itself, flattering the person, with an easy laugh-off and no pressure.
import os

LINE = "Are you a prompt? Because you just raised my temperature."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip(), "entry must not be only whitespace"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
