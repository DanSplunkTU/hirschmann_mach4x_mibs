#
# PySNMP MIB module CXR-TS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cxr-networks/CXR-TS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:58:20 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
DisplayString, = mibBuilder.importSymbols("RFC-1213", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, Counter32, MibIdentifier, IpAddress, iso, Bits, Gauge32, Counter64, ObjectIdentity, NotificationType, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "iso", "Bits", "Gauge32", "Counter64", "ObjectIdentity", "NotificationType", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxr = MibIdentifier((1, 3, 6, 1, 4, 1, 1425))
ts = MibIdentifier((1, 3, 6, 1, 4, 1, 1425, 1040))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 1425, 1040, 1))
productName = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('mandatory')
if mibBuilder.loadTexts: productName.setDescription('Product Name')
version = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('mandatory')
if mibBuilder.loadTexts: version.setDescription('Revision')
bootp = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bootp.setStatus('mandatory')
if mibBuilder.loadTexts: bootp.setDescription('Bootp')
mainIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mainIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mainIpAddress.setDescription('IP address')
ipNetmask = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipNetmask.setStatus('mandatory')
if mibBuilder.loadTexts: ipNetmask.setDescription('IP Netmask')
ipGateway = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipGateway.setStatus('mandatory')
if mibBuilder.loadTexts: ipGateway.setDescription('IP Gateway')
ethernetAddress = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetAddress.setDescription('Mac Address')
ftpdService = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ftpdService.setStatus('mandatory')
if mibBuilder.loadTexts: ftpdService.setDescription('FTPD Service')
httpdService = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpdService.setStatus('mandatory')
if mibBuilder.loadTexts: httpdService.setDescription('HTTPD Service')
telnetdService = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetdService.setStatus('mandatory')
if mibBuilder.loadTexts: telnetdService.setDescription('TELNETD Service')
snmpdService = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpdService.setStatus('mandatory')
if mibBuilder.loadTexts: snmpdService.setDescription('SNMPD Service')
snmpTrap = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrap.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrap.setDescription('SNMP Traps')
snmpTrapAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapAddr1.setDescription('Trap IP Address')
snmpTrapAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapAddr2.setDescription('Trap IP Address')
nameResolution = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nameResolution.setStatus('mandatory')
if mibBuilder.loadTexts: nameResolution.setDescription('Names Resolution')
nameServer1 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nameServer1.setStatus('mandatory')
if mibBuilder.loadTexts: nameServer1.setDescription('Names Server 1')
nameServer2 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nameServer2.setStatus('mandatory')
if mibBuilder.loadTexts: nameServer2.setDescription('Names Server 1')
radiusServer1 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusServer1.setStatus('mandatory')
if mibBuilder.loadTexts: radiusServer1.setDescription('Radius Server 1')
radiusSecret1 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSecret1.setStatus('mandatory')
if mibBuilder.loadTexts: radiusSecret1.setDescription('Secret for Radius Server 1')
radiusServer2 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusServer2.setStatus('mandatory')
if mibBuilder.loadTexts: radiusServer2.setDescription('Radius Server 2')
radiusSecret2 = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSecret2.setStatus('mandatory')
if mibBuilder.loadTexts: radiusSecret2.setDescription('Secret for Radius Server 2')
siteName = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: siteName.setStatus('mandatory')
if mibBuilder.loadTexts: siteName.setDescription('String indetifier for TS')
resetByButton = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetByButton.setStatus('mandatory')
if mibBuilder.loadTexts: resetByButton.setDescription('Reset by button Enable ot Disable')
reset = MibScalar((1, 3, 6, 1, 4, 1, 1425, 1040, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reset.setStatus('mandatory')
if mibBuilder.loadTexts: reset.setDescription('Reset the TS')
portTable = MibTable((1, 3, 6, 1, 4, 1, 1425, 1040, 2), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
if mibBuilder.loadTexts: portTable.setDescription('A table containing all the ports')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1), ).setIndexNames((0, "CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portEntry.setDescription('Port index 1 to 11 possible')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portIndex.setDescription('Port Index')
tcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: tcpPort.setDescription('TCP port')
aliasIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aliasIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: aliasIpAddress.setDescription('Alias IP address')
aliasIpNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aliasIpNetmask.setStatus('mandatory')
if mibBuilder.loadTexts: aliasIpNetmask.setDescription('Alias IP netmask')
timeoutRxTx = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeoutRxTx.setStatus('mandatory')
if mibBuilder.loadTexts: timeoutRxTx.setDescription('Timeout No rx/Tx Data(min)')
baudRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("b300", 1), ("b600", 2), ("b1200", 3), ("b2400", 4), ("b4800", 5), ("b9600", 6), ("b19200", 7), ("b38400", 8), ("b57600", 9), ("b115200", 10), ("b50", 11), ("b200", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: baudRate.setStatus('mandatory')
if mibBuilder.loadTexts: baudRate.setDescription('Baud rate')
nbParStop = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 17, 18, 33, 34, 49, 50, 65, 66, 129, 130, 145, 146, 161, 162, 177, 178, 193, 194))).clone(namedValues=NamedValues(("p7Odd1", 1), ("p7Odd2", 2), ("p7Even1", 17), ("p7Even2", 18), ("p7None1", 33), ("p7None2", 34), ("p7High1", 49), ("p7High2", 50), ("p7Low1", 65), ("p7Low2", 66), ("p8Odd1", 129), ("p8Odd2", 130), ("p8Even1", 145), ("p8Even2", 146), ("p8None1", 161), ("p8None2", 162), ("p8High1", 177), ("p8High2", 178), ("p8Low1", 193), ("p8Low2", 194)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbParStop.setStatus('mandatory')
if mibBuilder.loadTexts: nbParStop.setDescription('Nb bits/Parity/Nb stop bits')
ipServer = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("passive", 2), ("passiveExclusive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipServer.setStatus('mandatory')
if mibBuilder.loadTexts: ipServer.setDescription('Server IP')
remoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: remoteIpAddress.setDescription('Remote IP address')
gatewayToRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gatewayToRemote.setStatus('mandatory')
if mibBuilder.loadTexts: gatewayToRemote.setDescription('Gateway to remote')
remoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: remoteTcpPort.setDescription('remote TCP port')
flowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noFlowControl", 1), ("xonXoff", 2), ("rtsCts", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowControl.setStatus('mandatory')
if mibBuilder.loadTexts: flowControl.setDescription('Flow Control')
mode = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("rfc2217", 1), ("msgFormat", 2), ("carrierBreak", 3), ("telex", 4), ("rlogin", 5), ("lpd", 6), ("telnet", 7), ("rawIp", 8), ("rtelnet", 9), ("pad", 10), ("muxv24", 11), ("modbus", 12), ("hnzs2", 13), ("hnzs5", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mode.setStatus('mandatory')
if mibBuilder.loadTexts: mode.setDescription('Fonctionnement')
rxIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rxIdle.setStatus('mandatory')
if mibBuilder.loadTexts: rxIdle.setDescription('Rx Idle')
txIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: txIdle.setStatus('mandatory')
if mibBuilder.loadTexts: txIdle.setDescription('Tx Idle')
endMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: endMsg.setStatus('mandatory')
if mibBuilder.loadTexts: endMsg.setDescription('End msg character')
interFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interFrame.setStatus('mandatory')
if mibBuilder.loadTexts: interFrame.setDescription('Time Inter Frame(modem mode)')
beforeSend = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: beforeSend.setStatus('mandatory')
if mibBuilder.loadTexts: beforeSend.setDescription('Time Before Send(modem mode)')
afterSend = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: afterSend.setStatus('mandatory')
if mibBuilder.loadTexts: afterSend.setDescription('Time After Send(modem mode)')
timeoutPAD = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeoutPAD.setStatus('mandatory')
if mibBuilder.loadTexts: timeoutPAD.setDescription('Timeout PAD(modem PAD)')
terminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("console", 1), ("linux", 2), ("aixterm", 3), ("dec-vt100", 4), ("vt100", 5), ("vt200", 6), ("vt420", 7), ("xterm", 8), ("xterms", 9), ("xtermc", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: terminalType.setStatus('mandatory')
if mibBuilder.loadTexts: terminalType.setDescription('Terminal Type')
multiSession = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: multiSession.setStatus('mandatory')
if mibBuilder.loadTexts: multiSession.setDescription('multiSession')
authType = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remote", 1), ("radius", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authType.setStatus('mandatory')
if mibBuilder.loadTexts: authType.setDescription('Authentication type')
authRad1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authRad1.setStatus('mandatory')
if mibBuilder.loadTexts: authRad1.setDescription('Use Server Radius 1 for auth.')
authRad2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authRad2.setStatus('mandatory')
if mibBuilder.loadTexts: authRad2.setDescription('Use Server Radius 2 for auth.')
acctRad1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctRad1.setStatus('mandatory')
if mibBuilder.loadTexts: acctRad1.setDescription('Use Server Radius 1 for acct.')
acctRad2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctRad2.setStatus('mandatory')
if mibBuilder.loadTexts: acctRad2.setDescription('Use Server Radius 2 for acct.')
formFeed = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: formFeed.setStatus('mandatory')
if mibBuilder.loadTexts: formFeed.setDescription('LPD form Feed')
secondIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 29), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: secondIpAddress.setDescription('Second IP address')
secondGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 30), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondGateway.setStatus('mandatory')
if mibBuilder.loadTexts: secondGateway.setDescription('Second Gateway')
secondTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: secondTcpPort.setDescription('Second TCP port')
modbusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rtu", 1), ("ascii", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modbusMode.setStatus('mandatory')
if mibBuilder.loadTexts: modbusMode.setDescription('Modbus Mode')
modbusType = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("slave", 1), ("master", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modbusType.setStatus('mandatory')
if mibBuilder.loadTexts: modbusType.setDescription('Modbus Type')
portReset = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 2, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portReset.setStatus('mandatory')
if mibBuilder.loadTexts: portReset.setDescription('Apply changes to port')
portStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1425, 1040, 3), )
if mibBuilder.loadTexts: portStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: portStatsTable.setDescription('A table containing all the statistics ports')
portStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1425, 1040, 3, 1), ).setIndexNames((0, "CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: portStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portStatsEntry.setDescription('Port index 1 to 11 possible')
bytesReceiveFromV24 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bytesReceiveFromV24.setStatus('mandatory')
if mibBuilder.loadTexts: bytesReceiveFromV24.setDescription('Bytes received from V24')
bytesSendToV24 = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bytesSendToV24.setStatus('mandatory')
if mibBuilder.loadTexts: bytesSendToV24.setDescription('Bytes send to V24')
statusDTR = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusDTR.setStatus('mandatory')
if mibBuilder.loadTexts: statusDTR.setDescription('DTR Status')
modbusTable = MibTable((1, 3, 6, 1, 4, 1, 1425, 1040, 4), )
if mibBuilder.loadTexts: modbusTable.setStatus('mandatory')
if mibBuilder.loadTexts: modbusTable.setDescription('Master modbus table containing all the slave parameters table')
modbusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1425, 1040, 4, 1), ).setIndexNames((0, "CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: modbusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: modbusEntry.setDescription('Slave index 1 to 16 possible')
slaveHexaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slaveHexaAddress.setStatus('mandatory')
if mibBuilder.loadTexts: slaveHexaAddress.setDescription('Modbus Hexadecimal address')
slaveIPaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slaveIPaddr.setStatus('mandatory')
if mibBuilder.loadTexts: slaveIPaddr.setDescription('Modbus IP address')
slaveIPport = MibTableColumn((1, 3, 6, 1, 4, 1, 1425, 1040, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slaveIPport.setStatus('mandatory')
if mibBuilder.loadTexts: slaveIPport.setDescription('Modbus IP Port')
sessionStarted = NotificationType((1, 3, 6, 1, 4, 1, 1425) + (0,1041)).setObjects(("CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: sessionStarted.setDescription('Session Begin')
sessionStopped = NotificationType((1, 3, 6, 1, 4, 1, 1425) + (0,1042)).setObjects(("CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: sessionStopped.setDescription('Session End')
dtrUp = NotificationType((1, 3, 6, 1, 4, 1, 1425) + (0,1043)).setObjects(("CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: dtrUp.setDescription('DTR UP')
dtrDown = NotificationType((1, 3, 6, 1, 4, 1, 1425) + (0,1044)).setObjects(("CXR-TS-MIB", "portIndex"))
if mibBuilder.loadTexts: dtrDown.setDescription('DTR DOWN')
mibBuilder.exportSymbols("CXR-TS-MIB", afterSend=afterSend, remoteIpAddress=remoteIpAddress, nameServer2=nameServer2, baudRate=baudRate, ftpdService=ftpdService, rxIdle=rxIdle, dtrUp=dtrUp, formFeed=formFeed, ethernetAddress=ethernetAddress, aliasIpAddress=aliasIpAddress, sessionStopped=sessionStopped, bootp=bootp, portIndex=portIndex, sessionStarted=sessionStarted, siteName=siteName, txIdle=txIdle, authType=authType, acctRad1=acctRad1, statusDTR=statusDTR, modbusMode=modbusMode, portReset=portReset, interFrame=interFrame, slaveIPaddr=slaveIPaddr, secondGateway=secondGateway, mainIpAddress=mainIpAddress, radiusSecret1=radiusSecret1, reset=reset, remoteTcpPort=remoteTcpPort, telnetdService=telnetdService, authRad1=authRad1, radiusSecret2=radiusSecret2, tcpPort=tcpPort, ipServer=ipServer, timeoutRxTx=timeoutRxTx, ts=ts, portStatsEntry=portStatsEntry, cxr=cxr, snmpTrapAddr1=snmpTrapAddr1, system=system, secondTcpPort=secondTcpPort, httpdService=httpdService, resetByButton=resetByButton, ipNetmask=ipNetmask, modbusEntry=modbusEntry, productName=productName, modbusTable=modbusTable, ipGateway=ipGateway, mode=mode, bytesSendToV24=bytesSendToV24, timeoutPAD=timeoutPAD, snmpTrapAddr2=snmpTrapAddr2, acctRad2=acctRad2, nameResolution=nameResolution, version=version, snmpTrap=snmpTrap, secondIpAddress=secondIpAddress, endMsg=endMsg, radiusServer2=radiusServer2, snmpdService=snmpdService, radiusServer1=radiusServer1, authRad2=authRad2, flowControl=flowControl, beforeSend=beforeSend, modbusType=modbusType, gatewayToRemote=gatewayToRemote, dtrDown=dtrDown, portStatsTable=portStatsTable, aliasIpNetmask=aliasIpNetmask, nbParStop=nbParStop, nameServer1=nameServer1, terminalType=terminalType, slaveHexaAddress=slaveHexaAddress, portEntry=portEntry, multiSession=multiSession, bytesReceiveFromV24=bytesReceiveFromV24, portTable=portTable, slaveIPport=slaveIPport)
