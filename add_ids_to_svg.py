import xml.etree.ElementTree as ET

# Register the SVG namespace to avoid issues with prefixes
ET.register_namespace("", "http://www.w3.org/2000/svg")

# Manually defined Brazil states abbreviations in a plausible order
# This is a placeholder and will need to be manually verified
states_abbr = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO"
]

def clean_svg_and_assign_ids(input_svg_path, output_svg_path):
    # Parse the SVG file, removing unsupported attributes for security
    tree = ET.parse(input_svg_path, parser=ET.XMLParser(target=ET.TreeBuilder(insert_comments=False, insert_pis=False)))
    root = tree.getroot()

    # Find the group of states by ID
    states_group = root.find(".//*[@id='Estados']")
    if states_group is None:
        print("Error: Could not find the group with id='Estados'")
        return

    # Remove all non-path elements from the group
    for elem in list(states_group):
        if 'path' not in elem.tag:
            states_group.remove(elem)

    # Clean paths and assign IDs
    paths = states_group.findall("{http://www.w3.org/2000/svg}path")
    if len(paths) != len(states_abbr):
        print(f"Warning: Found {len(paths)} paths but have {len(states_abbr)} state abbreviations.")

    # Remove style elements from the entire SVG
    for style_elem in root.findall(".//{http://www.w3.org/2000/svg}style"):
        parent = root.find(".//*[style]")
        if parent is not None:
            parent.remove(style_elem)

    for i, path in enumerate(paths):
        # Preserve the 'd' attribute, which defines the shape
        d_attrib = path.attrib.get('d')

        # Clear all other attributes
        path.attrib.clear()

        if d_attrib:
            path.attrib['d'] = d_attrib

        # Assign a unique ID and a common class
        if i < len(states_abbr):
            path.attrib['id'] = states_abbr[i].lower()
        path.attrib['class'] = 'state'

    # Create a new SVG structure for the cleaned output
    new_root = ET.Element('svg', attrib=root.attrib)
    new_root.append(states_group)

    # Write the cleaned SVG to a new file
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_svg_path, encoding='utf-8', xml_declaration=True)

# Run the cleaning process
clean_svg_and_assign_ids('sources/Brazil_Blank_Map.svg', 'assets/map.svg')
