#!/usr/bin/python
from constants import ( TOTAL_KANJI, TO_STUDY_FILE, STUDIED_FILE )

import file_handler


# PUBLIC
def validate_study_files():
    """ Ensure `to_study` and `studied` files are valid """

    # 1. Check for missing files. If so, re-create them before continuing
    missing_files = _get_missing_files()
    if len(missing_files) > 0:
        file_handler.generate_missing_files(missing_files)
    
    # [to_study, studied]
    study_files = file_handler.get_study_files()

    # Clean the indices: remove out-of-range indices and duplicates
    for idx, indices in enumerate(study_files):
        # 2. Remove out-of-range indices
        filtered_indices = filter(lambda x: x > 0 and x <= TOTAL_KANJI, indices)

        # 3. Remove duplicate indices within the same file
        unique_indices = set(filtered_indices)

        # Store updated indices in `study_files` tuple
        study_files[idx] = unique_indices

    to_study_set, studied_set = study_files
    file_handler.create_json_file(TO_STUDY_FILE, list(to_study_set))
    # If sum of indices in both files doesn't equal TOTAL_KANJI, something is wrong
    if len(to_study_set) + len(studied_set) != TOTAL_KANJI:
        # Regenerate files using `to_study` indices
        return file_handler.generate_missing_files([STUDIED_FILE])
    
    # Unique indices for both files should add up to TOTAL_KANJI
    # Make sure there are no duplicates (index present in both files)
    for idx in to_study_set:
        # If duplicate is present, re-generate files using `to_study` indices
        if idx in studied_set:
            return file_handler.generate_missing_files([STUDIED_FILE])
    
    file_handler.create_json_file(STUDIED_FILE, list(studied_set))


# PRIVATE
def _get_missing_files():
    """ Check if study files exist. Return a List containing the names of the files that don't exist """
    not_found_files = []

    for file_name in [TO_STUDY_FILE, STUDIED_FILE]:
        try:
            f = open(file_name)
            f.close()
        except FileNotFoundError:
            not_found_files.append(file_name)

    return not_found_files


def _has_out_of_range_indices(indices):
    """ Check if indices are less than 0 or greater than `TOTAL_KANJI` """

    for idx in indices:
        if idx < 0 or idx > TOTAL_KANJI:
            return True
    
    return False


def _has_unique_indices(indices):
    unique_indices = list(set(indices))
    
    return len(indices) == len(unique_indices)