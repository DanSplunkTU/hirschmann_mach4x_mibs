#
# PySNMP MIB module UCD-DISKIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/UCD-DISKIO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:26 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, ObjectIdentity, Counter64, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, TimeTicks, MibIdentifier, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Counter64", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "TimeTicks", "MibIdentifier", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
ucdDiskIOMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 15))
ucdDiskIOMIB.setRevisions(('2016-04-04 00:00', '2005-04-20 00:00', '2002-02-13 00:00', '2000-01-26 00:00',))
if mibBuilder.loadTexts: ucdDiskIOMIB.setLastUpdated('201604040000Z')
if mibBuilder.loadTexts: ucdDiskIOMIB.setOrganization('University of California, Davis')
diskIOTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1), )
if mibBuilder.loadTexts: diskIOTable.setStatus('current')
diskIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1), ).setIndexNames((0, "UCD-DISKIO-MIB", "diskIOIndex"))
if mibBuilder.loadTexts: diskIOEntry.setStatus('current')
diskIOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOIndex.setStatus('current')
diskIODevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIODevice.setStatus('current')
diskIONRead = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONRead.setStatus('current')
diskIONWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWritten.setStatus('current')
diskIOReads = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOReads.setStatus('current')
diskIOWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOWrites.setStatus('current')
diskIOLA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA1.setStatus('current')
diskIOLA5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA5.setStatus('current')
diskIOLA15 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA15.setStatus('current')
diskIONReadX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONReadX.setStatus('current')
diskIONWrittenX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWrittenX.setStatus('current')
diskIOBusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOBusyTime.setStatus('current')
mibBuilder.exportSymbols("UCD-DISKIO-MIB", diskIOLA15=diskIOLA15, diskIODevice=diskIODevice, diskIOLA5=diskIOLA5, diskIOEntry=diskIOEntry, diskIOBusyTime=diskIOBusyTime, diskIONWritten=diskIONWritten, diskIOReads=diskIOReads, diskIONRead=diskIONRead, diskIONReadX=diskIONReadX, diskIONWrittenX=diskIONWrittenX, diskIOTable=diskIOTable, diskIOLA1=diskIOLA1, diskIOWrites=diskIOWrites, diskIOIndex=diskIOIndex, ucdDiskIOMIB=ucdDiskIOMIB, PYSNMP_MODULE_ID=ucdDiskIOMIB)
