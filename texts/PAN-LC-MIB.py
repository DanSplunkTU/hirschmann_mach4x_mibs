#
# PySNMP MIB module PAN-LC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-LC-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:27 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
panProductsMibs, panModules = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panProductsMibs", "panModules")
panM_100, = mibBuilder.importSymbols("PAN-PRODUCTS-MIB", "panM-100")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, TimeTicks, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, Counter64, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
panLogCollectorMibsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 6))
panLogCollectorMibsModule.setRevisions(('2012-01-11 10:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panLogCollectorMibsModule.setRevisionsDescriptions(('\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module PAN-LC-MIB.',))
if mibBuilder.loadTexts: panLogCollectorMibsModule.setLastUpdated('201201111013Z')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tPalo Alto Networks\n\t\t\t\t\t4401 Great America Pkwy\n\t\t\t\t\tSanta Clara, CA 95054-1211\n\n\t\t\t\t\t+1 866-898-9087\n\t\t\t\t\tsupport at paloaltonetworks dot com')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setDescription('\n\t\t\tA MIB module containing definitions of managed objects\n\t\t\timplemented by Log Collector Appliances from Palo Alto Networks.')
panLcStat = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1))
if mibBuilder.loadTexts: panLcStat.setStatus('current')
if mibBuilder.loadTexts: panLcStat.setDescription('\n\t\t\tSub-tree for the Log collection statistics.')
panLcLogRate = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogRate.setStatus('current')
if mibBuilder.loadTexts: panLcLogRate.setDescription('The write rate in logs/s on the Log Collection')
panLcLogDuration = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2))
if mibBuilder.loadTexts: panLcLogDuration.setStatus('current')
if mibBuilder.loadTexts: panLcLogDuration.setDescription('\n\t\t\tSub-tree for the Log Duration on the Log Collector. Log \n            Duration is Expressed in Days of storage.')
panLcDiskUsage = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3))
if mibBuilder.loadTexts: panLcDiskUsage.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsage.setDescription('\n\t\t\tSub-tree for the Log Disk Usage on the Log Collector. Log\n            Disk Usage is available as MB in use.')
panLcDiskUsageLd1 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd1.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd1.setDescription('The Log disk usage on logical disk 1 on the Log Collector')
panLcDiskUsageLd2 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd2.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd2.setDescription('The Log disk usage on logical disk 2 on the Log Collector')
panLcDiskUsageLd3 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd3.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd3.setDescription('The Log disk usage on logical disk 3 on the Log Collector')
panLcDiskUsageLd4 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd4.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd4.setDescription('The Log disk usage on logical disk 4 on the Log Collector')
panLcLogDurationTraffic = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTraffic.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationTraffic.setDescription('The Log duration (in days) for the traffic logs on the Log Collector')
panLcLogDurationConfig = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationConfig.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationConfig.setDescription('The Log duration (in days) for the config logs on the Log Collector')
panLcLogDurationSystem = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationSystem.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationSystem.setDescription('The Log duration (in days) for the system logs on the Log Collector')
panLcLogDurationThreat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThreat.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationThreat.setDescription('The Log duration (in days) for the threat logs on the Log Collector')
panLcLogDurationAppstat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAppstat.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationAppstat.setDescription('The Log duration (in days) for the appstat logs on the Log Collector')
panLcLogDurationTrsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTrsum.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationTrsum.setDescription('The Log duration (in days) for the trsum logs on the Log Collector')
panLcLogDurationThsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThsum.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationThsum.setDescription('The Log duration (in days) for the thsum logs on the Log Collector')
panLcLogDurationEvent = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationEvent.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationEvent.setDescription('The Log duration (in days) for the event logs on the Log Collector')
panLcLogDurationAlarm = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAlarm.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationAlarm.setDescription('The Log duration (in days) for the alarm logs on the Log Collector')
panLcLogDurationHipmatch = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationHipmatch.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationHipmatch.setDescription('The Log duration (in days) for the hipmatch logs on the Log Collector')
panLcLogDurationUserid = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationUserid.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationUserid.setDescription('The Log duration (in days) for the userid logs on the Log Collector')
panLcIsRedundancyMember = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcIsRedundancyMember.setStatus('current')
if mibBuilder.loadTexts: panLcIsRedundancyMember.setDescription('True value indicates this Log Collector is part of a Collector Group with Redundancy is enabled')
mibBuilder.exportSymbols("PAN-LC-MIB", panLcLogDurationAlarm=panLcLogDurationAlarm, panLcLogDurationTraffic=panLcLogDurationTraffic, panLcLogDuration=panLcLogDuration, panLcLogDurationThsum=panLcLogDurationThsum, panLcIsRedundancyMember=panLcIsRedundancyMember, panLcLogDurationUserid=panLcLogDurationUserid, panLcLogDurationTrsum=panLcLogDurationTrsum, panLcLogDurationThreat=panLcLogDurationThreat, PYSNMP_MODULE_ID=panLogCollectorMibsModule, panLcLogDurationConfig=panLcLogDurationConfig, panLcLogRate=panLcLogRate, panLcLogDurationSystem=panLcLogDurationSystem, panLcDiskUsageLd4=panLcDiskUsageLd4, panLcDiskUsageLd1=panLcDiskUsageLd1, panLogCollectorMibsModule=panLogCollectorMibsModule, panLcDiskUsage=panLcDiskUsage, panLcDiskUsageLd3=panLcDiskUsageLd3, panLcLogDurationEvent=panLcLogDurationEvent, panLcLogDurationHipmatch=panLcLogDurationHipmatch, panLcLogDurationAppstat=panLcLogDurationAppstat, panLcDiskUsageLd2=panLcDiskUsageLd2, panLcStat=panLcStat)
