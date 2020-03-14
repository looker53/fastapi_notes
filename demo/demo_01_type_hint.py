from typing import List

def loop(item:List[str]):
    for i in item:
        i.lower()

def full_name(family_name: str, last_name: int):
    return family_name + last_name