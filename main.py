"""Write one patch-note line to /output/entry.txt.

Entry for make.fun's "Real-Life Patch Notes: The Comedy Changelog" bounty.

The whole entry is the single line stored in TEXT below. This
program writes it exactly — deterministically, with no input, no
network, and nothing but the Python standard library — to
/output/entry.txt.
"""

import os

# The sealed patch note: one line, 133 characters, written verbatim.
TEXT = (
    "v3.2.0: fixed a bug where the arm fell asleep under the head and "
    "woke up as someone else's. Known issue: ownership is still disputed."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
