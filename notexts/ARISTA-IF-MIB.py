#
# PySNMP MIB module ARISTA-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-IF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:15:19 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, ObjectIdentity, iso, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, NotificationType, Bits, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "iso", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 15))
aristaIfMIB.setRevisions(('2014-10-09 00:00',))
if mibBuilder.loadTexts: aristaIfMIB.setLastUpdated('201410090000Z')
if mibBuilder.loadTexts: aristaIfMIB.setOrganization('Arista Networks, Inc.')
aristaIf = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1))
aristaIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1), )
if mibBuilder.loadTexts: aristaIfTable.setStatus('current')
aristaIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaIfEntry.setStatus('current')
aristaIfCounterLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfCounterLastUpdated.setStatus('current')
aristaIfRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRateInterval.setStatus('current')
aristaIfInPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInPktRate.setStatus('current')
aristaIfOutPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutPktRate.setStatus('current')
aristaIfInOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInOctetRate.setStatus('current')
aristaIfOutOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 6), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutOctetRate.setStatus('current')
aristaIfRatesLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRatesLastUpdated.setStatus('current')
aristaIfOperStatusChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOperStatusChanges.setStatus('current')
aristaIfInAclDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInAclDrops.setStatus('current')
aristaIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2))
aristaIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1))
aristaIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2))
aristaIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfAdditionalInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfCompliance = aristaIfCompliance.setStatus('current')
aristaIfAdditionalInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfCounterLastUpdated"), ("ARISTA-IF-MIB", "aristaIfRateInterval"), ("ARISTA-IF-MIB", "aristaIfInPktRate"), ("ARISTA-IF-MIB", "aristaIfOutPktRate"), ("ARISTA-IF-MIB", "aristaIfInOctetRate"), ("ARISTA-IF-MIB", "aristaIfOutOctetRate"), ("ARISTA-IF-MIB", "aristaIfRatesLastUpdated"), ("ARISTA-IF-MIB", "aristaIfOperStatusChanges"), ("ARISTA-IF-MIB", "aristaIfInAclDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfAdditionalInformationGroup = aristaIfAdditionalInformationGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-IF-MIB", aristaIfOutPktRate=aristaIfOutPktRate, aristaIfTable=aristaIfTable, aristaIfCompliance=aristaIfCompliance, PYSNMP_MODULE_ID=aristaIfMIB, aristaIfInOctetRate=aristaIfInOctetRate, aristaIfGroups=aristaIfGroups, aristaIfRateInterval=aristaIfRateInterval, aristaIfMIB=aristaIfMIB, aristaIfEntry=aristaIfEntry, aristaIfInPktRate=aristaIfInPktRate, aristaIfOutOctetRate=aristaIfOutOctetRate, aristaIfInAclDrops=aristaIfInAclDrops, aristaIfAdditionalInformationGroup=aristaIfAdditionalInformationGroup, aristaIf=aristaIf, aristaIfCounterLastUpdated=aristaIfCounterLastUpdated, aristaIfConformance=aristaIfConformance, aristaIfRatesLastUpdated=aristaIfRatesLastUpdated, aristaIfOperStatusChanges=aristaIfOperStatusChanges, aristaIfCompliances=aristaIfCompliances)
