import requests,time, getpass, datetime, argparse
import urllib3


parser=argparse.ArgumentParser(description='Generate')
parser.add_argument('--file',dest='file',action='store',default=None,help='inputfile')
parser.add_argument('--apicIPs',dest='apicIPs', nargs='+', action='store',default=None,help='inputfile')
args=parser.parse_args()

f=open(args.file,'r')
requestList = []
for rqline in f:
    requestList.append(rqline)

"""
requestList = [ '/api/node/class/topSystem.json?rsp-subtree-include=health,required',
                '/api/node/mo/topology/health.json',
                '/api/node/mo/fltCnts.json',
                '/api/node/mo/topology/HDfabricOverallHealth5min-0.json',
                '/api/node/class/compProv.json',
                '/api/node/mo/info.json,'
                '/api/aaaRefresh.json',
                '/api/node/class/polUni.json?target-subtree-class=aaaUserEp,aaaLdapEp,aaaRadiusEp,aaaTacacsPlusEp,aaaSamlEp,aaaAuthRealm,aaaFabricSec,pkiExportEncryptionKey&query-target=subtree',
                '/api/node/mo/uni/userext.json'
               ]
"""


urllib3.disable_warnings()
s = requests.Session()
apicIPs = args.apicIPs



ip = "place holder"
"""
print("Please type in your IP address, hit ENTER if finished")
while(ip is not ""):
    ip = raw_input('APIC IP address:')
    if (ip is not ""):
        apicIPs.append(ip)
print('Your APIC IP address: ')
"""
print(apicIPs)

usr = raw_input('Username: ')
pwd = getpass.getpass('Password:')

loginBody = '{"aaaUser" : {"attributes" : { "name" : "'\
                + usr +    '", "pwd" : "'\
                + pwd + '"}}}'

for apicIP in apicIPs:
    print('######### ' + apicIP + ' ########')
    startTime = time.time()
    response = s.post('https://' + apicIP + '/api/aaaLogin.json', data=loginBody, verify=False)
    elapsedTime = time.time() - startTime
    print("Request: " + "/aaaLogin.json")
    print(response)
    print("Elapsed time: " + str(elapsedTime) +"seconds")
    print("")
    for rq in requestList:
        startTime = time.time()
        response = s.get('https://'+apicIP + rq, verify=False)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print("Request: " + rq)
        print(response)
        print("Request sent out at: "+ datetime.datetime.fromtimestamp(startTime).strftime("%Y-%m-%d %H:%M:%S %f"))
        print("Response received at: " + datetime.datetime.fromtimestamp(endTime).strftime("%Y-%m-%d %H:%M:%S %f"))
        print("Elapsed time: "+ str(elapsedTime)+" seconds")
        print("")