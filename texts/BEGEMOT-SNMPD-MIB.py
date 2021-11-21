#
# PySNMP MIB module BEGEMOT-SNMPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-SNMPD
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:27 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32, Bits, Counter32, Integer32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Bits", "Counter32", "Integer32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
begemotSnmpd = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 1))
if mibBuilder.loadTexts: begemotSnmpd.setLastUpdated('200212040000Z')
if mibBuilder.loadTexts: begemotSnmpd.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: begemotSnmpd.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotSnmpd.setDescription('The MIB module for the Begemot SNMP daemon.')
begemotSnmpdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1))
begemotSnmpdDefs = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 2))
class SectionName(TextualConvention, OctetString):
    description = 'Name of a loadable module. Should consist of alphanumeric characers\n\tonly, the first character must be a letter.'
    status = 'current'
    displayHint = '14a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 14)

begemotSnmpdAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 2, 1))
begemotSnmpdAgentFreeBSD = ObjectIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 1, 2, 1, 1))
if mibBuilder.loadTexts: begemotSnmpdAgentFreeBSD.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdAgentFreeBSD.setDescription('Identifies the agent as running on FreeBSD.')
begemotSnmpdConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1))
begemotSnmpdTransmitBuffer = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 65535)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdTransmitBuffer.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransmitBuffer.setDescription('The size of the receive buffer in bytes. Larger messages\n\t    are dropped by SNMPd.')
begemotSnmpdReceiveBuffer = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 65535)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdReceiveBuffer.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdReceiveBuffer.setDescription('The size of the transmit buffer in bytes. Larger messages\n\t    cannot be sent by the SNMPd.')
begemotSnmpdCommunityDisable = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdCommunityDisable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityDisable.setDescription('Disables all access to the CommunityTable from SNMP. Once\n\t    set it cannot be cleared.')
begemotSnmpdTrap1Addr = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdTrap1Addr.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTrap1Addr.setDescription('The trap sink for v1 traps.')
begemotSnmpdVersionEnable = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 5), Unsigned32().clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdVersionEnable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdVersionEnable.setDescription('The SNMP versions that the agent processes. The following\n\t    bits are defined:\n\n\t    0x00000001\t- SNMPv1\n\t    0x00000002\t- SNMPv2c\n\t    0x00000004\t- SNMPv3')
begemotTrapSinkTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkAddr"), (0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkPort"))
if mibBuilder.loadTexts: begemotTrapSinkTable.setStatus('current')
if mibBuilder.loadTexts: begemotTrapSinkTable.setDescription('A table with destinations for standard traps.')
begemotTrapSinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkAddr"), (0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkPort"))
if mibBuilder.loadTexts: begemotTrapSinkEntry.setStatus('current')
if mibBuilder.loadTexts: begemotTrapSinkEntry.setDescription('Entry describes one trap destination.')
begemotTrapSinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: begemotTrapSinkAddr.setStatus('current')
if mibBuilder.loadTexts: begemotTrapSinkAddr.setDescription('Destination IP address of the manager station where to send\n\t    traps.')
begemotTrapSinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: begemotTrapSinkPort.setStatus('current')
if mibBuilder.loadTexts: begemotTrapSinkPort.setDescription('Destination UDP port of the manager station where to send\n\t    traps.')
begemotTrapSinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotTrapSinkStatus.setStatus('current')
if mibBuilder.loadTexts: begemotTrapSinkStatus.setDescription('Used to create/activate/destroy the entry.')
begemotSnmpdPortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4), )
if mibBuilder.loadTexts: begemotSnmpdPortTable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdPortTable.setDescription('A table with descriptions of UDP ports to listen on\n\t    for SNMP messages.')
begemotSnmpdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdPortAddress"), (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdPortPort"))
if mibBuilder.loadTexts: begemotSnmpdPortEntry.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdPortEntry.setDescription('An entry in the table with descriptions of UDP ports to\n\t    listen on for SNMP messages.')
begemotSnmpdPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: begemotSnmpdPortAddress.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdPortAddress.setDescription('The IP address to bind to.')
begemotSnmpdPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: begemotSnmpdPortPort.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdPortPort.setDescription('The UDP port to listen on for SNMP messages.')
begemotSnmpdPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotSnmpdPortStatus.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdPortStatus.setDescription('Set status to 1 to create entry, set it to 2 to delete it.')
begemotSnmpdCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5), )
if mibBuilder.loadTexts: begemotSnmpdCommunityTable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityTable.setDescription('A table with the community strings for access control.')
begemotSnmpdCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdCommunityModule"), (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdCommunityIndex"))
if mibBuilder.loadTexts: begemotSnmpdCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityEntry.setDescription('A table with the community strings for access control.\n\t    When begemotSnmpdCommDisable is true, this table disappears.')
begemotSnmpdCommunityModule = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 1), SectionName())
if mibBuilder.loadTexts: begemotSnmpdCommunityModule.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityModule.setDescription('Index of the module that has registered this community.\n\t    For global communities this is the empty string.')
begemotSnmpdCommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: begemotSnmpdCommunityIndex.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityIndex.setDescription('The numerical index of the community (private to the module).')
begemotSnmpdCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdCommunityString.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityString.setDescription('The string for access to SNMPd.')
begemotSnmpdCommunityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdCommunityDescr.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdCommunityDescr.setDescription('A description what this community is good for.')
begemotSnmpdModuleTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6), )
if mibBuilder.loadTexts: begemotSnmpdModuleTable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdModuleTable.setDescription('A table describing all the currently loaded dynamic modules.\n\t    Writing to this table loads and unloads modules.')
begemotSnmpdModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdModuleSection"))
if mibBuilder.loadTexts: begemotSnmpdModuleEntry.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdModuleEntry.setDescription('A table entry describing a loadable module.')
begemotSnmpdModuleSection = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 1), SectionName())
if mibBuilder.loadTexts: begemotSnmpdModuleSection.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdModuleSection.setDescription('The string used for matching configuration file sections\n\t    and indexes the module table.')
begemotSnmpdModulePath = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotSnmpdModulePath.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdModulePath.setDescription('The path name of the module. Set to empty string\n\t    to unload a module. The path of an existing module\n\t    may not be changed.')
begemotSnmpdModuleComment = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdModuleComment.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdModuleComment.setDescription('A comment describing this module.')
begemotSnmpdStats = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7))
begemotSnmpdStatsNoRxBufs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdStatsNoRxBufs.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdStatsNoRxBufs.setDescription('Number of times a receive buffer could not be allocated\n\t    for a packet.')
begemotSnmpdStatsNoTxBufs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdStatsNoTxBufs.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdStatsNoTxBufs.setDescription('Number of times a transmit buffer could not be allocated\n\t    for a packet.')
begemotSnmpdStatsInTooLongPkts = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdStatsInTooLongPkts.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdStatsInTooLongPkts.setDescription('Number of packets received that were longer than the\n\t    receive buffer. These packets are dropped.')
begemotSnmpdStatsInBadPduTypes = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdStatsInBadPduTypes.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdStatsInBadPduTypes.setDescription('Number of packets received with a bad type field.')
begemotSnmpdDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8))
begemotSnmpdDebugDumpPdus = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdDebugDumpPdus.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdDebugDumpPdus.setDescription('Dump PDUs to log file if true.')
begemotSnmpdDebugSnmpTrace = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdDebugSnmpTrace.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdDebugSnmpTrace.setDescription('Tracing flags for the SNMP library. These flags have the\n\t    following meaning:\n\t\t0x00000001\ttrace GET operator\n\t\t0x00000002\ttrace GETNEXT operator\n\t\t0x00000004\ttrace SET operator\n\t\t0x00000008\ttrace dependency processing\n\t\t0x00000010\ttrace node finding\n\t\t0x10000000\tlog ASN1 errors\n\t\t0x20000000\tlog SNMP errors\n\t    Individual values can be or-ed together.')
begemotSnmpdDebugSyslogPri = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotSnmpdDebugSyslogPri.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdDebugSyslogPri.setDescription('Events with this or higher priority should not be logged.')
begemotSnmpdLocalPortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9), )
if mibBuilder.loadTexts: begemotSnmpdLocalPortTable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdLocalPortTable.setDescription('A table with descriptions of local (unix domain) ports to listen\n\t    on for SNMP messages.')
begemotSnmpdLocalPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdLocalPortPath"))
if mibBuilder.loadTexts: begemotSnmpdLocalPortEntry.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdLocalPortEntry.setDescription('An entry in the table with descriptions of local ports to\n\t    listen on for SNMP messages.')
begemotSnmpdLocalPortPath = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 104)))
if mibBuilder.loadTexts: begemotSnmpdLocalPortPath.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdLocalPortPath.setDescription('The path name to create and listen on.')
begemotSnmpdLocalPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotSnmpdLocalPortStatus.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdLocalPortStatus.setDescription('Set status to 1 to create entry, set it to 2 to delete it.')
begemotSnmpdLocalPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dgram-unpriv", 1), ("dgram-priv", 2), ("stream-unpriv", 3), ("stream-priv", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotSnmpdLocalPortType.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdLocalPortType.setDescription('Type of the port. If the type is unpriv SET operations\n\t    are allowed from all clients if the community matches. For\n\t    priv SET operations are allowed only from peers with uid\n\t    zero. If the daemon cannot determine the peer uid it disallows\n\t    the SET operation for -priv ports.')
begemotSnmpdTransportMappings = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10))
begemotSnmpdTransportTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1), )
if mibBuilder.loadTexts: begemotSnmpdTransportTable.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransportTable.setDescription('A table containing all the currently loaded transport mappings.')
begemotSnmpdTransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1), ).setIndexNames((0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdTransportName"))
if mibBuilder.loadTexts: begemotSnmpdTransportEntry.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransportEntry.setDescription('An entry in the table with the transport mappings.')
begemotSnmpdTransportName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256)))
if mibBuilder.loadTexts: begemotSnmpdTransportName.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransportName.setDescription('The name of the mapping.')
begemotSnmpdTransportStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdTransportStatus.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransportStatus.setDescription('Used to create/activate/destroy the entry.')
begemotSnmpdTransportOid = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotSnmpdTransportOid.setStatus('current')
if mibBuilder.loadTexts: begemotSnmpdTransportOid.setDescription('A pointer to the group with the transport-dependend stuff.')
begemotSnmpdTransUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 2))
begemotSnmpdTransLsock = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 3))
mibBuilder.exportSymbols("BEGEMOT-SNMPD-MIB", begemotSnmpdPortPort=begemotSnmpdPortPort, begemotSnmpdDefs=begemotSnmpdDefs, begemotSnmpdDebugSyslogPri=begemotSnmpdDebugSyslogPri, begemotSnmpdModuleEntry=begemotSnmpdModuleEntry, begemotSnmpdTransportOid=begemotSnmpdTransportOid, begemotSnmpdPortTable=begemotSnmpdPortTable, begemotSnmpdCommunityString=begemotSnmpdCommunityString, begemotSnmpdTransportMappings=begemotSnmpdTransportMappings, begemotSnmpdPortStatus=begemotSnmpdPortStatus, begemotSnmpdTransportTable=begemotSnmpdTransportTable, begemotTrapSinkTable=begemotTrapSinkTable, begemotSnmpdPortEntry=begemotSnmpdPortEntry, begemotSnmpdCommunityTable=begemotSnmpdCommunityTable, begemotSnmpdModuleComment=begemotSnmpdModuleComment, begemotSnmpdConfig=begemotSnmpdConfig, begemotSnmpdTrap1Addr=begemotSnmpdTrap1Addr, begemotSnmpdDebugSnmpTrace=begemotSnmpdDebugSnmpTrace, begemotSnmpdAgentFreeBSD=begemotSnmpdAgentFreeBSD, begemotSnmpdStats=begemotSnmpdStats, begemotSnmpdLocalPortTable=begemotSnmpdLocalPortTable, begemotSnmpdLocalPortType=begemotSnmpdLocalPortType, begemotTrapSinkPort=begemotTrapSinkPort, begemotSnmpdAgent=begemotSnmpdAgent, begemotSnmpdModuleSection=begemotSnmpdModuleSection, begemotSnmpdTransUdp=begemotSnmpdTransUdp, begemotSnmpdDebug=begemotSnmpdDebug, begemotSnmpdTransmitBuffer=begemotSnmpdTransmitBuffer, begemotSnmpdTransportName=begemotSnmpdTransportName, begemotTrapSinkAddr=begemotTrapSinkAddr, SectionName=SectionName, begemotSnmpdCommunityEntry=begemotSnmpdCommunityEntry, begemotSnmpdStatsInTooLongPkts=begemotSnmpdStatsInTooLongPkts, PYSNMP_MODULE_ID=begemotSnmpd, begemotSnmpdCommunityDescr=begemotSnmpdCommunityDescr, begemotSnmpdStatsNoTxBufs=begemotSnmpdStatsNoTxBufs, begemotSnmpdStatsInBadPduTypes=begemotSnmpdStatsInBadPduTypes, begemotSnmpdLocalPortPath=begemotSnmpdLocalPortPath, begemotSnmpdLocalPortStatus=begemotSnmpdLocalPortStatus, begemotSnmpdCommunityModule=begemotSnmpdCommunityModule, begemotSnmpdCommunityDisable=begemotSnmpdCommunityDisable, begemotSnmpdPortAddress=begemotSnmpdPortAddress, begemotSnmpdModuleTable=begemotSnmpdModuleTable, begemotSnmpdCommunityIndex=begemotSnmpdCommunityIndex, begemotSnmpdTransportStatus=begemotSnmpdTransportStatus, begemotSnmpd=begemotSnmpd, begemotSnmpdVersionEnable=begemotSnmpdVersionEnable, begemotTrapSinkStatus=begemotTrapSinkStatus, begemotTrapSinkEntry=begemotTrapSinkEntry, begemotSnmpdReceiveBuffer=begemotSnmpdReceiveBuffer, begemotSnmpdModulePath=begemotSnmpdModulePath, begemotSnmpdStatsNoRxBufs=begemotSnmpdStatsNoRxBufs, begemotSnmpdTransLsock=begemotSnmpdTransLsock, begemotSnmpdObjects=begemotSnmpdObjects, begemotSnmpdDebugDumpPdus=begemotSnmpdDebugDumpPdus, begemotSnmpdLocalPortEntry=begemotSnmpdLocalPortEntry, begemotSnmpdTransportEntry=begemotSnmpdTransportEntry)
