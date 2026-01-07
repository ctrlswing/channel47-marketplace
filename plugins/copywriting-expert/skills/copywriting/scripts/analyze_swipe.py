#!/usr/bin/env python3
"""
Swipe File Analyzer

Deconstructs copy into its component parts for analysis and learning.
Returns structured analysis that can be used for pattern recognition.

Usage:
    python analyze_swipe.py "Copy text to analyze"
    python analyze_swipe.py --file /path/to/copy.txt
"""

import argparse
import re
import json
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class SwipeAnalysis:
    """Structured analysis of a piece of copy."""

    # Basic metrics
    word_count: int
    sentence_count: int
    avg_sentence_length: float
    paragraph_count: int

    # Structure detection
    has_headline: bool
    headline_text: Optional[str]
    has_subheadline: bool
    has_ps: bool
    ps_text: Optional[str]

    # Content markers
    question_count: int
    exclamation_count: int
    you_count: int
    power_words_found: List[str]
    proof_indicators: List[str]
    urgency_indicators: List[str]

    # Estimated attributes
    estimated_awareness_level: int
    estimated_formality: str
    has_story_elements: bool
    has_testimonial_indicators: bool


# Power words commonly used in effective copy
POWER_WORDS = [
    'free', 'new', 'now', 'proven', 'secret', 'discover', 'instant',
    'easy', 'guaranteed', 'results', 'powerful', 'exclusive', 'limited',
    'breakthrough', 'revolutionary', 'transform', 'finally', 'imagine',
    'revealed', 'announcing', 'introducing', 'warning', 'urgent'
]

# Proof indicators
PROOF_INDICATORS = [
    'percent', '%', 'study', 'research', 'according to', 'statistic',
    'data', 'survey', 'scientist', 'doctor', 'expert', 'testimonial',
    'customer', 'client', 'case study', 'guarantee', 'risk-free',
    'money back', 'review', 'rating', 'star', 'verified'
]

# Urgency indicators
URGENCY_INDICATORS = [
    'now', 'today', 'limited', 'hurry', 'expires', 'deadline', 'last chance',
    'only', 'remaining', 'before', 'ends', 'closing', 'final', 'immediate',
    'act now', 'don\'t wait', 'running out', 'while supplies last'
]

# Story indicators
STORY_INDICATORS = [
    'once upon', 'story', 'happened', 'remember when', 'years ago',
    'let me tell you', 'imagine', 'picture this', 'one day', 'suddenly',
    'then', 'before', 'after', 'journey', 'discovered', 'realized'
]


def count_sentences(text: str) -> int:
    """Count sentences in text."""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def find_power_words(text: str) -> List[str]:
    """Find power words in text."""
    text_lower = text.lower()
    found = []
    for word in POWER_WORDS:
        if word in text_lower:
            found.append(word)
    return found


def find_indicators(text: str, indicator_list: List[str]) -> List[str]:
    """Find indicators from a list in text."""
    text_lower = text.lower()
    found = []
    for indicator in indicator_list:
        if indicator in text_lower:
            found.append(indicator)
    return found


def estimate_awareness_level(text: str) -> int:
    """
    Estimate the Schwartz awareness level the copy is targeting.

    1 = Most aware (offer-focused)
    2 = Product aware (differentiation-focused)
    3 = Solution aware (mechanism-focused)
    4 = Problem aware (pain-focused)
    5 = Unaware (story/curiosity-focused)
    """
    text_lower = text.lower()

    # Check for offer-heavy language (Level 1)
    offer_words = ['discount', 'price', 'buy now', 'order', 'sale', 'off', 'deal']
    offer_count = sum(1 for word in offer_words if word in text_lower)

    # Check for differentiation language (Level 2)
    diff_words = ['unlike', 'different', 'better than', 'compared to', 'only we']
    diff_count = sum(1 for word in diff_words if word in text_lower)

    # Check for mechanism language (Level 3)
    mech_words = ['how it works', 'method', 'system', 'approach', 'process', 'technique']
    mech_count = sum(1 for word in mech_words if word in text_lower)

    # Check for problem language (Level 4)
    prob_words = ['frustrated', 'struggling', 'tired of', 'sick of', 'problem', 'pain']
    prob_count = sum(1 for word in prob_words if word in text_lower)

    # Check for story language (Level 5)
    story_count = len(find_indicators(text, STORY_INDICATORS))

    # Weight and determine level
    scores = [offer_count, diff_count, mech_count, prob_count, story_count]
    max_score = max(scores)

    if max_score == 0:
        return 3  # Default to middle

    # Return the level with highest score (1-indexed)
    return scores.index(max_score) + 1


def estimate_formality(text: str) -> str:
    """Estimate the formality level of the copy."""
    informal_markers = ['hey', 'gonna', 'wanna', "don't", "can't", 'awesome', 'cool']
    formal_markers = ['therefore', 'furthermore', 'subsequently', 'hereby', 'pursuant']

    text_lower = text.lower()
    informal_count = sum(1 for word in informal_markers if word in text_lower)
    formal_count = sum(1 for word in formal_markers if word in text_lower)

    if informal_count > formal_count + 2:
        return 'casual'
    elif formal_count > informal_count + 2:
        return 'formal'
    else:
        return 'conversational'


