#
# PySNMP MIB module CT-PRIORITY-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:06 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctPriorityExtClassifyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5))
pClassifyRTP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1))
pClassifyUDP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2))
pClassifyRTPLowDelayQueuePreference = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTPLowDelayQueuePreference.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPLowDelayQueuePreference.setDescription('This value represents one of eight preference levels, \n                        0 through 7, with 0 being the worst and 7 the best. \n                        The value will be translated by the device into a three \n                        bit binary number. This value shall be used to put \n                        incoming RTP packets on an internal queue.')
pClassifyRTCPParsing = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTCPParsing.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTCPParsing.setDescription("This object will enable or disable parsing of all \n                        forwarded packets looking for RTCP packets. \n                        Enabled(2) means that all fowarded packets will be \n                        parsed for RTCP.  When an RTCP packet is found, the \n                        identification of the associated RTP 'connection' \n                        (next lower port number) is added to the list of low \n                        delay ports. Disabled(1) means that no packets will be\n                        parsed. ")
pClassifyRTPTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3), )
if mibBuilder.loadTexts: pClassifyRTPTable.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPTable.setDescription('A list describing which MIB-II interfaces\n                        will allow 802.1 P/Q tagging or modification of the \n                        precedence field in the TOS portion of an IP packet or \n                        both.  It also specifies the tagging value and the TOS \n                        precedence where applicable. ')
pClassifyRTPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1), ).setIndexNames((0, "CT-PRIORITY-CLASSIFY-MIB", "pClassifyRTPInterfaceNumber"))
if mibBuilder.loadTexts: pClassifyRTPEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPEntry.setDescription('This entry for pClassifyRTPEntry.')
pClassifyRTPInterfaceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pClassifyRTPInterfaceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPInterfaceNumber.setDescription('The index of the MIB-II interface that the \n                        packet is destined for.')
pClassifyRTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noModification", 1), ("onlyQTag", 2), ("onlyQTOS", 3), ("qTagAndQTOS", 4))).clone('noModification')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTPState.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPState.setDescription('This object will enable  or disable                                                                    modification of the TOS precedence field and the 802.1 \n                        P/Q tagging. A value of NoModification(1) implies that \n                        modification is not allowed. OnlyQTag(2) means that only\n                        802.1 P/Q tagging is allowed. When this object has a \n                        value OnlyQTOS(3), modification of only the TOS \n                        precedence field is permitted.  QTagAndQTOS means that \n                        both TOS precedence modification and P/Q tagging is \n                        allowed.')
pClassifyRTPTOSPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTPTOSPrecedence.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPTOSPrecedence.setDescription('This value represents one of eight precedence levels, \n                        0 through 7, with 0 being the lowest and 7 the highest.\n                        The value will be translated by the device into a three \n                        bit binary number for use as the precedence field in the\n                        TOS portion of the IP Datagram.  This object is valid \n                        only if pClassifyRTPState is OnlyQTOS or QTagAndQTOS.')
pClassifyRTPTagPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTPTagPriority.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPTagPriority.setDescription('This value represents one of eight priority levels, \n                        0 through 7, with 0 being the lowest and 7 the highest. \n                        The value will be translated by the device into a three \n                        bit binary number for use as the user_priority field of \n                        the TCI (Tag Control Information) format.  This object \n                        is only valid if pClassifyRTPState is OnlyQTag or \n                        QTagAndQTOS.')
pClassifyRTPTagVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyRTPTagVID.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyRTPTagVID.setDescription('This value represents a twelve bit VLAN identifier \n                        (VID) as specified in the IEEE 802.1Q standard. This \n                        object will provide a twelve bit VID in the TCI (Tag \n                        Control Information) portion of a tagged frame as \n                        specified in the IEEE 802.1Q. This value will be used \n                        to classify qualified packets in accordance with the \n                        IEEE 802.1Q standard.  This object will also be used to\n                        reclassify certain packets exiting the port specified\n                        in pClassifyRTPInterfaceNumber whose TCI field contains \n                        a VID equal to the NULL VLAN ID.  This object is valid \n                        only if pClassifyRTPState is OnlyQTag or QTagAndQTOS.')
pClassifyUDPTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1), )
if mibBuilder.loadTexts: pClassifyUDPTable.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyUDPTable.setDescription(' A list of UDP destination port numbers, UDP packets\n                        whose port numbers appear in this table will be put on \n                        a low delay queue, and the preference specified.')
pClassifyUDPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1), ).setIndexNames((0, "CT-PRIORITY-CLASSIFY-MIB", "pClassifyUDPPortNumber"))
if mibBuilder.loadTexts: pClassifyUDPEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyUDPEntry.setDescription('A list of objects that describe the UDP port numbers                                           that qualify as candidates for low delay queue \n                        preference classification.')
pClassifyUDPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyUDPPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyUDPPortNumber.setDescription('The UDP destination port number tha qualifies as a \n                        candidate for low delay classification.')
pClassifyUDPState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("remove", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyUDPState.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyUDPState.setDescription('A packet with UDP port number equal to \n                        pClassifyUDPPortNumber will be put on a low_delay queue\n                         if state is Enabled(2).')
pClassifyUDPLowDelayQueuePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pClassifyUDPLowDelayQueuePreference.setStatus('mandatory')
if mibBuilder.loadTexts: pClassifyUDPLowDelayQueuePreference.setDescription('Preference with which packet with UDP destination port\n                        number equal to pClassifyUDPPortNumberis put on the \n                        queue.  ')
mibBuilder.exportSymbols("CT-PRIORITY-CLASSIFY-MIB", ctPriorityExtClassifyConfig=ctPriorityExtClassifyConfig, pClassifyRTPTagPriority=pClassifyRTPTagPriority, pClassifyRTPTagVID=pClassifyRTPTagVID, pClassifyUDPEntry=pClassifyUDPEntry, pClassifyUDPLowDelayQueuePreference=pClassifyUDPLowDelayQueuePreference, pClassifyUDP=pClassifyUDP, pClassifyRTPEntry=pClassifyRTPEntry, pClassifyRTPInterfaceNumber=pClassifyRTPInterfaceNumber, pClassifyUDPTable=pClassifyUDPTable, pClassifyUDPState=pClassifyUDPState, pClassifyUDPPortNumber=pClassifyUDPPortNumber, pClassifyRTPTOSPrecedence=pClassifyRTPTOSPrecedence, pClassifyRTP=pClassifyRTP, pClassifyRTPTable=pClassifyRTPTable, pClassifyRTPState=pClassifyRTPState, pClassifyRTPLowDelayQueuePreference=pClassifyRTPLowDelayQueuePreference, pClassifyRTCPParsing=pClassifyRTCPParsing)
