#
# PySNMP MIB module IB-DNSONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DNSONE-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:39:45 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ibDNSOne, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDNSOne", "IbString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, NotificationType, Gauge32, Integer32, Unsigned32, MibIdentifier, IpAddress, enterprises, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "NotificationType", "Gauge32", "Integer32", "Unsigned32", "MibIdentifier", "IpAddress", "enterprises", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibDnsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1))
ibDnsModule.setRevisions(('2010-03-23 00:00', '2005-06-09 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))
if mibBuilder.loadTexts: ibDnsModule.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: ibDnsModule.setOrganization('Infoblox')
ibZoneStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ibZoneStatisticsTable.setStatus('current')
ibZoneStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "IB-DNSONE-MIB", "ibBindZoneName"))
if mibBuilder.loadTexts: ibZoneStatisticsEntry.setStatus('current')
ibBindZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneName.setStatus('current')
ibBindZoneSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneSuccess.setStatus('current')
ibBindZoneReferral = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneReferral.setStatus('current')
ibBindZoneNxRRset = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneNxRRset.setStatus('current')
ibBindZoneNxDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneNxDomain.setStatus('current')
ibBindZoneRecursion = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneRecursion.setStatus('current')
ibBindZoneFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneFailure.setStatus('current')
ibZonePlusViewStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2), )
if mibBuilder.loadTexts: ibZonePlusViewStatisticsTable.setStatus('current')
ibZonePlusViewStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1), ).setIndexNames((0, "IB-DNSONE-MIB", "ibBindViewName"), (0, "IB-DNSONE-MIB", "ibBindZonePlusViewName"))
if mibBuilder.loadTexts: ibZonePlusViewStatisticsEntry.setStatus('current')
ibBindZonePlusViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewName.setStatus('current')
ibBindZonePlusViewSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewSuccess.setStatus('current')
ibBindZonePlusViewReferral = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewReferral.setStatus('current')
ibBindZonePlusViewNxRRset = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewNxRRset.setStatus('current')
ibBindZonePlusViewNxDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewNxDomain.setStatus('current')
ibBindZonePlusViewRecursion = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewRecursion.setStatus('current')
ibBindZonePlusViewFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewFailure.setStatus('current')
ibBindViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 8), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindViewName.setStatus('current')
ibDDNSUpdateStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3))
ibDDNSUpdateSuccess = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateSuccess.setStatus('current')
ibDDNSUpdateFailure = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateFailure.setStatus('current')
ibDDNSUpdateReject = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateReject.setStatus('current')
ibDDNSUpdatePrerequisiteReject = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdatePrerequisiteReject.setStatus('current')
ibBindZoneTransferCount = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneTransferCount.setStatus('current')
mibBuilder.exportSymbols("IB-DNSONE-MIB", ibDDNSUpdatePrerequisiteReject=ibDDNSUpdatePrerequisiteReject, ibBindZonePlusViewName=ibBindZonePlusViewName, ibBindZoneNxRRset=ibBindZoneNxRRset, ibBindZonePlusViewRecursion=ibBindZonePlusViewRecursion, ibDDNSUpdateSuccess=ibDDNSUpdateSuccess, ibZoneStatisticsEntry=ibZoneStatisticsEntry, ibDnsModule=ibDnsModule, ibDDNSUpdateStatistics=ibDDNSUpdateStatistics, ibZonePlusViewStatisticsEntry=ibZonePlusViewStatisticsEntry, ibDDNSUpdateFailure=ibDDNSUpdateFailure, ibDDNSUpdateReject=ibDDNSUpdateReject, ibBindZoneRecursion=ibBindZoneRecursion, ibBindZonePlusViewFailure=ibBindZonePlusViewFailure, ibBindViewName=ibBindViewName, PYSNMP_MODULE_ID=ibDnsModule, ibBindZonePlusViewNxRRset=ibBindZonePlusViewNxRRset, ibBindZoneFailure=ibBindZoneFailure, ibBindZonePlusViewReferral=ibBindZonePlusViewReferral, ibBindZoneSuccess=ibBindZoneSuccess, ibBindZonePlusViewNxDomain=ibBindZonePlusViewNxDomain, ibBindZoneReferral=ibBindZoneReferral, ibZoneStatisticsTable=ibZoneStatisticsTable, ibBindZoneNxDomain=ibBindZoneNxDomain, ibBindZoneTransferCount=ibBindZoneTransferCount, ibBindZonePlusViewSuccess=ibBindZonePlusViewSuccess, ibZonePlusViewStatisticsTable=ibZonePlusViewStatisticsTable, ibBindZoneName=ibBindZoneName)
