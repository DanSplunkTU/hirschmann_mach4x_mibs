#
# PySNMP MIB module CTRON-FRONTPANEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FRONTPANEL-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:06 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctFpRedundancy, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFpRedundancy")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFpRedund = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1))
ctFpRedundReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundReset.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundReset.setDescription('If this object is set to Reset it will cause a reset\n                     of the front panel redundancy. Setting this object to\n                     NoReset will do nothing. This object will always be \n                     read as NoReset.')
ctFpRedundPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundPollInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundPollInterval.setDescription('Get/Set the number of seconds between polls for front\n                     panel redundancy.')
ctFpRedundRetrys = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundRetrys.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundRetrys.setDescription('Get/Set the the number of unanswered polls allowed for\n                     the front panel redundancy before it switches ports.')
ctFpRedundNumAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundNumAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundNumAddr.setDescription('Get the number of IP Addresses associated with front panel\n                     redundancy.')
ctFpRedundAddAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundAddAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundAddAddr.setDescription('Add an IP Address to the polling list for the front panel\n                     redundancy.')
ctFpRedundDelAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundDelAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundDelAddr.setDescription('Delete an IP Address from the polling list for the \n                     front panel redundancy.')
ctFpRedundActivePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundActivePort.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundActivePort.setDescription('Get/Set the front panel port you want to be active \n                     when front panel redundancy is enabled.')
ctFpRedundEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFpRedundEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundEnable.setDescription('If this object is set to enable, the front panel\n                     redundancy will be activated. If this object is set \n                     to disable,  the front panel redundancy will be \n                     deactivated.  When read, this object will returns the \n                     state of the object based on the last request \n                     made.')
ctFpRedundAddrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9), )
if mibBuilder.loadTexts: ctFpRedundAddrTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundAddrTable.setDescription('')
ctFpRedundAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1), ).setIndexNames((0, "CTRON-FRONTPANEL-MIB", "ctFpRedundAddrId"))
if mibBuilder.loadTexts: ctFpRedundAddrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundAddrEntry.setDescription('')
ctFpRedundAddrId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundAddrId.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundAddrId.setDescription('A unique value identifying an element in a sequence of\n                     member IP Addresses which belong to the front panel \n                     redundancy.  This value goes from 1 to the maximum \n                     number of IP Addresses which may be included in  \n                     front panel redundancy.')
ctFpRedundAddrIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFpRedundAddrIPAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctFpRedundAddrIPAddr.setDescription('Returns an IP Address associated with the front panel\n                     redundancy.')
mibBuilder.exportSymbols("CTRON-FRONTPANEL-MIB", ctFpRedundAddAddr=ctFpRedundAddAddr, ctFpRedundNumAddr=ctFpRedundNumAddr, ctFpRedundRetrys=ctFpRedundRetrys, ctFpRedundAddrEntry=ctFpRedundAddrEntry, ctFpRedundAddrId=ctFpRedundAddrId, ctFpRedundPollInterval=ctFpRedundPollInterval, ctFpRedundActivePort=ctFpRedundActivePort, ctFpRedundReset=ctFpRedundReset, ctFpRedundDelAddr=ctFpRedundDelAddr, ctFpRedundEnable=ctFpRedundEnable, ctFpRedundAddrTable=ctFpRedundAddrTable, ctFpRedund=ctFpRedund, ctFpRedundAddrIPAddr=ctFpRedundAddrIPAddr)
