#!/usr/bin/env python3
"""Tests — strix Anything-CLI Suite v1.0 | IntentHash: 0xTEST_STRIX_ANYTHING_20260615"""
import sys
from pathlib import Path

STRIX_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(STRIX_ROOT))


def _validate(result, name):
    assert isinstance(result, dict), f"{name}: not a dict"
    for k in ("tool", "status", "intent_hash", "result", "timestamp", "phi_cps"):
        assert k in result, f"{name}: missing '{k}'"
    assert result["tool"] == name
    assert result["status"] in ("success", "error")
    assert result["phi_cps"] == 4.092


# ── deal-anything ──────────────────────────────────────────────────────────────
def test_deal_success():
    from cli_tools.anything import deal_anything
    r = deal_anything(merchant="M-1", country="FR", vat_applicable=True)
    _validate(r, "deal-anything")
    assert r["status"] == "success"
    assert r["result"]["merchant"] == "M-1"


def test_deal_missing_merchant():
    from cli_tools.anything import deal_anything
    r = deal_anything(merchant="", country="FR", vat_applicable=False)
    _validate(r, "deal-anything")
    assert r["status"] == "error"


# ── invoice-anything ───────────────────────────────────────────────────────────
def test_invoice_success():
    from cli_tools.anything import invoice_anything
    r = invoice_anything(invoice_id="INV-001", amount=99.9, currency="EUR")
    _validate(r, "invoice-anything")
    assert r["status"] == "success"
    assert r["result"]["amount"] == 99.9


def test_invoice_invalid_amount():
    from cli_tools.anything import invoice_anything
    r = invoice_anything(invoice_id="INV-002", amount=-10, currency="USD")
    _validate(r, "invoice-anything")
    assert r["status"] == "error"


# ── tax-anything ───────────────────────────────────────────────────────────────
def test_tax_success():
    from cli_tools.anything import tax_anything
    r = tax_anything(country="FR", vat_rate=0.20)
    _validate(r, "tax-anything")
    assert r["status"] == "success"
    assert r["result"]["vat_rate"] == 0.20


def test_tax_invalid_rate():
    from cli_tools.anything import tax_anything
    r = tax_anything(country="FR", vat_rate=1.5)
    _validate(r, "tax-anything")
    assert r["status"] == "error"


# ── merchant-anything ──────────────────────────────────────────────────────────
def test_merchant_success():
    from cli_tools.anything import merchant_anything
    r = merchant_anything(merchant_id="M-1", sector="retail")
    _validate(r, "merchant-anything")
    assert r["status"] == "success"


def test_merchant_missing_id():
    from cli_tools.anything import merchant_anything
    r = merchant_anything(merchant_id="", sector="retail")
    _validate(r, "merchant-anything")
    assert r["status"] == "error"


# ── payment-anything ────────────────────────────────────────────────────────────
def test_payment_success():
    from cli_tools.anything import payment_anything
    r = payment_anything(payment_id="PAY-001", method="card", amount=49.9)
    _validate(r, "payment-anything")
    assert r["status"] == "success"


def test_payment_bad_method():
    from cli_tools.anything import payment_anything
    r = payment_anything(payment_id="PAY-002", method="crypto", amount=10)
    _validate(r, "payment-anything")
    assert r["status"] == "error"


# ── refund-anything ────────────────────────────────────────────────────────────
def test_refund_success():
    from cli_tools.anything import refund_anything
    r = refund_anything(refund_id="REF-001", reason="duplicate", amount=19.9)
    _validate(r, "refund-anything")
    assert r["status"] == "success"


def test_refund_missing_reason():
    from cli_tools.anything import refund_anything
    r = refund_anything(refund_id="REF-002", reason="", amount=0.0)
    _validate(r, "refund-anything")
    assert r["status"] == "error"


# ── reconciliation-anything ────────────────────────────────────────────────────
def test_reconciliation_success():
    from cli_tools.anything import reconciliation_anything
    r = reconciliation_anything(period="2026-06", scope="full")
    _validate(r, "reconciliation-anything")
    assert r["status"] == "success"


def test_reconciliation_invalid_scope():
    from cli_tools.anything import reconciliation_anything
    r = reconciliation_anything(period="2026-06", scope="invalid")
    _validate(r, "reconciliation-anything")
    assert r["status"] == "error"


# ── audit-anything ─────────────────────────────────────────────────────────────
def test_audit_success():
    from cli_tools.anything import audit_anything
    r = audit_anything(scope="merchants")
    _validate(r, "audit-anything")
    assert r["status"] == "success"


def test_audit_invalid_scope():
    from cli_tools.anything import audit_anything
    r = audit_anything(scope="unknown")
    _validate(r, "audit-anything")
    assert r["status"] == "error"


# ── TOOL_MAP ───────────────────────────────────────────────────────────────────
def test_tool_map():
    from cli_tools.anything import TOOL_MAP
    expected = ["deal-anything", "invoice-anything", "tax-anything",
                "merchant-anything", "payment-anything", "refund-anything",
                "reconciliation-anything", "audit-anything"]
    for t in expected:
        assert t in TOOL_MAP, f"Missing: {t}"
    assert len(TOOL_MAP) == 8


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    p = f = 0
    for t in tests:
        try:
            t()
            p += 1
            print(f"  [OK] {t.__name__}")
        except Exception as e:
            f += 1
            print(f"  [FAIL] {t.__name__}: {e}")
    print(f"\n{p} passed, {f} failed, {p+f} total")
    sys.exit(0 if f == 0 else 1)
