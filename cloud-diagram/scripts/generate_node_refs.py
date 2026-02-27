#!/usr/bin/env python3
"""
Node Reference Generator for the diagrams library.

Introspects the diagrams library and emits markdown reference files
listing every available node class, grouped by module.

Usage:
    python generate_node_refs.py --provider azure --output-dir references/
    python generate_node_refs.py --provider aws --output-dir references/
    python generate_node_refs.py --all --output-dir references/
"""

import argparse
import importlib
import inspect
import os
import pkgutil
import sys

# Providers to generate references for with --all
DEFAULT_PROVIDERS = ["aws", "azure", "gcp", "k8s", "onprem"]

# All known providers in the diagrams library
ALL_KNOWN_PROVIDERS = [
    "alibabacloud", "aws", "azure", "digitalocean", "elastic",
    "firebase", "gcp", "generic", "ibm", "k8s", "oci",
    "onprem", "openstack", "outscale", "programming", "saas",
]


def get_provider_nodes(provider):
    """
    Introspect a diagrams provider and return a dict of
    {module_name: [ClassName, ...]} with private _Base classes filtered out.
    """
    try:
        provider_mod = importlib.import_module(f"diagrams.{provider}")
    except ImportError:
        print(f"Warning: diagrams.{provider} not found, skipping", file=sys.stderr)
        return {}

    provider_path = os.path.dirname(provider_mod.__file__)
    modules = {}

    for _, module_name, _ in sorted(pkgutil.iter_modules([provider_path])):
        fqn = f"diagrams.{provider}.{module_name}"
        try:
            mod = importlib.import_module(fqn)
        except Exception:
            continue

        classes = []
        for name, obj in inspect.getmembers(mod, inspect.isclass):
            # Filter out private/base classes and re-exports from other modules
            if name.startswith("_"):
                continue
            if obj.__module__ != fqn:
                continue
            classes.append(name)

        if classes:
            modules[module_name] = sorted(classes)

    return modules


def generate_markdown(provider, modules):
    """Generate a markdown reference file for a provider."""
    # Friendly names for display
    display_names = {
        "aws": "AWS",
        "azure": "Azure",
        "gcp": "GCP (Google Cloud Platform)",
        "k8s": "Kubernetes",
        "onprem": "On-Premises / Open Source",
        "alibabacloud": "Alibaba Cloud",
        "digitalocean": "DigitalOcean",
        "elastic": "Elastic",
        "firebase": "Firebase",
        "generic": "Generic",
        "ibm": "IBM",
        "oci": "Oracle Cloud Infrastructure",
        "openstack": "OpenStack",
        "outscale": "Outscale",
        "programming": "Programming",
        "saas": "SaaS",
    }

    display = display_names.get(provider, provider)
    total = sum(len(v) for v in modules.values())

    lines = [
        f"# {display} Node Reference",
        "",
        f"Complete list of available {display} node classes in the `diagrams` library.",
        f"Use: `from diagrams.{provider}.<module> import <ClassName>`",
        "",
        f"**Total: {total} node classes across {len(modules)} modules**",
        "",
    ]

    for module_name, classes in sorted(modules.items()):
        lines.append(f"## {provider}.{module_name}")
        lines.append("")
        for cls in classes:
            lines.append(f"- `{cls}`")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate diagrams node reference files")
    parser.add_argument("--provider", help="Single provider to generate (e.g., aws, gcp)")
    parser.add_argument("--all", action="store_true", help="Generate for all default providers (aws, azure, gcp, k8s, onprem)")
    parser.add_argument("--all-providers", action="store_true", help="Generate for every provider in the diagrams library")
    parser.add_argument("--output-dir", default="references", help="Output directory (default: references/)")
    args = parser.parse_args()

    if not args.provider and not args.all and not args.all_providers:
        parser.error("Specify --provider <name>, --all, or --all-providers")

    os.makedirs(args.output_dir, exist_ok=True)

    if args.all_providers:
        providers = ALL_KNOWN_PROVIDERS
    elif args.all:
        providers = DEFAULT_PROVIDERS
    else:
        providers = [args.provider]

    for provider in providers:
        modules = get_provider_nodes(provider)
        if not modules:
            continue

        md = generate_markdown(provider, modules)
        out_path = os.path.join(args.output_dir, f"{provider}-nodes.md")
        with open(out_path, "w") as f:
            f.write(md)

        total = sum(len(v) for v in modules.values())
        print(f"{provider}: {total} nodes across {len(modules)} modules → {out_path}")


if __name__ == "__main__":
    main()
