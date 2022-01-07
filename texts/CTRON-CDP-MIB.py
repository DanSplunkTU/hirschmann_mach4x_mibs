#
# PySNMP MIB module CTRON-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-CDP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ctCDP, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctCDP")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, TimeTicks, ObjectIdentity, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, NotificationType, ModuleIdentity, Gauge32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity", "Gauge32", "Integer32", "IpAddress")
TextualConvention, MacAddress, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TimeStamp", "DisplayString")
ctronCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3))
if mibBuilder.loadTexts: ctronCdpMIB.setLastUpdated('199908280000Z')
if mibBuilder.loadTexts: ctronCdpMIB.setOrganization('Cabletron Systems, Inc.')
if mibBuilder.loadTexts: ctronCdpMIB.setContactInfo('Cabletron Systems, Inc.\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@ctron.com\n     http://www.ctron.com')
if mibBuilder.loadTexts: ctronCdpMIB.setDescription('This module defines a schema that maintains per port\n      neighbor information for the express purpose\n      of helping a managment application map \n      Layaer 2 topology.')
class CTCDPCapability(TextualConvention, Integer32):
    description = 'The current capabilities of the neighbor device on a per\nport basis.  '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("igmp", 1), ("rip", 2), ("bgp", 3), ("ospf", 4), ("dvmrp", 5), ("ieee8021q", 6), ("gvrp", 7), ("gmrp", 8), ("igmpSnoop", 9), ("dhcpServer", 10), ("dnsServer", 11), ("activeDirectory", 12))

