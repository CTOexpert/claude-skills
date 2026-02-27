#!/usr/bin/env python3
"""
Cloud Architecture Diagram Generator

Generates PNG architecture diagrams using the mingrammer/diagrams library.
Supports Azure, AWS, GCP, Kubernetes, on-premises, and 15+ other providers.
Requires: pip install diagrams, apt install graphviz

Usage:
    python generate_diagram.py                              # Run default (azure) example
    python generate_diagram.py --example azure              # Azure 3-tier example
    python generate_diagram.py --example aws                # AWS 3-tier example
    python generate_diagram.py --example multicloud         # Multi-cloud hybrid example
    python generate_diagram.py --json spec.json             # From JSON spec
    python generate_diagram.py --output my_diagram          # Custom output name
    python generate_diagram.py --format svg                 # SVG output
    python generate_diagram.py --direction TB               # Top-to-bottom layout
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def ensure_dependencies():
    """Install diagrams and graphviz if missing."""
    try:
        import diagrams  # noqa: F401
    except ImportError:
        print("Installing diagrams library...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "diagrams", "--break-system-packages", "-q"]
        )

    # Check graphviz
    if subprocess.run(["which", "dot"], capture_output=True).returncode != 0:
        print("Installing graphviz...")
        subprocess.run(["apt-get", "install", "-y", "graphviz", "-q"], capture_output=True)


def generate_azure_example(output="cloud_architecture", fmt="png", direction="LR"):
    """Generate an Azure 3-tier web application diagram."""
    from diagrams import Cluster, Diagram, Edge
    from diagrams.azure.compute import AppServices, FunctionApps
    from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis
    from diagrams.azure.identity import ActiveDirectory
    from diagrams.azure.network import ApplicationGateway, FrontDoors
    from diagrams.azure.security import KeyVaults
    from diagrams.azure.storage import BlobStorage
    from diagrams.azure.devops import ApplicationInsights

    graph_attr = {
        "fontsize": "16",
        "bgcolor": "white",
        "pad": "0.5",
        "nodesep": "0.8",
        "ranksep": "1.2",
    }

    with Diagram(
        "Azure 3-Tier Web Application",
        show=False,
        filename=output,
        outformat=fmt,
        direction=direction,
        graph_attr=graph_attr,
    ):
        users = FrontDoors("Azure Front Door")
        ad = ActiveDirectory("Entra ID")

        with Cluster("Production VNet"):
            agw = ApplicationGateway("App Gateway\n+ WAF")

            with Cluster("App Tier"):
                web = AppServices("Web App")
                api = AppServices("API App")
                func = FunctionApps("Background\nJobs")

            with Cluster("Data Tier"):
                sql = SQLDatabases("Azure SQL")
                cosmos = CosmosDb("Cosmos DB")
                cache = CacheForRedis("Redis Cache")

        with Cluster("Shared Services"):
            kv = KeyVaults("Key Vault")
            blob = BlobStorage("Blob Storage")
            insights = ApplicationInsights("App Insights")

        # Request flow
        users >> Edge(label="HTTPS") >> agw
        agw >> web
        agw >> api
        ad >> Edge(label="OAuth", style="dashed") >> agw

        # App to data
        web >> cache
        api >> sql
        api >> cosmos
        func >> cosmos
        func >> blob

        # Shared services
        web >> Edge(style="dotted") >> kv
        api >> Edge(style="dotted") >> kv
        web >> insights
        api >> insights

    print(f"Diagram saved: {output}.{fmt}")
    return f"{output}.{fmt}"


def generate_aws_example(output="cloud_architecture", fmt="png", direction="LR"):
    """Generate an AWS 3-tier web application diagram."""
    from diagrams import Cluster, Diagram, Edge
    from diagrams.aws.network import CloudFront, ELB, Route53
    from diagrams.aws.compute import EC2, ECS
    from diagrams.aws.database import RDS, ElastiCache
    from diagrams.aws.storage import S3
    from diagrams.aws.security import WAF, IAMRole
    from diagrams.aws.management import Cloudwatch

    graph_attr = {
        "fontsize": "16",
        "bgcolor": "white",
        "pad": "0.5",
        "nodesep": "0.8",
        "ranksep": "1.2",
    }

    with Diagram(
        "AWS 3-Tier Web Application",
        show=False,
        filename=output,
        outformat=fmt,
        direction=direction,
        graph_attr=graph_attr,
    ):
        dns = Route53("Route 53")
        cdn = CloudFront("CloudFront")
        waf = WAF("WAF")

        with Cluster("VPC"):
            alb = ELB("Application\nLoad Balancer")

            with Cluster("App Tier (Private Subnets)"):
                web = ECS("Web Service")
                api = ECS("API Service")
                workers = EC2("Worker\nInstances")

            with Cluster("Data Tier (Private Subnets)"):
                rds = RDS("RDS PostgreSQL\n(Multi-AZ)")
                cache = ElastiCache("ElastiCache\nRedis")

        with Cluster("Storage & Monitoring"):
            s3 = S3("S3 Bucket")
            cw = Cloudwatch("CloudWatch")
            iam = IAMRole("IAM Roles")

        # Request flow
        dns >> Edge(label="DNS") >> cdn
        cdn >> waf >> alb
        alb >> web
        alb >> api

        # App to data
        web >> cache
        api >> rds
        api >> cache
        workers >> rds
        workers >> s3

        # Monitoring
        web >> Edge(style="dotted") >> cw
        api >> Edge(style="dotted") >> cw
        api >> Edge(style="dotted") >> iam

    print(f"Diagram saved: {output}.{fmt}")
    return f"{output}.{fmt}"


def generate_multicloud_example(output="cloud_architecture", fmt="png", direction="TB"):
    """Generate a multi-cloud hybrid architecture diagram mixing AWS, Azure, and GCP."""
    from diagrams import Cluster, Diagram, Edge
    from diagrams.aws.network import CloudFront
    from diagrams.aws.compute import ECS
    from diagrams.aws.database import RDS
    from diagrams.azure.compute import AppServices
    from diagrams.azure.database import CosmosDb
    from diagrams.azure.network import FrontDoors
    from diagrams.gcp.compute import Run
    from diagrams.gcp.database import Spanner
    from diagrams.gcp.network import CDN
    from diagrams.onprem.monitoring import Grafana, Prometheus
    from diagrams.onprem.network import Nginx

    graph_attr = {
        "fontsize": "16",
        "bgcolor": "white",
        "pad": "0.5",
        "nodesep": "0.8",
        "ranksep": "1.2",
    }

    with Diagram(
        "Multi-Cloud Active-Active Architecture",
        show=False,
        filename=output,
        outformat=fmt,
        direction=direction,
        graph_attr=graph_attr,
    ):
        lb = Nginx("Global Load\nBalancer")

        with Cluster("AWS (us-east-1)"):
            aws_cdn = CloudFront("CloudFront")
            aws_app = ECS("API Service")
            aws_db = RDS("RDS PostgreSQL")
            aws_cdn >> aws_app >> aws_db

        with Cluster("Azure (East US)"):
            az_fd = FrontDoors("Front Door")
            az_app = AppServices("App Service")
            az_db = CosmosDb("Cosmos DB")
            az_fd >> az_app >> az_db

        with Cluster("GCP (us-central1)"):
            gcp_cdn = CDN("Cloud CDN")
            gcp_app = Run("Cloud Run")
            gcp_db = Spanner("Cloud Spanner")
            gcp_cdn >> gcp_app >> gcp_db

        with Cluster("Observability (On-Prem)"):
            prom = Prometheus("Prometheus")
            graf = Grafana("Grafana")
            prom >> graf

        # Traffic routing
        lb >> Edge(label="Region 1") >> aws_cdn
        lb >> Edge(label="Region 2") >> az_fd
        lb >> Edge(label="Region 3") >> gcp_cdn

        # Cross-cloud replication
        aws_db >> Edge(label="replication", style="dashed", color="gray") >> az_db
        az_db >> Edge(label="replication", style="dashed", color="gray") >> gcp_db

        # Monitoring
        aws_app >> Edge(style="dotted") >> prom
        az_app >> Edge(style="dotted") >> prom
        gcp_app >> Edge(style="dotted") >> prom

    print(f"Diagram saved: {output}.{fmt}")
    return f"{output}.{fmt}"


def generate_from_json(spec_path, output="cloud_architecture", fmt="png", direction="LR"):
    """
    Generate a diagram from a JSON specification.

    Expected JSON format:
    {
        "title": "My Architecture",
        "direction": "LR",
        "clusters": [
            {
                "name": "VNet",
                "nodes": [
                    {"id": "web", "type": "azure.compute.AppServices", "label": "Web App"},
                    {"id": "sql", "type": "azure.database.SQLDatabases", "label": "SQL DB"}
                ],
                "children": []
            }
        ],
        "nodes": [],
        "edges": [
            {"from": "web", "to": "sql", "label": "SQL"}
        ]
    }

    Node types use dotted paths relative to `diagrams.`, e.g.:
        "azure.compute.AppServices"
        "aws.compute.EC2"
        "gcp.compute.Run"
        "k8s.compute.Pod"
        "onprem.database.PostgreSQL"
    """
    import importlib
    from diagrams import Cluster, Diagram, Edge

    with open(spec_path) as f:
        spec = json.load(f)

    title = spec.get("title", "Cloud Architecture")
    direction = spec.get("direction", direction)

    # Resolve node type string to class
    def resolve_node_class(type_str):
        # e.g., "azure.compute.AppServices" -> diagrams.azure.compute.AppServices
        parts = type_str.split(".")
        module_path = "diagrams." + ".".join(parts[:-1])
        class_name = parts[-1]
        mod = importlib.import_module(module_path)
        return getattr(mod, class_name)

    node_registry = {}

    def create_nodes(node_defs):
        for node_def in node_defs:
            cls = resolve_node_class(node_def["type"])
            node_registry[node_def["id"]] = cls(node_def.get("label", node_def["id"]))

    def create_cluster(cluster_def):
        with Cluster(cluster_def["name"]):
            create_nodes(cluster_def.get("nodes", []))
            for child in cluster_def.get("children", []):
                create_cluster(child)

    with Diagram(title, show=False, filename=output, outformat=fmt, direction=direction):
        # Top-level nodes
        create_nodes(spec.get("nodes", []))

        # Clusters (recursive)
        for cluster_def in spec.get("clusters", []):
            create_cluster(cluster_def)

        # Edges
        for edge_def in spec.get("edges", []):
            src = node_registry[edge_def["from"]]
            dst = node_registry[edge_def["to"]]
            label = edge_def.get("label", "")
            color = edge_def.get("color", "")
            style = edge_def.get("style", "")
            edge_kwargs = {}
            if label:
                edge_kwargs["label"] = label
            if color:
                edge_kwargs["color"] = color
            if style:
                edge_kwargs["style"] = style
            if edge_kwargs:
                src >> Edge(**edge_kwargs) >> dst
            else:
                src >> dst

    print(f"Diagram saved: {output}.{fmt}")
    return f"{output}.{fmt}"


EXAMPLES = {
    "azure": generate_azure_example,
    "aws": generate_aws_example,
    "multicloud": generate_multicloud_example,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate cloud architecture diagrams")
    parser.add_argument("--json", help="Path to JSON spec file")
    parser.add_argument("--example", choices=list(EXAMPLES.keys()),
                        help="Run a built-in example (azure, aws, multicloud)")
    parser.add_argument("--output", default="cloud_architecture", help="Output filename (no extension)")
    parser.add_argument("--format", default="png", choices=["png", "svg", "pdf", "dot"], help="Output format")
    parser.add_argument("--direction", default="LR", choices=["LR", "TB", "RL", "BT"], help="Layout direction")
    args = parser.parse_args()

    ensure_dependencies()

    if args.json:
        generate_from_json(args.json, args.output, args.format, args.direction)
    elif args.example:
        EXAMPLES[args.example](args.output, args.format, args.direction)
    else:
        # Default to Azure example for backwards compatibility
        generate_azure_example(args.output, args.format, args.direction)
