"""Match a small authored practice set without guessing grammar or intent.

There is no model, network request, speech assessment, or general translation.
All language feedback comes from lessons.json. Unknown phrases are explicitly
unsupported. HTTP validation, retention, and correction timing belong upstream.
"""

import json
import unicodedata
from functools import lru_cache
from importlib.resources import files


def _normalize(text: str) -> str:
    """Normalize canonical Unicode, case and whitespace; keep punctuation."""
    return " ".join(unicodedata.normalize("NFC", text).casefold().split())


@lru_cache(maxsize=1)
def _content() -> dict:
    return json.loads(files(__package__).joinpath("lessons.json").read_text(encoding="utf-8"))


def scenarios() -> list[dict]:
    """Return independent public scenario descriptions and supported inputs."""
    return [
        {**scenario, "example_inputs": list(scenario["example_inputs"])}
        for scenario in _content()["scenarios"]
    ]


def _result(kind: str, suggestions: list[str], explanation: str, reply: str,
            next_question: str, *, supported: bool = True) -> dict:
    return {
        "kind": kind,
        "suggestions": list(suggestions),
        "explanation": explanation,
        "reply": reply,
        "next_question": next_question,
        "engine": "offline_practice",
        "supported": supported,
    }


def coach(text: str, scenario_id: str = "everyday") -> dict:
    """Return authored feedback for a known phrase or an honest fallback.

    The match is scenario-scoped. A suggested English phrase is accepted on a
    retry in the same scenario. This recognizes practice completion, not general
    English proficiency. Invalid scenarios raise ValueError; non-text input
    raises TypeError. Original text is intentionally left to the HTTP layer.
    """
    content = _content()
    scenario = next((s for s in content["scenarios"] if s["id"] == scenario_id), None)
    if scenario is None:
        raise ValueError(f"Unknown scenario: {scenario_id}")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    normalized = _normalize(text)

    lessons = [lesson for lesson in content["lessons"] if lesson["scenario_id"] == scenario_id]
    for lesson in lessons:
        if normalized in {_normalize(phrase) for phrase in lesson["inputs"]}:
            return _result(
                lesson["kind"], lesson["suggestions"], lesson["explanation"],
                lesson["reply"], lesson["next_question"],
            )

    for lesson in lessons:
        if normalized in {_normalize(phrase) for phrase in lesson["suggestions"]}:
            return _result(
                "accepted", [],
                "That matches an English phrase in this authored practice set.",
                "That phrase expresses the meaning from this practice example.",
                lesson["next_question"],
            )

    return _result(
        "unsupported", [],
        "I can only help with the listed phrases. This input has not been assessed "
        "as right or wrong; I cannot infer a correction or translation.",
        "This is limited offline phrase practice, not a general AI English tutor.",
        f"Try a supported example: {scenario['example_inputs'][0]}",
        supported=False,
    )
