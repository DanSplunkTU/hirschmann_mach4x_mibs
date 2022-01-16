#
# PySNMP MIB module CTRON-DLSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DLSW-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ctDLSW, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDLSW")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, iso, Counter64, Unsigned32, MibIdentifier, Integer32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class NBName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

ctdlswNode = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1))
ctdlswNodeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1))
ctdlswPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2))
ctdlswFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3))
ctdlswTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4))
ctdlswTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 5))
ctdlswEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6))
ctdlswEventLogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1))
ctdlswEventLogFilterTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2))
ctdlswEventLogTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3))
ctdlswVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswVersion.setDescription('Indicates the current revision level of the DLSw firmware\n        in textual format.')
ctdlswAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswAdminStatus.setDescription('Sets the system-wide administrative state of DLSw services.')
ctdlswOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswOperStatus.setDescription('Indicates the current system-wide status of DLSw services.')
ctdlswUpTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswUpTime.setDescription('Indicates the time (in hundredths of a second) since the DLSw\n        services portion of the system was enabled.')
ctdlswOperVirtualRingNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswOperVirtualRingNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswOperVirtualRingNumber.setDescription('Specifies the operational ring/segment number that uniquely\n        identifies the virtual segment to which this DLSw is connected.\n        This object may only be modified when ctdlswOperStatus is\n        disabled.')
ctdlswNBLocalFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswNBLocalFilterType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswNBLocalFilterType.setDescription('Specifies the type of filtering to be applied\n        to NetBIOS frames received on a local LAN segment.\n        If set to block(1), any frame matching any entry in\n        ctdlswNBLocalFilterTable will not be forwarded.\n        If set to pass(2), only frames matching any entry in\n        ctdlswNBLocalFilterTable will be forwarded.')
ctdlswNBRemoteFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswNBRemoteFilterType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswNBRemoteFilterType.setDescription('Specifies the type of filtering to be applied to\n        NetBIOS frames received from a remote DLSw partner.\n        If set to block(1), any frame matching any entry in\n        ctdlswNBRemoteFilterTable will not be forwarded.\n        If set to pass(2), only frames matching any entry in\n        ctdlswNBRemoteFilterTable will be forwarded.')
ctdlswMacLocalFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswMacLocalFilterType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswMacLocalFilterType.setDescription('Specifies the type of address filtering to be applied\n        to SNA MAC frames received on a local LAN segment.\n        If set to block(1), any frame matching any entry in\n        ctdlswMacLocalFilterTable will not be forwarded.\n        If set to pass(2), only frames matching any entry in\n        ctdlswMacLocalFilterTable will be forwarded.')
ctdlswMacRemoteFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswMacRemoteFilterType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswMacRemoteFilterType.setDescription('Specifies the type of address filtering to be applied\n        to SNA MAC frames received from a remote DLSw partner.\n        If set to block(1), any frame matching any entry in\n        ctdlswMacRemoteFilterTable will not be forwarded.\n        If set to pass(2), only frames matching any entry in\n        ctdlswMacRemoteFilterTable will be forwarded.')
ctdlswAcceptDynamicTConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswAcceptDynamicTConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswAcceptDynamicTConn.setDescription('Specifies whether this DLSw allows unconfigured DLSw partners\n        to establish transport connections.  Yes(1) means unconfigured\n        DLSw partners may establish transport connections with this\n        DLSw.  No(2) means only user configured DLSw partners may\n        establish transport connections with this DLSw.')
ctdlswDefaultPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswDefaultPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswDefaultPortNumber.setDescription("Specifies the index of the port whose associated IP address\n        will be used to identify this DLSw node to its DLSw partners.\n        The value must be consistent with 'ifIndex' of mib-II.")
ctdlswPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1), )
if mibBuilder.loadTexts: ctdlswPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortTable.setDescription('This table contains an entry for each port, and specifies\n        configuration parameters used to establish circuits over that\n        port.  This table is indexed by ctdlswPortName, which \n        identifies the port for which an entry exists.  These port\n        configuration entries will be provided automatically based on\n        the physical port configuration.  These entries cannot be\n        created or deleted - only modified.')
ctdlswPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswPortName"))
if mibBuilder.loadTexts: ctdlswPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortEntry.setDescription('Each entry specifies configuration parameters for a port for\n        which the entry exists.')
ctdlswPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortIndex.setDescription("Specifies a unique value for each port.  Values are derived\n        from 'ifIndex' of mib-II.")
ctdlswPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortName.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortName.setDescription('Specifies the user friendly name for this port.')
ctdlswPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortAddress.setDescription('Specifies the MAC address of this port.')
ctdlswPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswPortAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortAdminStatus.setDescription('Sets the administrative state of DLSw frame forwarding\n        for this port.')
ctdlswPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortOperStatus.setDescription('Specifies the current operating status of DLSw frame\n        forwarding for this port.')
ctdlswPortUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswPortUpTime.setDescription('Indicates the time (in hundredths of a second) since this port\n        was enabled.  A value of zero means this port is not presently\n        enabled.')
ctdlswLocalNBFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1), )
if mibBuilder.loadTexts: ctdlswLocalNBFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalNBFilterTable.setDescription('A list of NETBIOS source-destination name pairs whose frames\n        are allowed (or not allowed) to be forwarded via this DLSw.\n        Only source-destination name pairs from locally generated \n        NetBIOS frames are compared against entries in this table.')
ctdlswLocalNBFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterSrcName"), (0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterDestName"))
if mibBuilder.loadTexts: ctdlswLocalNBFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalNBFilterEntry.setDescription('Information for one NetBIOS source-destination name pair.')
ctdlswLocalNBFilterSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 1), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalNBFilterSrcName.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalNBFilterSrcName.setDescription('The source NETBIOS name to filter on.')
ctdlswLocalNBFilterDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 2), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalNBFilterDestName.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalNBFilterDestName.setDescription('The destination NETBIOS NAME to filter on.')
ctdlswLocalNBFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswLocalNBFilterControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalNBFilterControl.setDescription('Set this object to delete(3) to remove this entry.  Set to\n        create(2) to add this entry.  A get of this object will return\n        other(1).')
ctdlswRemoteNBFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2), )
if mibBuilder.loadTexts: ctdlswRemoteNBFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteNBFilterTable.setDescription('A list of NETBIOS source-destination name pairs whose frames\n        are allowed (or not allowed) to be forwarded via this DLSw.\n        Only source-destination name pairs from NetBIOS frames received\n        from remote DLSw partners are compared against entries in this table.')
ctdlswRemoteNBFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterSrcName"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterDestName"))
if mibBuilder.loadTexts: ctdlswRemoteNBFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteNBFilterEntry.setDescription('Information for one NetBIOS source-destination name pair.')
ctdlswRemoteNBFilterSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 1), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterSrcName.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteNBFilterSrcName.setDescription('The source NETBIOS name to filter on.')
ctdlswRemoteNBFilterDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 2), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterDestName.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteNBFilterDestName.setDescription('The destination NETBIOS name to filter on.')
ctdlswRemoteNBFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteNBFilterControl.setDescription('Set this object to delete(3) to remove this entry.  Set to\n        create(2) to add this entry.  A get of this object will return\n        other(1).')
ctdlswLocalMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3), )
if mibBuilder.loadTexts: ctdlswLocalMacFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterTable.setDescription('A list of source-destination MAC address pairs whose frames\n        are allowed (or not allowed) to be forwarded via this DLSw.\n        Only source-destination name pairs from locally generated \n        SNA MAC frames are compared against entries in this table.')
ctdlswLocalMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcAddr"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcMask"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestAddr"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestMask"))
if mibBuilder.loadTexts: ctdlswLocalMacFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterEntry.setDescription('Information for one source-destination MAC address pair.')
ctdlswLocalMacFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcAddr.setDescription('The source MAC Address to filter on.')
ctdlswLocalMacFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcMask.setDescription('The source MAC Address mask to filter on.')
ctdlswLocalMacFilterDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestAddr.setDescription('The destination MAC Address to filter on.')
ctdlswLocalMacFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestMask.setDescription('The destination MAC Address mask to filter on.')
ctdlswLocalMacFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswLocalMacFilterControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswLocalMacFilterControl.setDescription('Set this object to delete(3) to remove this entry.  Set to\n        create(2) to add this entry.  A get of this object will return\n        other(1).')
ctdlswRemoteMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4), )
if mibBuilder.loadTexts: ctdlswRemoteMacFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterTable.setDescription('A list of source-destination MAC address pairs whose frames\n        are allowed (or not allowed) to be forwarded via this DLSw.\n        Only source-destination name pairs from SNA MAC frames received\n        from remote DLSw partners are compared against entries in this table.')
ctdlswRemoteMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcAddr"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcMask"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestAddr"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestMask"))
if mibBuilder.loadTexts: ctdlswRemoteMacFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterEntry.setDescription('Information for one source-destination MAC address pair.')
ctdlswRemoteMacFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcAddr.setDescription('The source MAC Address to filter on.')
ctdlswRemoteMacFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcMask.setDescription('The source MAC Address mask to filter on.')
ctdlswRemoteMacFilterDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestAddr.setDescription('The destination MAC Address to filter on.')
ctdlswRemoteMacFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestMask.setDescription('The destination MAC Address mask to filter on.')
ctdlswRemoteMacFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswRemoteMacFilterControl.setDescription('Set this object to delete(3) to remove this entry.  Set to\n        create(2) to add this entry.  A get of this object will return\n        other(1).')
ctdlswTConnTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1), )
if mibBuilder.loadTexts: ctdlswTConnTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnTable.setDescription('A list of transport connections which are either user defined\n        or dynamically created for this DLSw.')
ctdlswTConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswTConnRemoteTAddr"))
if mibBuilder.loadTexts: ctdlswTConnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnEntry.setDescription('')
ctdlswTConnRemoteTAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnRemoteTAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnRemoteTAddr.setDescription('Specifies the remote transport address for this transport\n        connection.  It can be defined by the user, or established\n        dynamically upon receiving a connection setup request from\n        another DLSw.')
ctdlswTConnControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswTConnControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnControl.setDescription('Set this object to delete(3) to remove this entry.  Set to\n        create(2) to add this entry.  A get of this object will\n        return other(1).')
ctdlswTConnUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnUpTime.setDescription('Indicates the time (in hundredths of a second) since this\n        transport connection was last established.  A value of zero\n        means this transport connection is not presently established.')
ctdlswTConnOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pendingDisable", 4), ("pendingEnable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnOperStatus.setDescription('Indicates the status of this transport connection.')
ctdlswTConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configured", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswTConnType.setDescription('Indicates the means by which this transport connection was\n        determined.  Configured(1) means this entry was user defined.\n        Dynamic(2) means this entry was not user defined but was \n        created as a result of a connection initiated by another DLSw.')
ctdlswEventAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventAdminStatus.setDescription('Set the administrative state of Data Link Switching event\n        logging. enabled(3) causes the event log to become active.\n        disabled(2) causes the event log to become inactive.')
ctdlswEventMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 2), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventMaxEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventMaxEntries.setDescription('Sets the maximum number of entries allowed in the event log\n       table.  When the number of entries reaches the value of\n       ctdlswEventMaxEntries the first (oldest) entry is deleted\n       to allow a new entry to be added.')
ctdlswEventTraceAll = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventTraceAll.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventTraceAll.setDescription('enabled(3) allows logging of all event types.\n        disabled(2) causes the event log filter table to specify\n        which events to log.')
ctdlswEventFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1), )
if mibBuilder.loadTexts: ctdlswEventFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFilterTable.setDescription('This table contains descriptions of how to filter log entries.')
ctdlswEventFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswEventFltrProtocol"), (0, "CTRON-DLSW-MIB", "ctdlswEventFltrIfNum"))
if mibBuilder.loadTexts: ctdlswEventFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFilterEntry.setDescription('Each entry specifies the filter for log entries.  The\n        instance ctdlswEventProtocol refers to the instance used\n        in the nwRtgProtocolTable and nwComponentTable specified\n        by the ctrouter-mib.txt. ')
ctdlswEventFltrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventFltrProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrProtocol.setDescription('Selects the protocol to log events from.')
ctdlswEventFltrIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventFltrIfNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrIfNum.setDescription('Specifies the port on which to log events.')
ctdlswEventFltrControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("delete", 2), ("add", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrControl.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrControl.setDescription('Setting this field to delete will allow entries to be\n        removed from the table.  This is done by adding new entries\n        with instance fields that match the entry to be removed from\n        the table.  The new entry being added must have this control\n        field set to delete in order for the matching entry already\n        in the table to be deleted.  Setting this field to add will\n        add the entry to the table.')
ctdlswEventFltrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("misc", 1), ("timer", 2), ("rcv", 4), ("xmit", 8), ("event", 16), ("error", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrType.setDescription('This bit field mask filter will allow only events of\n        certain types to be logged.  By default all types will be\n        logged.  Clearing event types from this field will cause\n        those types not to be logged.  Adding event types to this\n        field will enable those types to be logged. ')
ctdlswEventFltrSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("highest", 1), ("highmed", 2), ("highlow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrSeverity.setDescription('This filter controls the amount of logging by ignoring events\n        of lower priority than that specified by the filter value.\n        Specifying highest(1) causes all events except those of highest\n        severity to be ignored. Specifying highmed(2) causes lowest\n        severity events to be ignored.  Specifying highlow(3) causes\n        all events to be logged.  highmed(2) is the default setting.')
ctdlswEventFltrAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("log", 1), ("trap", 2), ("logTrap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrAction.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventFltrAction.setDescription('This field specifies how the events are to be logged.\n        Specifying log(1) stores the events in the event log\n        table (defined below).  Specifying trap(2) sends events\n        out through the trap mechanism. Specifying logTrap(3)\n        does both. ')
ctdlswEventTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1), )
if mibBuilder.loadTexts: ctdlswEventTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventTable.setDescription('This table contains all events that have been logged.')
ctdlswEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswEventNumber"))
if mibBuilder.loadTexts: ctdlswEventEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventEntry.setDescription('Each entry specifies events that have been logged.')
ctdlswEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventNumber.setDescription('The number uniquely identifies events.')
ctdlswEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventTime.setDescription('This number specifies when the event was logged.')
ctdlswEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("misc", 1), ("timer", 2), ("rcv", 4), ("xmit", 8), ("event", 16), ("error", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventType.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventType.setDescription('Specifies type of event logged.')
ctdlswEventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("highest", 1), ("highmed", 2), ("highlow", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventSeverity.setDescription('Specifies the severity of the event logged.')
ctdlswEventProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventProtocol.setDescription('Specifies the protocol where the event occured.')
ctdlswEventIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventIfNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventIfNum.setDescription('Specifies the port the event occurred on.')
ctdlswEventTextString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventTextString.setStatus('mandatory')
if mibBuilder.loadTexts: ctdlswEventTextString.setDescription('Specifies the actual text string to be logged.')
mibBuilder.exportSymbols("CTRON-DLSW-MIB", ctdlswEventLogConfig=ctdlswEventLogConfig, ctdlswRemoteMacFilterEntry=ctdlswRemoteMacFilterEntry, ctdlswRemoteNBFilterControl=ctdlswRemoteNBFilterControl, ctdlswNodeConfig=ctdlswNodeConfig, ctdlswLocalNBFilterControl=ctdlswLocalNBFilterControl, ctdlswPortAdminStatus=ctdlswPortAdminStatus, ctdlswEventProtocol=ctdlswEventProtocol, ctdlswLocalNBFilterSrcName=ctdlswLocalNBFilterSrcName, ctdlswEventFltrIfNum=ctdlswEventFltrIfNum, ctdlswRemoteNBFilterEntry=ctdlswRemoteNBFilterEntry, ctdlswPortAddress=ctdlswPortAddress, ctdlswEventTraceAll=ctdlswEventTraceAll, ctdlswPortName=ctdlswPortName, ctdlswPortIndex=ctdlswPortIndex, ctdlswEventEntry=ctdlswEventEntry, ctdlswTrap=ctdlswTrap, ctdlswEventFltrControl=ctdlswEventFltrControl, ctdlswNBLocalFilterType=ctdlswNBLocalFilterType, ctdlswLocalNBFilterEntry=ctdlswLocalNBFilterEntry, ctdlswTConn=ctdlswTConn, ctdlswEventFltrProtocol=ctdlswEventFltrProtocol, ctdlswEventType=ctdlswEventType, ctdlswRemoteNBFilterDestName=ctdlswRemoteNBFilterDestName, ctdlswMacLocalFilterType=ctdlswMacLocalFilterType, ctdlswTConnOperStatus=ctdlswTConnOperStatus, ctdlswRemoteNBFilterSrcName=ctdlswRemoteNBFilterSrcName, ctdlswLocalMacFilterEntry=ctdlswLocalMacFilterEntry, ctdlswRemoteMacFilterSrcAddr=ctdlswRemoteMacFilterSrcAddr, ctdlswNBRemoteFilterType=ctdlswNBRemoteFilterType, ctdlswEventLogFilterTable=ctdlswEventLogFilterTable, ctdlswEventLogTable=ctdlswEventLogTable, ctdlswEventTable=ctdlswEventTable, ctdlswMacRemoteFilterType=ctdlswMacRemoteFilterType, ctdlswEventNumber=ctdlswEventNumber, ctdlswLocalMacFilterControl=ctdlswLocalMacFilterControl, ctdlswTConnUpTime=ctdlswTConnUpTime, ctdlswLocalMacFilterDestAddr=ctdlswLocalMacFilterDestAddr, ctdlswLocalNBFilterDestName=ctdlswLocalNBFilterDestName, ctdlswRemoteMacFilterDestAddr=ctdlswRemoteMacFilterDestAddr, ctdlswPortUpTime=ctdlswPortUpTime, ctdlswEventMaxEntries=ctdlswEventMaxEntries, ctdlswPortTable=ctdlswPortTable, ctdlswEventFilterEntry=ctdlswEventFilterEntry, ctdlswRemoteMacFilterSrcMask=ctdlswRemoteMacFilterSrcMask, ctdlswEventTime=ctdlswEventTime, ctdlswEventTextString=ctdlswEventTextString, ctdlswTConnTable=ctdlswTConnTable, ctdlswUpTime=ctdlswUpTime, ctdlswOperVirtualRingNumber=ctdlswOperVirtualRingNumber, ctdlswRemoteMacFilterControl=ctdlswRemoteMacFilterControl, ctdlswPortEntry=ctdlswPortEntry, ctdlswEventAdminStatus=ctdlswEventAdminStatus, ctdlswEventFltrType=ctdlswEventFltrType, ctdlswLocalNBFilterTable=ctdlswLocalNBFilterTable, ctdlswLocalMacFilterDestMask=ctdlswLocalMacFilterDestMask, NBName=NBName, ctdlswEventFltrSeverity=ctdlswEventFltrSeverity, ctdlswLocalMacFilterSrcMask=ctdlswLocalMacFilterSrcMask, ctdlswTConnRemoteTAddr=ctdlswTConnRemoteTAddr, ctdlswPortOperStatus=ctdlswPortOperStatus, ctdlswRemoteNBFilterTable=ctdlswRemoteNBFilterTable, ctdlswPort=ctdlswPort, ctdlswRemoteMacFilterTable=ctdlswRemoteMacFilterTable, ctdlswEvent=ctdlswEvent, ctdlswLocalMacFilterSrcAddr=ctdlswLocalMacFilterSrcAddr, ctdlswAdminStatus=ctdlswAdminStatus, ctdlswLocalMacFilterTable=ctdlswLocalMacFilterTable, ctdlswVersion=ctdlswVersion, ctdlswTConnType=ctdlswTConnType, ctdlswEventSeverity=ctdlswEventSeverity, ctdlswTConnControl=ctdlswTConnControl, ctdlswNode=ctdlswNode, ctdlswOperStatus=ctdlswOperStatus, ctdlswEventFilterTable=ctdlswEventFilterTable, ctdlswFilter=ctdlswFilter, ctdlswEventFltrAction=ctdlswEventFltrAction, ctdlswDefaultPortNumber=ctdlswDefaultPortNumber, ctdlswRemoteMacFilterDestMask=ctdlswRemoteMacFilterDestMask, ctdlswEventIfNum=ctdlswEventIfNum, ctdlswAcceptDynamicTConn=ctdlswAcceptDynamicTConn, ctdlswTConnEntry=ctdlswTConnEntry)
