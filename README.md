# Objective
test pdb will control pod restart based on pod liveness.

# test
```sh
kubecli apply -f .
# fake remote svc will be create
# nginx2.default.svc.cluster.local
# shutdown the remote service
kubectl scale --replicas=0 deployment/nginx2
# watch the pod probe based on remote call will restart or not
watch kubecli get po
```

# result
the pod will still restart and crash.

# finding
Liveness livenessProbe is not subject to PodDisruptionBudget ( pdb )

# timeout do not apply to exec
1. https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

# bash issue
U cannot use $RANDOM directly via `sh -c`
`$RANDOM` is a bash extension; in dash, it is not special and not assigned by default.
1. https://stackoverflow.com/questions/30719911/arithmetic-expression-expecting-primary

# related
1. https://stackoverflow.com/questions/67276029/are-kubernetes-liveness-probe-failures-voluntary-or-involuntary-disruptions
1. https://unix.stackexchange.com/questions/94604/does-curl-have-a-timeout/94612
1. https://unix.stackexchange.com/questions/124918/how-to-check-whether-a-command-such-as-curl-completed-without-error
