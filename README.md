# Objective
test pdb will control pod restart based on pod liveness.

# test
```sh
kubecli apply -f .
# fake remote svc will be create
# nginx2.default.svc.cluster.local
kubectl scale --replicas=0 deployment/nginx2
watch kubecli get po
```

# result
the pod will still restart and crash.

# finding
Liveness livenessProbe is not subject to PodDisruptionBudget ( pdb )

# related
https://stackoverflow.com/questions/67276029/are-kubernetes-liveness-probe-failures-voluntary-or-involuntary-disruptions
