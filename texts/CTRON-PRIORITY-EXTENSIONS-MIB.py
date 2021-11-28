#
# PySNMP MIB module CTRON-PRIORITY-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PRIORITY-EXTENSIONS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:22 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Integer32, Bits, Gauge32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Integer32", "Bits", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
ctPriorityExtTxQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1))
ctPriorityExtTXQueueTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1), )
if mibBuilder.loadTexts: ctPriorityExtTXQueueTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtTXQueueTable.setDescription('This table provides information pertaining to the number\n        of physical transmit queues per interface.')
ctPriorityExtTXQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1), ).setIndexNames((0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtSlotNum"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtInterfaceNum"))
if mibBuilder.loadTexts: ctPriorityExtTXQueueEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtTXQueueEntry.setDescription('Specifies the number of transmit queues for this interface.')
ctPriorityExtSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtSlotNum.setDescription('The slot num of the device that the interface is located on.')
ctPriorityExtInterfaceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtInterfaceNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtInterfaceNum.setDescription('The interface number for which the information is requested.\n         This is equal to the MIB-II ifIndex.')
ctPriorityExtNumTXQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtNumTXQueues.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtNumTXQueues.setDescription('The number of physical transmit queues for the requested interface.')
ctPriorityExtMACConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2))
ctPriorityExtMACStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtMACStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACStatus.setDescription('Defines the status of the priority packet forwarding based\n        on MAC address.  Setting ctIfPriorityExtMACStatus to a value of \n        disable(2), disables the forwarding of packets based on priority table \n        information.  All information remains in existence but is not \n        considered in the forwarding decision.')
ctPriorityExtNumMACEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtNumMACEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtNumMACEntries.setDescription('The number of active entries in the ctPriorityExtMACTable.')
ctPriorityExtMaxNumMACEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtMaxNumMACEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMaxNumMACEntries.setDescription('The maximum number of entries allowed in the ctPriorityExtMACTable.')
ctPriorityExtMaxNumPktTypesPerMACEntry = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtMaxNumPktTypesPerMACEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMaxNumPktTypesPerMACEntry.setDescription('The maximum number of packet types that can be asssociated\n        with any one MAC address in the ctPriorityExtMACTable')
ctPriorityExtMACTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5), )
if mibBuilder.loadTexts: ctPriorityExtMACTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACTable.setDescription('This table provides the ability to specify priority based\n        on the MAC addresses encoded in a packet.  There are several\n        possible permutations achieveable via this table. Priorities\n        in this table may be based on the following criteria:\n             \n           Destination address and specific packet type and VLAN ID\n           Destination address and specific packet type\n           Destination address\n           Source address and specific packet type and VLAN ID\n           Source address and specific packet type\n           Source address\n           Destination or source address and specific packet type and VLAN ID \n           Destination or source address and specific packet type\n           Destination or source address\n        Depending on the values set in the table which of these criteria\n        will be used for any given packet.\n\n        If any given relationship can not be created the set will fail with a \n        BAD-VALUE error.')
ctPriorityExtMACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1), ).setIndexNames((0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACAddr"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtAddrType"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACPktType"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACVlanId"))
if mibBuilder.loadTexts: ctPriorityExtMACEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACEntry.setDescription('Describes a particular MAC address priority entry.')
ctPriorityExtMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtMACAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACAddr.setDescription('The MAC address which will have a priority associated with it\n        as specified by ctPriorityExtMACPriority.')
ctPriorityExtAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("destAddr", 1), ("srcAddr", 2), ("destOrSource", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtAddrType.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtAddrType.setDescription('The type of MAC address which will have priority associated\n        with it as specified by ctPriorityExtMACPriority.')
ctPriorityExtMACPktType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtMACPktType.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACPktType.setDescription('The packet type associated with a particular MAC address,\n        specified by ctPriorityExtMACAddr, which will have priority\n        associated with it as specified by ctPriorityExtMACPriority.\n        A value of 1 indicates that this entry pertains to all \n        packet types.  A single value in the range of 0x0600..0xFFFF\n        indicates that this entry only pertains to that particular packet\n        type.')
ctPriorityExtMACVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtMACVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACVlanId.setDescription('A set of 65335 (0xFFFF) causes the priority value specified in \n         ctPriorityExtMACPriority to apply to all packets\n         matching the criteria specified by ctPriorityExtMACAddr, \n         ctPriorityExtAddrType, and ctPriorityExtMACPktType. Any \n         value between 1 and 4095 is a valid VLAN ID (IEEE 802.1q)\n         and causes ctPriorityExtMACPriority to only apply\n         to packets that are of matching the above criteria and that are \n         members of the IEEE 802.1q VLAN specified by the value set.')
ctPriorityExtMACPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 100))).clone(namedValues=NamedValues(("priority0", 1), ("priority1", 2), ("priority2", 3), ("priority3", 4), ("priority4", 5), ("priority5", 6), ("priority6", 7), ("priority7", 8), ("delete", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtMACPriority.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMACPriority.setDescription('A set of delete(100) will delete this row from the \n        ctPriorityExtMACTable.  A set of priority(1-8) will either\n        create a row in the ctPriorityExtMACTable with the specified\n        priority or modify an existing entry with the newly specified \n        priority.')
ctPriorityExtPktTypeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3))
ctPriorityExtPktTypeStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtPktTypeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktTypeStatus.setDescription('Defines the status of the priority packet forwarding based \n        exclusively on packet type.  Setting ctIfPriorityPktTypeExtStatus \n        to a value of disable(2) disables the forwarding of packets \n        based on priority table information.  All information remains \n        in existence but is not considered in the forwarding decision.')
ctPriorityExtNumPktTypeEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtNumPktTypeEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtNumPktTypeEntries.setDescription('The number of active entries in the ctPriorityExtPktTypeTable.')
ctPriorityExtMaxNumPktTypeEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtMaxNumPktTypeEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtMaxNumPktTypeEntries.setDescription('The maximum number of entries allowed in the \n        ctPriorityExtPktTypeTable.')
ctPriorityExtPktTypeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4), )
if mibBuilder.loadTexts: ctPriorityExtPktTypeTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktTypeTable.setDescription('This table provides the ability to specify priority based\n        on the packet type encoded in a packet. Priorities  \n        in this table may be based on the following criteria:\n             \n           Packet type and VLAN ID\n           Packet type\n\n        If any given relationship can not be created the set will fail with a \n        BAD-VALUE error.')
ctPriorityExtPktTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1), ).setIndexNames((0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPktType"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPktTypeVlanId"))
if mibBuilder.loadTexts: ctPriorityExtPktTypeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktTypeEntry.setDescription('Describes a particular packet type priority entry.')
ctPriorityExtPktType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtPktType.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktType.setDescription('The packet type which will have priority associated with \n        it as specified by ctPriorityExtPktTypePriority.\n        A value of 1 indicates that this entry pertains to all \n        packet types.  A single value in the range of 0x0600..0xFFFF\n        indicates that this entry only pertains to that particular packet\n        type.')
ctPriorityExtPktTypeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtPktTypeVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktTypeVlanId.setDescription('A set of 65535 (0xFFFF) causes the priority value specified in \n         ctPriorityExtPktTypePriority to apply to all packets\n         of the type specified by ctPriorityExtPktType.  Any\n         value between 1 and 4095 is a valid VLAN ID (IEEE 802.1q)\n         and causes ctPriorityExtPktTypePriority to only apply\n         to packets that are of ctPriorityExtPktType type and are \n         members of the IEEE 802.1q VLAN specified by the value set.')
ctPriorityExtPktTypePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 100))).clone(namedValues=NamedValues(("priority0", 1), ("priority1", 2), ("priority2", 3), ("priority3", 4), ("priority4", 5), ("priority5", 6), ("priority6", 7), ("priority7", 8), ("delete", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtPktTypePriority.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPktTypePriority.setDescription('A set of delete(100) will delete this row from the \n        ctPriorityExtPriorityTypeTable.  A set of priority(1-8) will either\n        create a row in the ctPriorityExtPriorityTypeTable with the specified\n        priority or modify an existing entry with the newly specified \n        priority.')
ctPriorityExtPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4))
ctPriorityExtPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortStatus.setDescription('Defines the status of the priority packet forwarding based\n        on receive port.  Setting ctIfPriorityExtPortStatus to a value of \n        disable(2), disables the forwarding of packets based on priority table \n        information.  All information remains in existence but is not \n        considered in the forwarding decision.')
ctPriorityExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2), )
if mibBuilder.loadTexts: ctPriorityExtPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortTable.setDescription('This table provides information pertaining to the priority associated \n         with a receive port.')
ctPriorityExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1), ).setIndexNames((0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPortSlotNum"), (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPortInterfaceNum"))
if mibBuilder.loadTexts: ctPriorityExtPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortEntry.setDescription('Specifies the priority associated with a specific physical \n        interface.')
ctPriorityExtPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtPortSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortSlotNum.setDescription('The slot num of the device that the interface is located on.')
ctPriorityExtPortInterfaceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriorityExtPortInterfaceNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortInterfaceNum.setDescription('The interface number for which the information is requested.')
ctPriorityExtPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("priority0", 1), ("priority1", 2), ("priority2", 3), ("priority3", 4), ("priority4", 5), ("priority5", 6), ("priority6", 7), ("priority7", 8))).clone('priority0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtPortPriority.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtPortPriority.setDescription('A set of priority(1-8) will modify an existing entry \n        with the newly specified priority.  Entries cannot be \n        deleted from this table.')
ctPriorityExtFwdInboundPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriorityExtFwdInboundPriority.setStatus('mandatory')
if mibBuilder.loadTexts: ctPriorityExtFwdInboundPriority.setDescription('This controls whether a packet that is received with a priority tag\n        is forwarded with the priority encoded in the tag or the default\n        priority of the port.  A value of enable(1) means the packet will \n        be forwarded with the priority encoded in the tag.  A value of\n        disable(2) means the packet will be given the default priority\n        of the port it was received on.')
mibBuilder.exportSymbols("CTRON-PRIORITY-EXTENSIONS-MIB", ctPriorityExtPortConfig=ctPriorityExtPortConfig, ctPriorityExtMACAddr=ctPriorityExtMACAddr, ctPriorityExtMACVlanId=ctPriorityExtMACVlanId, ctPriorityExtMaxNumPktTypeEntries=ctPriorityExtMaxNumPktTypeEntries, ctPriorityExtPktTypeVlanId=ctPriorityExtPktTypeVlanId, ctPriorityExtPktTypeStatus=ctPriorityExtPktTypeStatus, ctPriorityExtSlotNum=ctPriorityExtSlotNum, ctPriorityExtMaxNumPktTypesPerMACEntry=ctPriorityExtMaxNumPktTypesPerMACEntry, ctPriorityExtPktTypeTable=ctPriorityExtPktTypeTable, ctPriorityExtMACPktType=ctPriorityExtMACPktType, ctPriorityExtTXQueueEntry=ctPriorityExtTXQueueEntry, ctPriorityExtPortTable=ctPriorityExtPortTable, ctPriorityExtPortSlotNum=ctPriorityExtPortSlotNum, ctPriorityExtPortStatus=ctPriorityExtPortStatus, ctPriorityExtPortEntry=ctPriorityExtPortEntry, ctPriorityExtNumTXQueues=ctPriorityExtNumTXQueues, ctPriorityExtNumMACEntries=ctPriorityExtNumMACEntries, ctPriorityExtMACEntry=ctPriorityExtMACEntry, ctPriorityExtMACTable=ctPriorityExtMACTable, ctPriorityExtFwdInboundPriority=ctPriorityExtFwdInboundPriority, ctPriorityExtPktTypePriority=ctPriorityExtPktTypePriority, ctPriorityExtPortInterfaceNum=ctPriorityExtPortInterfaceNum, ctPriorityExtTxQueue=ctPriorityExtTxQueue, ctPriorityExtTXQueueTable=ctPriorityExtTXQueueTable, ctPriorityExtAddrType=ctPriorityExtAddrType, ctPriorityExtNumPktTypeEntries=ctPriorityExtNumPktTypeEntries, ctPriorityExtPortPriority=ctPriorityExtPortPriority, ctPriorityExtMACPriority=ctPriorityExtMACPriority, ctPriorityExtMACStatus=ctPriorityExtMACStatus, ctPriorityExtPktType=ctPriorityExtPktType, ctPriorityExtMaxNumMACEntries=ctPriorityExtMaxNumMACEntries, ctPriorityExtInterfaceNum=ctPriorityExtInterfaceNum, ctPriorityExtPktTypeConfig=ctPriorityExtPktTypeConfig, ctPriorityExtPktTypeEntry=ctPriorityExtPktTypeEntry, ctPriorityExtMACConfig=ctPriorityExtMACConfig)
