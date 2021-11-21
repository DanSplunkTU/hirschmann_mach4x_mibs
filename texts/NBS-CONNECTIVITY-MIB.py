#
# PySNMP MIB module NBS-CONNECTIVITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-CONNECTIVITY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:26:50 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
nbsCmmcChassisIndex, nbsCmmcSlotIndex, nbsCmmcPortIndex = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcChassisIndex", "nbsCmmcSlotIndex", "nbsCmmcPortIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Counter32, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Integer32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Integer32", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsConnectivityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 238))
if mibBuilder.loadTexts: nbsConnectivityMib.setLastUpdated('201405280000Z')
if mibBuilder.loadTexts: nbsConnectivityMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsConnectivityMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsConnectivityMib.setDescription('Read-only MIB which lists externally linked ports')
nbsConnectivityGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 1))
if mibBuilder.loadTexts: nbsConnectivityGrp.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityGrp.setDescription('Connectivity information')
nbsConnectivityTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 100))
if mibBuilder.loadTexts: nbsConnectivityTraps.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityTraps.setDescription('SNMP Traps or Notifications')
nbsConnectivityEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 100, 0))
if mibBuilder.loadTexts: nbsConnectivityEvent.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityEvent.setDescription('Event Notification Definitions')
nbsConnectivityTable = MibTable((1, 3, 6, 1, 4, 1, 629, 238, 1, 1), )
if mibBuilder.loadTexts: nbsConnectivityTable.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityTable.setDescription('List of externally connected port pairs.\n\n                 The connectivity table entries come from discovery\n                 protocols.')
nbsConnectivityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1), ).setIndexNames((0, "NBS-CONNECTIVITY-MIB", "nbsConnectivitySourceIfIndex"), (0, "NBS-CONNECTIVITY-MIB", "nbsConnectivityOrdinalIndex"))
if mibBuilder.loadTexts: nbsConnectivityEntry.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityEntry.setDescription('Contains a description of a particular Port Connection.')
nbsConnectivitySourceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 10), InterfaceIndex())
if mibBuilder.loadTexts: nbsConnectivitySourceIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivitySourceIfIndex.setDescription('MIB II Interface index.')
nbsConnectivityOrdinalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: nbsConnectivityOrdinalIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityOrdinalIndex.setDescription('The ordinal index for this entry. A given source\n                 port may have one or more destination ports.')
nbsConnectivityDestIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 20), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestIfIndex.setDescription('MIB II Interface index.')
nbsConnectivityDestIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 30), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestIPAddress.setStatus('deprecated')
if mibBuilder.loadTexts: nbsConnectivityDestIPAddress.setDescription('Deprecated. IPv4 information is in\n                 nbsConnectivityDestAddr instead.')
nbsConnectivityDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 40), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestAddrType.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestAddrType.setDescription('The address type of nbsConnectivityDestAddr.\n                 Currently ipv4 and ipv6 are supported.')
nbsConnectivityDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 50), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestAddr.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestAddr.setDescription("IP Address (Usually IPv4) of the remote port's SNMP agent")
nbsConnectivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3), ("notSupported", 4), ("sourceBlocked", 5), ("destBlocked", 6))).clone('notSupported')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityStatus.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityStatus.setDescription('This object is used to indicate the link status.')
nbsConnectivityDestV6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 70), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestV6AddrType.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestV6AddrType.setDescription('The address type of nbsConnectivityDestV6Addr.')
nbsConnectivityDestV6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 80), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestV6Addr.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestV6Addr.setDescription("IP Address (Usually IPv6) of the remote port's SNMP agent")
nbsConnectivityChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 238, 100, 0, 10)).setObjects(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"), ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"), ("NBS-CMMC-MIB", "nbsCmmcPortIndex"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddrType"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddr"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityStatus"))
if mibBuilder.loadTexts: nbsConnectivityChanged.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityChanged.setDescription('Sent after the port goes up or down.\n\n        This Notification is of severity ERROR, which means it should\n        be emitted unless disabled or nbsCmmcSysTrapTblEntLevel is set\n        to a severity worse than error(3).')
mibBuilder.exportSymbols("NBS-CONNECTIVITY-MIB", nbsConnectivityDestIPAddress=nbsConnectivityDestIPAddress, nbsConnectivityDestAddr=nbsConnectivityDestAddr, nbsConnectivityEntry=nbsConnectivityEntry, nbsConnectivityDestV6AddrType=nbsConnectivityDestV6AddrType, nbsConnectivityTraps=nbsConnectivityTraps, nbsConnectivityGrp=nbsConnectivityGrp, nbsConnectivityStatus=nbsConnectivityStatus, nbsConnectivityTable=nbsConnectivityTable, nbsConnectivityDestIfIndex=nbsConnectivityDestIfIndex, nbsConnectivityMib=nbsConnectivityMib, nbsConnectivityChanged=nbsConnectivityChanged, nbsConnectivityDestV6Addr=nbsConnectivityDestV6Addr, nbsConnectivitySourceIfIndex=nbsConnectivitySourceIfIndex, nbsConnectivityEvent=nbsConnectivityEvent, nbsConnectivityOrdinalIndex=nbsConnectivityOrdinalIndex, nbsConnectivityDestAddrType=nbsConnectivityDestAddrType, PYSNMP_MODULE_ID=nbsConnectivityMib)
