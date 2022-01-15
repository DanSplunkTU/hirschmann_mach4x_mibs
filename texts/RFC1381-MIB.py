#
# PySNMP MIB module RFC1381-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC1381-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
PositiveInteger, = mibBuilder.importSymbols("RFC1253-MIB", "PositiveInteger")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
transmission, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, IpAddress, Gauge32, Bits, NotificationType, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lapb = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16))
class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

lapbAdmnTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 1), )
if mibBuilder.loadTexts: lapbAdmnTable.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnTable.setDescription('This table contains objects that can be\n                          changed to manage a LAPB interface.\n                          Changing one of these parameters may take\n                          effect in the operating LAPB immediately or\n                          may wait until the interface is restarted\n                          depending on the details of the\n                          implementation.\n\n                          Most of the objects in this read-write table\n                          have corresponding read-only objects in the\n                          lapbOperTable that return the current\n                          operating value.\n\n                          The operating values may be different from\n                          these configured values if changed by XID\n                          negotiation or if a configured parameter was\n                          changed after the interface was started.')
lapbAdmnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 1, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbAdmnIndex"))
if mibBuilder.loadTexts: lapbAdmnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnEntry.setDescription('Configured parameter values for a specific\n                          LAPB.')
lapbAdmnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbAdmnIndex.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnIndex.setDescription('The ifIndex value for the LAPB interface.')
lapbAdmnStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dxe", 3))).clone('dte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnStationType.setReference('ISO 7776 section 3.1')
if mibBuilder.loadTexts: lapbAdmnStationType.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnStationType.setDescription('Identifies the desired station type of this\n                          interface.')
lapbAdmnControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2))).clone('modulo8')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnControlField.setReference('ISO 8885 Table 3, Name: HDLC Option - 10')
if mibBuilder.loadTexts: lapbAdmnControlField.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnControlField.setDescription('The desired size of the sequence numbers\n                          used to number frames.')
lapbAdmnTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 4), PositiveInteger().clone(36000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnTransmitN1FrameSize.setReference('ISO 8885 Table 3,\n                          Name: Information Field length')
if mibBuilder.loadTexts: lapbAdmnTransmitN1FrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnTransmitN1FrameSize.setDescription('The default maximum N1 frame size desired\n                          in number of bits for a frame transmitted by\n                          this DTE.  This excludes flags and 0 bits\n                          inserted for transparency.')
lapbAdmnReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 5), PositiveInteger().clone(36000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnReceiveN1FrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnReceiveN1FrameSize.setDescription('The default maximum N1 frame size desired\n                          in number of bits for a frame the DCE/remote\n                          DTE transmits to this DTE.  This excludes\n                          flags and 0 bits inserted for transparency.')
lapbAdmnTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnTransmitKWindowSize.setReference('ISO 8885 Table 3, Name: Window size')
if mibBuilder.loadTexts: lapbAdmnTransmitKWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnTransmitKWindowSize.setDescription('The default transmit window size for this\n                          Interface.  This is the maximum number of\n                          unacknowledged sequenced PDUs that may be\n                          outstanding from this DTE at any one time.')
lapbAdmnReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnReceiveKWindowSize.setReference('ISO 8885 Table 3, Name: Window size')
if mibBuilder.loadTexts: lapbAdmnReceiveKWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnReceiveKWindowSize.setDescription('The default receive window size for this\n                          Interface.  This is the maximum number of\n\n\n                          unacknowledged sequenced PDUs that may be\n                          outstanding from the DCE/remote DTE at any\n                          one time.')
lapbAdmnN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnN2RxmitCount.setReference('ISO 8885 Table 3,\n                          Name: Retransmission Attempts')
if mibBuilder.loadTexts: lapbAdmnN2RxmitCount.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnN2RxmitCount.setDescription('The default N2 retry counter for this\n                          interface.  This specifies the number of\n                          times a PDU will be resent after the T1\n                          timer expires without an acknowledgement for\n                          the PDU.')
lapbAdmnT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 9), PositiveInteger().clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT1AckTimer.setReference('ISO 8885 Table 3, Name:\n                          Acknowledgement timer')
if mibBuilder.loadTexts: lapbAdmnT1AckTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnT1AckTimer.setDescription('The default T1 timer for this interface.\n                          This specifies the maximum time in\n                          Milliseconds to wait for acknowledgment of a\n                          PDU.')
lapbAdmnT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 10), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT2AckDelayTimer.setReference('ISO 8885 Table 3,\n\n\n                          Name: Reply delay timer')
if mibBuilder.loadTexts: lapbAdmnT2AckDelayTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnT2AckDelayTimer.setDescription('The default T2 timer for this interface.\n                          This specifies the maximum time in\n                          Milliseconds to wait before sending an\n                          acknowledgment for a sequenced PDU.  A value\n                          of zero means there will be no delay in\n                          acknowledgement generation.')
lapbAdmnT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 11), PositiveInteger().clone(60000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT3DisconnectTimer.setReference('ISO 7776 section 5.7.1.3')
if mibBuilder.loadTexts: lapbAdmnT3DisconnectTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnT3DisconnectTimer.setDescription('The T3 timer for this interface.  This\n                          specifies the time in Milliseconds to wait\n                          before considering the link disconnected.  A\n                          value of zero indicates the link will be\n                          considered disconnected upon completion of\n                          the frame exchange to disconnect the link.')
lapbAdmnT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 12), PositiveInteger().clone(2147483647)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT4IdleTimer.setReference('ISO 7776 section 5.7.1.4')
if mibBuilder.loadTexts: lapbAdmnT4IdleTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnT4IdleTimer.setDescription('The T4 timer for this interface.  This\n                          specifies the maximum time in Milliseconds\n                          to allow without frames being exchanged on\n                          the data link.  A value of 2147483647\n                          indicates no idle timer is being kept.')
lapbAdmnActionInitiate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sendSABM", 1), ("sendDISC", 2), ("sendDM", 3), ("none", 4), ("other", 5))).clone('sendSABM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnActionInitiate.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnActionInitiate.setDescription('This identifies the action LAPB will take\n                          to initiate link set-up.')
lapbAdmnActionRecvDM = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sendSABM", 1), ("sendDISC", 2), ("other", 3))).clone('sendSABM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnActionRecvDM.setStatus('mandatory')
if mibBuilder.loadTexts: lapbAdmnActionRecvDM.setDescription('This identifies the action LAPB will take\n                          when it receives a DM response.')
lapbOperTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 2), )
if mibBuilder.loadTexts: lapbOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperTable.setDescription('This table contains configuration\n                          information about interface parameters\n                          currently set in the interface.  Many of\n                          these objects have corresponding objects in\n                  the lapbAdmnTable.')
lapbOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 2, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbOperIndex"))
if mibBuilder.loadTexts: lapbOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperEntry.setDescription('Currently set parameter values for a\n                          specific LAPB.')
lapbOperIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperIndex.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperIndex.setDescription('The ifIndex value for the LAPB interface.')
lapbOperStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dxe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperStationType.setReference('ISO 7776 section 3.1')
if mibBuilder.loadTexts: lapbOperStationType.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperStationType.setDescription('Identifies the current operating station\n                          type of this interface.  A value of dxe (3)\n                          indicates XID negotiation has not yet taken\n                          place.')
lapbOperControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperControlField.setReference('ISO 7776 section 3.3')
if mibBuilder.loadTexts: lapbOperControlField.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperControlField.setDescription('The current operating size of the sequence\n                          numbers used to number frames.')
lapbOperTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitN1FrameSize.setReference('ISO 7776 section 5.7.3')
if mibBuilder.loadTexts: lapbOperTransmitN1FrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperTransmitN1FrameSize.setDescription('The current operating N1 frame size used\n                          for the maximum number of bits in a frame\n                          this DTE can transmit.  This excludes flags\n                          and 0 bits inserted for transparency.')
lapbOperReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveN1FrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperReceiveN1FrameSize.setDescription('The current operating N1 frame size used\n                          for the maximum number of bits in a frame\n                          the DCE/remote DTE can transmit.  This\n                          excludes flags and 0 bits inserted for\n                          transparency.')
lapbOperTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitKWindowSize.setReference('ISO 7776 section 5.7.4')
if mibBuilder.loadTexts: lapbOperTransmitKWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperTransmitKWindowSize.setDescription('The current PDU window size this Interface\n                          uses to transmit.  This is the maximum\n\n\n                          number of unacknowledged sequenced PDUs that\n                          may be outstanding from this DTE at any one\n                          time.')
lapbOperReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveKWindowSize.setReference('ISO 7776 section 5.7.4')
if mibBuilder.loadTexts: lapbOperReceiveKWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperReceiveKWindowSize.setDescription('The current receive PDU window size for\n                          this Interface.  This is the maximum number\n                          of unacknowledged sequenced PDUs that may be\n                          outstanding from the DCE/remote DTE at any\n                          one time.')
lapbOperN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperN2RxmitCount.setReference('ISO 7776 section 5.7.2')
if mibBuilder.loadTexts: lapbOperN2RxmitCount.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperN2RxmitCount.setDescription('The current N2 retry counter used for this\n                          interface.  This specifies the number of\n                          times a PDU will be resent after the T1\n                          timer expires without an acknowledgement for\n                          the PDU.')
lapbOperT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 9), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT1AckTimer.setReference('ISO 7776 section 5.7.1.1')
if mibBuilder.loadTexts: lapbOperT1AckTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperT1AckTimer.setDescription('The current T1 timer for this interface.\n                          This specifies the maximum time in\n                          Milliseconds to wait for acknowledgment of a\n                          PDU.')
lapbOperT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 10), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT2AckDelayTimer.setReference('ISO 7776 section 5.7.1.2')
if mibBuilder.loadTexts: lapbOperT2AckDelayTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperT2AckDelayTimer.setDescription('The current T2 timer for this interface.\n                          This specifies the maximum time in\n                          Milliseconds to wait before sending an\n                          acknowledgment for a sequenced PDU.  A value\n                          of zero means there will be no delay in\n                          acknowledgement generation.')
lapbOperT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 11), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT3DisconnectTimer.setReference('ISO 7776 section 5.7.1.3')
if mibBuilder.loadTexts: lapbOperT3DisconnectTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperT3DisconnectTimer.setDescription('The current T3 timer for this interface.\n                          This specifies the time in Milliseconds to\n                          wait before considering the link\n                          disconnected.  A value of zero indicates the\n                          link will be considered disconnected upon\n                          completion of the frame exchange to\n                          disconnect the link.')
lapbOperT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 12), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbOperT4IdleTimer.setReference('ISO 7776 section 5.7.1.4')
if mibBuilder.loadTexts: lapbOperT4IdleTimer.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperT4IdleTimer.setDescription('The current T4 timer for this interface.\n                          This specifies the maximum time in\n                          Milliseconds to allow without frames being\n                          exchanged on the data link.  A value of\n                          2147483647 indicates no idle timer is being\n                          kept.')
lapbOperPortId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 13), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperPortId.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperPortId.setDescription('This object identifies an instance of the\n                          index object in the first group of objects\n                          in the MIB specific to the physical device\n                          or interface used to send and receive\n\n\n                          frames.  If an agent does not support any\n                          such objects, it should return nullSpec\n                          OBJECT IDENTIFIER {0 0}.')
lapbOperProtocolVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 14), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperProtocolVersionId.setStatus('mandatory')
if mibBuilder.loadTexts: lapbOperProtocolVersionId.setDescription('This object identifies the version of the\n                          lapb protocol implemented by this\n                          interface.')
lapbFlowTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 3), )
if mibBuilder.loadTexts: lapbFlowTable.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowTable.setDescription('This table defines the objects recorded by\n                          LAPB to provide information about the\n                          traffic flow through the interface.')
lapbFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 3, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbFlowIfIndex"))
if mibBuilder.loadTexts: lapbFlowEntry.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowEntry.setDescription('The information regarding the effects of\n                          flow controls in LAPB.')
lapbFlowIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowIfIndex.setDescription('The ifIndex value for the LAPB Interface.')
lapbFlowStateChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowStateChanges.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowStateChanges.setDescription('The number of LAPB State Changes, including\n                          resets.')
lapbFlowChangeReason = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("notStarted", 1), ("abmEntered", 2), ("abmeEntered", 3), ("abmReset", 4), ("abmeReset", 5), ("dmReceived", 6), ("dmSent", 7), ("discReceived", 8), ("discSent", 9), ("frmrReceived", 10), ("frmrSent", 11), ("n2Timeout", 12), ("other", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowChangeReason.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowChangeReason.setDescription('The reason for the most recent incrementing\n                          of lapbFlowStateChanges.  A DM or DISC frame\n                          generated to initiate link set-up does not\n                          alter this object.  When the MIB-II object\n                          ifOperStatus does not have a value of\n                          testing, there exists a correlation between\n                          this object and ifOperStatus.  IfOperStatus\n                          will have a value of up when this object\n                          contains:  abmEntered, abmeEntered,\n                          abmReset, or abmeReset.  IfOperStatus will\n                          have a value of down when this object has a\n                          value of notStarted, or dmReceived through\n                          n2Timeout.  There is no correlation when\n                          this object has the value other.')
lapbFlowCurrentMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("disconnected", 1), ("linkSetup", 2), ("frameReject", 3), ("disconnectRequest", 4), ("informationTransfer", 5), ("rejFrameSent", 6), ("waitingAcknowledgement", 7), ("stationBusy", 8), ("remoteStationBusy", 9), ("bothStationsBusy", 10), ("waitingAckStationBusy", 11), ("waitingAckRemoteBusy", 12), ("waitingAckBothBusy", 13), ("rejFrameSentRemoteBusy", 14), ("xidFrameSent", 15), ("error", 16), ("other", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowCurrentMode.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowCurrentMode.setDescription('The current condition of the conversation.')
lapbFlowBusyDefers = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowBusyDefers.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowBusyDefers.setDescription('The number of times this device was unable\n                          to transmit a frame due to a perceived\n                          remote busy condition.  Busy conditions can\n\n\n                          result from the receipt of an RNR from the\n                          remote device, the lack of valid sequence\n                          number space (window saturation), or other\n                          conditions.')
lapbFlowRejOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejOutPkts.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowRejOutPkts.setDescription('The number of REJ or SREJ frames sent by\n                          this station.')
lapbFlowRejInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejInPkts.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowRejInPkts.setDescription('The number of REJ or SREJ frames received\n                          by this station.')
lapbFlowT1Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowT1Timeouts.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowT1Timeouts.setDescription('The number of times a re-transmission was\n                          effected by the T1 Timer expiring.')
lapbFlowFrmrSent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrSent.setReference('ISO 7776 Section 4.3.9, tables 7 and 8')
if mibBuilder.loadTexts: lapbFlowFrmrSent.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowFrmrSent.setDescription("The Information Field of the FRMR most\n                          recently sent.  If no FRMR has been sent\n                          (the normal case) or the information isn't\n                          available, this will be an OCTET STRING of\n                          zero length.")
lapbFlowFrmrReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrReceived.setReference('ISO 7776 Section 4.3.9, tables 7 and 8')
if mibBuilder.loadTexts: lapbFlowFrmrReceived.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowFrmrReceived.setDescription("The Information Field of the FRMR most\n                          recently received.  If no FRMR has been\n                          received (the normal case) or the\n                          information isn't available, this will be an\n                          OCTET STRING of zero length.")
lapbFlowXidReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8206))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowXidReceived.setReference('ISO 8885')
if mibBuilder.loadTexts: lapbFlowXidReceived.setStatus('mandatory')
if mibBuilder.loadTexts: lapbFlowXidReceived.setDescription('The Information Field of the XID frame most\n                          recently received.  If no XID frame has been\n                          received, this will be an OCTET STRING of\n                          zero length.')
lapbXidTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 4), )
if mibBuilder.loadTexts: lapbXidTable.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidTable.setDescription("This table defines values to use for XID\n                          negotiation that are not found in the\n                          lapbAdmnTable.  This table is optional for\n                          implementations that don't support XID and\n                          mandatory for implementations that do\n                          initiate XID negotiation.")
lapbXidEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 4, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbXidIndex"))
if mibBuilder.loadTexts: lapbXidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidEntry.setDescription('XId negotiation parameter values for a\n                          specific LAPB.')
lapbXidIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbXidIndex.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidIndex.setDescription('The ifIndex value for the LAPB interface.')
lapbXidAdRIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidAdRIdentifier.setReference('ISO 8885 Table 2, Name: Identifier')
if mibBuilder.loadTexts: lapbXidAdRIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidAdRIdentifier.setDescription('The value of the Address Resolution\n                          Identifier.  A zero length string indicates\n                          no Identifier value has been assigned.')
lapbXidAdRAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidAdRAddress.setReference('ISO 8885 Table 2, Name: Address')
if mibBuilder.loadTexts: lapbXidAdRAddress.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidAdRAddress.setDescription('The value of the Address Resolution\n                          Address.  A zero length string indicates no\n                          Address value has been assigned.')
lapbXidParameterUniqueIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidParameterUniqueIdentifier.setReference('ISO 8885 Table 3, Name: Identifier')
if mibBuilder.loadTexts: lapbXidParameterUniqueIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidParameterUniqueIdentifier.setDescription('The value of the parameter unique\n                          Identifier.  A zero length string indicates\n                          no Unique identifier value has been\n                          assigned.')
lapbXidGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidGroupAddress.setReference('ISO 8885 Table 3, Name: Group address')
if mibBuilder.loadTexts: lapbXidGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidGroupAddress.setDescription('The value of the parameter Group address.\n                          A zero length string indicates no Group\n                          address value has been assigned.')
lapbXidPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidPortNumber.setReference('ISO 8885 Table 3, Name: Port number')
if mibBuilder.loadTexts: lapbXidPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidPortNumber.setDescription('The port number assigned for this link.  A\n                          zero length string indicates no local port\n                          number identifier has been assigned.')
lapbXidUserDataSubfield = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8206)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidUserDataSubfield.setReference('ISO 8885 section 4.3')
if mibBuilder.loadTexts: lapbXidUserDataSubfield.setStatus('mandatory')
if mibBuilder.loadTexts: lapbXidUserDataSubfield.setDescription('A user data subfield, if any, to be\n                          transmitted in an XID frame.  A zero length\n                          frame indicates no user data subfield has\n                          been assigned.  The octet string should\n                          include both the User data identifier and\n                          User data field as shown in Figures 1 and\n                          4.')
lapbProtocolVersion = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5))
lapbProtocolIso7776v1986 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 1))
lapbProtocolCcittV1980 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 2))
lapbProtocolCcittV1984 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 3))
mibBuilder.exportSymbols("RFC1381-MIB", lapbXidIndex=lapbXidIndex, lapbOperReceiveN1FrameSize=lapbOperReceiveN1FrameSize, lapbFlowChangeReason=lapbFlowChangeReason, lapbFlowFrmrSent=lapbFlowFrmrSent, lapbXidAdRIdentifier=lapbXidAdRIdentifier, lapbProtocolCcittV1984=lapbProtocolCcittV1984, lapbOperIndex=lapbOperIndex, lapbFlowFrmrReceived=lapbFlowFrmrReceived, lapbAdmnTransmitN1FrameSize=lapbAdmnTransmitN1FrameSize, lapbOperEntry=lapbOperEntry, lapbXidGroupAddress=lapbXidGroupAddress, lapbXidPortNumber=lapbXidPortNumber, lapbOperN2RxmitCount=lapbOperN2RxmitCount, lapbFlowCurrentMode=lapbFlowCurrentMode, lapbOperProtocolVersionId=lapbOperProtocolVersionId, lapbOperT2AckDelayTimer=lapbOperT2AckDelayTimer, lapbAdmnReceiveKWindowSize=lapbAdmnReceiveKWindowSize, lapbAdmnReceiveN1FrameSize=lapbAdmnReceiveN1FrameSize, lapbOperPortId=lapbOperPortId, lapbXidTable=lapbXidTable, lapbAdmnTransmitKWindowSize=lapbAdmnTransmitKWindowSize, lapbOperTransmitN1FrameSize=lapbOperTransmitN1FrameSize, lapbOperTable=lapbOperTable, lapbFlowRejInPkts=lapbFlowRejInPkts, lapbAdmnT2AckDelayTimer=lapbAdmnT2AckDelayTimer, lapbFlowEntry=lapbFlowEntry, lapbFlowBusyDefers=lapbFlowBusyDefers, lapbFlowXidReceived=lapbFlowXidReceived, IfIndexType=IfIndexType, lapbAdmnStationType=lapbAdmnStationType, lapbAdmnEntry=lapbAdmnEntry, lapbOperT1AckTimer=lapbOperT1AckTimer, lapbXidEntry=lapbXidEntry, lapbAdmnN2RxmitCount=lapbAdmnN2RxmitCount, lapbProtocolIso7776v1986=lapbProtocolIso7776v1986, lapbOperStationType=lapbOperStationType, lapbProtocolVersion=lapbProtocolVersion, lapbAdmnT1AckTimer=lapbAdmnT1AckTimer, lapbAdmnT4IdleTimer=lapbAdmnT4IdleTimer, lapbOperReceiveKWindowSize=lapbOperReceiveKWindowSize, lapbAdmnActionRecvDM=lapbAdmnActionRecvDM, lapbOperT3DisconnectTimer=lapbOperT3DisconnectTimer, lapbXidAdRAddress=lapbXidAdRAddress, lapbOperControlField=lapbOperControlField, lapbFlowStateChanges=lapbFlowStateChanges, lapbAdmnT3DisconnectTimer=lapbAdmnT3DisconnectTimer, lapbAdmnActionInitiate=lapbAdmnActionInitiate, lapbAdmnControlField=lapbAdmnControlField, lapb=lapb, lapbOperT4IdleTimer=lapbOperT4IdleTimer, lapbFlowIfIndex=lapbFlowIfIndex, lapbProtocolCcittV1980=lapbProtocolCcittV1980, lapbFlowRejOutPkts=lapbFlowRejOutPkts, lapbOperTransmitKWindowSize=lapbOperTransmitKWindowSize, lapbXidUserDataSubfield=lapbXidUserDataSubfield, lapbXidParameterUniqueIdentifier=lapbXidParameterUniqueIdentifier, lapbFlowT1Timeouts=lapbFlowT1Timeouts, lapbFlowTable=lapbFlowTable, lapbAdmnTable=lapbAdmnTable, lapbAdmnIndex=lapbAdmnIndex)
