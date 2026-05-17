# ssot-pack-customer-commerce-semantics

Installable SSOT governance pack for customer commerce semantics, products, offers, orders, invoices, reviews, ratings, and conversion actions.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:customer-commerce-semantics`
- Priority: `P2.2`
- PyPI package: `ssot-pack-customer-commerce-semantics`
- Import package: `ssot_pack_customer_commerce_semantics`
- GitHub repository: `groupsum/customer-commerce-semantics-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-customer-commerce-semantics`

## Domain Focus

Customer Commerce And Product Semantics

## Authority Sources

- Schema.org Person
- Schema.org Product
- Schema.org Offer
- Schema.org Order
- Schema.org Invoice
- Schema.org Review
- Schema.org AggregateRating
- Schema.org Action and Event
- GS1 Web Vocabulary

## Included ADRs

- `adr:commerce-source-policy` - Commerce Source Policy
- `adr:schema-org-product-policy` - Schema.org Product Policy
- `adr:schema-org-offer-policy` - Schema.org Offer Policy
- `adr:schema-org-order-policy` - Schema.org Order Policy
- `adr:schema-org-invoice-policy` - Schema.org Invoice Policy
- `adr:schema-org-review-rating-policy` - Schema.org Review Rating Policy
- `adr:schema-org-commerce-action-policy` - Schema.org Commerce Action Policy
- `adr:gs1-product-vocabulary-policy` - GS1 Product Vocabulary Policy
- `adr:commerce-identifier-policy` - Commerce Identifier Policy
- `adr:commerce-conversion-boundary-policy` - Commerce Conversion Boundary Policy

## Included SPECs

- `spc:schema-org-product-offer-contract` - Schema.org Product Offer Contract
- `spc:schema-org-order-invoice-contract` - Schema.org Order Invoice Contract
- `spc:schema-org-review-rating-contract` - Schema.org Review Rating Contract
- `spc:commerce-action-contract` - Commerce Action Contract

## Install With uv

```bash
uv add ssot-pack-customer-commerce-semantics
uv add ssot-registry ssot-pack-customer-commerce-semantics
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-customer-commerce-semantics
uvx --from ssot-registry ssot pack sync . ssot-pack-customer-commerce-semantics
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_customer_commerce_semantics import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/customer-commerce-semantics-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-customer-commerce-semantics/
- SSOT Registry: https://pypi.org/project/ssot-registry/
