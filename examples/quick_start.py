"""Inspect the installed pack identity."""

from ssot_pack_customer_commerce_semantics import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:customer-commerce-semantics"
print(metadata["origin"]["id"])
