#
# PySNMP MIB module CTRON-WAN-IMUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WAN-IMUX-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctWanServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctWanServices")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Integer32, Counter32, ObjectIdentity, NotificationType, Gauge32, MibIdentifier, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctWanMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1))
ctWANMuxGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1))
ctWANMuxMaxNumGroups = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWANMuxMaxNumGroups.setStatus('mandatory')
if mibBuilder.loadTexts: ctWANMuxMaxNumGroups.setDescription('Get the maximum number of Inverse Multiplexer groups\n                        allowed to be programmed for this device.  This value\n                        is the number of physical WAN connections, divided by\n                        the minimum number of channels for a single mux\n                        to be operational (2).  However, some devices may only\n                        support a single inverse multiplexer group.')
ctWanMuxAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMuxAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxAdmin.setDescription('Used to enable and disable the Inverse Multiplexer\n                        Application.  This object is used to enable/disable\n                        Inverse Multiplexing for the entire device.  Inverse\n                        Multiplexer Groups may be enabled/disabled independently\n                        using ctWanMuxGroupAdmin.  This object must be set to \n                        enabled for any inverse multiplexing to occur on the \n                        device.')
ctWanMuxGroupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2), )
if mibBuilder.loadTexts: ctWanMuxGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupTable.setDescription('Information describing the configured parameters\n                        of one of the Inverse Multiplexer groups.')
ctWanMuxGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1), ).setIndexNames((0, "CTRON-WAN-IMUX-MIB", "ctWanMuxGroupId"))
if mibBuilder.loadTexts: ctWanMuxGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupEntry.setDescription('A description of a single Inverse Multiplexer group \n                        entry.')
ctWanMuxGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupId.setDescription('A unique value identifying an element in a sequence of\n                        groups which belong to the WAN Inverse Multiplexer.  \n                        This value ranges from 1 to the maximum number of \n                        programmable groups as described by\n                        ctWANMuxMaxNumGroups.')
ctWanMuxGroupAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMuxGroupAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupAdmin.setDescription("Used to enable and disable an Inverse Multiplexer\n                        group which evenly distributes data traffic in a\n                        properly sequenced fashion, over two or more single \n                        channel Wide Area Network connections such as DS1, \n                        E1, DDS, or SYNC.  Each of the single channel \n                        connections must be configured with an appropriate \n                        datalink protocol. A minimum of two channels, each \n                        assigned to it's own physical interface, is required\n                        before the Inverse Multiplexer group can be enabled.")
ctWanMuxGroupNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxGroupNumChannels.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupNumChannels.setDescription("Get the number of channels currently\n                        associated with this Inverse Multiplexer group. A \n                        minimum of two channels, each assigned to it's own\n                        physical interface, is required before the Inverse \n                        Multiplexer group can be enabled.")
ctWanMuxGroupAddChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMuxGroupAddChannel.setReference('rfc-1213')
if mibBuilder.loadTexts: ctWanMuxGroupAddChannel.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupAddChannel.setDescription('Add a channel to the channel list used by this Inverse\n                        Multiplexer group.  Before a channel is added, the \n                        channel must be assigned a MIB II ifindex, and an\n                        acceptable Datalink Protocol. When this object is set,\n                        it is set with the ifindex value. This object is always\n                        read as a 1.')
ctWanMuxGroupDelChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMuxGroupDelChannel.setReference('rfc-1213')
if mibBuilder.loadTexts: ctWanMuxGroupDelChannel.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxGroupDelChannel.setDescription("Delete a channel to the channel list used by this \n                        Inverse Multiplexer group.  Before a channel is\n                        deleted, the channel must exist in the Inverse\n                        Multiplexer group's channel table.  When this object\n                        is set, it is set with the ifindex value of the channel\n                        the user wishes to delete from the channel table. This \n                        object is always read as a 1.")
ctWanMuxChannelTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3), )
if mibBuilder.loadTexts: ctWanMuxChannelTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelTable.setDescription('Table containing ifindex values, representing WAN \n                        channels, used by the Inverse Multiplexer. The table \n                        also contains statistics reported about each channel.')
ctWanMuxChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1), ).setIndexNames((0, "CTRON-WAN-IMUX-MIB", "ctWanMuxChannelGroupId"), (0, "CTRON-WAN-IMUX-MIB", "ctWanMuxChannelId"))
if mibBuilder.loadTexts: ctWanMuxChannelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelEntry.setDescription('A description of a single entry.')
ctWanMuxChannelGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelGroupId.setDescription('A unique value identifying an element in a sequence \n                        of groups which belong to the WAN Inverse Multiplexer.\n                        This value ranges from 1 to the maximum number of \n                        programmable groups as described by\n                        ctWANMuxMaxNumGroups.')
ctWanMuxChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelId.setDescription('A unique value identifying an element in a sequence of\n                        member channel ifindex values which belong to a WAN \n                        Inverse Multiplexer group.')
ctWanMuxChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelIfIndex.setDescription('Returns an ifindex associated with a WAN\n                        channel used for Inverse Multiplexing.')
ctWanMuxChannelPhysNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelPhysNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelPhysNum.setDescription("Returns a unique physical connection identifier \n                        associated with this channel's physical WAN\n                        connection.")
ctWanMuxChannelBwAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelBwAvail.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelBwAvail.setDescription('Returns a value which represents the available \n                        bandwidth for transmitting data existing for the \n                        physical WAN connection associated with this channel.\n                        The value is represented in bits/sec.')
ctWanMuxChannelByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelByteCount.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelByteCount.setDescription('Returns a value which represents a cumulative count\n                        of bytes transmitted out from this interface.  The \n                        count includes any bytes transmitted across the\n                        physical medium, less physical medium framing.')
ctWanMuxChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMuxChannelStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMuxChannelStatus.setDescription('Returns the current status of the channel associated\n                        with an inverse multiplexer group.  The channel is \n                        active when the group admin status is enabled, and \n                        the channel is operational.  The channel is inactive \n                        when either the group admin status is disabled, or \n                        the channel is not operational.')
mibBuilder.exportSymbols("CTRON-WAN-IMUX-MIB", ctWanMuxChannelBwAvail=ctWanMuxChannelBwAvail, ctWanMuxAdmin=ctWanMuxAdmin, ctWanMuxGroupTable=ctWanMuxGroupTable, ctWanMuxChannelEntry=ctWanMuxChannelEntry, ctWanMuxChannelByteCount=ctWanMuxChannelByteCount, ctWanMuxGroupAdmin=ctWanMuxGroupAdmin, ctWANMuxGeneralGroup=ctWANMuxGeneralGroup, ctWanMuxGroupNumChannels=ctWanMuxGroupNumChannels, ctWanMuxChannelStatus=ctWanMuxChannelStatus, ctWanMux=ctWanMux, ctWanMuxChannelTable=ctWanMuxChannelTable, ctWanMuxGroupId=ctWanMuxGroupId, ctWanMuxChannelGroupId=ctWanMuxChannelGroupId, ctWanMuxChannelId=ctWanMuxChannelId, ctWanMuxGroupEntry=ctWanMuxGroupEntry, ctWanMuxChannelPhysNum=ctWanMuxChannelPhysNum, ctWanMuxGroupAddChannel=ctWanMuxGroupAddChannel, ctWanMuxChannelIfIndex=ctWanMuxChannelIfIndex, ctWANMuxMaxNumGroups=ctWANMuxMaxNumGroups, ctWanMuxGroupDelChannel=ctWanMuxGroupDelChannel)
