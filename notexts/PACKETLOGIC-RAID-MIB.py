#
# PySNMP MIB module PACKETLOGIC-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-RAID-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:18:25 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, ObjectIdentity, Bits, NotificationType, MibIdentifier, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Gauge32, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "Unsigned32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
raid = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1))
raid.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: raid.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: raid.setOrganization('Procera Networks, Inc.')
raidCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1))
ld = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3), )
if mibBuilder.loadTexts: ld.setStatus('current')
ldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "ldEntryIndex"))
if mibBuilder.loadTexts: ldEntry.setStatus('current')
ldEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ldEntryIndex.setStatus('current')
disk = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4), )
if mibBuilder.loadTexts: disk.setStatus('current')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "diskEntryIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
diskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: diskEntryIndex.setStatus('current')
adpNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpNumber.setStatus('current')
ldNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldNumber.setStatus('current')
diskNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('current')
ldId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldId.setStatus('current')
ldState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldState.setStatus('current')
diskId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskId.setStatus('current')
diskState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskState.setStatus('current')
diskLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskLabel.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-RAID-MIB", ldNumber=ldNumber, diskNumber=diskNumber, diskId=diskId, diskEntryIndex=diskEntryIndex, ldState=ldState, ld=ld, diskEntry=diskEntry, raidCfg=raidCfg, raid=raid, adpNumber=adpNumber, ldEntry=ldEntry, ldId=ldId, diskLabel=diskLabel, PYSNMP_MODULE_ID=raid, ldEntryIndex=ldEntryIndex, diskState=diskState, disk=disk)
