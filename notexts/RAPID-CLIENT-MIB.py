#
# PySNMP MIB module RAPID-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-CLIENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:51 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, TimeTicks, ObjectIdentity, enterprises, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, NotificationType, Counter32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "enterprises", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "NotificationType", "Counter32", "IpAddress", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsClientMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 2))
if mibBuilder.loadTexts: rsClientMIB.setStatus('current')
rsClientDHCPServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1))
if mibBuilder.loadTexts: rsClientDHCPServer.setStatus('current')
rsClientDHCPClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2))
if mibBuilder.loadTexts: rsClientDHCPClient.setStatus('current')
rsClientPPPoEClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3))
if mibBuilder.loadTexts: rsClientPPPoEClient.setStatus('current')
rsClientDHCPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerEnable.setStatus('current')
rsClientDHCPServerStartIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerStartIpAddress.setStatus('current')
rsClientDHCPServerEndIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerEndIpAddress.setStatus('current')
rsClientDHCPServerLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerLeaseTime.setStatus('current')
rsClientDHCPServerNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerNum.setStatus('current')
rsClientDHCPServerConnTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6), )
if mibBuilder.loadTexts: rsClientDHCPServerConnTable.setStatus('current')
rsClientDHCPServerRelayServer = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerRelayServer.setStatus('current')
rsClientDHCPServerConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1), ).setIndexNames((0, "RAPID-CLIENT-MIB", "rsClientDHCPServerConnIPAddr"))
if mibBuilder.loadTexts: rsClientDHCPServerConnEntry.setStatus('current')
rsClientDHCPServerConnClientHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerConnClientHostName.setStatus('current')
rsClientDHCPServerConnIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerConnIPAddr.setStatus('current')
rsClientDHCPServerConnMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerConnMACAddr.setStatus('current')
rsClientDHCPServerConnLeaseTimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerConnLeaseTimeStart.setStatus('current')
rsClientDHCPServerConnLeaseTimeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPServerConnLeaseTimeEnd.setStatus('current')
rsClientDHCPClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPClientEnable.setStatus('current')
rsClientDHCPClientDomainName = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPClientDomainName.setStatus('current')
rsClientDHCPClientDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPClientDefaultGateway.setStatus('current')
rsClientDHCPClientDNSOne = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPClientDNSOne.setStatus('current')
rsClientDHCPClientDNSTwo = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientDHCPClientDNSTwo.setStatus('current')
rsClientPPPoEClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientEnable.setStatus('current')
rsClientPPPoEClientADSLStatus = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disconnect", 0), ("initialize", 1), ("establish", 2), ("authenticate", 3), ("network", 4), ("running", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientADSLStatus.setStatus('current')
rsClientPPPoEClientLocalIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientLocalIPAddr.setStatus('current')
rsClientPPPoEClientRemoteIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientRemoteIPAddr.setStatus('current')
rsClientPPPoEClientNetMask = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientNetMask.setStatus('current')
rsClientPPPoEClientDNSOne = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientDNSOne.setStatus('current')
rsClientPPPoEClientDNSTwo = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientDNSTwo.setStatus('current')
rsClientPPPoEADSLPeerMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEADSLPeerMACAddr.setStatus('current')
rsClientPPPoEClientConnTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsClientPPPoEClientConnTime.setStatus('current')
mibBuilder.exportSymbols("RAPID-CLIENT-MIB", rsClientDHCPClient=rsClientDHCPClient, rsClientDHCPServerEnable=rsClientDHCPServerEnable, rsClientDHCPClientDNSOne=rsClientDHCPClientDNSOne, rsClientPPPoEClientConnTime=rsClientPPPoEClientConnTime, rsClientPPPoEClientDNSOne=rsClientPPPoEClientDNSOne, rsClientPPPoEClientLocalIPAddr=rsClientPPPoEClientLocalIPAddr, rsClientMIB=rsClientMIB, rsClientDHCPServerConnIPAddr=rsClientDHCPServerConnIPAddr, rsClientDHCPServerRelayServer=rsClientDHCPServerRelayServer, rsClientDHCPClientDefaultGateway=rsClientDHCPClientDefaultGateway, rsClientDHCPServerConnLeaseTimeEnd=rsClientDHCPServerConnLeaseTimeEnd, rsClientPPPoEClientEnable=rsClientPPPoEClientEnable, rsClientDHCPServer=rsClientDHCPServer, rsClientDHCPClientDomainName=rsClientDHCPClientDomainName, rsClientDHCPServerConnTable=rsClientDHCPServerConnTable, rsClientDHCPServerConnClientHostName=rsClientDHCPServerConnClientHostName, rsClientPPPoEClientADSLStatus=rsClientPPPoEClientADSLStatus, rsClientPPPoEClientNetMask=rsClientPPPoEClientNetMask, rsClientPPPoEClient=rsClientPPPoEClient, PYSNMP_MODULE_ID=rsInfoModule, rsClientDHCPServerLeaseTime=rsClientDHCPServerLeaseTime, rsClientPPPoEClientDNSTwo=rsClientPPPoEClientDNSTwo, rsClientPPPoEADSLPeerMACAddr=rsClientPPPoEADSLPeerMACAddr, rsClientPPPoEClientRemoteIPAddr=rsClientPPPoEClientRemoteIPAddr, rsClientDHCPServerEndIpAddress=rsClientDHCPServerEndIpAddress, rsClientDHCPServerConnEntry=rsClientDHCPServerConnEntry, rsClientDHCPServerConnMACAddr=rsClientDHCPServerConnMACAddr, rsInfoModule=rsInfoModule, rsClientDHCPClientEnable=rsClientDHCPClientEnable, rsClientDHCPServerConnLeaseTimeStart=rsClientDHCPServerConnLeaseTimeStart, rsClientDHCPClientDNSTwo=rsClientDHCPClientDNSTwo, rsClientDHCPServerStartIpAddress=rsClientDHCPServerStartIpAddress, rsClientDHCPServerNum=rsClientDHCPServerNum)
