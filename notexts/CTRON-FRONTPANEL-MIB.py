#
# PySNMP MIB module CTRON-FRONTPANEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FRONTPANEL-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:06 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctFpRedundancy, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFpRedundancy")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFpRedund = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1))
ctFpRedundReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundReset.setStatus('mandatory')
ctFpRedundPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundPollInterval.setStatus('mandatory')
ctFpRedundRetrys = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundRetrys.setStatus('mandatory')
ctFpRedundNumAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundNumAddr.setStatus('mandatory')
ctFpRedundAddAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundAddAddr.setStatus('mandatory')
ctFpRedundDelAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundDelAddr.setStatus('mandatory')
ctFpRedundActivePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundActivePort.setStatus('mandatory')
ctFpRedundEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundEnable.setStatus('mandatory')
ctFpRedundAddrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9), )
if mibBuilder.loadTexts: ctFpRedundAddrTable.setStatus('mandatory')
ctFpRedundAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1), ).setIndexNames((0, "CTRON-FRONTPANEL-MIB", "ctFpRedundAddrId"))
if mibBuilder.loadTexts: ctFpRedundAddrEntry.setStatus('mandatory')
ctFpRedundAddrId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundAddrId.setStatus('mandatory')
ctFpRedundAddrIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundAddrIPAddr.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-FRONTPANEL-MIB", ctFpRedundPollInterval=ctFpRedundPollInterval, ctFpRedundDelAddr=ctFpRedundDelAddr, ctFpRedundActivePort=ctFpRedundActivePort, ctFpRedundReset=ctFpRedundReset, ctFpRedundAddrIPAddr=ctFpRedundAddrIPAddr, ctFpRedundAddrTable=ctFpRedundAddrTable, ctFpRedundAddAddr=ctFpRedundAddAddr, ctFpRedundNumAddr=ctFpRedundNumAddr, ctFpRedundEnable=ctFpRedundEnable, ctFpRedundAddrId=ctFpRedundAddrId, ctFpRedundAddrEntry=ctFpRedundAddrEntry, ctFpRedund=ctFpRedund, ctFpRedundRetrys=ctFpRedundRetrys)
