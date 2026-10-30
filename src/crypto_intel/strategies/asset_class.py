"""Asset-class specific research strategies (paper-only). Enhanced v0.51."""

ASSET_CLASSES = {
    "major": {"risk_cap": 0.08, "cost_bps": 8},
    "large_alt": {"risk_cap": 0.04, "cost_bps": 14},
    "stable": {"risk_cap": 0.0, "cost_bps": 0},
    "defi": {"risk_cap": 0.02, "cost_bps": 22},
    "meme": {"risk_cap": 0.005, "cost_bps": 45},
    "l2": {"risk_cap": 0.03, "cost_bps": 16},
    "rwa": {"risk_cap": 0.02, "cost_bps": 12},
    "perp": {"risk_cap": 0.02, "cost_bps": 10},
    "ai_token": {"risk_cap": 0.01, "cost_bps": 30},  # new hybrid
}

def score_signal(asset_class: str, regime: str, factors: dict) -> float:
    """Multi-factor score with enhanced gates. Research only."""
    if regime == "stress" or factors.get("isolation", 0) > 0.6:
        return 0.0
    base = factors.get("strength", 0.5)
    if factors.get("anomaly", 0) > 0.65:
        base *= 0.4
    if factors.get("correlation", 0) > 0.8:
        base *= 0.7  # high correlation penalty
    # Class-specific adjustments (proxies)
    if asset_class == "meme" or asset_class == "ai_token":
        if factors.get("burst", 0) < 0.15:
            base *= 0.3
    cap = ASSET_CLASSES.get(asset_class, {}).get("risk_cap", 0.0)
    return min(max(base, 0.0), cap)
