#
# PySNMP MIB module NBS-USER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-USER-SESSION-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:01 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Integer32, Counter64, Bits, Counter32, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Integer32", "Counter64", "Bits", "Counter32", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
nbsUserSessionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 218))
if mibBuilder.loadTexts: nbsUserSessionMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsUserSessionMib.setOrganization('MRV')
if mibBuilder.loadTexts: nbsUserSessionMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsUserSessionMib.setDescription('MIB for representing MRV User Session information')
nbsUserSessionGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 218, 1))
if mibBuilder.loadTexts: nbsUserSessionGrp.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionGrp.setDescription('User Session MIB')
nbsUserSessionTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 218, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionTableSize.setDescription('The number of rows in the nbsUserSession table')
nbsUserSessionTable = MibTable((1, 3, 6, 1, 4, 1, 629, 218, 1, 2), )
if mibBuilder.loadTexts: nbsUserSessionTable.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionTable.setDescription('A table describing the user sessions')
nbsUserSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1), ).setIndexNames((0, "NBS-USER-SESSION-MIB", "nbsUserSessionPID"))
if mibBuilder.loadTexts: nbsUserSessionEntry.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionEntry.setDescription('Contains the information describing a UI Session')
nbsUserSessionPID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: nbsUserSessionPID.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionPID.setDescription('The process id of the task servicing this session.')
nbsUserSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsUserSessionRowStatus.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionRowStatus.setDescription('Writing destroy(6) to this object will destroy the session.\n           It is only allowed when nbsUserSessionType is\n           userProcess(7).')
nbsUserSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("runLvl", 1), ("bootTime", 2), ("newTime", 3), ("oldTime", 4), ("initProcess", 5), ("loginProcess", 6), ("userProcess", 7), ("deadProcess", 8), ("accounting", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionType.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionType.setDescription('This object follows the ut_type entry in struct utmp.')
nbsUserSessionLine = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionLine.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionLine.setDescription('Device name of the tty being used by this session.')
nbsUserSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionId.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionId.setDescription('This object follows the ut_type entry in struct utmp.')
nbsUserSessionUser = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionUser.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionUser.setDescription('The name of the user using this session.')
nbsUserSessionHost = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionHost.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionHost.setDescription('Hostname of the remote IP from which the user is originating.')
nbsUserSessionConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionConnectTime.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionConnectTime.setDescription('This object indicates the time the entry was created, in\n           seconds, since the Epoch, 1970-01-01 00:00:00 (UTC). It will\n           wrap around at 03:14:07 2038-01-19 (UTC).')
nbsUserSessionVia = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 0), ("console", 1), ("ssh", 2), ("telnet", 3), ("api", 4), ("snmp", 5), ("gui", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsUserSessionVia.setStatus('current')
if mibBuilder.loadTexts: nbsUserSessionVia.setDescription('This object indicates the type of session. Note that this\n           field is decided by the system, and is not stored in the\n           utmp file.')
mibBuilder.exportSymbols("NBS-USER-SESSION-MIB", nbsUserSessionHost=nbsUserSessionHost, nbsUserSessionVia=nbsUserSessionVia, nbsUserSessionRowStatus=nbsUserSessionRowStatus, nbsUserSessionId=nbsUserSessionId, nbsUserSessionType=nbsUserSessionType, nbsUserSessionEntry=nbsUserSessionEntry, nbsUserSessionTableSize=nbsUserSessionTableSize, nbsUserSessionUser=nbsUserSessionUser, nbsUserSessionPID=nbsUserSessionPID, nbsUserSessionConnectTime=nbsUserSessionConnectTime, nbsUserSessionLine=nbsUserSessionLine, nbsUserSessionGrp=nbsUserSessionGrp, nbsUserSessionMib=nbsUserSessionMib, nbsUserSessionTable=nbsUserSessionTable, PYSNMP_MODULE_ID=nbsUserSessionMib)
