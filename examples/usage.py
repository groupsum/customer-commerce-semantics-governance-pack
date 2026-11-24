"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_customer_commerce_semantics import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:schema-org-product-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-schema-org-product-requirements.yaml"
