#
# PySNMP MIB module NETGEAR-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netgear/NETGEAR-REF-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:18 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, iso, IpAddress, Counter64, ObjectIdentity, Gauge32, Counter32, Integer32, Unsigned32, Bits, ModuleIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "iso", "IpAddress", "Counter64", "ObjectIdentity", "Gauge32", "Counter32", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: broadcom.setRevisionsDescriptions(('Netgear branding related changes.', 'Revisions made for new release.', 'Updated for release',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Netgear Inc')
if mibBuilder.loadTexts: broadcom.setContactInfo('')
if mibBuilder.loadTexts: broadcom.setDescription('')
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
managedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
vpnrouter = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 2))
carrier = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 3))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4))
rps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 5))
wlanswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 6))
fsm726s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 1))
fsm750s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 2))
gsm712 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 3))
fsm726 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 4))
gsm712f = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 5))
fsm726v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 10))
me103 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 1))
wg302 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2))
wg102 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 3))
wag302 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 4))
wag102 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 5))
wg302v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 6))
wag302v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 7))
wls538 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 6, 1))
gsm7312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6))
gsm7324 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 7))
gsm7224 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 8))
fsm7326p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 9))
ng7000managedswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10))
ng700smartswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 11))
ngrouter = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 12))
ngfirewall = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 13))
ngap = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 14))
ngwlan = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 15))
ng9000chassisswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 16))
ng700stacksmartswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 17))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100))
stackswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1))
l2switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2))
l3switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3))
smartswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4))
l2Rswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6))
accesspoint = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7))
wirelessLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 8))
chassisswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 9))
stacksmartswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10))
fsm7328s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 1))
fsm7352s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 2))
gsm7328s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 3))
gsm7352s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 4))
fsm7352ps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 5))
fsm7328ps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 8))
gsm7328fs = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 7))
gsm7228ps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 9))
gsm7252ps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 10))
fsm7226rs = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 11))
fsm7250rs = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 12))
gsm7328se = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 13))
gsm7352se = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 14))
xsm7224s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 15))
m530028gpoe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 16))
m530052gpoe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 17))
m530028g3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 18))
m530052g3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 19))
m530028gf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 20))
m530028g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 21))
m530052g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 22))
gsm7312v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 1))
gsm7324v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 2))
xsm7312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 3))
gsm7324p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 4))
gsm7224r = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 1))
gsm7248r = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 2))
gsm7224rp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 3))
gsm7248rp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 4))
gsm7224v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 5))
gsm7248v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 6))
gsm7212f = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 7))
gsm5212p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 8))
gsm7212p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 9))
gsm7224p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 10))
m4100_26g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 16)).setLabel("m4100-26g")
m4100_50g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 17)).setLabel("m4100-50g")
m4100_26_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 18)).setLabel("m4100-26-poe")
m4100_26g_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 19)).setLabel("m4100-26g-poe")
m4100_50g_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 20)).setLabel("m4100-50g-poe")
m4100_50_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 21)).setLabel("m4100-50-poe")
m4100_d12g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 22)).setLabel("m4100-d12g")
m4100_d10_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 23)).setLabel("m4100-d10-poe")
m4100_12gf = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 24)).setLabel("m4100-12gf")
m4100_d12g_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 25)).setLabel("m4100-d12g-poe")
m4100_12g_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 26)).setLabel("m4100-12g-poe")
m4100_24g_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 11, 27)).setLabel("m4100-24g-poe")
gsm7312i = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 5))
gsm7324i = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 6))
fsm7326pi = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 7))
gsm7248 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 1))
gsm7212 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 2))
gsm7224i = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 3))
fsm7226 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 4))
gcm9000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 9, 1))
xcm8903 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 9, 6))
gs748t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 1))
fs726t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 2))
gs716t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 3))
fs750t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 4))
gs724t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 5))
fs726tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 6))
fs728tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 7))
gs108t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 8))
gs108tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 9))
gs724tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 10))
gs748tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 11))
gs724tr = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 12))
gs748tr = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 13))
gs716tv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 16))
gs724tv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 17))
gs108tv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 18))
gs110tp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 19))
fs728tpv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 20))
gs716tv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 31))
gs724tv4 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 32))
gs748tv5 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 33))
xs712t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 30))
fs728ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 1))
fs752ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 2))
fs752tps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 3))
gs724ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 4))
gs748ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 5))
gs752ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 12))
gs728ts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 11))
gs752tstps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 8))
gs728tps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 13))
gs752tps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 14))
gs752txs = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 10))
gs728txs = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 15))
s3300_28x = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 16)).setLabel("s3300-28x")
s3300_28x_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 17)).setLabel("s3300-28x-poe")
s3300_52x = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 18)).setLabel("s3300-52x")
s3300_52x_poe = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 10, 19)).setLabel("s3300-52x-poe")
fvx538 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 1))
fvs338 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 2))
fvg318 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 3))
fvs336g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 4))
fwag114 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6, 3))
fvs124g = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6, 4))
fvs318v3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6, 5))
dgfv338 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6, 6))
wpn802 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7, 1))
wg312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7, 2))
wag312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7, 3))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight\n        ports, with the first octet specifying ports 1 through\n        8, the second octet specifying ports 9 through 16, etc.\n        Within each octet, the most significant bit represents\n        the lowest numbered port, and the least significant bit\n        represents the highest numbered port.  Thus, each port\n        of the bridge is represented by a single bit within the\n        value of this object.  If that bit has a value of '1'\n        then that port is included in the set of ports; the port\n        is not included if its bit has a value of '0'\n             \n        When setting this value, the system will ignore \n        configuration for ports not between the first and last \n        valid ports.  Configuration of any port numbers between \n        this range that are not valid ports return a failure \n        message, but will still apply configuration for valid \n        ports."
    status = 'current'

