#
# PySNMP MIB module EQLAGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLAGENT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:36:36 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, ModuleIdentity, Counter32, Integer32, enterprises, Bits, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "ModuleIdentity", "Counter32", "Integer32", "enterprises", "Bits", "iso", "Unsigned32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
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
mibBuilder.exportSymbols("EQLAGENT-MIB", eqlAgentModule=eqlAgentModule, eqlExtInetErrorEntry=eqlExtInetErrorEntry, eqlEntInetAddrType=eqlEntInetAddrType, eqlEntInetAddr=eqlEntInetAddr, eqlExtInetErrorTable=eqlExtInetErrorTable, eqlExtErrorTable=eqlExtErrorTable, eqlAgentObjects=eqlAgentObjects, eqlSNMPExtErrMsg=eqlSNMPExtErrMsg, eqlSNMPInetExtErrCode=eqlSNMPInetExtErrCode, eqlEntIpAddr=eqlEntIpAddr, eqlSNMPrid=eqlSNMPrid, eqlSNMPInetExtErrMsg=eqlSNMPInetExtErrMsg, PYSNMP_MODULE_ID=eqlAgentModule, eqlAgentConformance=eqlAgentConformance, eqlSNMPExtErrCode=eqlSNMPExtErrCode, eqlAgentInetObjects=eqlAgentInetObjects, eqlSNMPInetrid=eqlSNMPInetrid, eqlAgentNotifications=eqlAgentNotifications, eqlExtErrorEntry=eqlExtErrorEntry)
