#
# PySNMP MIB module PRVT-SWITCH-FIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-SWITCH-FIB-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ipNetToMediaPhysAddress, ipNetToMediaNetAddress, ipNetToMediaIfIndex = mibBuilder.importSymbols("IP-MIB", "ipNetToMediaPhysAddress", "ipNetToMediaNetAddress", "ipNetToMediaIfIndex")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, Counter32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
TruthValue, MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
prvtSwitchFIBMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 3))
prvtSwitchFIBMib.setRevisions(('2008-01-01 00:00', '2005-02-18 00:00', '2003-05-08 00:00', '2002-05-21 09:59', '2001-01-21 09:59',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtSwitchFIBMib.setRevisionsDescriptions(('Removed redefined OIDs in private vendor extension definitions.', 'Correction of the object descriptions.', 'Move to SMI-V2.', 'Add new IP trap', 'Initial version.',))
if mibBuilder.loadTexts: prvtSwitchFIBMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtSwitchFIBMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtSwitchFIBMib.setContactInfo('BATM/Telco Systems Support team\n\t\t\t\tEmail: \n\t\t\t\tFor North America: techsupport@telco.com\n\t\t\t\tFor North Europe: support@batm.de, info@batm.de\n\t\t\t\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtSwitchFIBMib.setDescription('The FIB MIB module controls the IP forwarding database \n        in L3 switches.')
prvtSwitchFIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 0))
fib = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1))
prvtSwitchFIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3))
fibTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1), )
if mibBuilder.loadTexts: fibTable.setStatus('current')
if mibBuilder.loadTexts: fibTable.setDescription('This table controls the IP forwarding database.')
fibEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1), ).setIndexNames((0, "PRVT-SWITCH-FIB-MIB", "fibIP"), (0, "PRVT-SWITCH-FIB-MIB", "fibMask"))
if mibBuilder.loadTexts: fibEntry.setStatus('current')
if mibBuilder.loadTexts: fibEntry.setDescription('')
fibIP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fibIP.setStatus('current')
if mibBuilder.loadTexts: fibIP.setDescription('This object identifies the name of the IP address of the FIB entry.')
fibMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fibMask.setStatus('current')
if mibBuilder.loadTexts: fibMask.setDescription('This object identifies the IP address mask of the FIB entry.')
fibProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 16, 100))).clone(namedValues=NamedValues(("other", 1), ("direct", 2), ("static", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("ospf", 13), ("bgp", 14), ("arp", 15), ("remote", 16), ("unknown", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fibProtocol.setStatus('current')
if mibBuilder.loadTexts: fibProtocol.setDescription('This object identifies the IP address learning protocol type of the FIB entry.')
fibNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibNextHop.setStatus('current')
if mibBuilder.loadTexts: fibNextHop.setDescription('This object identifies the next hop IP address of the FIB entry.')
fibNextHopMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibNextHopMac.setStatus('current')
if mibBuilder.loadTexts: fibNextHopMac.setDescription('This object identifies the next hop MAC address of the FIB entry.')
fibVID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibVID.setStatus('current')
if mibBuilder.loadTexts: fibVID.setDescription('This object identifies the VLAN ID of the FIB entry.')
fibOutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibOutPort.setStatus('current')
if mibBuilder.loadTexts: fibOutPort.setDescription('This object identifies the output interface number of the FIB entry.')
fibPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibPriority.setStatus('current')
if mibBuilder.loadTexts: fibPriority.setDescription('This object identifies the FIB entry priority.')
fibDiscardabilty = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("discard", 1), ("nondiscard", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibDiscardabilty.setStatus('current')
if mibBuilder.loadTexts: fibDiscardabilty.setDescription('This object identifies the FIB entry discardabilty.')
fibDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibDSCP.setStatus('current')
if mibBuilder.loadTexts: fibDSCP.setDescription('This object identifies the FIB entry DSCP.')
fibRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fibRowStatus.setStatus('current')
if mibBuilder.loadTexts: fibRowStatus.setDescription('This object indicates the row status, and enables creation & deletion of \n        rows in this table. See SNMPv2-TC for more information.')
newIP = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 0, 1)).setObjects(("IP-MIB", "ipNetToMediaIfIndex"), ("IP-MIB", "ipNetToMediaPhysAddress"), ("IP-MIB", "ipNetToMediaNetAddress"))
if mibBuilder.loadTexts: newIP.setStatus('current')
if mibBuilder.loadTexts: newIP.setDescription('The newIP trap indicates that a new IP address was learnt by the switch\n          in ifIndex ipNetToMediaIfIndex and a MAC address - in ipNetToMediaPhysAddress.\n\t \t  The IP address is given by ipNetToMediaNetAddress.')
prvtSwitchFIBMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3, 2))
prvtSwitchFIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3, 2, 3)).setObjects(("PRVT-SWITCH-FIB-MIB", "newIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtSwitchFIBNotificationGroup = prvtSwitchFIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: prvtSwitchFIBNotificationGroup.setDescription('Private Notification Group.')
mibBuilder.exportSymbols("PRVT-SWITCH-FIB-MIB", fibMask=fibMask, fibNextHop=fibNextHop, fibOutPort=fibOutPort, newIP=newIP, fibEntry=fibEntry, prvtSwitchFIBMib=prvtSwitchFIBMib, PYSNMP_MODULE_ID=prvtSwitchFIBMib, fibIP=fibIP, fibTable=fibTable, prvtSwitchFIBConformance=prvtSwitchFIBConformance, prvtSwitchFIBNotificationGroup=prvtSwitchFIBNotificationGroup, fib=fib, fibDiscardabilty=fibDiscardabilty, fibVID=fibVID, fibProtocol=fibProtocol, fibDSCP=fibDSCP, fibNextHopMac=fibNextHopMac, fibPriority=fibPriority, fibRowStatus=fibRowStatus, prvtSwitchFIBNotifications=prvtSwitchFIBNotifications, prvtSwitchFIBMIBGroups=prvtSwitchFIBMIBGroups)
