from returnsuite_website.services.spam import detected_spam


def test_detected_spam_none():
    assert detected_spam(None) is False


def test_detected_spam_empty():
    assert detected_spam(" ") is False


def test_detected_spam_valid():
    assert detected_spam("We watched your video and are interested in more.") is False


def test_detected_spam_single_word():
    assert detected_spam("random") is True


def test_detected_spam_domain_name():
    assert detected_spam("How are you returnsuite.com,") is True


def test_detected_spam_traffic():
    assert detected_spam("We can send visitors and increase traffic") is True


def test_detected_spam_seo():
    assert detected_spam("Your site is so beautiful. Let us improve the (SEO).") is True


def test_detected_spam_free_report():
    assert detected_spam("... with a FREE report, click here ...") is True


def test_detected_spam_shortened_url():
    assert detected_spam("Check us out at https://bit.ly/example") is True
