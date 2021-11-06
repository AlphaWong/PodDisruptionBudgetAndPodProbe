# Objective
test pdb will control pod restart based on pod liveness.

# minikube
```sh
minikube start --kubernetes-version=v1.15.12
```
# importance
Before Kubernetes 1.20, the field `timeoutSeconds` was not respected for exec probes: probes continued running indefinitely, even past their configured deadline, until a result was returned.
## reference
1. https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes

# test
```sh
kubecli apply -f bash-deploy.yaml, remote.yaml, remote.svc.yaml
# fake remote svc will be create
# nginx2.default.svc.cluster.local
# shutdown the remote service
kubectl scale --replicas=0 deployment/nginx2
# watch the pod probe based on remote call will restart or not
watch kubecli get po
```

# perl ( it does not work )
```perl
'sleep(rand(10));my $code = `curl --max-time 15 -L -o /dev/null -s -w "%{http_code}\n" http://nginx2.default.svc.cluster.local`;if ($code == "200"){exit 0}else{exit 1};'
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

# liveness
```go
# reference:
https://github.com/kubernetes/kubernetes/blob/master/pkg/probe/exec/exec.go#L50

# try it in ur self
package main

import (
        "log"
        "os/exec"
        "strings"
)

func main() {
        var sb strings.Builder
        cmd := exec.Command("/bin/bash", "-c", "SLEEP_TIME=$(shuf -i 2-10 -n 1);echo $SLEEP_TIME")
        cmd.Stdout=&sb
        err := cmd.Start()
        if err != nil {
                log.Fatal(err)
        }
        log.Printf("Waiting for command to finish...")
        err = cmd.Wait()
        log.Println(sb.String())
        log.Printf("Command finished with error: %v", err)
}
```

# how to debug liveness
https://medium.com/@gabytal333/kubernetes-powerful-liveness-probe-with-python-b6dd43adcf9b

# related
1. https://stackoverflow.com/questions/67276029/are-kubernetes-liveness-probe-failures-voluntary-or-involuntary-disruptions
1. https://unix.stackexchange.com/questions/94604/does-curl-have-a-timeout/94612
1. https://unix.stackexchange.com/questions/124918/how-to-check-whether-a-command-such-as-curl-completed-without-error
1. https://access.redhat.com/documentation/en-us/openshift_container_platform/3.11/html/developer_guide/dev-guide-application-health