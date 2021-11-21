#
# PySNMP MIB module AT-XEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-XEM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:44:40 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, ObjectIdentity, IpAddress, Counter64, Gauge32, NotificationType, MibIdentifier, TimeTicks, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xem = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11))
xem.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2009-07-15 00:00', '2008-02-29 00:00',))
if mibBuilder.loadTexts: xem.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: xem.setOrganization('Allied Telesis, Inc.')
xemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0))
xemInserted = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 1)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInserted.setStatus('current')
xemRemoved = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 2)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemRemoved.setStatus('current')
xemInsertedFail = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 3)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInsertedFail.setStatus('current')
xemNumOfXem = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemNumOfXem.setStatus('current')
xemInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2), )
if mibBuilder.loadTexts: xemInfoTable.setStatus('current')
xemInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1), ).setIndexNames((0, "AT-XEM-MIB", "xemInfoMemberId"), (0, "AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInfoEntry.setStatus('current')
xemInfoMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoMemberId.setStatus('current')
xemInfoBayId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBayId.setStatus('current')
xemInfoXemId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoXemId.setStatus('current')
xemInfoBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardType.setStatus('current')
xemInfoBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardName.setStatus('current')
xemInfoRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoRevision.setStatus('current')
xemInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoSerialNumber.setStatus('current')
mibBuilder.exportSymbols("AT-XEM-MIB", xemInserted=xemInserted, xemInfoRevision=xemInfoRevision, xemNumOfXem=xemNumOfXem, xemRemoved=xemRemoved, xemInfoTable=xemInfoTable, xem=xem, xemInfoMemberId=xemInfoMemberId, xemInfoXemId=xemInfoXemId, xemInfoBayId=xemInfoBayId, PYSNMP_MODULE_ID=xem, xemInfoBoardType=xemInfoBoardType, xemInfoSerialNumber=xemInfoSerialNumber, xemInfoEntry=xemInfoEntry, xemInfoBoardName=xemInfoBoardName, xemInsertedFail=xemInsertedFail, xemTraps=xemTraps)
