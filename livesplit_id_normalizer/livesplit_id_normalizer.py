import xml.etree.ElementTree as ET


def normalize(path, initial_run=None):
    tree = ET.parse(path)
    # TODO read the minimum id from runs OR take passed in arg
    if not initial_run:
        # parse initial run
        pass
    pass
