#
# PySNMP MIB module IEEE8021-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-PFC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
ifGeneralInformationGroup, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup", "ifEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021PFCMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 21))
ieee8021PFCMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2010-02-08 00:00',))
if mibBuilder.loadTexts: ieee8021PFCMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PFCMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PfcMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 1))
ieee8021PfcConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2))
ieee8021PfcIfTable = MibTable((1, 3, 111, 2, 802, 1, 1, 21, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfTable.setStatus('current')
ieee8021PfcIfEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1), )
ifEntry.registerAugmentions(("IEEE8021-PFC-MIB", "ieee8021PfcIfEntry"))
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setStatus('current')
ieee8021PfcLinkDelayAllowance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setStatus('current')
ieee8021PfcRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 2), Counter32()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcRequests.setStatus('current')
ieee8021PfcIndications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 3), Counter32()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcIndications.setStatus('current')
ieee8021PfcCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 1))
ieee8021PfcGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 2))
ieee8021PfcGlobalReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 21, 2, 2, 1)).setObjects(("IEEE8021-PFC-MIB", "ieee8021PfcLinkDelayAllowance"), ("IEEE8021-PFC-MIB", "ieee8021PfcRequests"), ("IEEE8021-PFC-MIB", "ieee8021PfcIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcGlobalReqdGroup = ieee8021PfcGlobalReqdGroup.setStatus('current')
ieee8021PfcCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 21, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("IEEE8021-PFC-MIB", "ieee8021PfcGlobalReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcCompliance = ieee8021PfcCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PFC-MIB", ieee8021PfcLinkDelayAllowance=ieee8021PfcLinkDelayAllowance, ieee8021PFCMib=ieee8021PFCMib, ieee8021PfcCompliances=ieee8021PfcCompliances, ieee8021PfcIfTable=ieee8021PfcIfTable, PYSNMP_MODULE_ID=ieee8021PFCMib, ieee8021PfcMIBObjects=ieee8021PfcMIBObjects, ieee8021PfcGroups=ieee8021PfcGroups, ieee8021PfcIndications=ieee8021PfcIndications, ieee8021PfcCompliance=ieee8021PfcCompliance, ieee8021PfcRequests=ieee8021PfcRequests, ieee8021PfcGlobalReqdGroup=ieee8021PfcGlobalReqdGroup, ieee8021PfcConformance=ieee8021PfcConformance, ieee8021PfcIfEntry=ieee8021PfcIfEntry)
