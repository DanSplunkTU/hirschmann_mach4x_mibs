#
# PySNMP MIB module NBS-USER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-USER-SESSION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:30:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ModuleIdentity, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, IpAddress, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
nbsUserSessionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 218))
if mibBuilder.loadTexts: nbsUserSessionMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsUserSessionMib.setOrganization('MRV')
nbsUserSessionGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 218, 1))
if mibBuilder.loadTexts: nbsUserSessionGrp.setStatus('current')
nbsUserSessionTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 218, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionTableSize.setStatus('current')
nbsUserSessionTable = MibTable((1, 3, 6, 1, 4, 1, 629, 218, 1, 2), )
if mibBuilder.loadTexts: nbsUserSessionTable.setStatus('current')
nbsUserSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1), ).setIndexNames((0, "NBS-USER-SESSION-MIB", "nbsUserSessionPID"))
if mibBuilder.loadTexts: nbsUserSessionEntry.setStatus('current')
nbsUserSessionPID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: nbsUserSessionPID.setStatus('current')
nbsUserSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsUserSessionRowStatus.setStatus('current')
nbsUserSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("runLvl", 1), ("bootTime", 2), ("newTime", 3), ("oldTime", 4), ("initProcess", 5), ("loginProcess", 6), ("userProcess", 7), ("deadProcess", 8), ("accounting", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionType.setStatus('current')
nbsUserSessionLine = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionLine.setStatus('current')
nbsUserSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionId.setStatus('current')
nbsUserSessionUser = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionUser.setStatus('current')
nbsUserSessionHost = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionHost.setStatus('current')
nbsUserSessionConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionConnectTime.setStatus('current')
nbsUserSessionVia = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 0), ("console", 1), ("ssh", 2), ("telnet", 3), ("api", 4), ("snmp", 5), ("gui", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionVia.setStatus('current')
mibBuilder.exportSymbols("NBS-USER-SESSION-MIB", nbsUserSessionEntry=nbsUserSessionEntry, nbsUserSessionVia=nbsUserSessionVia, nbsUserSessionTable=nbsUserSessionTable, nbsUserSessionPID=nbsUserSessionPID, nbsUserSessionMib=nbsUserSessionMib, nbsUserSessionLine=nbsUserSessionLine, nbsUserSessionType=nbsUserSessionType, nbsUserSessionGrp=nbsUserSessionGrp, nbsUserSessionRowStatus=nbsUserSessionRowStatus, nbsUserSessionTableSize=nbsUserSessionTableSize, nbsUserSessionId=nbsUserSessionId, nbsUserSessionHost=nbsUserSessionHost, nbsUserSessionUser=nbsUserSessionUser, nbsUserSessionConnectTime=nbsUserSessionConnectTime, PYSNMP_MODULE_ID=nbsUserSessionMib)
