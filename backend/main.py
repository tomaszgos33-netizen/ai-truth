def analyze_text(text: str) -> dict:
    length = len(text)

    if length < 50:
        verdict = "Human"
    elif length < 200:
        verdict = "Mixed"
    else:
        verdict = "AI"

    return {
        "verdict": verdict,
        "confidence": min(90, length // 5)
    }


if __name__ == "__main__":
    sample = "This is a sample text generated for analysis."
    print(analyze_text(sample))