"""Behavior checks for authored practice and its explicit coverage boundary."""

import sys
import unicodedata
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from english_friend import coach, scenarios


class CoachTests(unittest.TestCase):
    def test_scenarios_have_usable_examples_and_are_independent(self):
        choices = scenarios()
        self.assertEqual({choice["id"] for choice in choices}, {"everyday", "work", "travel"})
        for choice in choices:
            self.assertTrue(choice["title"])
            self.assertTrue(choice["description"])
            self.assertTrue(choice["starter"])
            for text in choice["example_inputs"]:
                with self.subTest(scenario=choice["id"], text=text):
                    self.assertTrue(coach(text, choice["id"])["supported"])
        choices[0]["example_inputs"].clear()
        self.assertTrue(scenarios()[0]["example_inputs"])

    def test_correction_then_accepted_retry_preserves_past_meaning(self):
        feedback = coach("Yesterday I go market.")
        self.assertEqual(feedback["kind"], "correction")
        self.assertEqual(feedback["suggestions"], ["I went to the market yesterday."])
        self.assertIn("past", feedback["explanation"])
        retry = coach(feedback["suggestions"][0])
        self.assertEqual(retry["kind"], "accepted")
        self.assertEqual(retry["suggestions"], [])
        self.assertEqual(retry["engine"], "offline_practice")

    def test_bangla_and_transliteration_keep_same_intention(self):
        expected = "I want to speak English, but I feel embarrassed when I make mistakes."
        for phrase in (
            "আমি ইংরেজিতে কথা বলতে চাই, কিন্তু ভুল করলে লজ্জা লাগে।",
            "Ami ingrejite kotha bolte chai, kintu bhul korle lojja lage.",
        ):
            with self.subTest(phrase=phrase):
                feedback = coach(phrase)
                self.assertEqual(feedback["kind"], "translation")
                self.assertIn(expected, feedback["suggestions"])
                self.assertNotIn("I can't speak English.", feedback["suggestions"])

    def test_code_switching_offers_context_specific_authored_phrase(self):
        feedback = coach("Today office-e amar presentation ache, I am little tension.", "work")
        self.assertEqual(feedback["kind"], "translation")
        self.assertEqual(feedback["suggestions"], [
            "I have a presentation at work today, and I'm a little nervous."
        ])

    def test_valid_english_variants_are_not_marked_wrong(self):
        for phrase in ("I've got two brothers.", "I have two brothers.", "I’ve got two brothers."):
            with self.subTest(phrase=phrase):
                feedback = coach(phrase)
                self.assertEqual(feedback["kind"], "accepted")
                self.assertEqual(feedback["suggestions"], [])

    def test_ambiguous_time_requests_clarification_without_guessing(self):
        feedback = coach("I am coming tomorrow yesterday.")
        self.assertEqual(feedback["kind"], "clarification")
        self.assertEqual(feedback["suggestions"], [])
        self.assertIn("yesterday", feedback["next_question"])
        self.assertIn("tomorrow", feedback["next_question"])

    def test_unknown_input_does_not_invent_or_echo_a_correction(self):
        for phrase in ("I has seven umbrella.", "তুমি কেমন আছ?", "<script>alert(1)</script>", "", "   "):
            with self.subTest(phrase=phrase):
                feedback = coach(phrase)
                self.assertEqual(feedback["kind"], "unsupported")
                self.assertFalse(feedback["supported"])
                self.assertEqual(feedback["suggestions"], [])
                self.assertIn("not been assessed as right or wrong", feedback["explanation"])
                self.assertNotIn("<script>", str(feedback))

    def test_normalization_preserves_coverage_boundaries(self):
        self.assertEqual(coach(" \tYESTERDAY\nI  GO MARKET.  "), coach("Yesterday I go market."))
        bangla = "আমি কাজটা শেষ করেছি।"
        self.assertEqual(coach(unicodedata.normalize("NFD", bangla), "work"), coach(bangla, "work"))
        # Punctuation and extra words change the authored input, so ask for a supported example.
        self.assertEqual(coach("Yesterday I go market!!!")["kind"], "unsupported")
        self.assertEqual(coach("Yesterday I go market with my sister.")["kind"], "unsupported")

    def test_scenarios_do_not_claim_other_contexts_are_supported(self):
        self.assertEqual(coach("Where is train station?", "travel")["kind"], "correction")
        self.assertEqual(coach("Where is train station?", "everyday")["kind"], "unsupported")

    def test_invalid_scenario_and_non_text_are_rejected(self):
        with self.assertRaises(ValueError):
            coach("Hello", "unknown")
        with self.assertRaises(TypeError):
            coach(None)

    def test_mutating_result_cannot_change_later_feedback(self):
        first = coach("I am agree.")
        first["suggestions"].append("unwanted mutation")
        self.assertEqual(coach("I am agree.")["suggestions"], ["I agree."])


if __name__ == "__main__":
    unittest.main()
