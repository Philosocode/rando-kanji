#!/usr/bin/python
import json
import os
import pickle

from constants import *


# PUBLIC
def create_kanji_dict():
    kanji_lines = _get_lines_from_file(KANJI_DATA_FILE)
    kanji_dict = {}

    for line in kanji_lines:
        split_line = line.split(":")
        idx, kanji, meaning, *rest = split_line

        kanji_dict[kanji] = { 
            "index": int(idx), 
            "meaning": meaning, 
            "studied": False 
        }
    
    return kanji_dict


def get_kanji_dict():
    if not _file_exists(KANJI_DICT_FILE):
        print("Kanji data not found. Creating kanji dict.")
        kanji_dict = create_kanji_dict()
        save(kanji_dict)
    
    return _load_json_file(KANJI_DICT_FILE)


def save(kanji_dict):
    _create_json_file(KANJI_DICT_FILE, kanji_dict)
    print("Data saved.")


# PRIVATE
def _file_exists(file_name):
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        return False

    return True


def _get_lines_from_file(file_name):
    with open(file_name, "r") as f:
        return [line.rstrip("\n") for line in f]


def _create_json_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"SAVED: {file_name}.")


def _load_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)