mibBuilder.exportSymbols("NETGEAR-REF-MIB", gsm7224i=gsm7224i, fs750t=fs750t, gsm7228ps=gsm7228ps, fsm7352ps=fsm7352ps, wg102=wg102, fsm7328s=fsm7328s, fs726t=fs726t, gs716tv3=gs716tv3, fs752tps=fs752tps, ng700stacksmartswitch=ng700stacksmartswitch, gsm7248rp=gsm7248rp, fwag114=fwag114, m4100_d12g_poe=m4100_d12g_poe, wag302=wag302, gs752ts=gs752ts, xsm7224s=xsm7224s, wireless=wireless, xsm7312=xsm7312, gs728ts=gs728ts, l3switch=l3switch, gs752tstps=gs752tstps, gsm712=gsm712, chassisswitch=chassisswitch, m530028g3=m530028g3, gsm7328s=gsm7328s, m4100_d10_poe=m4100_d10_poe, stackswitch=stackswitch, gs108tp=gs108tp, fs752ts=fs752ts, fvs124g=fvs124g, gs748t=gs748t, dgfv338=dgfv338, gs724ts=gs724ts, router=router, gs724tp=gs724tp, fvs318v3=fvs318v3, gsm7352s=gsm7352s, gsm7312v2=gsm7312v2, gsm712f=gsm712f, ngrouter=ngrouter, m530028gf3=m530028gf3, wag102=wag102, broadcom=broadcom, m4100_12gf=m4100_12gf, xs712t=xs712t, ngwlan=ngwlan, netgear=netgear, smartswitch=smartswitch, fsm726v2=fsm726v2, gs728txs=gs728txs, vpnrouter=vpnrouter, m4100_26g_poe=m4100_26g_poe, fvx538=fvx538, wirelessLAN=wirelessLAN, ng700smartswitch=ng700smartswitch, gsm7324i=gsm7324i, fs728tpv2=fs728tpv2, stacksmartswitch=stacksmartswitch, wpn802=wpn802, gs724tv4=gs724tv4, gs752tps=gs752tps, s3300_52x_poe=s3300_52x_poe, gsm7212p=gsm7212p, gcm9000=gcm9000, wag312=wag312, gs724tr=gs724tr, gsm7328fs=gsm7328fs, gsm5212p=gsm5212p, fsm7326pi=fsm7326pi, gs752txs=gs752txs, gs728tps=gs728tps, fvs336g=fvs336g, accesspoint=accesspoint, gs110tp=gs110tp, ng7000managedswitch=ng7000managedswitch, fs728ts=fs728ts, m4100_50g=m4100_50g, wg312=wg312, l2Rswitch=l2Rswitch, gsm7324=gsm7324, gsm7248v2=gsm7248v2, wag302v2=wag302v2, gsm7212f=gsm7212f, gs748tv5=gs748tv5, wls538=wls538, ng9000chassisswitch=ng9000chassisswitch, fsm7352s=fsm7352s, gs108tv2=gs108tv2, s3300_52x=s3300_52x, m530052g=m530052g, fs726tp=fs726tp, fsm7328ps=fsm7328ps, gs748ts=gs748ts, xcm8903=xcm8903, gs716t=gs716t, s3300_28x=s3300_28x, ngap=ngap, fsm7250rs=fsm7250rs, m4100_50g_poe=m4100_50g_poe, gs724tv3=gs724tv3, s3300_28x_poe=s3300_28x_poe, gsm7224p=gsm7224p, productID=productID, firewall=firewall, wlanswitch=wlanswitch, fsm7226rs=fsm7226rs, gsm7324v2=gsm7324v2, fsm750s=fsm750s, gsm7252ps=gsm7252ps, AgentPortMask=AgentPortMask, gsm7312i=gsm7312i, PYSNMP_MODULE_ID=broadcom, gs108t=gs108t, fvg318=fvg318, carrier=carrier, m4100_26_poe=m4100_26_poe, gsm7328se=gsm7328se, gs716tv2=gs716tv2, m4100_50_poe=m4100_50_poe, wg302=wg302, gsm7224r=gsm7224r, fsm726s=fsm726s, fsm726=fsm726, wg302v2=wg302v2, m530028g=m530028g, managedSwitch=managedSwitch, gsm7212=gsm7212, m4100_d12g=m4100_d12g, rps=rps, m530052gpoe=m530052gpoe, ngfirewall=ngfirewall, gsm7352se=gsm7352se, m530052g3=m530052g3, gsm7248r=gsm7248r, l2switch=l2switch, gs748tr=gs748tr, gsm7324p=gsm7324p, fsm7326p=fsm7326p, gs724t=gs724t, gsm7224v2=gsm7224v2, gs748tp=gs748tp, fs728tp=fs728tp, gsm7248=gsm7248, gsm7224rp=gsm7224rp, m4100_12g_poe=m4100_12g_poe, gsm7224=gsm7224, m4100_26g=m4100_26g, m530028gpoe=m530028gpoe, fvs338=fvs338, gsm7312=gsm7312, fsm7226=fsm7226, me103=me103, m4100_24g_poe=m4100_24g_poe)
