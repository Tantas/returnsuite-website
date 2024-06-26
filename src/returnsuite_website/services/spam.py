def detected_spam(comment: str | None) -> bool:
    """
    Returns true when any keywords associated with spam are found in the comment.
    """
    if not comment or not comment.strip():
        return False

    lower = comment.lower()

    # Remove if fewer than two words.
    if len(lower.split(" ")) < 2:
        return True

    # Domain name is commonly entered in spam messages.
    if "returnsuite.com" in lower:
        return True

    # Any reference to non-professional contact methods.
    if "spam" in lower or "telegram" in lower or "whatsapp" in lower:
        return True

    # Any reference to any content about marketing.
    if (
        " seo" in lower
        or "(seo)" in lower
        or "-seo" in lower
        or "search engine optimization" in lower
    ):
        return True

    # SEO marketing sell.
    if "free report" in lower or "text-to-video" in lower:
        return True

    # Any reference to a search engine (likely marketing SEO).
    if "yahoo" in lower or "bing" in lower:
        return True

    # Any reference to keywords about optimizing traffic to the website.
    if "traffic" in lower or "visitor" in lower:
        return True

    # Adult content advertisements.
    if "bored" in lower or "adult" in lower or "private video" in lower:
        return True

    # Remove generic shortened/redirect urls.
    if "bit.ly" in lower or "tinyurl.com" in lower or "rb.gy" in lower:
        return True

    # Remove additional shortened/redirect urls.
    if "short.io" in lower or "short.gy" in lower or "short.fy" in lower:
        return True

    # Cryptocurrency garbage.
    if "btc" in lower or "bitcoin" in lower or " ether" in lower:
        return True

    # Hacking claims garbage.
    if " hack" in lower or "ransom" in lower or "decrypt" in lower:
        return True

    # Product sales lines.
    if "free shipping" in lower or "today only" in lower or "limited time" in lower:
        return True

    return False
