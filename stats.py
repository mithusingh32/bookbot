from typing import Dict, List

def get_num_words(string: str) -> str:
    return f"Found {len(string.split())} total words"

def get_of_char_appear(string: str) -> Dict[str, int]:
    result = {}
    for char in string.lower():
        if not char in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def sort_on(dict: Dict[str, int]):
    return dict['num']

def get_sorted_dict_as_list(dictionary: Dict[str, int]) -> List[Dict[str, int]]:
    result = []
    for key, value in dictionary.items():
        result.append({
            'char': key,
            'num': value
        })
    result.sort(reverse=True, key=sort_on)
    return result