#
# PySNMP MIB module ARRIS-C3-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-STATS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:37 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
docsIfCmtsServiceEntry, = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsServiceEntry")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Integer32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Gauge32, Counter32, ObjectIdentity, Unsigned32, iso, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Gauge32", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "enterprises", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmtsC3StatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1))
if mibBuilder.loadTexts: cmtsC3StatsMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3StatsMIB.setOrganization('Arris International')
dcxUpstreamStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1))
dcxUpstreamStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1), )
if mibBuilder.loadTexts: dcxUpstreamStatsTable.setStatus('current')
dcxUpstreamStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-STATS-MIB", "dcxUsStatsIfIndex"))
if mibBuilder.loadTexts: dcxUpstreamStatsEntry.setStatus('current')
dcxUsStatsOther = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsOther.setStatus('current')
dcxUsStatsRanging = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsRanging.setStatus('current')
dcxUsStatsRngAborted = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsRngAborted.setStatus('current')
dcxUsStatsRngComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsRngComplete.setStatus('current')
dcxUsStatsIpComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsIpComplete.setStatus('current')
dcxUsStatsRegComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsRegComplete.setStatus('current')
dcxUsStatsAccessDenied = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsAccessDenied.setStatus('current')
dcxUsStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxUsStatsIfIndex.setStatus('current')
dcxCmtsServiceStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2))
dcxCmtsServiceTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1), )
if mibBuilder.loadTexts: dcxCmtsServiceTable.setStatus('current')
dcxCmtsServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1), )
docsIfCmtsServiceEntry.registerAugmentions(("ARRIS-C3-STATS-MIB", "dcxCmtsServiceEntry"))
dcxCmtsServiceEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())
if mibBuilder.loadTexts: dcxCmtsServiceEntry.setStatus('current')
dcxCmtsServiceOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxCmtsServiceOutOctets.setStatus('current')
dcxCmtsServiceOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxCmtsServiceOutPackets.setStatus('current')
cdxCmtsServiceUpBWExcessReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdxCmtsServiceUpBWExcessReqs.setStatus('current')
cdxCmtsServiceDownBWExcessPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdxCmtsServiceDownBWExcessPkts.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-STATS-MIB", cdxCmtsServiceDownBWExcessPkts=cdxCmtsServiceDownBWExcessPkts, dcxUpstreamStatsObjects=dcxUpstreamStatsObjects, dcxUsStatsOther=dcxUsStatsOther, dcxCmtsServiceStatsObjects=dcxCmtsServiceStatsObjects, dcxUsStatsRanging=dcxUsStatsRanging, dcxUsStatsIfIndex=dcxUsStatsIfIndex, dcxCmtsServiceEntry=dcxCmtsServiceEntry, PYSNMP_MODULE_ID=cmtsC3StatsMIB, dcxUsStatsRegComplete=dcxUsStatsRegComplete, cdxCmtsServiceUpBWExcessReqs=cdxCmtsServiceUpBWExcessReqs, dcxUpstreamStatsEntry=dcxUpstreamStatsEntry, dcxUsStatsRngComplete=dcxUsStatsRngComplete, dcxUsStatsIpComplete=dcxUsStatsIpComplete, dcxCmtsServiceTable=dcxCmtsServiceTable, dcxCmtsServiceOutPackets=dcxCmtsServiceOutPackets, dcxUsStatsAccessDenied=dcxUsStatsAccessDenied, dcxUpstreamStatsTable=dcxUpstreamStatsTable, cmtsC3StatsMIB=cmtsC3StatsMIB, dcxCmtsServiceOutOctets=dcxCmtsServiceOutOctets, dcxUsStatsRngAborted=dcxUsStatsRngAborted)
