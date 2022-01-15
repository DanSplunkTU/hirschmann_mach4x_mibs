#
# PySNMP MIB module SIAE-MAB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-MAB-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:19:22 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Gauge32, Counter32, Counter64, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, iso, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
mabMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 93))
mabMib.setRevisions(('2015-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mabMib.setRevisionsDescriptions(('Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: mabMib.setLastUpdated('201502170000Z')
if mibBuilder.loadTexts: mabMib.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: mabMib.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail:  help@siaemic.com\n            ')
if mibBuilder.loadTexts: mabMib.setDescription('Microwave Adaptive Bandwidth (MAB)\n\n             This management information module supports the configuration of  \n             the MW Capacity Management (MCM) feature developed by\n             SIAE MICROELETTRONICA and Cisco that offers reliable QoS and\n             optimized performances even under worst radio propagation\n             conditions. \n\n             The extension to the original functionality, consisting of the\n             Link ID TLV, is considered by this MIB.\n            ')
class MabBwCalculationMethod(TextualConvention, Integer32):
    description = 'This Textual Convention describes the method of calculation of the \n             radio bandwitdh (or the throughput of an interface):\n              - average:  Average Tx BW value across the observation interval\n              - min:      Minimum Tx BW value across the observation interval\n              - max:      Maximum Tx BW value across the observation interval\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("average", 1), ("min", 2), ("max", 3))

class MabPduCompliance(TextualConvention, Integer32):
    reference = '[1] - MW CAPACITY MANAGEMENT (MCM) - FUNCTIONAL DESCRIPTION\n                   This document provides a description of the MW Capacity\n                   Management (MCM) feature developed by SIAE MICROELETTRONICA\n                   and Cisco.\n             [2] - E-OAM Extensions for Microwave Adaptive Modulation\n                   Cisco Document Number EDCS-997459\n             [3] - Draft revised Recommendation ITU-T G.8021/Y.1341\n                   (for Consent, 5 December 2014)\n             [4] - Draft Amendment 1 to Recommendation ITU-T G.8013/Y.1731(2013)\n                   (for Consent, 5 December 2014) \n            '
    description = 'This Textual Convention describes the compliance of the MAB PDU \n             sent by a MAB PDU sender:\n              - stdMcmCompliant:   PDU format is compliant with [1]\n              - extMcmCompliant:   PDU format is compliant with [2]\n              - ituG8013Compliant: PDU format is compliant with [4]\n\n             Since [3] and [4] are a draft edition at the time when this MIB\n             is being written, the value ituG8013Compliant(3) is defined for\n             future use.\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stdMcmCompliant", 1), ("extMcmCompliant", 2), ("ituG8013Compliant", 3))

class MabSenderOption(TextualConvention, Bits):
    reference = '[3] - Draft revised Recommendation ITU-T G.8021/Y.1341\n                   (for Consent, 5 December 2014)\n            '
    description = 'This Textual Convention describes the supported option of a \n             MAB PDU sender:\n              - enableAlways:     Enable periodic PDU sending even if the\n                                  current bandwidth is equal to the nominal\n                                  bandwidth.\n              - enableSignalFail: PDU are transmitted periodically when the\n                                  link fails in the tranmit direction. If the\n                                  NE usually sends PDUs also when the radio \n                                  bandwitdh (or the throughput of an interface)\n                                  is null, this option has no effect.\n            '
    status = 'current'
    namedValues = NamedValues(("enableAlways", 0), ("enableSignalFail", 1))

mabMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabMibVersion.setStatus('current')
if mibBuilder.loadTexts: mabMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.\n            ')
mabSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2), )
if mibBuilder.loadTexts: mabSensorTable.setStatus('current')
if mibBuilder.loadTexts: mabSensorTable.setDescription("Table with MAB sensors entries. Each sensor is associated to a\n             interface, usually an interface with the physical layer\n             consisting of a radio link, and comapares the current bandwidth\n             (throughput) with the nominal one. When nominal and current\n             bandwidth doesn't match to PDU senders associated with a sensor\n             is required to send a MAB PDU every observation time.\n            ")
mabSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabSensorIndex"))
if mibBuilder.loadTexts: mabSensorEntry.setStatus('current')
if mibBuilder.loadTexts: mabSensorEntry.setDescription('A row in the mabSensorTable.\n            ')
mabSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mabSensorIndex.setStatus('current')
if mibBuilder.loadTexts: mabSensorIndex.setDescription('This object identifies the MAB sensor inside the Network Element.\n            ')
mabSensorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorRowStatus.setStatus('current')
if mibBuilder.loadTexts: mabSensorRowStatus.setDescription('The status of this MAB sensor entry.\n\n             An entry may not exist in the active state unless all\n             objects in the entry have an appropriate value: mabSensorIfIndex\n             must be set to a valid ifIndex number. Otherwise, the error\n             inconsistentValue is returned on the attempt to set active this \n             row.\n\n             When set to notInService changes may be made to mabSensorIfIndex.\n             Other objects can be changed when mabSensorRowStatus is set to\n             active.\n\n             A sensor can not be deleted if there is any MAB PDU sender\n             associated with it.\n            ')
mabSensorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mabSensorAdminStatus.setDescription('Administative status of the MAB sensor.\n             The value down(1) turn off all MAB advisers associated with\n             this sensor.\n            ')
mabSensorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorIfIndex.setStatus('current')
if mibBuilder.loadTexts: mabSensorIfIndex.setDescription('This object accepts a greater than zero value to identify an\n             interface in ifTable. The throughput of the selected interface\n             is monitored and notified to all MAB PDU sender associated with\n             this sensor.\n            ')
mabSensorLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorLinkId.setStatus('current')
if mibBuilder.loadTexts: mabSensorLinkId.setDescription('This object set the (radio) link identifier that will be inserted \n             in the Link ID TLV of the MAB PDU.\n            ')
mabSensorBwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 6), MabBwCalculationMethod().clone('average')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorBwMode.setStatus('current')
if mibBuilder.loadTexts: mabSensorBwMode.setDescription('This object defines the method of calculation of the current \n             bandwidth. The value of this parameter is sent inside MAB PDUs.\n            ')
mabSensorHoldoffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorHoldoffTime.setStatus('current')
if mibBuilder.loadTexts: mabSensorHoldoffTime.setDescription('This object defines the wait time (in seconds) for MAB protocol\n             before sending packets if the current bandwidth (throughput)\n             is lower than the nominal.\n            ')
mabSensorObservationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(10, 10), ValueRangeConstraint(60, 60), )).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorObservationTime.setStatus('current')
if mibBuilder.loadTexts: mabSensorObservationTime.setDescription('This object defines the observation time (in seconds) for MAB\n             protocol during which calculate the minimum, maximum and average\n             value of the current bandwidth (throughput). At the end of each\n             period, a MAB PDU is sent by every MAB PDU sender associated with\n             this sensor.\n            ')
mabSensorFastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 59)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorFastTime.setReference('Draft revised Recommendation ITU-T G.8021/Y.1341 (for Consent,\n             5 December 2014) - 8.1.18 BNM insert process\n            ')
if mibBuilder.loadTexts: mabSensorFastTime.setStatus('current')
if mibBuilder.loadTexts: mabSensorFastTime.setDescription('This value is used in place of mabSensorObservationTime for the\n             first mabSensorFastCount PDU packets sent by a MAB PDU sender.\n             The value of mabSensorFastTime must be less than or equal to\n             mabSensorObservationTime.\n            ')
mabSensorFastCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorFastCount.setReference('Draft revised Recommendation ITU-T G.8021/Y.1341 (for Consent,\n             5 December 2014) - 8.1.18 BNM insert process\n            ')
if mibBuilder.loadTexts: mabSensorFastCount.setStatus('current')
if mibBuilder.loadTexts: mabSensorFastCount.setDescription('This value specifies how many MAB PDU packets are sent every\n             mabSensorFastTime before to use the standard observation time\n             (mabSensorObservationTime).\n             Zero means which quick sending of packets is disabled.\n            ')
mabSensorStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3), )
if mibBuilder.loadTexts: mabSensorStatusTable.setStatus('current')
if mibBuilder.loadTexts: mabSensorStatusTable.setDescription('Table with the status of MAB sensor entries. For each row in\n             mabSensorTable a row is created in this table.\n            ')
mabSensorStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabSensorIndex"))
if mibBuilder.loadTexts: mabSensorStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mabSensorStatusEntry.setDescription('A row in the mabSensorTable.\n            ')
mabSensorNominalBw = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabSensorNominalBw.setStatus('current')
if mibBuilder.loadTexts: mabSensorNominalBw.setDescription('This object reports the nominal bandwidth (throughput) of the \n             interface selected by mabSensorIfIndex.\n            ')
mabSensorCurrentBw = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabSensorCurrentBw.setStatus('current')
if mibBuilder.loadTexts: mabSensorCurrentBw.setDescription('This object reports the current bandwidth (throughput) of the \n             interface selected by mabSensorIfIndex and calculated according \n             to the method set in mabSensorBwMode.\n            ')
mabPduSenderTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4), )
if mibBuilder.loadTexts: mabPduSenderTable.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderTable.setDescription('Table with MAB PDU sender entries. Each PDU sender refers to an\n             ifIndex in ifTable on which to send a PDU MAB and a sensor that\n             triggers the sending.\n            ')
mabPduSenderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabPduSenderIndex"))
if mibBuilder.loadTexts: mabPduSenderEntry.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderEntry.setDescription('A row in the mabPduSenderTable.\n            ')
mabPduSenderIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: mabPduSenderIndex.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderIndex.setDescription('This object identifies the MAB PDU sender inside the Network \n             Element.\n            ')
mabPduSenderRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderRowStatus.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderRowStatus.setDescription('The status of this mabPduSender entry.\n\n             An entry may not exist in the active state unless all objects in\n             the entry have an appropriate value: mabPduSenderIfIndex must be\n             set to a valid ifIndex number and mabPduSenderSensorIndex must be\n             set to a valid MAB sensor, Otherwise, the error inconsistentValue\n             is returned on the attempt to set active this row.\n\n             When set to notInService changes may be made to mabPduSenderIfIndex,\n             mabPduSenderSensorIndex. Other objects can be changed when\n             mabPduSenderRowStatus is set to active.\n            ')
mabPduSenderAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderAdminStatus.setDescription('Administative status of the MAB PDU sender.\n            ')
mabPduSenderIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderIfIndex.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderIfIndex.setDescription('This object accepts a greater than zero value to identify an\n             interface in ifTable. MAB PDU is sent over this interface.\n            ')
mabPduSenderSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderSensorIndex.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderSensorIndex.setDescription('This object associates a MAB sensor to this PDU sender.\n            ')
mabPduSenderVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderVlanId.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderVlanId.setDescription('This object defines the VLAN identifier used to tag the MAB PDU.\n             Zero means the PDU is not tagged.\n            ')
mabPduSenderPcp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderPcp.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderPcp.setDescription('This object defines packet priority written into the tag of\n             the MAB PDU.\n            ')
mabPduSenderOamMaintLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderOamMaintLevel.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderOamMaintLevel.setDescription('This object defines the OAM maintenance level of the MAB PDU.\n             The multicast destination address of the PDU is according to \n             the selected maintenance level:\n                01-80-C2-00-00-3x\n             where x = Maintenance Level\n            ')
mabPduSenderDAType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multicastDA", 1), ("unicastDA", 2))).clone('multicastDA')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderDAType.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderDAType.setDescription('This object defines the destination MAC address type of the PDU:\n              - multicastDA(1): Multicast Class 1 Destination Address (DA)\n              - unicastDA(2):   Unicast Destination Address (DA)\n            ')
mabPduSenderUnicastDA = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 10), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderUnicastDA.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderUnicastDA.setDescription('This object defines the unuicast destination address of the PDU\n             when mabPduSenderDAType is set to unicastDA(2).\n            ')
mabPduSenderOption = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 11), MabSenderOption()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderOption.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderOption.setDescription('This object enable the option supported by the MAB PDU sender:\n              - enableAlways:     Enable periodic PDU sending even if the\n                                  current bandwidth is equal to the nominal\n                                  bandwidth.\n              - enableSignalFail: PDU are transmitted periodically when the\n                                  link fails in the tranmit direction. If the\n                                  NE usually sends PDUs also when the radio \n                                  bandwitdh (or the throughput of an interface)\n                                  is null, this option has no effect.\n            ')
mabPduSenderPduCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 12), MabPduCompliance().clone('stdMcmCompliant')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderPduCompliance.setStatus('current')
if mibBuilder.loadTexts: mabPduSenderPduCompliance.setDescription('This object defines the compliance of the MAB PDU format.\n            ')
mibBuilder.exportSymbols("SIAE-MAB-MIB", mabSensorAdminStatus=mabSensorAdminStatus, mabSensorHoldoffTime=mabSensorHoldoffTime, mabPduSenderAdminStatus=mabPduSenderAdminStatus, mabPduSenderSensorIndex=mabPduSenderSensorIndex, mabSensorFastTime=mabSensorFastTime, mabMibVersion=mabMibVersion, MabSenderOption=MabSenderOption, mabPduSenderVlanId=mabPduSenderVlanId, mabSensorBwMode=mabSensorBwMode, mabPduSenderUnicastDA=mabPduSenderUnicastDA, mabPduSenderIndex=mabPduSenderIndex, mabMib=mabMib, mabSensorTable=mabSensorTable, mabSensorLinkId=mabSensorLinkId, mabPduSenderDAType=mabPduSenderDAType, mabSensorIndex=mabSensorIndex, MabPduCompliance=MabPduCompliance, mabSensorObservationTime=mabSensorObservationTime, mabPduSenderTable=mabPduSenderTable, mabSensorStatusEntry=mabSensorStatusEntry, mabPduSenderRowStatus=mabPduSenderRowStatus, mabPduSenderOption=mabPduSenderOption, PYSNMP_MODULE_ID=mabMib, mabSensorFastCount=mabSensorFastCount, mabPduSenderOamMaintLevel=mabPduSenderOamMaintLevel, mabSensorRowStatus=mabSensorRowStatus, mabPduSenderPcp=mabPduSenderPcp, mabSensorCurrentBw=mabSensorCurrentBw, mabSensorNominalBw=mabSensorNominalBw, mabSensorIfIndex=mabSensorIfIndex, mabPduSenderPduCompliance=mabPduSenderPduCompliance, mabSensorEntry=mabSensorEntry, MabBwCalculationMethod=MabBwCalculationMethod, mabSensorStatusTable=mabSensorStatusTable, mabPduSenderIfIndex=mabPduSenderIfIndex, mabPduSenderEntry=mabPduSenderEntry)
