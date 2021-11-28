#
# PySNMP MIB module AT-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-RESOURCE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:24:49 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Bits, ModuleIdentity, Counter32, MibIdentifier, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Bits", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
resource = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21))
resource.setRevisions(('2014-05-26 00:00', '2014-04-30 00:00', '2014-04-16 00:00', '2012-09-21 00:00', '2012-05-22 03:00', '2010-06-15 00:15', '2009-10-22 23:00', '2008-10-20 10:00', '1920-08-09 04:00',))
if mibBuilder.loadTexts: resource.setLastUpdated('201405260000Z')
if mibBuilder.loadTexts: resource.setOrganization('Allied Telesis, Inc.')
rscBoardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1), )
if mibBuilder.loadTexts: rscBoardTable.setStatus('current')
rscBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"), (0, "AT-RESOURCE-MIB", "rscResourceId"))
if mibBuilder.loadTexts: rscBoardEntry.setStatus('current')
rscStkId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: rscStkId.setStatus('current')
rscResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rscResourceId.setStatus('current')
rscBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardType.setStatus('current')
rscBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardName.setStatus('current')
rscBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardID.setStatus('current')
rscBoardBay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscBoardBay.setStatus('current')
rscBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardRevision.setStatus('current')
rscBoardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardSerialNumber.setStatus('current')
hostInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2), )
if mibBuilder.loadTexts: hostInfoTable.setStatus('current')
hostInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"))
if mibBuilder.loadTexts: hostInfoEntry.setStatus('current')
hostInfoDRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoDRAM.setStatus('current')
hostInfoFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoFlash.setStatus('current')
hostInfoUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoUptime.setStatus('current')
hostInfoBootloaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoBootloaderVersion.setStatus('current')
mibBuilder.exportSymbols("AT-RESOURCE-MIB", rscStkId=rscStkId, rscBoardEntry=rscBoardEntry, hostInfoDRAM=hostInfoDRAM, hostInfoBootloaderVersion=hostInfoBootloaderVersion, hostInfoUptime=hostInfoUptime, rscBoardID=rscBoardID, rscBoardTable=rscBoardTable, rscBoardSerialNumber=rscBoardSerialNumber, hostInfoEntry=hostInfoEntry, rscBoardType=rscBoardType, rscBoardBay=rscBoardBay, rscBoardRevision=rscBoardRevision, PYSNMP_MODULE_ID=resource, hostInfoTable=hostInfoTable, rscBoardName=rscBoardName, hostInfoFlash=hostInfoFlash, rscResourceId=rscResourceId, resource=resource)
