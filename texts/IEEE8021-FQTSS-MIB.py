#
# PySNMP MIB module IEEE8021-FQTSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-FQTSS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:23 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
ieee8021BridgeBaseComponentId, ieee8021BridgeBasePortEntry, ieee8021BridgeBasePort, ieee8021BridgeBaseEntry = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePortEntry", "ieee8021BridgeBasePort", "ieee8021BridgeBaseEntry")
ieee802dot1mibs, IEEE8021PriorityValue = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs", "IEEE8021PriorityValue")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, NotificationType, IpAddress, Counter32, Bits, Counter64, Gauge32, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "IpAddress", "Counter32", "Bits", "Counter64", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ieee8021FqtssMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 16))
ieee8021FqtssMib.setRevisions(('2018-10-04 00:00', '2018-06-28 00:00', '2015-12-02 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2009-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021FqtssMib.setRevisionsDescriptions(('Published as part of IEEE 802.1Qcc-2018.\n\t\t\tAdded managed objects for Stream Reservation\n\t\t\tProtocol (SRP) Enhancements and Performance\n\t\t\tImprovements', 'Published as part of IEEE Std 802.1Q 2017.\n            Cross references corrected and updated. ', 'Published as part of IEEE Std 802.1Q 2014 Cor-1.\n            ETS code point added to the textual convention\n            IEEE8021FqtssTxSelectionAlgorithmIDValue ', 'Published as part of IEEE Std 802.1Q 2014 revision.\n            Cross references updated and corrected.', 'Minor edits to contact information etc. as part of\n          2011 revision of IEEE Std 802.1Q.', 'Initial revision, included in IEEE 802.1Qav.',))
if mibBuilder.loadTexts: ieee8021FqtssMib.setLastUpdated('201810040000Z')
if mibBuilder.loadTexts: ieee8021FqtssMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021FqtssMib.setContactInfo('  WG-URL: http://ieee802.org/1/\n         WG-EMail: STDS-802-1-L@IEEE.ORG\n\n          Contact: IEEE 802.1 Working Group Chair\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   Piscataway\n                   NJ 08854\n                   USA\n           E-mail: STDS-802-1-L@IEEE.ORG')
if mibBuilder.loadTexts: ieee8021FqtssMib.setDescription('The Bridge MIB module for managing devices that support\n        the Forwarding and Queuing Enhancements\n        for Time Sensitive Streams.\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1Q.\n\n        Copyright (C) IEEE (2018).\n        This version of this MIB module is part of IEEE Std 802.1Q;\n        see the draft itself for full legal notices.')
class IEEE8021FqtssTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.20.1'
    description = 'An 802.1 FQTSS traffic class value.\n        This is the numerical value associated with a traffic\n        class in a Bridge. Larger values are associated with\n        higher priority traffic classes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021FqtssDeltaBandwidthValue(TextualConvention, Unsigned32):
    reference = '12.20.1, 34.4'
    description = 'An 802.1 FQTSS delta bandwidth percentage,\n        represented as a fixed point number scaled by\n        1,000,000.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class IEEE8021FqtssTxSelectionAlgorithmIDValue(TextualConvention, Unsigned32):
    reference = '8.6.8, 12.20.2'
    description = 'An 802.1 transmission selection algorithm identifier\n         value. This is an integer, with the following\n         interpretation placed on the value:\n\n         0: Strict priority algorithm,\n         1: Credit-based shaper algorithm,\n         2: Enhanced Transmission Selection algorithm,\n         3-255: Reserved for future standardization,\n         256-4294967295: Vendor-specific transmission selection\n                         algorithm identifiers, consisting of a\n                         four-octet integer, where the most\n                         significant 3 octets hold an OUI or CID value,\n                         and the least significant octet holds\n                         an integer value in the range 0-255\n                         assigned by the owner of the OUI or CID.'
    status = 'current'
    displayHint = 'd'

ieee8021FqtssNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 0))
ieee8021FqtssObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1))
ieee8021FqtssConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2))
ieee8021FqtssBap = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 1))
ieee8021FqtssMappings = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 2))
ieee8021FqtssBapX = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 3))
ieee8021FqtssBapTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setReference('12.20.1')
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setDescription('A table containing a set of bandwidth availability\n        parameters for each traffic class that supports the\n        credit-based shaper algorithm.\n        All writable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021FqtssBapEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssBapEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapEntry.setDescription('A list of objects containing bandwidth allocation\n        information for each traffic class that supports the\n        credit-based shaper algorithm. Rows in the table are\n        automatically created and deleted as a result of the\n        operation of the algorithm described in 34.5. ')
ieee8021FqtssBAPTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setReference('12.20.2, 34.3, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setDescription('The traffic class number associated with the row of\n        the table.\n\n        A row in this table is created for each traffic class\n        that supports the credit-based shaper algorithm. The\n        recommended mappings of priorities to traffic classes\n        for support of the credit-based shaper algorithm are\n        described in 34.5.')
ieee8021FqtssDeltaBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 2), IEEE8021FqtssDeltaBandwidthValue()).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setDescription('The value of the deltaBandwidth parameter\n        for the traffic class.\n        This value is represented as a fixed point number\n        scaled by a factor of 1,000,000; i.e., 100,000,000\n        (the maximum value) represents 100%.\n\n        The default value of the deltaBandwidth parameter\n        for the highest numbered traffic class that supports\n        the credit-based shaper algorithm is 75%; for all\n        lower numbered traffic classes that support the\n        credit-based shaper algorithm the default value is 0%.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssOperIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 3), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setDescription('The most significant 32 bits of the bandwidth,\n        in bits per second, that is currently allocated to the\n        traffic class (idleSlope(N)). This object MUST be read\n        at the same time as ieee8021FqtssOperIdleSlopeLs,\n        which represents the LS 32 bits of the value, in order\n        for the read operation to succeed.\n\n        If SRP is supported and in operation, then the reserved\n        bandwidth is determined by the operation of SRP; otherwise,\n        the value of ieee8021FqtssOperIdleSlopeMs is equal to\n        the value of ieee8021FqtssAdminIdleSlopeMs.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssOperIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 4), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setDescription('The least significant 32 bits of the bandwidth,\n        in bits per second, that is currently allocated to the\n        traffic class (idleSlope(N)). This object MUST be read\n        at the same time as ieee8021FqtssOperIdleSlopeMs,\n        which represents the LS 32 bits of the value, in order\n        for the read operation to succeed.\n\n        If SRP is supported and in operation, then the reserved\n        bandwidth is determined by the operation of SRP; otherwise,\n        the value of ieee8021FqtssOperIdleSlopeLs is equal to\n        the value of ieee8021FqtssAdminIdleSlopeMs.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssAdminIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 5), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setDescription('The most significant 32 bits of the bandwidth,\n        in bits per second, that the manager desires to allocate\n        to the traffic class as  idleSlope(N). This object MUST be\n        read or written at the same time as\n        ieee8021FqtssAdminIdleSlopeLs,\n        which represents the LS 32 bits of the value, in order\n        for the read or write operation to succeed.\n\n        If SRP is supported and in operation, then the reserved\n        bandwidth is determined by the operation of SRP, and any\n        changes to the value of this object have no effect on the\n        operational value of idleSlope(N).\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssAdminIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 6), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setDescription('The least significant 32 bits of the bandwidth,\n        in bits per second, that the manager desires to allocate\n        to the traffic class as  idleSlope(N). This object MUST be\n        read or written at the same time as\n        ieee8021FqtssAdminIdleSlopeMs,\n        which represents the LS 32 bits of the value, in order\n        for the read or write operation to succeed.\n\n        If SRP is supported and in operation, then the reserved\n        bandwidth is determined by the operation of SRP, and any\n        changes to the value of this object have no effect on the\n        operational value of idleSlope(N).\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssBapRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBapRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapRowStatus.setDescription('Indicates the status of an entry (row) in this table, and is\n        used to create/delete entries.\n\n        The corresponding instances of the following objects\n        must be set before this object can be made active(1):\n           ieee8021FqtssBAPTrafficClass\n           ieee8021FqtssDeltaBandwidth\n           ieee8021FqtssOperIdleSlopeMs\n           ieee8021FqtssOperIdleSlopeLs\n           ieee8021FqtssAdminIdleSlopeMs\n           ieee8021FqtssAdminIdleSlopeLs\n\n        The corresponding instances of the following objects\n        may not be changed while this object is active(1):\n           ieee8021FqtssBAPTrafficClass')
ieee8021FqtssTxSelectionAlgorithmTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setDescription('A table containing the assignment of transmission\n        selection algorithms to traffic classes for the Port.\n        This table provides management of the Transmission\n        Selection Algorithm Table defined in 8.6.8.\n\n        For a given Port, a row in the table exists for each\n        traffic class that is supported by the Port.\n\n        The default assignments of transmission selection\n        algorithms to traffic classes in the table are made\n        on instantiation of the table, in accordance\n        with the defaults defined in 8.6.8 and 34.5.\n\n        All writable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021FqtssTxSelectionAlgorithmEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmEntry.setDescription('A list of objects that contain the mapping of a\n        traffic class value to a transmission selection algorithm\n        value.')
ieee8021FqtssTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setDescription('The traffic class to which the transmission selection\n         algorithm is assigned.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssTxSelectionAlgorithmID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 2), IEEE8021FqtssTxSelectionAlgorithmIDValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setDescription('The identifier of the transmission selection algorithm\n        assigned to the traffic class.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssSrpRegenOverrideTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2), )
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setDescription('A table containing the set of priority regeneration\n        table override values for the Port.\n\n        The recommended default values of priorities\n        associated with SR classes, and the corresponding\n        override values, are defined in 6.9.4.\n\n        All writable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021FqtssSrpRegenOverrideEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"))
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideEntry.setDescription('A list of objects that contain the mapping of a\n        priority value to a priority regeneration override\n        value, and a boundary port indication.\n        Rows in the table exist for all priorities that are\n        associated with SR classes.')
ieee8021FqtssSrClassPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 1), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setDescription('The priority value that is overridden at the\n        SRP domain boundary. ')
ieee8021FqtssPriorityRegenOverride = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 2), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setDescription('The priority value that is used to override the\n         priority regeneration table entry at the SRP\n         domain boundary.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssSrpBoundaryPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setDescription('The value of the SRPdomainBoundaryPort parameter\n        (35.1.4) for the priority. ')
ieee8021FqtssSRClassToPriorityTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3), )
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityTable.setReference('12.40.4, 35.2.2.9.2, 6.9.3')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityTable.setDescription('A table containing the mapping of the SR Class to\n            the associated priority.\n\n            The default values for the entries of this table are\n            specified in 34.5')
ieee8021FqtssSRClassToPriorityEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"))
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityEntry.setDescription('This attribute holds the Data Frame Priority\n            (35.2.2.8.5(a)) value that will be used for streams\n            that belong to the associated SR class.')
ieee8021FqtssSRClassToPrioritySrClassID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 1), IEEE8021FqtssTrafficClassValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPrioritySrClassID.setReference('12.20.4, 35.2.2.9.2 ')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPrioritySrClassID.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPrioritySrClassID.setDescription('The srClassId attribute provides the SR class ID\n                    from Table 35-7 of 35.2.2.9.2, so that management\n                    software can associate the traffic class to the\n                    corresponding SR class A or B used by protocols\n                    such as SRP.\n\n                    The default values for this attribute use the\n                    default values specified in 34.5 (i.e. Priority 3\n                    for SRclassID 6 and Priority 2 for SRclassID 5).\n\n                    If this managed object is not supported, the default\n                    values specified in 34.5 are used as the fixed\n                    configuration.')
ieee8021FqtssSRClassToPriorityRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityRowStatus.setDescription('Indicates the status of an entry (row) in this table, and is\n                    used to create/delete entries.')
ieee8021FqtssBapXTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1), )
if mibBuilder.loadTexts: ieee8021FqtssBapXTable.setReference('12.20.1')
if mibBuilder.loadTexts: ieee8021FqtssBapXTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapXTable.setDescription('A table containing a set of bandwidth availability\n        parameters for each traffic class configured for use with time-sensitive streams.\n        All writable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021FqtssBapXEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1), )
ieee8021FqtssBapEntry.registerAugmentions(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapXEntry"))
ieee8021FqtssBapXEntry.setIndexNames(*ieee8021FqtssBapEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021FqtssBapXEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapXEntry.setDescription('A list of objects containing bandwidth allocation\n        information for each traffic class configured for use with time-sensitive streams. Rows in the table are\n        automatically created and deleted as a result of the\n        operation of the algorithm described in 34.5.')
ieee8021FqtssBAPClassMeasurementInterval = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBAPClassMeasurementInterval.setReference('12.20.1, 34.3, 34.4, 34.6')
if mibBuilder.loadTexts: ieee8021FqtssBAPClassMeasurementInterval.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBAPClassMeasurementInterval.setDescription('The value of the ClassMeasurementInterval\n        parameter for the traffic class.\n        This attribute uses units of nanoseconds,\n        converted to/from units of seconds for use in\n        34.3.\n\n        If management of classMeasurementInterval is\n        not supported, the default values (34.5) are\n        used as the fixed Port configuration.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021FqtssBAPLockClassBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBAPLockClassBandwidth.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssBAPLockClassBandwidth.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBAPLockClassBandwidth.setDescription('This attribute determines the interpretation of\n        deltaBandwidth. For the value false(2), deltaBandwidth\n        is specified in 34.3.1. For true(1), deltaBandwidth is\n        specified in 34.3.2')
ieee8021FqtssCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 1))
ieee8021FqtssGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 2))
ieee8021FqtssBapGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssDeltaBandwidth"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBapGroup = ieee8021FqtssBapGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapGroup.setDescription('Objects that define bandwidth allocation for FQTSS.')
ieee8021FqtssTxSelectionAlgorithmGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 2)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssTxSelectionAlgorithmGroup = ieee8021FqtssTxSelectionAlgorithmGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmGroup.setDescription('Objects that define transmission selection\n        mappings for FQTSS.')
ieee8021FqtssBoundaryPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 3)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssPriorityRegenOverride"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSrpBoundaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBoundaryPortGroup = ieee8021FqtssBoundaryPortGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBoundaryPortGroup.setDescription('Objects that define boundary port priority override\n        mappings for FQTSS.')
ieee8021FqtssBapMeasurementGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 4)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPClassMeasurementInterval"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPLockClassBandwidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBapMeasurementGroup = ieee8021FqtssBapMeasurementGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapMeasurementGroup.setDescription('Objects that define the SRP TSpec measurement interval\n        and deltaBandwidth interpretation for FQTSS.')
ieee8021FqtssSRClassPriorityGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 5)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPrioritySrClassID"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPriorityRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssSRClassPriorityGroup = ieee8021FqtssSRClassPriorityGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSRClassPriorityGroup.setDescription('Objects that define mappings of the SR class ID to\n        the associated priority for FQTSS.')
ieee8021FqtssCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 16, 2, 1, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBoundaryPortGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapMeasurementGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssCompliance = ieee8021FqtssCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssCompliance.setDescription('The compliance statement for devices supporting\n        forwarding and queuing for time sensitive streams.\n\n        Support of the objects defined in the IEEE8021-FQTSS MIB\n        also requires support of the IEEE8021-BRIDGE-MIB; the\n        provisions of 17.3.2 apply to implementations claiming\n        support of the IEEE8021-FQTSS MIB. ')
mibBuilder.exportSymbols("IEEE8021-FQTSS-MIB", ieee8021FqtssTxSelectionAlgorithmEntry=ieee8021FqtssTxSelectionAlgorithmEntry, PYSNMP_MODULE_ID=ieee8021FqtssMib, ieee8021FqtssBAPLockClassBandwidth=ieee8021FqtssBAPLockClassBandwidth, ieee8021FqtssBAPTrafficClass=ieee8021FqtssBAPTrafficClass, ieee8021FqtssTxSelectionAlgorithmGroup=ieee8021FqtssTxSelectionAlgorithmGroup, ieee8021FqtssNotifications=ieee8021FqtssNotifications, ieee8021FqtssSRClassToPriorityTable=ieee8021FqtssSRClassToPriorityTable, ieee8021FqtssBapTable=ieee8021FqtssBapTable, ieee8021FqtssSRClassToPrioritySrClassID=ieee8021FqtssSRClassToPrioritySrClassID, ieee8021FqtssConformance=ieee8021FqtssConformance, ieee8021FqtssSRClassToPriorityRowStatus=ieee8021FqtssSRClassToPriorityRowStatus, ieee8021FqtssSRClassPriorityGroup=ieee8021FqtssSRClassPriorityGroup, IEEE8021FqtssTrafficClassValue=IEEE8021FqtssTrafficClassValue, ieee8021FqtssBapEntry=ieee8021FqtssBapEntry, ieee8021FqtssTxSelectionAlgorithmTable=ieee8021FqtssTxSelectionAlgorithmTable, ieee8021FqtssTxSelectionAlgorithmID=ieee8021FqtssTxSelectionAlgorithmID, ieee8021FqtssOperIdleSlopeLs=ieee8021FqtssOperIdleSlopeLs, ieee8021FqtssPriorityRegenOverride=ieee8021FqtssPriorityRegenOverride, ieee8021FqtssBapXTable=ieee8021FqtssBapXTable, IEEE8021FqtssTxSelectionAlgorithmIDValue=IEEE8021FqtssTxSelectionAlgorithmIDValue, ieee8021FqtssSrpRegenOverrideTable=ieee8021FqtssSrpRegenOverrideTable, ieee8021FqtssAdminIdleSlopeMs=ieee8021FqtssAdminIdleSlopeMs, ieee8021FqtssBapGroup=ieee8021FqtssBapGroup, ieee8021FqtssSRClassToPriorityEntry=ieee8021FqtssSRClassToPriorityEntry, IEEE8021FqtssDeltaBandwidthValue=IEEE8021FqtssDeltaBandwidthValue, ieee8021FqtssBapX=ieee8021FqtssBapX, ieee8021FqtssAdminIdleSlopeLs=ieee8021FqtssAdminIdleSlopeLs, ieee8021FqtssSrpBoundaryPort=ieee8021FqtssSrpBoundaryPort, ieee8021FqtssBoundaryPortGroup=ieee8021FqtssBoundaryPortGroup, ieee8021FqtssMib=ieee8021FqtssMib, ieee8021FqtssTrafficClass=ieee8021FqtssTrafficClass, ieee8021FqtssBapXEntry=ieee8021FqtssBapXEntry, ieee8021FqtssOperIdleSlopeMs=ieee8021FqtssOperIdleSlopeMs, ieee8021FqtssCompliance=ieee8021FqtssCompliance, ieee8021FqtssBapMeasurementGroup=ieee8021FqtssBapMeasurementGroup, ieee8021FqtssSrpRegenOverrideEntry=ieee8021FqtssSrpRegenOverrideEntry, ieee8021FqtssObjects=ieee8021FqtssObjects, ieee8021FqtssBAPClassMeasurementInterval=ieee8021FqtssBAPClassMeasurementInterval, ieee8021FqtssBapRowStatus=ieee8021FqtssBapRowStatus, ieee8021FqtssCompliances=ieee8021FqtssCompliances, ieee8021FqtssMappings=ieee8021FqtssMappings, ieee8021FqtssGroups=ieee8021FqtssGroups, ieee8021FqtssBap=ieee8021FqtssBap, ieee8021FqtssSrClassPriority=ieee8021FqtssSrClassPriority, ieee8021FqtssDeltaBandwidth=ieee8021FqtssDeltaBandwidth)
