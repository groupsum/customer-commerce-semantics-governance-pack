# customer-commerce-semantics-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>customer-commerce-semantics-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for customer commerce semantics, products, offers, orders, invoices, reviews, ratings, and conversion actions.</p>
<p align="center">
<a href="https://pypi.org/project/customer-commerce-semantics-governance-pack/"><img alt="pypi: customer-commerce-semantics-governance-pack" src="https://img.shields.io/pypi/v/customer-commerce-semantics-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/customer-commerce-semantics-governance-pack/"><img alt="Monthly PyPI downloads: customer-commerce-semantics-governance-pack" src="https://img.shields.io/pypi/dm/customer-commerce-semantics-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/README.md"><img alt="README hits: customer-commerce-semantics-governance-pack" src="https://hits.sh/github.com/groupsum/customer-commerce-semantics-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for customer commerce semantics, products, offers, orders, invoices, reviews, ratings, and conversion actions.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern customer commerce and product semantics, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Customer Commerce And Product Semantics.

### Features

**Included ADRs**

- [`adr:commerce-source-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1001-commerce-source-policy.yaml) — Commerce Source Policy
- [`adr:schema-org-product-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1002-schema-org-product-policy.yaml) — Schema.org Product Policy
- [`adr:schema-org-offer-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1003-schema-org-offer-policy.yaml) — Schema.org Offer Policy
- [`adr:schema-org-order-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1004-schema-org-order-policy.yaml) — Schema.org Order Policy
- [`adr:schema-org-invoice-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1005-schema-org-invoice-policy.yaml) — Schema.org Invoice Policy
- [`adr:schema-org-review-rating-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1006-schema-org-review-rating-policy.yaml) — Schema.org Review Rating Policy
- [`adr:schema-org-commerce-action-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1007-schema-org-commerce-action-policy.yaml) — Schema.org Commerce Action Policy
- [`adr:commerce-identifier-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1009-commerce-identifier-policy.yaml) — Commerce Identifier Policy
- [`adr:commerce-conversion-boundary-policy`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1010-commerce-conversion-boundary-policy.yaml) — Commerce Conversion Boundary Policy
- [`adr:commerce-semantics-consume-canonical-gs1-identifiers`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/adr/ADR-1011-commerce-semantics-consume-canonical-gs1-identifiers.yaml) — Commerce Semantics Consume Canonical GS1 Identifiers

**Included SPECs**

- [`spc:schema-org-product-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2001-schema-org-product-requirements.yaml) — Schema.org Product Requirements
- [`spc:schema-org-offer-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2002-schema-org-offer-requirements.yaml) — Schema.org Offer Requirements
- [`spc:schema-org-aggregate-offer-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2003-schema-org-aggregate-offer-requirements.yaml) — Schema.org Aggregate Offer Requirements
- [`spc:schema-org-order-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2004-schema-org-order-requirements.yaml) — Schema.org Order Requirements
- [`spc:schema-org-invoice-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2005-schema-org-invoice-requirements.yaml) — Schema.org Invoice Requirements
- [`spc:schema-org-review-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2006-schema-org-review-requirements.yaml) — Schema.org Review Requirements
- [`spc:schema-org-rating-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2007-schema-org-rating-requirements.yaml) — Schema.org Rating Requirements
- [`spc:schema-org-aggregate-rating-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2008-schema-org-aggregate-rating-requirements.yaml) — Schema.org Aggregate Rating Requirements
- [`spc:schema-org-commerce-action-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2009-schema-org-commerce-action-requirements.yaml) — Schema.org Commerce Action Requirements
- [`spc:schema-org-commerce-event-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2010-schema-org-commerce-event-requirements.yaml) — Schema.org Commerce Event Requirements
- [`spc:commerce-identifier-classification-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2014-commerce-identifier-classification-requirements.yaml) — Commerce Identifier Classification Requirements
- [`spc:commerce-transaction-state-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2015-commerce-transaction-state-requirements.yaml) — Commerce Transaction State Requirements
- [`spc:commerce-conversion-action-requirements`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2016-commerce-conversion-action-requirements.yaml) — Commerce Conversion Action Requirements
- [`spc:gs1-to-commerce-semantic-mapping-profile`](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates/specs/SPEC-2017-gs1-to-commerce-semantic-mapping-profile.yaml) — GS1 To Commerce Semantic Mapping Profile

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add customer-commerce-semantics-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install customer-commerce-semantics-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add customer-commerce-semantics-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_customer_commerce_semantics import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:customer-commerce-semantics"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:customer-commerce-semantics` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_customer_commerce_semantics import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:schema-org-product-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-schema-org-product-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `customer-commerce-semantics-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_customer_commerce_semantics
uv run ssot pack preflight . ssot_pack_customer_commerce_semantics --all
uv run ssot pack sync . ssot_pack_customer_commerce_semantics --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_customer_commerce_semantics` in SSOT Registry. Review reservation owner `extension-pack:customer-commerce-semantics-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Removed duplicate GS1 syntax ownership and added a GS1-to-commerce integration profile.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_customer_commerce_semantics` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/customer-commerce-semantics-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/src/ssot_pack_customer_commerce_semantics/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/customer-commerce-semantics-governance-pack)
- [Issues](https://github.com/groupsum/customer-commerce-semantics-governance-pack/issues)
- [Repository](https://github.com/groupsum/customer-commerce-semantics-governance-pack)
- [pypi: customer-commerce-semantics-governance-pack](https://pypi.org/project/customer-commerce-semantics-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/customer-commerce-semantics-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:customer-commerce-semantics`. The pack's reservation owner is `extension-pack:customer-commerce-semantics-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [Schema.org Person](https://schema.org/Person)
- [Schema.org Product](https://schema.org/Product)
- [Schema.org Offer](https://schema.org/Offer)
- [Schema.org Order](https://schema.org/Order)
- [Schema.org Invoice](https://schema.org/Invoice)
- [Schema.org Review](https://schema.org/Review)
- [Schema.org AggregateRating](https://schema.org/AggregateRating)
- [Schema.org Action](https://schema.org/Action) and [Schema.org Event](https://schema.org/Event)
- [GS1 Web Vocabulary](https://www.gs1.org/gs1-web-vocabulary)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/customer-commerce-semantics-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
