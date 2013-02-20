
def parse(inputs_file, groupping_symbol="group", input_parts=["name", "path"]):
    """Parses a yayaml file and returns dict of inputs."""

    inputs_lines = [line.strip() for line in open(inputs_file, "r").readlines()]
    inputs_lines = [line for line in inputs_lines if line and not line.startswith("#")]
    cur_group = None
    i = 0
    group_prefix = "%s:" % groupping_symbol
    input_prefixes = ["%s:" % input_part for input_part in input_parts]

    groups = {}
    while i < len(inputs_lines):
        line = inputs_lines[i]
        if line.startswith(group_prefix):
            # Start new group
            cur_group = line[len(group_prefix):]
            i += 1
        elif line.startswith(input_prefixes[0]):
            input = []
            for j, input_prefix in enumerate(input_prefixes):
                part_line = inputs_lines[i + j]
                part = part_line[len(input_prefixes[j]):]
                input.append(part)
            if cur_group not in groups:
                groups[cur_group] = []
            groups[cur_group].append(input)
            i += len(input_prefixes)
        else:
            # Skip empty line
            i += 1
    return groups
