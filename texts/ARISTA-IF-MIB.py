#
# PySNMP MIB module ARISTA-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-IF-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:09:48 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, ModuleIdentity, Counter32, iso, Bits, TimeTicks, MibIdentifier, NotificationType, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "iso", "Bits", "TimeTicks", "MibIdentifier", "NotificationType", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 15))
aristaIfMIB.setRevisions(('2014-10-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaIfMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: aristaIfMIB.setLastUpdated('201410090000Z')
if mibBuilder.loadTexts: aristaIfMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaIfMIB.setContactInfo('Arista Networks, Inc.\n\n         Postal: 5453 Great America Parkway\n                 Santa Clara, CA 95054\n\n         Tel: +1 408 547-5500\n\n         E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaIfMIB.setDescription('The MIB module for reporting additional interface statistics\n            on Arista devices.')
aristaIf = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1))
aristaIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1), )
if mibBuilder.loadTexts: aristaIfTable.setStatus('current')
if mibBuilder.loadTexts: aristaIfTable.setDescription('This table contains additional interface statistics not\n                contained in the IF-MIB.')
aristaIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaIfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaIfEntry.setDescription('An entry containing statistics for a given interface.')
aristaIfCounterLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfCounterLastUpdated.setStatus('current')
if mibBuilder.loadTexts: aristaIfCounterLastUpdated.setDescription('The value of sysUpTime at which the counters in the ifTable and ifXTable\n        were sampled from the hardware.')
aristaIfRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRateInterval.setStatus('current')
if mibBuilder.loadTexts: aristaIfRateInterval.setDescription('The amount of time over which the aristaIf*Rate values\n        are averaged for this interface.')
aristaIfInPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInPktRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfInPktRate.setDescription('The rate, in packets per second, of packets inbound on\n        this interface, averaged over aristaIfRateInterval.')
aristaIfOutPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutPktRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfOutPktRate.setDescription('The rate, in packets per second, of packets outbound on\n        this interface, averaged over aristaIfRateInterval.')
aristaIfInOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInOctetRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfInOctetRate.setDescription('The rate, in octets per second, of data inbound on\n        this interface, averaged over aristaIfRateInterval.')
aristaIfOutOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 6), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutOctetRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfOutOctetRate.setDescription('The rate, in octets per second, of data inbound on\n        this interface, averaged over aristaIfRateInterval.')
aristaIfRatesLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRatesLastUpdated.setStatus('current')
if mibBuilder.loadTexts: aristaIfRatesLastUpdated.setDescription('The value of sysUpTime at which the aristaIf*Rate gauges were\n        last calculated.')
aristaIfOperStatusChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOperStatusChanges.setStatus('current')
if mibBuilder.loadTexts: aristaIfOperStatusChanges.setDescription('The number of times since system boot that ifOperStatus has\n        changed.')
aristaIfInAclDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInAclDrops.setStatus('current')
if mibBuilder.loadTexts: aristaIfInAclDrops.setDescription('The number of inbound packets dropped because of an\n        Access Control List (ACL).\n\n        Discontinuities in the value of this counter can occur at\n        re-initialization of the management system, and at other\n        times as indicated by the value of\n        ifCounterDiscontinuityTime.')
aristaIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2))
aristaIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1))
aristaIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2))
aristaIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfAdditionalInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfCompliance = aristaIfCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaIfCompliance.setDescription('The compliance statement for Arista devices\n        that implement the IF-MIB')
aristaIfAdditionalInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfCounterLastUpdated"), ("ARISTA-IF-MIB", "aristaIfRateInterval"), ("ARISTA-IF-MIB", "aristaIfInPktRate"), ("ARISTA-IF-MIB", "aristaIfOutPktRate"), ("ARISTA-IF-MIB", "aristaIfInOctetRate"), ("ARISTA-IF-MIB", "aristaIfOutOctetRate"), ("ARISTA-IF-MIB", "aristaIfRatesLastUpdated"), ("ARISTA-IF-MIB", "aristaIfOperStatusChanges"), ("ARISTA-IF-MIB", "aristaIfInAclDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfAdditionalInformationGroup = aristaIfAdditionalInformationGroup.setStatus('current')
if mibBuilder.loadTexts: aristaIfAdditionalInformationGroup.setDescription('A collection of objects providing additional information\n        above and beyond what the IF-MIB provides, applicable to\n        all network interfaces.')
mibBuilder.exportSymbols("ARISTA-IF-MIB", aristaIf=aristaIf, aristaIfAdditionalInformationGroup=aristaIfAdditionalInformationGroup, aristaIfInAclDrops=aristaIfInAclDrops, aristaIfInOctetRate=aristaIfInOctetRate, aristaIfMIB=aristaIfMIB, aristaIfGroups=aristaIfGroups, PYSNMP_MODULE_ID=aristaIfMIB, aristaIfEntry=aristaIfEntry, aristaIfOutPktRate=aristaIfOutPktRate, aristaIfOutOctetRate=aristaIfOutOctetRate, aristaIfCompliance=aristaIfCompliance, aristaIfOperStatusChanges=aristaIfOperStatusChanges, aristaIfCounterLastUpdated=aristaIfCounterLastUpdated, aristaIfConformance=aristaIfConformance, aristaIfRatesLastUpdated=aristaIfRatesLastUpdated, aristaIfTable=aristaIfTable, aristaIfInPktRate=aristaIfInPktRate, aristaIfCompliances=aristaIfCompliances, aristaIfRateInterval=aristaIfRateInterval)
