# aci-rest-api-test

```
usage: rest-api-test.py [-h] [--file FILE] [--apicIPs APICIPS [APICIPS ...]]

Generate

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           file with API request URLs
  --apicIPs APICIPS [APICIPS ...]
                        APIC IPs
```


## Example

```
python rest-api-test.py --file rqlist.txt --apicIPs 10.66.80.162 10.66.80.163
['10.66.80.162', '10.66.80.163']
Username: diqiu
Password:
######### 10.66.80.162 ########
Request: /aaaLogin.json
<Response [200]>
Elapsed time: 0.0932159423828seconds

Request: /api/node/class/topSystem.json?rsp-subtree-include=health,required

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 561224
Response received at: 2018-06-06 06:52:55 566144
Elapsed time: 0.00492000579834seconds

Request: /api/node/mo/topology/health.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 566373
Response received at: 2018-06-06 06:52:55 569384
Elapsed time: 0.00301098823547seconds

Request: /api/node/mo/fltCnts.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 569494
Response received at: 2018-06-06 06:52:55 572271
Elapsed time: 0.00277709960938seconds

Request: /api/node/mo/topology/HDfabricOverallHealth5min-0.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 572380
Response received at: 2018-06-06 06:52:55 575259
Elapsed time: 0.00287890434265seconds

Request: /api/node/class/compProv.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 575370
Response received at: 2018-06-06 06:52:55 578347
Elapsed time: 0.00297689437866seconds

Request: /api/node/mo/info.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 578458
Response received at: 2018-06-06 06:52:55 581333
Elapsed time: 0.00287485122681seconds

Request: /api/aaaRefresh.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 581442
Response received at: 2018-06-06 06:52:55 584408
Elapsed time: 0.00296592712402seconds

Request: /api/node/class/polUni.json?target-subtree-class=aaaUserEp,aaaLdapEp,aaaRadiusEp,aaaTacacsPlusEp,aaaSamlEp,aaaAuthRealm,aaaFabricSec,pkiExportEncryptionKey&query-target=subtree

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 584516
Response received at: 2018-06-06 06:52:55 587471
Elapsed time: 0.00295495986938seconds

Request: /api/node/mo/uni/userext.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 587583
Response received at: 2018-06-06 06:52:55 590516
Elapsed time: 0.00293302536011seconds

######### 10.66.80.163 ########
Request: /aaaLogin.json
<Response [200]>
Elapsed time: 0.086168050766seconds

Request: /api/node/class/topSystem.json?rsp-subtree-include=health,required

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 676902
Response received at: 2018-06-06 06:52:55 680335
Elapsed time: 0.00343298912048seconds

Request: /api/node/mo/topology/health.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 680452
Response received at: 2018-06-06 06:52:55 683498
Elapsed time: 0.00304579734802seconds

Request: /api/node/mo/fltCnts.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 683609
Response received at: 2018-06-06 06:52:55 686681
Elapsed time: 0.00307202339172seconds

Request: /api/node/mo/topology/HDfabricOverallHealth5min-0.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 686793
Response received at: 2018-06-06 06:52:55 690514
Elapsed time: 0.00372099876404seconds

Request: /api/node/class/compProv.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 690735
Response received at: 2018-06-06 06:52:55 695299
Elapsed time: 0.00456380844116seconds

Request: /api/node/mo/info.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 695482
Response received at: 2018-06-06 06:52:55 699056
Elapsed time: 0.00357389450073seconds

Request: /api/aaaRefresh.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 699165
Response received at: 2018-06-06 06:52:55 702063
Elapsed time: 0.00289797782898seconds

Request: /api/node/class/polUni.json?target-subtree-class=aaaUserEp,aaaLdapEp,aaaRadiusEp,aaaTacacsPlusEp,aaaSamlEp,aaaAuthRealm,aaaFabricSec,pkiExportEncryptionKey&query-target=subtree

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 702172
Response received at: 2018-06-06 06:52:55 705236
Elapsed time: 0.00306391716003seconds

Request: /api/node/mo/uni/userext.json

<Response [400]>
Request sent out at: 2018-06-06 06:52:55 705346
Response received at: 2018-06-06 06:52:55 708337
Elapsed time: 0.00299096107483seconds
```

## Example Input File

```
/api/node/class/topSystem.json?rsp-subtree-include=health,required
/api/node/mo/topology/health.json
/api/node/mo/fltCnts.json
/api/node/mo/topology/HDfabricOverallHealth5min-0.json
/api/node/class/compProv.json
/api/node/mo/info.json
/api/aaaRefresh.json
/api/node/class/polUni.json?target-subtree-class=aaaUserEp,aaaLdapEp,aaaRadiusEp,aaaTacacsPlusEp,aaaSamlEp,aaaAuthRealm,aaaFabricSec,pkiExportEncryptionKey&query-target=subtree
/api/node/mo/uni/userext.json
```
