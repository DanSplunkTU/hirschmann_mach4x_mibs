#
# PySNMP MIB module PT-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-PM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:06 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, ModuleIdentity, Gauge32, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ptPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 5))
ptPM.setRevisions(('2018-08-29 12:30', '2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptPM.setLastUpdated('201808291230Z')
if mibBuilder.loadTexts: ptPM.setOrganization('Ericsson')
ptPMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2))
ptPMTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1), )
if mibBuilder.loadTexts: ptPMTable.setStatus('current')
ptPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1), ).setIndexNames((0, "PT-PM-MIB", "queueIndex"))
if mibBuilder.loadTexts: ptPMEntry.setStatus('current')
queueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: queueIndex.setStatus('current')
forwardingPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingPacket.setStatus('current')
forwardingOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingOctets.setStatus('current')
discardPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardPackets.setStatus('current')
discardOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardOctets.setStatus('current')
inputPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputPackets.setStatus('current')
inputOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputOctets.setStatus('current')
ptPMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1))
ptPMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2))
ptPMFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1, 1)).setObjects(("PT-PM-MIB", "ptPMCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMFullCompliance = ptPMFullCompliance.setStatus('current')
ptPMCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2, 1)).setObjects(("PT-PM-MIB", "forwardingPacket"), ("PT-PM-MIB", "forwardingOctets"), ("PT-PM-MIB", "discardPackets"), ("PT-PM-MIB", "discardOctets"), ("PT-PM-MIB", "inputPackets"), ("PT-PM-MIB", "inputOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMCompleteGroup = ptPMCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-PM-MIB", ptPMFullCompliance=ptPMFullCompliance, ptPMCompleteGroup=ptPMCompleteGroup, PYSNMP_MODULE_ID=ptPM, queueIndex=queueIndex, ptPMEntry=ptPMEntry, discardOctets=discardOctets, discardPackets=discardPackets, inputPackets=inputPackets, forwardingOctets=forwardingOctets, inputOctets=inputOctets, ptPM=ptPM, ptPMTable=ptPMTable, ptPMGroups=ptPMGroups, ptPMConformance=ptPMConformance, ptPMCompliances=ptPMCompliances, forwardingPacket=forwardingPacket)