def extract_headline(text: str) -> Optional[str]:
    """Try to extract the headline from copy."""
    lines = text.strip().split('\n')
    if lines:
        first_line = lines[0].strip()
        # Headlines are typically short and may be all caps or have special formatting
        if len(first_line) < 150:
            return first_line
    return None


def extract_ps(text: str) -> Optional[str]:
    """Extract P.S. section if present."""
    ps_match = re.search(r'P\.?S\.?:?\s*(.*?)(?:\n\n|$)', text, re.IGNORECASE | re.DOTALL)
    if ps_match:
        return ps_match.group(1).strip()[:200]
    return None


def analyze_copy(text: str) -> SwipeAnalysis:
    """Perform full analysis of copy."""

    # Basic counts
    words = text.split()
    word_count = len(words)
    sentence_count = count_sentences(text)
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)

    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0

    # Structure detection
    headline = extract_headline(text)
    ps_text = extract_ps(text)

    lines = text.strip().split('\n')
    has_subheadline = len(lines) > 1 and len(lines[1].strip()) < 200

    # Content markers
    question_count = text.count('?')
    exclamation_count = text.count('!')
    you_count = text.lower().count(' you ')

    power_words = find_power_words(text)
    proof_indicators = find_indicators(text, PROOF_INDICATORS)
    urgency_indicators = find_indicators(text, URGENCY_INDICATORS)

    # Estimations
    awareness_level = estimate_awareness_level(text)
    formality = estimate_formality(text)
    has_story = len(find_indicators(text, STORY_INDICATORS)) > 2
    has_testimonial = 'said' in text.lower() or '"' in text or "'" in text

    return SwipeAnalysis(
        word_count=word_count,
        sentence_count=sentence_count,
        avg_sentence_length=round(avg_sentence_length, 1),
        paragraph_count=paragraph_count,
        has_headline=headline is not None,
        headline_text=headline,
        has_subheadline=has_subheadline,
        has_ps=ps_text is not None,
        ps_text=ps_text,
        question_count=question_count,
        exclamation_count=exclamation_count,
        you_count=you_count,
        power_words_found=power_words,
        proof_indicators=proof_indicators,
        urgency_indicators=urgency_indicators,
        estimated_awareness_level=awareness_level,
        estimated_formality=formality,
        has_story_elements=has_story,
        has_testimonial_indicators=has_testimonial
    )


def format_analysis(analysis: SwipeAnalysis) -> str:
    """Format analysis for display."""
    output = []
    output.append("=" * 50)
    output.append("SWIPE FILE ANALYSIS")
    output.append("=" * 50)

    output.append("\n📊 BASIC METRICS")
    output.append(f"  Words: {analysis.word_count}")
    output.append(f"  Sentences: {analysis.sentence_count}")
    output.append(f"  Avg sentence length: {analysis.avg_sentence_length} words")
    output.append(f"  Paragraphs: {analysis.paragraph_count}")

    output.append("\n📋 STRUCTURE")
    output.append(f"  Has headline: {'✓' if analysis.has_headline else '✗'}")
    if analysis.headline_text:
        output.append(f"    → \"{analysis.headline_text[:50]}...\"" if len(analysis.headline_text) > 50 else f"    → \"{analysis.headline_text}\"")
    output.append(f"  Has subheadline: {'✓' if analysis.has_subheadline else '✗'}")
    output.append(f"  Has P.S.: {'✓' if analysis.has_ps else '✗'}")

    output.append("\n🎯 ENGAGEMENT MARKERS")
    output.append(f"  Questions: {analysis.question_count}")
    output.append(f"  Exclamations: {analysis.exclamation_count}")
    output.append(f"  'You' count: {analysis.you_count}")

    output.append("\n💪 POWER WORDS FOUND")
    output.append(f"  {', '.join(analysis.power_words_found) if analysis.power_words_found else 'None detected'}")

    output.append("\n📈 PROOF INDICATORS")
    output.append(f"  {', '.join(analysis.proof_indicators) if analysis.proof_indicators else 'None detected'}")

    output.append("\n⏰ URGENCY INDICATORS")
    output.append(f"  {', '.join(analysis.urgency_indicators) if analysis.urgency_indicators else 'None detected'}")

    awareness_labels = {
        1: "Most Aware (Offer-focused)",
        2: "Product Aware (Differentiation)",
        3: "Solution Aware (Mechanism)",
        4: "Problem Aware (Pain-focused)",
        5: "Unaware (Story-driven)"
    }

    output.append("\n🎭 ESTIMATED ATTRIBUTES")
    output.append(f"  Awareness level: {analysis.estimated_awareness_level} - {awareness_labels[analysis.estimated_awareness_level]}")
    output.append(f"  Formality: {analysis.estimated_formality}")
    output.append(f"  Story elements: {'✓' if analysis.has_story_elements else '✗'}")
    output.append(f"  Testimonial indicators: {'✓' if analysis.has_testimonial_indicators else '✗'}")

    output.append("\n" + "=" * 50)

    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description='Analyze copy structure and elements')
    parser.add_argument('text', nargs='?', help='Copy text to analyze')
    parser.add_argument('--file', '-f', help='Path to file containing copy')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    # Get the text to analyze
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Error: Provide copy text or use --file flag")
        return

    # Analyze
    analysis = analyze_copy(text)

    # Output
    if args.json:
        print(json.dumps(asdict(analysis), indent=2))
    else:
        print(format_analysis(analysis))


if __name__ == '__main__':
    main()
