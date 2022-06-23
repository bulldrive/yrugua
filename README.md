# [Company name]:
"As we discussed in our phone call today, here is the home assignment..."  
[...]
---
  Solution:
1. Download the repo
  - git clone git@github.com:bulldrive/yrugua.git
  - cd yrugua
2. Build the docker image
  - the first way
    * docker --log-level "debug" build --tag bulldrive/yrugua:dev .
    * docker run -d -p 9003:9003 bulldrive/yrugua:dev
    * curl localhost:9003 (reply is: try "/get_variable" or "/healthy")
  - the second way
    * you can use the script dockerbuild.sh
3. skiped
4. How to deploy it to kubernetes
  - the first way (kubectl)
    * kubectl apply -f k8s/
    * curl http://[EXTERNAL-IP]
    * curl http://[EXTERNAL-IP]/get_variable
    * curl http://[EXTERNAL-IP]/healthy
  - the second way (helm)
    * cd yrugua; helm install yrugua . -f values.yaml --namespace yrugua
