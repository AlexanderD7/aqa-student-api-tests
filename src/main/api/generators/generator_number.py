from dataclasses import dataclass
import exrex

@dataclass
class CreationRule:
    regex: str

def generate_by_regex(rule: CreationRule) -> str:
    return exrex.getone(rule.regex)