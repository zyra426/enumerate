def find_and_replace(lines):
    name_err = "Kladin"
    actual_name = "Kaladin"
    found = 0
    log = []
    
    for linenum, line in enumerate(lines, start=1):
        if name_err in line:
            lines[linenum - 1] = line.replace(name_err, actual_name)
            found += 1

        if linenum % 3 == 0:
            log.append(update_log(linenum, found))
    
    print(lines)
    return log


# don't touch below this line


def update_log(linenum, found):
    return f"lines checked: {linenum}, errors found and corrected: {found}"
