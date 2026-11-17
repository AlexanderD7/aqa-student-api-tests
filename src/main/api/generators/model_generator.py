import random
import uuid
from typing import Annotated, Any, Literal, get_args, get_origin, get_type_hints

import exrex

from src.main.api.generators.generator_number import CreationRule


class RandomModelGenerator:
    @staticmethod
    def generate(cls: type) -> Any:
        type_hints = get_type_hints(cls, include_extras=True)
        init_data: dict[str, Any] = {}

        for field_name, annotated_type in type_hints.items():
            actual_type = annotated_type
            rule: CreationRule | None = None

            if get_origin(annotated_type) is Annotated:
                actual_type, *annotations = get_args(annotated_type)
                for ann in annotations:
                    if isinstance(ann, CreationRule):
                        rule = ann

            if rule is not None:
                init_data[field_name] = RandomModelGenerator._generate_from_regex(rule, actual_type)
            else:
                init_data[field_name] = RandomModelGenerator._generate_value(actual_type)

        return cls(**init_data)

    @staticmethod
    def _generate_from_regex(rule: CreationRule, field_type: type) -> Any:
        generated = exrex.getone(rule.regex)
        if field_type is int:
            return int(generated)
        if field_type is float:
            return float(generated)
        return generated

    @staticmethod
    def _generate_value(field_type: type) -> Any:
        origin = get_origin(field_type)

        if origin is not None and type(None) in get_args(field_type):
            non_none = [a for a in get_args(field_type) if a is not type(None)]
            field_type = non_none[0] if non_none else str
            origin = get_origin(field_type)

        if origin is Literal:
            return random.choice(get_args(field_type))

        if field_type is str:
            return str(uuid.uuid4())[:8]
        if field_type is int:
            return random.randint(1, 9999)
        if field_type is float:
            return round(random.uniform(0, 100.0), 2)
        if field_type is bool:
            return random.choice([True, False])
        if isinstance(field_type, type):
            try:
                return RandomModelGenerator.generate(field_type)
            except Exception:
                return None
        return None