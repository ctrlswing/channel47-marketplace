#!/usr/bin/env python3
"""
Awareness Level Checker

Helps determine the Schwartz awareness level of a target audience
based on their description and market context.

Usage:
    python awareness_check.py "Description of target audience"
    python awareness_check.py --interactive
"""

import argparse
import json
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class AwarenessAssessment:
    """Assessment of audience awareness level."""
    level: int
    level_name: str
    confidence: str  # high, medium, low
    reasoning: List[str]
    recommended_lead_type: str
    proof_requirements: str
    example_opening: str


# Question frameworks for assessing awareness
AWARENESS_QUESTIONS = {
    'product_knowledge': {
        'question': 'Does the audience know your specific product exists?',
        'yes_indicates': 1,  # Most aware or product aware
        'no_indicates': 3    # Solution aware or lower
    },
    'solution_awareness': {
        'question': 'Does the audience know solutions to their problem exist?',
        'yes_indicates': 3,  # Solution aware
        'no_indicates': 4    # Problem aware
    },
    'problem_awareness': {
        'question': 'Does the audience actively recognize they have a problem?',
        'yes_indicates': 4,  # Problem aware
        'no_indicates': 5    # Unaware
    },
    'purchase_intent': {
        'question': 'Is the audience actively shopping/comparing options?',
        'yes_indicates': 2,  # Product aware
        'no_indicates': 3    # Solution aware or lower
    },
    'previous_purchase': {
        'question': 'Has the audience bought from you before?',
        'yes_indicates': 1,  # Most aware
        'no_indicates': 2    # Product aware or lower
    }
}

LEVEL_DETAILS = {
    1: {
        'name': 'Most Aware',
        'description': 'They know your product and are ready to buy',
        'lead_type': 'Offer Lead - Jump straight to the deal',
        'proof_requirements': 'Minimal - they already trust you',
        'example_opening': 'For the next 48 hours only: Get [Product] at our lowest price ever...'
    },
    2: {
        'name': 'Product Aware',
        'description': 'They know your product but need convincing',
        'lead_type': 'Differentiation Lead - Why you\'re the best choice',
        'proof_requirements': 'Heavy - they\'re comparing options',
        'example_opening': 'What makes [Product] different from everything else you\'ve tried...'
    },
    3: {
        'name': 'Solution Aware',
        'description': 'They know solutions exist but don\'t know your product',
        'lead_type': 'Mechanism Lead - Your unique approach',
        'proof_requirements': 'Moderate - establish credibility for your method',
        'example_opening': 'A new approach to [problem] that works differently from anything you\'ve seen...'
    },
    4: {
        'name': 'Problem Aware',
        'description': 'They feel the pain but don\'t know solutions exist',
        'lead_type': 'Problem/Empathy Lead - Show you understand',
        'proof_requirements': 'Gradual - build belief step by step',
        'example_opening': 'If you\'ve ever woken up at 3am worrying about [problem]...'
    },
    5: {
        'name': 'Unaware',
        'description': 'They don\'t even know they have a problem',
        'lead_type': 'Story/Curiosity Lead - Capture attention first',
        'proof_requirements': 'Build slowly - you\'re educating them',
        'example_opening': '[Name] wasn\'t looking for a solution. She didn\'t know she needed one...'
    }
}


def assess_awareness_from_description(description: str) -> AwarenessAssessment:
    """
    Estimate awareness level from audience description.

    This uses keyword matching as a heuristic. In practice,
    the interactive mode or human judgment is more accurate.
    """
    desc_lower = description.lower()
    reasoning = []
    score = 3  # Default to middle level

    # Check for high awareness indicators
    if any(word in desc_lower for word in ['existing customer', 'subscriber', 'returning', 'bought before']):
        score = 1
        reasoning.append("Audience has previous relationship with brand")
    elif any(word in desc_lower for word in ['comparing', 'shopping', 'evaluating', 'looking for', 'searching']):
        score = 2
        reasoning.append("Audience is actively shopping/comparing")
    elif any(word in desc_lower for word in ['heard of', 'knows about', 'aware of solutions']):
        score = 3
        reasoning.append("Audience knows solutions exist")
    elif any(word in desc_lower for word in ['struggling', 'frustrated', 'problem', 'issue', 'pain']):
        score = 4
        reasoning.append("Audience is experiencing pain but may not know solutions")
    elif any(word in desc_lower for word in ['cold', 'unaware', 'doesn\'t know', 'general audience', 'broad']):
        score = 5
        reasoning.append("Audience may not be aware of the problem")
    else:
        reasoning.append("Limited indicators - defaulting to middle level")

    level_info = LEVEL_DETAILS[score]

    return AwarenessAssessment(
        level=score,
        level_name=level_info['name'],
        confidence='medium',
        reasoning=reasoning,
        recommended_lead_type=level_info['lead_type'],
        proof_requirements=level_info['proof_requirements'],
        example_opening=level_info['example_opening']
    )


