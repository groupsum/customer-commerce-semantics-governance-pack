# customer-commerce-semantics-governance-pack

Installable SSOT governance pack for customer commerce semantics, products, offers, orders, invoices, reviews, ratings, and conversion actions.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:customer-commerce-semantics`
- Priority: `P2.2`
- PyPI package: `customer-commerce-semantics-governance-pack`
- Import package: `ssot_pack_customer_commerce_semantics`
- GitHub repository: `groupsum/customer-commerce-semantics-governance-pack`
- Reservation owner: `extension-pack:customer-commerce-semantics-governance-pack`

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

- `spc:schema-org-product-requirements` - Schema.org Product Requirements
- `spc:schema-org-offer-requirements` - Schema.org Offer Requirements
- `spc:schema-org-aggregate-offer-requirements` - Schema.org Aggregate Offer Requirements
- `spc:schema-org-order-requirements` - Schema.org Order Requirements
- `spc:schema-org-invoice-requirements` - Schema.org Invoice Requirements
- `spc:schema-org-review-requirements` - Schema.org Review Requirements
- `spc:schema-org-rating-requirements` - Schema.org Rating Requirements
- `spc:schema-org-aggregate-rating-requirements` - Schema.org Aggregate Rating Requirements
- `spc:schema-org-commerce-action-requirements` - Schema.org Commerce Action Requirements
- `spc:schema-org-commerce-event-requirements` - Schema.org Commerce Event Requirements
- `spc:gs1-product-identifier-requirements` - GS1 Product Identifier Requirements
- `spc:gs1-trade-item-requirements` - GS1 Trade Item Requirements
- `spc:gs1-organization-location-requirements` - GS1 Organization Location Requirements
- `spc:commerce-identifier-classification-requirements` - Commerce Identifier Classification Requirements
- `spc:commerce-transaction-state-requirements` - Commerce Transaction State Requirements
- `spc:commerce-conversion-action-requirements` - Commerce Conversion Action Requirements

## Install With uv

```bash
uv add customer-commerce-semantics-governance-pack
uv add ssot-registry customer-commerce-semantics-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install customer-commerce-semantics-governance-pack
uvx --from ssot-registry ssot pack sync . customer-commerce-semantics-governance-pack
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
- PyPI package: https://pypi.org/project/customer-commerce-semantics-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
