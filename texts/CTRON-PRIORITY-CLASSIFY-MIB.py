#
# PySNMP MIB module CTRON-PRIORITY-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:22 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Integer32, Bits, Gauge32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Integer32", "Bits", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ModuleIdentity", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ctPriClassify = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6))
if mibBuilder.loadTexts: ctPriClassify.setLastUpdated('200203121855Z')
if mibBuilder.loadTexts: ctPriClassify.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ctPriClassify.setContactInfo('       Cabletron Systems, Inc.\n        Postal: 35 Industrial Way, P.O. Box 5005\n                Rochester, NH 03867-0505\n         Phone: (603) 332-9400\n         Email: support@cabletron.com\n           Web: http://www.cabletron.com')
if mibBuilder.loadTexts: ctPriClassify.setDescription('The Cabletron Priority Classify MIB module for controlling\n        Cabletron specific priority classification criteria based\n        on packet content.')
ctPriClassifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1))
class CtPriClassifyType(TextualConvention, Integer32):
    description = 'Each enumerated value represents a unique classification\n        type.  Different types have different rules regarding\n        how data is interpreted during classification.  These\n        rules are spelled out in the comments preceding each type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("etherType", 1), ("llcDsapSsap", 2), ("ipTypeOfService", 3), ("ipProtocolType", 4), ("ipxClassOfService", 5), ("ipxPacketType", 6), ("ipAddressSource", 7), ("ipAddressDestination", 8), ("ipAddressBilateral", 9), ("ipxNetworkSource", 10), ("ipxNetworkDestination", 11), ("ipxNetworkBilateral", 12), ("ipUdpPortSource", 13), ("ipUdpPortDestination", 14), ("ipUdpPortBilateral", 15), ("ipTcpPortSource", 16), ("ipTcpPortDestination", 17), ("ipTcpPortBilateral", 18), ("ipxSocketSource", 19), ("ipxSocketDestination", 20), ("ipxSocketBilateral", 21), ("macAddressSource", 22), ("macAddressDestination", 23), ("macAddressBilateral", 24), ("ipFragments", 25))

class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight\n        ports, with the first octet specifying ports 1 through\n        8, the second octet specifying ports 9 through 16, etc.\n        Within each octet, the most significant bit represents\n        the lowest numbered port, and the least significant bit\n        represents the highest numbered port.  Thus, each port\n        of the bridge is represented by a single bit within the\n        value of this object.  If that bit has a value of '1'\n        then that port is included in the set of ports; the port\n        is not included if its bit has a value of '0'."
    status = 'current'

ctPriClassifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyStatus.setDescription('Allows the Priority Classification feature to be globally\n        enabled/disabled.  A value of disable(2), functionally\n        supersedes the RowStatus of individual entries in the\n        ctPriClassifyTable, but does not change their actual\n        RowStatus value.')
ctPriClassifyMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setDescription('The maximum number of entries allowed in the\n        ctPriClassifyTable.')
ctPriClassifyNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setDescription('The current number of entries in the ctPriClassifyTable.')
ctPriClassifyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4), )
if mibBuilder.loadTexts: ctPriClassifyTable.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTable.setDescription('A table containing configuration information for each\n        Priority classification configured into the device by (local\n        or network) management.  All entries are permanent and\n        will be restored after the device is reset.')
ctPriClassifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPriority"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMeaning"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataVal"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMask"))
if mibBuilder.loadTexts: ctPriClassifyEntry.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyEntry.setDescription('Describes a particular entry of ctPriClassifyTable.')
ctPriClassifyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ctPriClassifyPriority.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyPriority.setDescription('The priority for this entry.  Any packet meeting the\n        classification criteria specified by this conceptual row\n        will be given the priority indicated by this object.')
ctPriClassifyDataMeaning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 2), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setDescription('The meaning of the ctPriClassifyDataVal leaf for this\n        conceptual row.  The ctPriClassifyDataVal specifies a\n        particular value which, when compared to packet data,\n        is used to classify that packet to a particular priority.\n        The part of the packet (if any), to which this data\n        comparison applies, is determined by this object.\n\n        For example, the value ipAddressBilateral(8) means that\n        the value ctPriClassifyDataVal for this entry is an IP\n        address.  It further means that the given IP address\n        will be compared against both source and destination\n        IP address fields in a packet.  Such an entry obviously\n        would not not match against any non-IP packets.\n\n        Additionally, the value of this leaf will impose certain\n        implicit ranges and interpretations of data contained\n        within the ctPriClassifyDataVal leaf for this entry.  The\n        specific limitations of each type should be spelled out\n        in the comments for that type.')
ctPriClassifyDataVal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataVal.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataVal.setDescription('The data value associated with ctPriClassifyDataMeaning.\n        The explicit range of this value is any unsigned 32-bit\n        integer(0..4294967295).  This range may vary, however, \n        depending upon the value of ctPriClassifyDataMeaning.\n        Illegal values should not be allowed.')
ctPriClassifyDataMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataMask.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataMask.setDescription("This object is the one's complement of a 32-bit mask.\n        This mask is applicable to the data comparison of\n        ctPriClassifyDataVal.  The mask is applied to the actual\n        packet data under consideration through a logical bitwise\n        AND operation.  This result is then compared to the data.\n\n        For example, we want to classify according to a bilateral\n        IP address of 134.141.0.0 with a mask of 255.255.240.0.\n        This would be reflected by the following values:\n\n        ctPriClassifyDataMeaning: ipAddressBilateral(8)\n        ctPriClassifyDataVal:     0x868d0000\n        ctPriClassifyDataMask:    0x00000fff\n\n        Again there are contextual implications for this leaf\n        depending upon the value of ctPriClassifyDataMeaning.\n        Not all types will use the mask, and others will impose\n        restrictions.  This value should however be a true\n        indication of the masking operation.  In other words,\n        data types that don't use a mask should only allow a\n        value of zero, indicating that all data bits are\n        significant in the comparison.\n\n        The specific restrictions of each type should be spelled\n        out in the comments for that type.  Illegal values should\n        not be allowed.")
ctPriClassifyIngressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 5), PortList().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyIngressList.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyIngressList.setDescription('The set of ports on which this classification rule applies.\n        Classification occurs on ingress.  An agent implementation\n        should allow a set operation of this object to create a\n        row if it does not exist.')
ctPriClassifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setDescription("This object provides both control and status for the\n        associated conceptual row in the table.  Rows can be\n        created in two ways.\n\n        createAndGo - The specified row will be created and\n            activated if the instance is allowable.  If not, an\n            inconsistentValue exception will be returned and the\n            row will not be created.  This provides the most\n            optimal method of creating an active row, but provides\n            the user no explanation if the row cannot be created.\n\n        createAndWait - The specified row will be created and put\n            in the notInService state if the instance is allowable.\n            A subsequent activation of this row will bring it into\n            the active state.  If the instance is not allowable,\n            the row will be created and put in the notReady state.\n            A subsequent activation of this row will fail.  Since\n            the inappropriate information is always contained in the\n            indexing leaves, activation will never succeed and the\n            row should be removed by the management station.  When\n            a row is in the notReady state, the ctPriClassifyRowInfo\n            may be retrieved to obtain a plain English explanation\n            of why this row cannot be activated.  createAndWait is\n            the preferred method for this reason.\n        \n        Both methods described above leave ctPriClassifyIngressList\n        in it's default state, requiring an additional set operation\n        in order to modify it.  An even more optimal twist on the\n        createAndWait method is to set the ctPriClassifyIngressList\n        to it's desired value as a method for row creation.  This\n        will essentially cause an implicit createAndWait since it\n        too will leave the row in either the notInService or\n        notReady state.  This leaves only activation or error\n        analysis as the last step.\n\n        Any rows left in the notReady or notInService state for\n        more than 5 minutes should be automatically removed by\n        the agent implementation.")
ctPriClassifyRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setDescription("This object provides info about this row in the form of\n        an ASCII string, suitable for display purposes.  The\n        intended purpose of this object is to provide an\n        'agent-specific' explanation as to why the\n        ctPriClassifyRowStatus for this conceptual row is in\n        the 'notReady' state.  A management station should read\n        this object and display it to the user in this case.\n\n        A conceptual row that does not fall into this category may\n        simply return a single NULL, but may also provide any useful\n        info of its choice.  A management station may attempt to\n        display such info if it so chooses, but is under no burden\n        to do so.")
ctPriClassifyTOSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setDescription('This object indicates whether an IP Type Of Service (TOS)\n        value, defined by ctPriClassifyTOSValue, should be written\n        into the TOS field of the IP header for any packet matching\n        the classification specified by this conceptual row. This\n        object may be set to enable only for the conceptual rows\n        whose ctPriClassifyDataMeaning and ctPriClassifyDataVal have\n        the following values:\n\n        ctPriClassifyDataMeaning     ctPriClassifyDataVal\n        ------------------------     --------------------\n        etherType(1)                 0x0800 (IP)\n        llcDsapSsap(2)               0x0606 (IP)\n        ipTypeOfService(3)           any\n        ipProtocolType(4)            any\n        ipAddressSource(7)           any\n        ipAddressDestination(8)      any\n        ipAddressBilateral(9)        any\n        ipUdpPortSource(13)          any\n        ipUdpPortDestination(14)     any\n        ipUdpPortBilateral(15)       any\n        ipTdpPortSource(16)          any\n        ipTdpPortDestination(17)     any\n        ipTdpPortBilateral(18)       any\n        ipFrag(25)                   not applicable\n\n        A conceptual row that does not fall into these categories may\n        be set to disable(2) and will return disable(2).')
ctPriClassifyTOSValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setDescription('The value to be written into the IP TOS field of the IP header\n        of any packet that matches the classification specified by the\n        conceptual row.')
ctPriClassifyAbilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5), )
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setDescription('A table containing information for each of the priority\n        classification types.  Types for which there is no\n        corresponding row are not supported by this device.')
ctPriClassifyAbilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyAbility"))
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setDescription('Describes a particular entry of ctPriClassifyAbilityTable.')
ctPriClassifyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 1), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyAbility.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbility.setDescription('The priority classification type associated with this entry.')
ctPriClassifyPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyPorts.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyPorts.setDescription('The set of ports on which the classification type\n        specified by ctPriClassifyAbility is supported.')
ctPriClassifyTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setDescription('Indicates the sysUpTime at which the last\n         change was made to the ctPriClassifyTable.')
ctPriClassifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2))
ctPriClassifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1))
ctPriClassifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2))
ctPriClassifyBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyMaxEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyNumEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyIngressList"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowInfo"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSValue"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPorts"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTableLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyBaseGroup = ctPriClassifyBaseGroup.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyBaseGroup.setDescription('A collection of objects providing device level control\n        and status information for Priority classification.')
ctPriClassifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyCompliance = ctPriClassifyCompliance.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyCompliance.setDescription('The compliance statement for devices that support\n        Priority classification.')
mibBuilder.exportSymbols("CTRON-PRIORITY-CLASSIFY-MIB", ctPriClassifyRowInfo=ctPriClassifyRowInfo, ctPriClassifyMaxEntries=ctPriClassifyMaxEntries, ctPriClassifyDataMeaning=ctPriClassifyDataMeaning, ctPriClassifyTable=ctPriClassifyTable, PYSNMP_MODULE_ID=ctPriClassify, ctPriClassifyAbility=ctPriClassifyAbility, ctPriClassifyCompliances=ctPriClassifyCompliances, ctPriClassifyCompliance=ctPriClassifyCompliance, ctPriClassifyTOSValue=ctPriClassifyTOSValue, ctPriClassifyAbilityEntry=ctPriClassifyAbilityEntry, ctPriClassifyEntry=ctPriClassifyEntry, ctPriClassifyIngressList=ctPriClassifyIngressList, ctPriClassifyObjects=ctPriClassifyObjects, CtPriClassifyType=CtPriClassifyType, ctPriClassifyNumEntries=ctPriClassifyNumEntries, ctPriClassifyPorts=ctPriClassifyPorts, ctPriClassifyConformance=ctPriClassifyConformance, ctPriClassify=ctPriClassify, ctPriClassifyRowStatus=ctPriClassifyRowStatus, ctPriClassifyStatus=ctPriClassifyStatus, ctPriClassifyBaseGroup=ctPriClassifyBaseGroup, ctPriClassifyTableLastChange=ctPriClassifyTableLastChange, ctPriClassifyTOSStatus=ctPriClassifyTOSStatus, ctPriClassifyGroups=ctPriClassifyGroups, ctPriClassifyDataVal=ctPriClassifyDataVal, ctPriClassifyPriority=ctPriClassifyPriority, ctPriClassifyAbilityTable=ctPriClassifyAbilityTable, ctPriClassifyDataMask=ctPriClassifyDataMask, PortList=PortList)