def interactive_assessment() -> AwarenessAssessment:
    """Run interactive Q&A to determine awareness level."""
    print("\n" + "=" * 50)
    print("AWARENESS LEVEL ASSESSMENT")
    print("Answer the following questions about your audience")
    print("=" * 50 + "\n")

    responses = {}
    reasoning = []

    # Previous purchase
    print("1. Has this audience bought from you before?")
    print("   (y/n): ", end="")
    responses['previous_purchase'] = input().strip().lower() == 'y'

    if responses['previous_purchase']:
        reasoning.append("Previous customers = Most Aware")
        level = 1
    else:
        # Product knowledge
        print("\n2. Does this audience know your specific product exists?")
        print("   (y/n): ", end="")
        responses['product_knowledge'] = input().strip().lower() == 'y'

        if responses['product_knowledge']:
            # Purchase intent
            print("\n3. Are they actively shopping or comparing options?")
            print("   (y/n): ", end="")
            responses['purchase_intent'] = input().strip().lower() == 'y'

            if responses['purchase_intent']:
                reasoning.append("Know product + actively shopping = Product Aware")
                level = 2
            else:
                reasoning.append("Know product but not actively shopping = Product Aware (lower)")
                level = 2
        else:
            # Solution awareness
            print("\n3. Do they know that solutions to their problem exist?")
            print("   (y/n): ", end="")
            responses['solution_awareness'] = input().strip().lower() == 'y'

            if responses['solution_awareness']:
                reasoning.append("Know solutions exist but not your product = Solution Aware")
                level = 3
            else:
                # Problem awareness
                print("\n4. Do they actively recognize they have a problem?")
                print("   (y/n): ", end="")
                responses['problem_awareness'] = input().strip().lower() == 'y'

                if responses['problem_awareness']:
                    reasoning.append("Recognize problem but don't know solutions = Problem Aware")
                    level = 4
                else:
                    reasoning.append("Don't recognize the problem = Unaware")
                    level = 5

    level_info = LEVEL_DETAILS[level]

    return AwarenessAssessment(
        level=level,
        level_name=level_info['name'],
        confidence='high',
        reasoning=reasoning,
        recommended_lead_type=level_info['lead_type'],
        proof_requirements=level_info['proof_requirements'],
        example_opening=level_info['example_opening']
    )


def format_assessment(assessment: AwarenessAssessment) -> str:
    """Format assessment for display."""
    output = []
    output.append("\n" + "=" * 50)
    output.append("AWARENESS LEVEL ASSESSMENT RESULTS")
    output.append("=" * 50)

    output.append(f"\n🎯 LEVEL: {assessment.level} - {assessment.level_name}")
    output.append(f"   Confidence: {assessment.confidence}")

    output.append("\n📝 REASONING:")
    for reason in assessment.reasoning:
        output.append(f"   • {reason}")

    output.append(f"\n📣 RECOMMENDED LEAD TYPE:")
    output.append(f"   {assessment.recommended_lead_type}")

    output.append(f"\n📊 PROOF REQUIREMENTS:")
    output.append(f"   {assessment.proof_requirements}")

    output.append(f"\n✍️ EXAMPLE OPENING:")
    output.append(f"   \"{assessment.example_opening}\"")

    output.append("\n" + "=" * 50)

    # Add all levels for reference
    output.append("\n📚 ALL AWARENESS LEVELS (for reference):")
    for lvl, info in LEVEL_DETAILS.items():
        marker = "→ " if lvl == assessment.level else "  "
        output.append(f"{marker}Level {lvl}: {info['name']}")
        output.append(f"     {info['description']}")

    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description='Assess audience awareness level')
    parser.add_argument('description', nargs='?', help='Description of target audience')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run interactive Q&A assessment')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if args.interactive:
        assessment = interactive_assessment()
    elif args.description:
        assessment = assess_awareness_from_description(args.description)
    else:
        print("Error: Provide audience description or use --interactive flag")
        print("Example: python awareness_check.py 'Cold email leads who have never heard of us'")
        return

    if args.json:
        print(json.dumps(asdict(assessment), indent=2))
    else:
        print(format_assessment(assessment))


if __name__ == '__main__':
    main()
