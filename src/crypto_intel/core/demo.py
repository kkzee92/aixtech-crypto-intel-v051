"""Enhanced demo runner for paper-only research."""
from ..strategies.asset_class import score_signal, ASSET_CLASSES
from ..security.audit import seal_event
from ..security.redact import redact

def run_demo():
    print("AIxTech crypto intel v0.51 demo (paper-only)")
    print("Synthetic data only. No live execution. Zero-trust active.")
    print("Regime clustering, multi-factor strategies, expanded anomaly detection.")
    
    # Synthetic example
    factors = {"strength": 0.75, "anomaly": 0.3, "isolation": 0.2, "correlation": 0.4}
    for cls in ASSET_CLASSES:
        score = score_signal(cls, "trend", factors)
        print(f"{cls}: score={score:.3f} (cap={ASSET_CLASSES[cls]['risk_cap']})")
    
    event = seal_event({"action": "demo_scan", "status": "paper_ok"})
    print("Sealed audit:", redact(str(event)))
    print("Demo complete. Research only.")