ctCDPNeighbor = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1))
ctCDPStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2))
ctCDPStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4))
ctCDPNeighborLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborLastChange.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborLastChange.setDescription('The value of sysUpTime at the time the cdpNeighborTable\n         was subject to these events: row insertion, row deletion')
ctCDPNeighborLastDelete = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborLastDelete.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborLastDelete.setDescription('The value of sysUpTime the last time an entry in the\n        ctCDPNeighborTable was deleted. This should be polled \n        at an interval no greater than one second.\n        When it changes, the whole table should be \n        reread by management with a timeMark of 0 to rebuild\n        connectivity map.')
ctCDPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3), )
if mibBuilder.loadTexts: ctCDPNeighborTable.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborTable.setDescription('The CommonNeighborTable holds all known neighbors speaking\n         cdp protocols.')
ctCDPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1), ).setIndexNames((0, "CTRON-CDP-MIB", "ctCDPNeighborTimeMark"), (0, "IF-MIB", "ifIndex"), (0, "CTRON-CDP-MIB", "ctCDPNeighborMAC"))
if mibBuilder.loadTexts: ctCDPNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborEntry.setDescription('An entry containing objects pertaining to  \n          neighbor devices speaking CDP protocols.')
ctCDPNeighborTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 1), TimeFilter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborTimeMark.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborTimeMark.setDescription('A TimeFilter for this entry as defined in RFC 2021.')
ctCDPNeighborMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborMAC.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborMAC.setDescription('The interface mac address of neighboring entity.')
ctCDPNeighborIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborIP.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborIP.setDescription('The IP address of SNMP agent on neighboring entity from which\n         corresponding data for this port may be obtained. In the case\n         of unnumbered IP Interfaces, this may not be the same as the \n         port.')
ctCDPNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborPort.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborPort.setDescription('The ifIndex of the remote port. Note, there may not be an IP \n         Interface associated with this port.')
ctCDPNeighborType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("secureFastSwitch", 1), ("dot1qSwitch", 2), ("router", 3), ("dot1dBridge", 4), ("vlanManager", 5), ("dnsServer", 6), ("dhcpServer", 7), ("dnsDhcpServer", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborType.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborType.setDescription("The type of entity. This value is used to determine the\n         general type of the object or service connected to a given port.\n         In general, it is better to use system group sysServices to\n         obtain an object's functionality.")
ctCDPNeighborChassisMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborChassisMAC.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborChassisMAC.setDescription('The MAC Address of the chassis in architectures\n         where many manageable  elements exist within a \n         given chassis. If no containing chassis exists, \n         exists, this value must be set to 000000:000000')
ctCDPNeighborChassisIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborChassisIP.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborChassisIP.setDescription('The IP address of the chassis itself. If no containing chassis\n         exists, this value must be set to 0.0.0.0')
ctCDPNeighborDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborDescription.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborDescription.setDescription('A textual description of the neighbor. It\n         should contain operator diagnostic information \n         similar to sysDescr: system type, firmware version...')
ctCDPNeighborPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborPortName.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborPortName.setDescription("The value of object ifName of the neighbor's port.")
ctCDPNeighborCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 10), CTCDPCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborCapability.setStatus('current')
if mibBuilder.loadTexts: ctCDPNeighborCapability.setDescription('The current capabilities of the neighbor port.')
ctCDPGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("autoEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPGlobalStatus.setStatus('current')
if mibBuilder.loadTexts: ctCDPGlobalStatus.setDescription('The state of CDP for this entire managed entity. autoEnable(3)\n         should the default mode for new implementations. In autoEnable\n         mode, the device listens for CDP messages and upon receipt, begins\n         sending CDP messages of the same version and type as received.')
ctCDPAuthenticationCode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPAuthenticationCode.setStatus('current')
if mibBuilder.loadTexts: ctCDPAuthenticationCode.setDescription('The authentication code may be set to create individual CDP\n        domains. CDP packets that arrive on a port must contain this\n        string. This authentication code is global for the entire\n        managed entity. The default for this string is 16 nulls.')
ctCDPPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3), )
if mibBuilder.loadTexts: ctCDPPortTable.setStatus('current')
if mibBuilder.loadTexts: ctCDPPortTable.setDescription('This table shows enable/disable CDP status for each port.')
ctCDPPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1), ).setIndexNames((0, "CTRON-CDP-MIB", "ctCDPPort"))
if mibBuilder.loadTexts: ctCDPPortTableEntry.setStatus('current')
if mibBuilder.loadTexts: ctCDPPortTableEntry.setDescription('Each entry is indicative of a particuliar port in the system.')
ctCDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPPort.setStatus('current')
if mibBuilder.loadTexts: ctCDPPort.setDescription('The ifIndex for a physical port. ifConnectorPresent is true(1) \n         defines a physical port on which cdp pdus will be emitted.')
ctCDPPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("autoEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPPortStatus.setStatus('current')
if mibBuilder.loadTexts: ctCDPPortStatus.setDescription("The current state administrative of cdp on a physical port. \n         The ability to enable and disable the sending of CDP pdu's \n         on a per port basis is controlled here.")
ctCDPTransmitFrequency = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPTransmitFrequency.setStatus('current')
if mibBuilder.loadTexts: ctCDPTransmitFrequency.setDescription("The rate in seconds at which CDP pdu's are sent on all enabled ports.")
ctCDPHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPHoldTime.setStatus('current')
if mibBuilder.loadTexts: ctCDPHoldTime.setDescription('The maximum amount of time in seconds to wait before aging out\n         an entry in the ctCDPNeighborTable. The agent may choose to change\n         this value based on the hold time it receives from other devices\n         so as to have a stable neighbor table which ages out entries \n         in accordance with the transmit frequency.')
ctCDPVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPVersion.setStatus('current')
if mibBuilder.loadTexts: ctCDPVersion.setDescription('The CDP version supported by this device as a bit string.\n         For example, given support for two versions of cdp: 3 and 4\n         the bit representation in big endian form would be: 00001100.')
ctCDPInPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPInPackets.setStatus('current')
if mibBuilder.loadTexts: ctCDPInPackets.setDescription('Count of CDP packets received by the device over all \n         the ports.')
ctCDPOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPOutPackets.setStatus('current')
if mibBuilder.loadTexts: ctCDPOutPackets.setDescription('Count of CDP packets successfully transmitted by the \n         device over all the ports.')
ctCDPInvalidVersionPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPInvalidVersionPackets.setStatus('current')
if mibBuilder.loadTexts: ctCDPInvalidVersionPackets.setDescription('Count of CDP packets received with version not \n         supported by the device.')
ctCDPParseErrorPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPParseErrorPackets.setStatus('current')
if mibBuilder.loadTexts: ctCDPParseErrorPackets.setDescription('Count of CDP packets received and could not be parsed\n         successfully by the device.')
ctCDPTransmitErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPTransmitErrors.setStatus('current')
if mibBuilder.loadTexts: ctCDPTransmitErrors.setDescription('Count of errors occured by the device while trying \n         to transmit CDP packets.')
ctCDPMemoryErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPMemoryErrors.setStatus('current')
if mibBuilder.loadTexts: ctCDPMemoryErrors.setDescription('Count of memory errors occured in the device while \n         either trying to process the CDP packet or adding the \n         neighbor entry or while trying to send a CDP packet.')
ctCDPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11))
ctCDPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1))
ctCDPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2))
ctCDPComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1, 1)).setObjects(("CTRON-CDP-MIB", "ctCdpGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctCDPComplianceV10 = ctCDPComplianceV10.setStatus('current')
if mibBuilder.loadTexts: ctCDPComplianceV10.setDescription('The compliance statement for the ctronCdpMIB.')
ctCdpGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2, 1)).setObjects(("CTRON-CDP-MIB", "ctCDPNeighborLastChange"), ("CTRON-CDP-MIB", "ctCDPNeighborLastDelete"), ("CTRON-CDP-MIB", "ctCDPNeighborTimeMark"), ("CTRON-CDP-MIB", "ctCDPNeighborMAC"), ("CTRON-CDP-MIB", "ctCDPNeighborIP"), ("CTRON-CDP-MIB", "ctCDPNeighborPort"), ("CTRON-CDP-MIB", "ctCDPNeighborType"), ("CTRON-CDP-MIB", "ctCDPNeighborChassisMAC"), ("CTRON-CDP-MIB", "ctCDPNeighborChassisIP"), ("CTRON-CDP-MIB", "ctCDPGlobalStatus"), ("CTRON-CDP-MIB", "ctCDPAuthenticationCode"), ("CTRON-CDP-MIB", "ctCDPPort"), ("CTRON-CDP-MIB", "ctCDPPortStatus"), ("CTRON-CDP-MIB", "ctCDPNeighborDescription"), ("CTRON-CDP-MIB", "ctCDPNeighborPortName"), ("CTRON-CDP-MIB", "ctCDPNeighborCapability"), ("CTRON-CDP-MIB", "ctCDPTransmitFrequency"), ("CTRON-CDP-MIB", "ctCDPHoldTime"), ("CTRON-CDP-MIB", "ctCDPVersion"), ("CTRON-CDP-MIB", "ctCDPInPackets"), ("CTRON-CDP-MIB", "ctCDPOutPackets"), ("CTRON-CDP-MIB", "ctCDPInvalidVersionPackets"), ("CTRON-CDP-MIB", "ctCDPParseErrorPackets"), ("CTRON-CDP-MIB", "ctCDPTransmitErrors"), ("CTRON-CDP-MIB", "ctCDPMemoryErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctCdpGroupV10 = ctCdpGroupV10.setStatus('current')
if mibBuilder.loadTexts: ctCdpGroupV10.setDescription('The set of managed objects that make up version 2 of the\n   CTRON-CDP-MIB.')
mibBuilder.exportSymbols("CTRON-CDP-MIB", ctCDPNeighborDescription=ctCDPNeighborDescription, ctCDPVersion=ctCDPVersion, ctCDPNeighborChassisIP=ctCDPNeighborChassisIP, ctCDPNeighborMAC=ctCDPNeighborMAC, ctCDPStats=ctCDPStats, ctCDPNeighborCapability=ctCDPNeighborCapability, ctCDPHoldTime=ctCDPHoldTime, ctCDPNeighborType=ctCDPNeighborType, PYSNMP_MODULE_ID=ctronCdpMIB, ctCDPMemoryErrors=ctCDPMemoryErrors, ctCDPAuthenticationCode=ctCDPAuthenticationCode, ctCDPNeighborIP=ctCDPNeighborIP, ctCDPPortStatus=ctCDPPortStatus, ctCDPGlobalStatus=ctCDPGlobalStatus, ctCDPInPackets=ctCDPInPackets, ctCDPTransmitFrequency=ctCDPTransmitFrequency, ctCDPInvalidVersionPackets=ctCDPInvalidVersionPackets, CTCDPCapability=CTCDPCapability, ctCDPParseErrorPackets=ctCDPParseErrorPackets, ctCDPNeighborPort=ctCDPNeighborPort, ctCDPNeighborTimeMark=ctCDPNeighborTimeMark, ctCDPNeighbor=ctCDPNeighbor, ctronCdpMIB=ctronCdpMIB, ctCDPTransmitErrors=ctCDPTransmitErrors, ctCDPNeighborLastDelete=ctCDPNeighborLastDelete, ctCDPCompliances=ctCDPCompliances, ctCDPPortTable=ctCDPPortTable, ctCDPOutPackets=ctCDPOutPackets, ctCDPNeighborEntry=ctCDPNeighborEntry, ctCDPNeighborTable=ctCDPNeighborTable, ctCDPComplianceV10=ctCDPComplianceV10, ctCDPNeighborPortName=ctCDPNeighborPortName, ctCDPPort=ctCDPPort, ctCDPPortTableEntry=ctCDPPortTableEntry, ctCDPStatus=ctCDPStatus, ctCDPNeighborChassisMAC=ctCDPNeighborChassisMAC, ctCdpGroupV10=ctCdpGroupV10, ctCDPConformance=ctCDPConformance, ctCDPNeighborLastChange=ctCDPNeighborLastChange, ctCDPGroups=ctCDPGroups)
