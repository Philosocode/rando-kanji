import json
from constants import TO_STUDY_FILE, STUDIED_FILE

#!/usr/bin/python
def check_files_exist(*file_names):
    """ 
    DESC: Check if the file(s) passed exist.
    RETURN: List containing files that don't exist
    """
    not_found = []

    for file_name in file_names:
        try:
            f = open(file_name)
            f.close()
        except FileNotFoundError:
            not_found.append(file_name)

    return not_found


def create_study_files():
    """ Create to_study & studied JSON files """
    kanji_indices = _create_kanji_indices()
    _create_json_file(TO_STUDY_FILE, kanji_indices)
    _create_json_file(STUDIED_FILE, [])


def generate_missing_file(missing_file_name):
    """ Use `to_study` file to generate `studied` (and vice versa)"""
    
    if missing_file_name == TO_STUDY_FILE
        with open(TO_STUDY_FILE, "w", encoding="utf-8") as f:
            kanji_indices = _create_kanji_indices()
    
    if missing_file_name == STUDIED_FILE:
        pass


def _create_json_file(file_name, data):
    """ Create a JSON file with data passed """
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _create_kanji_indices():
    """ Return a list with the numbers 1 to 2200"""
    return list(range(1, 2200 + 1))
