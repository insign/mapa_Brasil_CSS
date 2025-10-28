import re

# List of Brazilian states abbreviations
states = [
    "ac", "al", "ap", "am", "ba", "ce", "df", "es", "go", "ma", "mt", "ms",
    "mg", "pa", "pb", "pr", "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc",
    "sp", "se", "to"
]

# Read the SVG file
with open("sources/Brazil_Blank_Map.svg", "r") as f:
    svg_content = f.read()

# Use a regular expression to find all path elements and add an id to each one
path_regex = re.compile(r'(<path\s)(.*?)(/>|>)', re.DOTALL)

# A function to replace each path with a state id
def add_id_to_path(match, state_list):
    if not state_list:
        return match.group(0)

    state_id = state_list.pop(0)
    return f'{match.group(1)}id="{state_id}" {match.group(2)}{match.group(3)}'

# Get a copy of the list to avoid modifying the original
states_copy = states[:]
modified_svg_content, num_replacements = path_regex.subn(
    lambda m: add_id_to_path(m, states_copy),
    svg_content
)

# Write the modified content to a new file
with open("assets/map.svg", "w") as f:
    f.write(modified_svg_content)

print(f"Added {num_replacements} IDs to the SVG file.")
