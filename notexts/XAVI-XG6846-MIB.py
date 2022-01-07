#
# PySNMP MIB module XAVI-XG6846-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/inteno/XAVI-XG6846-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:27:50 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, snmpModules, iso, Bits, IpAddress, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Gauge32, Counter32, TimeTicks, MibIdentifier, enterprises, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "snmpModules", "iso", "Bits", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Gauge32", "Counter32", "TimeTicks", "MibIdentifier", "enterprises", "mib-2")
TimeStamp, DisplayString, TestAndIncr, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TestAndIncr", "TextualConvention")
xg6846 = MibIdentifier((1, 3, 6, 1, 4, 1, 12919))
catv = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 1))
portmode = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 2))
qos = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 3))
vlan = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 4))
portStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 5))
ddminfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 6))
internetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 7))
reboot = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 8))
tftp = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 9))
portPower = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 10))
jumb = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 11))
deviceinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 12))
catvEnable = MibScalar((1, 3, 6, 1, 4, 1, 12919, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: catvEnable.setStatus('current')
lanportTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportTable.setStatus('current')
modeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "lanportIndex"))
if mibBuilder.loadTexts: modeEntry.setStatus('current')
lanportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanportIndex.setStatus('current')
lanportName = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanportName.setStatus('current')
lanportspeed = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 0), ("speed10mFD", 1), ("speed10mHD", 2), ("speed100mFD", 3), ("speed100mHD", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportspeed.setStatus('current')
lanportpause = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportpause.setStatus('current')
qosTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 3, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosTable.setStatus('current')
qosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "qosIndex"))
if mibBuilder.loadTexts: qosEntry.setStatus('current')
qosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosIndex.setStatus('current')
qmapping = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qmapping.setStatus('current')
portTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 4, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTable.setStatus('current')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('current')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('current')
vlanid = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanid.setStatus('current')
priority = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priority.setStatus('current')
qmode = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("fallback", 1), ("check", 2), ("secure", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qmode.setStatus('current')
dscpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscpEnable.setStatus('current')
vlangroupTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 4, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlangroupTable.setStatus('current')
groupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "groupIndex"))
if mibBuilder.loadTexts: groupEntry.setStatus('current')
groupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupIndex.setStatus('current')
groupid = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: groupid.setStatus('current')
lan1 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan1.setStatus('current')
lan2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan2.setStatus('current')
lan3 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan3.setStatus('current')
lan4 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan4.setStatus('current')
wan = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wan.setStatus('current')
statisticTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 5, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: statisticTable.setStatus('current')
portStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "statIndex"))
if mibBuilder.loadTexts: portStatEntry.setStatus('current')
statIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statIndex.setStatus('current')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('current')
unicastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unicastsReceived.setStatus('current')
broadcastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadcastsReceived.setStatus('current')
multicastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastsReceived.setStatus('current')
fcsErrorReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsErrorReceived.setStatus('current')
pauseReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pauseReceived.setStatus('current')
unicastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unicastsTransmitted.setStatus('current')
broadcastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadcastsTransmitted.setStatus('current')
multicastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastsTransmitted.setStatus('current')
fcsErrorTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsErrorTransmitted.setStatus('current')
pauseTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pauseTransmitted.setStatus('current')
speed = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: speed.setStatus('current')
vendorName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
vendorOui = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorOui.setStatus('current')
vendorPn = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorPn.setStatus('current')
vendorRev = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorRev.setStatus('current')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
voltage = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage.setStatus('current')
bias = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bias.setStatus('current')
txPower = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
rxPower = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxPower.setStatus('current')
wanType = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dhcp", 1), ("staticIp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanType.setStatus('current')
hostname = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostname.setStatus('current')
domainame = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: domainame.setStatus('current')
staticDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticDns.setStatus('current')
primaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: primaryDns.setStatus('current')
secondaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondaryDns.setStatus('current')
staticIpHostName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpHostName.setStatus('current')
staticIpDomainName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpDomainName.setStatus('current')
staticIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpAddr.setStatus('current')
staticIpSubMask = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpSubMask.setStatus('current')
staticIpGateway = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpGateway.setStatus('current')
staticIpPrimaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpPrimaryDns.setStatus('current')
staticIpSecondaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpSecondaryDns.setStatus('current')
rebootEnable = MibScalar((1, 3, 6, 1, 4, 1, 12919, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rebootEnable.setStatus('current')
tftpSevIp = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpSevIp.setStatus('current')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileName.setStatus('current')
fileType = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileType.setStatus('current')
action = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: action.setStatus('current')
adminStatus = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminStatus.setStatus('current')
operStatus = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: operStatus.setStatus('current')
port1 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port1.setStatus('current')
port2 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port2.setStatus('current')
port3 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port3.setStatus('current')
port4 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port4.setStatus('current')
jumblan1 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan1.setStatus('current')
jumblan2 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan2.setStatus('current')
jumblan3 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan3.setStatus('current')
jumblan4 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan4.setStatus('current')
jumbwan = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumbwan.setStatus('current')
serialnum = MibScalar((1, 3, 6, 1, 4, 1, 12919, 12, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialnum.setStatus('current')
mibBuilder.exportSymbols("XAVI-XG6846-MIB", vlanid=vlanid, pauseTransmitted=pauseTransmitted, lanportName=lanportName, port3=port3, staticIpGateway=staticIpGateway, unicastsReceived=unicastsReceived, tftp=tftp, staticIpSecondaryDns=staticIpSecondaryDns, ddminfo=ddminfo, jumbwan=jumbwan, speed=speed, reboot=reboot, serialnum=serialnum, unicastsTransmitted=unicastsTransmitted, deviceinfo=deviceinfo, port2=port2, lan2=lan2, internetPort=internetPort, jumb=jumb, vendorName=vendorName, primaryDns=primaryDns, groupEntry=groupEntry, portName=portName, action=action, fcsErrorReceived=fcsErrorReceived, qmode=qmode, domainame=domainame, portIndex=portIndex, catvEnable=catvEnable, port1=port1, rxPower=rxPower, qosIndex=qosIndex, port4=port4, vendorPn=vendorPn, tftpSevIp=tftpSevIp, portStatistic=portStatistic, multicastsTransmitted=multicastsTransmitted, portmode=portmode, multicastsReceived=multicastsReceived, secondaryDns=secondaryDns, vendorRev=vendorRev, jumblan2=jumblan2, portTable=portTable, wanType=wanType, staticIpHostName=staticIpHostName, modeEntry=modeEntry, qosEntry=qosEntry, adminStatus=adminStatus, wan=wan, jumblan3=jumblan3, qmapping=qmapping, staticDns=staticDns, hostname=hostname, fileName=fileName, broadcastsTransmitted=broadcastsTransmitted, dscpEnable=dscpEnable, statisticTable=statisticTable, lanportpause=lanportpause, lanportspeed=lanportspeed, staticIpDomainName=staticIpDomainName, jumblan4=jumblan4, temperature=temperature, lanportTable=lanportTable, vendorOui=vendorOui, staticIpPrimaryDns=staticIpPrimaryDns, jumblan1=jumblan1, portPower=portPower, txPower=txPower, voltage=voltage, lan4=lan4, broadcastsReceived=broadcastsReceived, rebootEnable=rebootEnable, bias=bias, qos=qos, portStatEntry=portStatEntry, portEntry=portEntry, catv=catv, pauseReceived=pauseReceived, lan1=lan1, staticIpAddr=staticIpAddr, qosTable=qosTable, groupid=groupid, lan3=lan3, staticIpSubMask=staticIpSubMask, groupIndex=groupIndex, statIndex=statIndex, priority=priority, vlan=vlan, vlangroupTable=vlangroupTable, lanportIndex=lanportIndex, fileType=fileType, operStatus=operStatus, xg6846=xg6846, fcsErrorTransmitted=fcsErrorTransmitted)
