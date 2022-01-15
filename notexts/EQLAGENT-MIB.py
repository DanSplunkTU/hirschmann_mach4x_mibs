#
# PySNMP MIB module EQLAGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLAGENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:01:56 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, ObjectIdentity, enterprises, Unsigned32, MibIdentifier, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ModuleIdentity, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ObjectIdentity", "enterprises", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ModuleIdentity", "Integer32", "NotificationType", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
eqlAgentModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 12))
eqlAgentModule.setRevisions(('2002-11-11 00:00',))
if mibBuilder.loadTexts: eqlAgentModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlAgentModule.setOrganization('EqualLogic Inc.')
eqlAgentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 1))
eqlAgentNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 2))
eqlAgentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 3))
eqlAgentInetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 4))
eqlExtErrorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1), )
if mibBuilder.loadTexts: eqlExtErrorTable.setStatus('current')
eqlExtErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1), ).setIndexNames((0, "EQLAGENT-MIB", "eqlEntIpAddr"), (0, "EQLAGENT-MIB", "eqlSNMPrid"))
if mibBuilder.loadTexts: eqlExtErrorEntry.setStatus('current')
eqlEntIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: eqlEntIpAddr.setStatus('current')
eqlSNMPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPrid.setStatus('current')
eqlSNMPExtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPExtErrCode.setStatus('current')
eqlSNMPExtErrMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPExtErrMsg.setStatus('current')
eqlExtInetErrorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4), )
if mibBuilder.loadTexts: eqlExtInetErrorTable.setStatus('current')
eqlExtInetErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1), ).setIndexNames((0, "EQLAGENT-MIB", "eqlEntInetAddrType"), (0, "EQLAGENT-MIB", "eqlEntInetAddr"), (0, "EQLAGENT-MIB", "eqlSNMPInetrid"))
if mibBuilder.loadTexts: eqlExtInetErrorEntry.setStatus('current')
eqlEntInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: eqlEntInetAddrType.setStatus('current')
eqlEntInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: eqlEntInetAddr.setStatus('current')
eqlSNMPInetrid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetrid.setStatus('current')
eqlSNMPInetExtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetExtErrCode.setStatus('current')
eqlSNMPInetExtErrMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetExtErrMsg.setStatus('current')
mibBuilder.exportSymbols("EQLAGENT-MIB", eqlSNMPInetExtErrMsg=eqlSNMPInetExtErrMsg, eqlSNMPInetrid=eqlSNMPInetrid, eqlExtErrorEntry=eqlExtErrorEntry, eqlExtInetErrorTable=eqlExtInetErrorTable, eqlAgentNotifications=eqlAgentNotifications, eqlSNMPExtErrCode=eqlSNMPExtErrCode, eqlSNMPExtErrMsg=eqlSNMPExtErrMsg, eqlAgentObjects=eqlAgentObjects, eqlExtErrorTable=eqlExtErrorTable, PYSNMP_MODULE_ID=eqlAgentModule, eqlEntIpAddr=eqlEntIpAddr, eqlAgentConformance=eqlAgentConformance, eqlExtInetErrorEntry=eqlExtInetErrorEntry, eqlAgentModule=eqlAgentModule, eqlEntInetAddr=eqlEntInetAddr, eqlSNMPInetExtErrCode=eqlSNMPInetExtErrCode, eqlSNMPrid=eqlSNMPrid, eqlEntInetAddrType=eqlEntInetAddrType, eqlAgentInetObjects=eqlAgentInetObjects)
