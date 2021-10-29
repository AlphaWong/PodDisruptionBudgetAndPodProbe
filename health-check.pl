#!/usr/bin/perl

sleep(rand(10))
my $code=`curl --max-time 15 -L -v http://nginx2.default.svc.cluster.local`
print rindex($code, "HTTP/1.1 200 OK")
# if (index($code,'HTTP/1.1 200 OK') == -1){
#   exit 1
# } else {
#   exit 0
# };