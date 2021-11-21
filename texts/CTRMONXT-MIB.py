#
# PySNMP MIB module CTRMONXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRMONXT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctronRmon, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronRmon")
EntryStatus, OwnerString = mibBuilder.importSymbols("RMON-MIB", "EntryStatus", "OwnerString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Integer32, Counter32, ObjectIdentity, NotificationType, Gauge32, MibIdentifier, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctDiscovery = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20))
ctDiscoveryProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1))
ctProtIP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 1))
ctProtNetware = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 2))
ctProtDecNet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 3))
ctDiscoveryControlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2), )
if mibBuilder.loadTexts: ctDiscoveryControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlTable.setDescription('A list of Discovery Control Entries.')
ctDiscoveryControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryControlIndex"))
if mibBuilder.loadTexts: ctDiscoveryControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlEntry.setDescription('A list of parameters that set up the discovery \n        of devices by mac address, network address, protocol\n        mapping and the interface they appear on.')
ctDiscoveryControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlIndex.setDescription('An index that uniquely identifies an entry in\n        the ctDiscoveryControl table.  Each entry identifies a \n        function that will discover relationships between\n        MAC and Network layer addresses on a particular\n        interface and of a particular protocol. Information\n        about these relationships will be placed in the\n        ctDiscoveryMediaToNetTable and the ctDiscoveryNetToMedia\n        table.')
ctDiscoveryControlDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlDataSource.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlDataSource.setDescription('This object identifies the source of\n        the data from which this entry creates address relationships.\n        This source can be any interface on this device.  In\n        order to identify a particular interface, this object\n        shall identify the instance of the ifIndex object,\n        defined in [4,6], for the desired interface.  For\n        example, if an entry were to receive data from\n        interface #1, this object would be set to ifIndex.1.\n\n        The statistics in this group reflect all packets\n        on the local network segment attached to the\n        identified interface.\n\n        This object may not be modified if the associated\n        ctDiscoveryControlStatus object is equal to valid(1).')
ctDiscoveryControlProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlProtocol.setDescription('This object identifies the protocol suite, and \n        hence the type of network addresses in the tables, for \n        the table associated with this control index..  NOTE:\n        In this table, this value applies only to the network\n        layer of the packet.')
ctDiscoveryControlTableSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlTableSize.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlTableSize.setDescription('The number of ctDiscoveryMediaToNetEntries in\n        the ctDiscoveryMediaToNetTable\n        associated with this ctDiscoveryControlTable.\n        This must also be the number of entries in the\n        ctDiscoveryNetToMediaTable for this\n        ctDiscoveryControlTable.')
ctDiscoveryControlLastDeleteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlLastDeleteTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlLastDeleteTime.setDescription('The value of sysUpTime when the last entry\n        was deleted from the ctDiscoveryMediaToNetTable\n        associated with this ctDiscoveryControlEntry.')
ctDiscoveryControlAgeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlAgeInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlAgeInterval.setDescription('The minimum amount of idle time that will be allowed\n        for an entry before it may be deleted from the table\n        by the agent.\n        The aging routine is not required to run every second.')
ctDiscoveryControlOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 7), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlOwner.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlOwner.setDescription('The entity that configured this entry and is \n        therefore using the resources assigned to it.')
ctDiscoveryControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 8), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryControlStatus.setDescription('The status of this ctDiscoveryControl Entry.')
ctDiscoveryMNTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3), )
if mibBuilder.loadTexts: ctDiscoveryMNTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNTable.setDescription('A list of ctDiscoveryMNEntries.')
ctDiscoveryMNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryMNIndex"), (0, "CTRMONXT-MIB", "ctDiscoveryMNMACAddress"), (0, "CTRMONXT-MIB", "ctDiscoveryMNNetworkAddress"))
if mibBuilder.loadTexts: ctDiscoveryMNEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNEntry.setDescription('A MAC/Network address assocaition.')
ctDiscoveryMNMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNMACAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNMACAddress.setDescription('The MAC layer address of this MAC/Network\n        association')
ctDiscoveryMNNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNNetworkAddress.setDescription('The network layer address of this MAC/Network\n        association.')
ctDiscoveryMNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNIndex.setDescription('An index that defines the set of collected \n        ctDiscoveryMNEntries of which this entry is part.\n        The set of MAC/Network associations identified by a\n        particular value of this index is associated with\n        the ctDiscoveryControlEntry with the same index.')
ctDiscoveryMNCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNCreationTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNCreationTime.setDescription('The value of SysUpTime when an error free frame\n        with this source MAC/Network address association\n        was detected, and an entry with a corresponding\n        association was not present in the ctDiscoveryMNTable.')
ctDiscoveryMNLastTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNLastTransmitTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNLastTransmitTime.setDescription('The value of SysUpTime when this entry was last\n        updated.  This time correponds to the last time that\n        a frame with the source MAC/Network association of\n        this dicovery entry was detected.\n        This object is useful in that the management station \n        can    compute idle time by the difference between this \n        value and current sysUpTime.')
ctDiscoveryMNBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNBoard.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNBoard.setDescription('The index of the board that this MAC/Network\n        association was last seen on.  A value of zero\n        indicates that this information was not available.')
ctDiscoveryMNPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryMNPort.setDescription('The index of the port that this MAC/Network\n        association was last seen on.  A value of zero\n        indicates that this information was not available.')
ctDiscoveryNMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4), )
if mibBuilder.loadTexts: ctDiscoveryNMTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMTable.setDescription('A list of ctDiscoveryNMEntries.')
ctDiscoveryNMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryNMIndex"), (0, "CTRMONXT-MIB", "ctDiscoveryNMNetworkAddress"), (0, "CTRMONXT-MIB", "ctDiscoveryNMMACAddress"))
if mibBuilder.loadTexts: ctDiscoveryNMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMEntry.setDescription('A MAC/Network address assocaition.')
ctDiscoveryNMNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMNetworkAddress.setDescription('The Network layer address of this MAC/Network\n        association')
ctDiscoveryNMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMMACAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMMACAddress.setDescription('The MAC layer address of this MAC/Network\n        association')
ctDiscoveryNMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMIndex.setDescription('An index that defines the set of collected \n        ctDiscoveryNMEntries of which this entry is part.\n        The set of MAC/Network associations identified by a\n        particular value of this index is associated with\n        the ctDiscoveryControlEntry with the same index.')
ctDiscoveryNMCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMCreationTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMCreationTime.setDescription('The value of SysUpTime when an error free frame\n         with this source MAC/Network address association\n         was detected, and an entry with a corresponding\n         association was not present in the ctDiscoveryNMTable.')
ctDiscoveryNMLastTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMLastTransmitTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMLastTransmitTime.setDescription('The value of SysUpTime when this entry was last\n         updated.  This time correponds to the last time that\n         a frame with the source MAC/Network association of\n         this dicovery entry was detected.\n         This object is useful in that the management station \n         can    compute idle time by the difference between this \n         value and current sysUpTime.')
ctDiscoveryNMBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMBoard.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMBoard.setDescription('The index of the board that this MAC/Network\n        association was last seen on.  A value of zero\n        indicates that this information was not available.')
ctDiscoveryNMPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctDiscoveryNMPort.setDescription('The index of the port that this MAC/Network\n        association was last seen on.  A value of zero\n        indicates that this information was not available.')
mibBuilder.exportSymbols("CTRMONXT-MIB", ctDiscoveryProtocol=ctDiscoveryProtocol, ctDiscoveryControlDataSource=ctDiscoveryControlDataSource, ctDiscoveryNMIndex=ctDiscoveryNMIndex, ctProtNetware=ctProtNetware, ctDiscoveryNMLastTransmitTime=ctDiscoveryNMLastTransmitTime, ctDiscoveryMNTable=ctDiscoveryMNTable, ctDiscoveryNMTable=ctDiscoveryNMTable, ctDiscoveryControlLastDeleteTime=ctDiscoveryControlLastDeleteTime, ctDiscoveryMNPort=ctDiscoveryMNPort, ctDiscoveryControlAgeInterval=ctDiscoveryControlAgeInterval, ctDiscoveryControlProtocol=ctDiscoveryControlProtocol, ctDiscoveryMNBoard=ctDiscoveryMNBoard, ctDiscoveryMNLastTransmitTime=ctDiscoveryMNLastTransmitTime, ctDiscoveryNMNetworkAddress=ctDiscoveryNMNetworkAddress, ctDiscoveryNMMACAddress=ctDiscoveryNMMACAddress, ctDiscoveryNMPort=ctDiscoveryNMPort, ctProtIP=ctProtIP, ctDiscoveryControlStatus=ctDiscoveryControlStatus, ctDiscoveryNMCreationTime=ctDiscoveryNMCreationTime, ctDiscoveryControlIndex=ctDiscoveryControlIndex, ctDiscoveryMNNetworkAddress=ctDiscoveryMNNetworkAddress, ctDiscoveryNMBoard=ctDiscoveryNMBoard, ctProtDecNet=ctProtDecNet, ctDiscoveryControlOwner=ctDiscoveryControlOwner, ctDiscoveryMNCreationTime=ctDiscoveryMNCreationTime, ctDiscoveryMNEntry=ctDiscoveryMNEntry, ctDiscoveryMNIndex=ctDiscoveryMNIndex, ctDiscoveryNMEntry=ctDiscoveryNMEntry, ctDiscovery=ctDiscovery, ctDiscoveryControlTableSize=ctDiscoveryControlTableSize, ctDiscoveryControlTable=ctDiscoveryControlTable, ctDiscoveryControlEntry=ctDiscoveryControlEntry, ctDiscoveryMNMACAddress=ctDiscoveryMNMACAddress)
