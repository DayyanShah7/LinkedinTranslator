def build_prompt(user_text: str, mode: str = "linkedin_cringe") -> str:
    mode_instructions = {
        "linkedin_cringe": (
            "Rewrite the input as a dramatic LinkedIn post. "
            "Make it reflective, slightly exaggerated, and inspirational. "
            "Use expressive language, storytelling, and include 2-4 relevant emojis. "
            "End with 2-4 hashtags."
        ),

        "ultra_cringe": (
            "Rewrite the input as the MOST exaggerated LinkedIn post possible. "
            "Make it extremely dramatic, emotional, and deeply reflective. "
            "Turn even a simple event into a life-changing journey of growth, resilience, and leadership. "
            "Use storytelling, strong emotional language, and corporate tone. "
            "Include 4-8 expressive emojis throughout the text (not just at the end). "
            "Break into short paragraphs like real LinkedIn posts. "
            "End with 3-6 powerful hashtags."
        ),

        "ceo_mode": (
            "Rewrite the input as if a visionary CEO is sharing it on LinkedIn. "
            "Make it bold, confident, and leadership-focused. "
            "Use strong language, ambition, and include 2-3 subtle emojis. "
            "End with 2-4 hashtags."
        ),

        "humble_brag": (
            "Rewrite the input as a classic LinkedIn humble brag. "
            "Sound grateful and reflective while subtly highlighting achievement. "
            "Include 2-3 emojis and 2-4 hashtags."
        ),

        "thought_leader": (
            "Rewrite the input like a deep LinkedIn thought leader post. "
            "Turn it into a lesson about life, mindset, or growth. "
            "Use reflective tone, storytelling, and include 2-4 emojis. "
            "End with 2-4 hashtags."
        ),

        "de_linkedin": (
            "Rewrite the input into simple, normal everyday English. "
            "Remove all exaggeration, emojis, and corporate tone. "
            "Keep it casual and direct."
        )
    }

    instruction = mode_instructions.get(mode, mode_instructions["linkedin_cringe"])

    return f"""
You are an expert LinkedIn content creator who specializes in exaggerated, emotional, and engaging storytelling.

Task:
{instruction}

Rules:
- Make it sound like a real viral LinkedIn post.
- Use natural line breaks (short paragraphs).
- Be expressive but still readable.
- Do NOT use quotation marks.
- Do NOT explain anything.
- Just return the final post.

Input:
{user_text}
""".strip()