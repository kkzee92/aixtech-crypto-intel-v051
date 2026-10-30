def test_version():
    from crypto_intel import __version__
    assert __version__ == "0.51.0"

def test_redact():
    from crypto_intel.security.redact import redact
    assert "[REDACTED]" in redact("my private key is abc")
    assert "[REDACTED]" in redact("0x1234567890abcdef1234567890abcdef12345678")

def test_score():
    from crypto_intel.strategies.asset_class import score_signal
    factors = {"strength": 0.8, "anomaly": 0.2}
    assert score_signal("major", "trend", factors) > 0
    assert score_signal("stable", "trend", factors) == 0.0
    assert score_signal("major", "stress", factors) == 0.0

def test_seal():
    from crypto_intel.security.audit import seal_event
    e = seal_event({"test": True})
    assert "sha256" in e and "sha3" in e and "blake2" in e
