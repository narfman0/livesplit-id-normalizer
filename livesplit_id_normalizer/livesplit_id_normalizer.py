import xml.etree.ElementTree as ET


def normalize(path, initial_run=None):
    root = parse_tree(path)
    if not initial_run:
        initial_run = find_initial_run(root)
    update_run(root, path, initial_run)


def find_initial_run(root):
    """ Scan all attempts in run to find lowest id """
    initial_run = None
    for item in root.findall("AttemptHistory/Attempt"):
        current_run = int(item.attrib["id"])
        if initial_run == None or current_run < initial_run:
            initial_run = current_run
    return initial_run


def parse_tree(path):
    """ Parse path to return root node """
    return ET.parse(path).getroot()


def update_run(root, path, initial_run):
    """ Update the splits file with path to subtract initial_run
    from id """
    # TODO update xml to change all id references
    pass
