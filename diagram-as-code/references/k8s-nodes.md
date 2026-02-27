# Kubernetes Node Reference

Complete list of available Kubernetes node classes in the `diagrams` library.
Use: `from diagrams.k8s.<module> import <ClassName>`

**Total: 69 node classes across 12 modules**

## k8s.chaos

- `ChaosMesh`
- `LitmusChaos`

## k8s.clusterconfig

- `HPA`
- `HorizontalPodAutoscaler`
- `LimitRange`
- `Limits`
- `Quota`

## k8s.compute

- `Cronjob`
- `DS`
- `DaemonSet`
- `Deploy`
- `Deployment`
- `Job`
- `Pod`
- `RS`
- `ReplicaSet`
- `STS`
- `StatefulSet`

## k8s.controlplane

- `API`
- `APIServer`
- `CCM`
- `CM`
- `ControllerManager`
- `KProxy`
- `KubeProxy`
- `Kubelet`
- `Sched`
- `Scheduler`

## k8s.ecosystem

- `ExternalDns`
- `Helm`
- `Krew`
- `Kustomize`

## k8s.group

- `NS`
- `Namespace`

## k8s.infra

- `ETCD`
- `Master`
- `Node`

## k8s.network

- `Endpoint`
- `Ep`
- `Ing`
- `Ingress`
- `Netpol`
- `NetworkPolicy`
- `SVC`
- `Service`

## k8s.others

- `CRD`
- `PSP`

## k8s.podconfig

- `CM`
- `ConfigMap`
- `Secret`

## k8s.rbac

- `CRB`
- `CRole`
- `ClusterRole`
- `ClusterRoleBinding`
- `Group`
- `RB`
- `Role`
- `RoleBinding`
- `SA`
- `ServiceAccount`
- `User`

## k8s.storage

- `PV`
- `PVC`
- `PersistentVolume`
- `PersistentVolumeClaim`
- `SC`
- `StorageClass`
- `Vol`
- `Volume`
