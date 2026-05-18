# customer-commerce-semantics-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/customer-commerce-semantics-governance-pack.svg)](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/customer-commerce-semantics-governance-pack.svg)](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
[![License](https://img.shields.io/pypi/l/customer-commerce-semantics-governance-pack.svg)](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
[![Publish](https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/customer-commerce-semantics-governance-pack)

Installable SSOT governance pack for customer commerce semantics, products, offers, orders, invoices, reviews, ratings, and conversion actions.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `customer-commerce-semantics-governance-pack` is an installable SSOT governance pack for Customer Commerce And Product Semantics. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern customer commerce and product semantics, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`customer-commerce-semantics-governance-pack`](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
- GitHub package repository: [`groupsum/customer-commerce-semantics-governance-pack`](https://github.com/groupsum/customer-commerce-semantics-governance-pack)
- Import package: `ssot_pack_customer_commerce_semantics`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:customer-commerce-semantics`
- PyPI package: `customer-commerce-semantics-governance-pack`
- Import package: `ssot_pack_customer_commerce_semantics`
- GitHub repository: `groupsum/customer-commerce-semantics-governance-pack`
- Reservation owner: `extension-pack:customer-commerce-semantics-governance-pack`

## Domain Focus

Customer Commerce And Product Semantics

## Authority Sources

- [Schema.org Person](https://schema.org/Person)
- [Schema.org Product](https://schema.org/Product)
- [Schema.org Offer](https://schema.org/Offer)
- [Schema.org Order](https://schema.org/Order)
- [Schema.org Invoice](https://schema.org/Invoice)
- [Schema.org Review](https://schema.org/Review)
- [Schema.org AggregateRating](https://schema.org/AggregateRating)
- [Schema.org Action](https://schema.org/Action) and [Schema.org Event](https://schema.org/Event)
- [GS1 Web Vocabulary](https://www.gs1.org/gs1-web-vocabulary)

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

- GitHub package repository: [groupsum/customer-commerce-semantics-governance-pack](https://github.com/groupsum/customer-commerce-semantics-governance-pack)
- PyPI package: [customer-commerce-semantics-governance-pack](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
