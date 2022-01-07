#
# PySNMP MIB module RFC1284-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC1284-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:16 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Unsigned32, transmission, iso, Counter32, TimeTicks, Bits, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Unsigned32", "transmission", "iso", "Counter32", "TimeTicks", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dot3 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7))
dot3Table = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 1), )
if mibBuilder.loadTexts: dot3Table.setStatus('mandatory')
if mibBuilder.loadTexts: dot3Table.setDescription('Status information and control variables for a\n                collection of ethernet-like interfaces attached to\n                a particular system.')
dot3Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 1, 1), ).setIndexNames((0, "RFC1284-MIB", "dot3Index"))
if mibBuilder.loadTexts: dot3Entry.setStatus('mandatory')
if mibBuilder.loadTexts: dot3Entry.setDescription('Status information and control variables for a\n                particular interface to an ethernet-like medium.')
dot3Index = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3Index.setStatus('mandatory')
if mibBuilder.loadTexts: dot3Index.setDescription('An index value that uniquely identifies an\n                interface to an ethernet-like medium.  The\n                interface identified by a particular value of this\n                index is the same interface as identified by the\n                same value of ifIndex.')
dot3InitializeMac = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("initialized", 1), ("uninitialized", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3InitializeMac.setStatus('mandatory')
if mibBuilder.loadTexts: dot3InitializeMac.setDescription('The initialization status of the MAC and PLS\n                (Physical Layer Signalling) subsystems for a\n                particular interface. The value initialized(1)\n                signifies that the subsystems for a particular\n                interface have been previously initialized; the\n                value uninitialized(2) signifies that they have\n                not been previously initialized.\n\n                Each alteration of an instance of this object to\n                either of the values initialized(1) or\n                uninitialized(2) is analogous to an invocation of\n                the initializeMAC action defined in [9] and has\n                the effect of (re-)initializing the MAC and PLS\n                subsystems for the associated interface. In\n                particular,\n                     all management counters pertaining to the MAC\n                     and PLS subsystems for said interface are\n                     reset to zero;\n\n                     the receive and transmit layer management\n                     state variables (receiveEnabled and\n                     transmitEnabled in [9]) are set to enable\n                     reception and transmission of frames;\n\n                     the promiscuous receive function is disabled;\n                     and\n\n                     multicast reception is disabled.')
dot3MacSubLayerStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3MacSubLayerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot3MacSubLayerStatus.setDescription("The operational status of the MAC sublayer for a\n                particular interface.  The value enabled(1)\n                signifies that the MAC sublayer for said interface\n                is operational for both transmitting and receiving\n                frames -- that is, that the value of both the\n                receive and transmit layer management state\n                variables (receiveEnabled and transmitEnabled in\n                [9]) for said interface are true.  The value\n                disabled(2) signifies that the MAC sublayer for\n                said interface is not operational for either\n                transmitting or receiving frames. In particular,\n                the value of an instance of this object is\n                disabled(2) whenever the value of the\n                corresponding instance of the dot3Enabled object\n                is false(2).\n\n                Each alteration of an instance of this object to\n                the value enabled(1) is analogous to an invocation\n                of the enableMACSublayer action defined in [9] and\n                has the effect of starting normal transmit and\n                receive operations (from the ``idle'' state) on\n                the associated interface. In particular, such an\n                alteration has the effect of resetting the PLS for\n                said interface and of setting the receive and\n                transmit layer management state variables\n                (receiveEnabled and transmitEnabled in [9]) to be\n                true.\n                Each alteration of an instance of this object to\n                the value disabled(2) is analogous to an\n                invocation of the disableMACSublayer action\n                defined in [9] and has the effect of terminating\n                transmit and receive operations on the associated\n                interface. In particular, such an alteration has\n                the effect of setting the receive and transmit\n                layer management state variables (receiveEnabled\n                and transmitEnabled in [9]) to be false. Any\n                transmissions/receptions in progress are completed\n                before operation is terminated.")
dot3MulticastReceiveStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3MulticastReceiveStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot3MulticastReceiveStatus.setDescription('The multicast receive status for a particular\n                interface.  The value enabled(1) signifies that\n                reception of multicast frames by the MAC sublayer\n                is enabled on said interface. The value\n                disabled(2) signifies that reception of multicast\n                frames by the MAC sublayer is not enabled on said\n                interface.\n\n                Each alteration of an instance of this object to\n                the value enabled(1) is analogous to an invocation\n                of the enableMulticastReceive action defined in\n                [9] and has the effect of enabling multicast frame\n                reception on the associated interface. Actual\n                reception of multicast frames is only possible on\n                an interface when the values for the associated\n                instances of the dot3MulticastReceiveStatus and\n                dot3MacSubLayerStatus objects are enabled(1) and\n                enabled(1), respectively.\n\n                Each alteration of an instance of this object to\n                the value disabled(2) is analogous to an\n                invocation of the disableMulticastReceive action\n                defined in [9] and has the effect of inhibiting\n                multicast frame reception on the associated\n                interface.')
dot3TxEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3TxEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: dot3TxEnabled.setDescription('The transmit layer management state variable\n                (transmitEnabled as defined in [9]) for a\n                particular interface.  The value true(1) signifies\n                that the MAC frame transmission is enabled on said\n                interface. The value false(2) signifies that the\n                MAC frame transmission is inhibited on said\n                interface. In particular, the value of an instance\n                of this object is false(2) whenever the value of\n                the corresponding instance of the\n                dot3MacSubLayerStatus object is disabled(2).\n\n                Each alteration of an instance of this object to\n                the value true(1) is analogous to an invocation of\n                the enableTransmit action defined in [9] and has\n                the effect of enabling MAC sublayer frame\n                transmission on the associated interface. In\n                particular, such an alteration has the effect of\n                setting the transmit layer management state\n                variable (transmitEnabled in [9]) for said\n                interface to be true.\n\n                Each alteration of an instance of this object to\n                the value false(2) is analogous to an invocation\n                of the disableTransmit action defined in [9] and\n                has the effect of inhibiting MAC sublayer frame\n                transmission on the associated interface. In\n                particular, such an alteration has the effect of\n                setting the transmit layer management state\n                variable (transmitEnabled in [9]) for said\n                interface to be false. Any transmissions in\n                progress are completed before transmission is\n                inhibited.')
dot3TestTdrValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3TestTdrValue.setStatus('mandatory')
if mibBuilder.loadTexts: dot3TestTdrValue.setDescription('The number of 10 MHz ticks which elapsed between\n               the beginning of a TDR measurement and the\n               collision which ended it, for the most recently\n               executed TDR test.  If no TDR test has been\n               executed, or the last TDR value is not available,\n              this object has the value 0.')
dot3StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 2), )
if mibBuilder.loadTexts: dot3StatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsTable.setDescription('Statistics for a collection of ethernet-like\n                interfaces attached to a particular system.')
dot3StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 2, 1), ).setIndexNames((0, "RFC1284-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: dot3StatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsEntry.setDescription('Statistics for a particular interface to an\n                ethernet-like medium.')
dot3StatsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsIndex.setDescription('An index value that uniquely identifies an\n                interface to an ethernet-like medium.  The\n                interface identified by a particular value of this\n                index is the same interface as identified by the\n                same value of ifIndex.')
dot3StatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsAlignmentErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsAlignmentErrors.setDescription('A count of frames received on a particular\n                interface that are not an integral number of\n                octets in length and do not pass the FCS check.\n                The count represented by an instance of this\n                object is incremented when the alignmentError\n                status is returned by the MAC service to the LLC\n                (or other MAC user). Received frames for which\n                multiple error conditions obtain are, according to\n                the conventions of [9], counted exclusively\n                according to the error status presented to the\n                LLC.')
dot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsFCSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsFCSErrors.setDescription('A count of frames received on a particular\n                interface that are an integral number of octets in\n                length but do not pass the FCS check.\n\n                The count represented by an instance of this\n                object is incremented when the frameCheckError\n                status is returned by the MAC service to the LLC\n                (or other MAC user). Received frames for which\n                multiple error conditions obtain are, according to\n                the conventions of [9], counted exclusively\n                according to the error status presented to the\n                LLC.')
dot3StatsSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsSingleCollisionFrames.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsSingleCollisionFrames.setDescription('A count of successfully transmitted frames on a\n                particular interface for which transmission is\n                inhibited by exactly one collision.\n\n                A frame that is counted by an instance of this\n                object is also counted by the corresponding\n                instance of either the ifOutUcastPkts or\n                ifOutNUcastPkts object and is not counted by the\n                corresponding instance of the\n                dot3StatsMultipleCollisionFrames object.')
dot3StatsMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsMultipleCollisionFrames.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsMultipleCollisionFrames.setDescription('A count of successfully transmitted frames on a\n                particular interface for which transmission is\n                inhibited by more than one collision.\n\n                A frame that is counted by an instance of this\n                object is also counted by the corresponding\n                instance of either the ifOutUcastPkts or\n                ifOutNUcastPkts object and is not counted by the\n                corresponding instance of the\n                dot3StatsSingleCollisionFrames object.')
dot3StatsSQETestErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsSQETestErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsSQETestErrors.setDescription('A count of times that the SQE TEST ERROR message\n                is generated by the PLS sublayer for a particular\n                interface. The SQE TEST ERROR message is defined\n                in section 7.2.2.2.4 of [12] and its generation is\n                described in section 7.2.4.6 of the same\n                document.')
dot3StatsDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsDeferredTransmissions.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsDeferredTransmissions.setDescription('A count of frames for which the first\n                transmission attempt on a particular interface is\n                delayed because the medium is busy.\n\n                The count represented by an instance of this\n                object does not include frames involved in\n                collisions.')
dot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsLateCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsLateCollisions.setDescription('The number of times that a collision is detected\n                on a particular interface later than 512 bit-times\n                into the transmission of a packet.\n\n                Five hundred and twelve bit-times corresponds to\n                51.2 microseconds on a 10 Mbit/s system. A (late)\n                collision included in a count represented by an\n                instance of this object is also considered as a\n                (generic) collision for purposes of other\n                collision-related statistics.')
dot3StatsExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsExcessiveCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsExcessiveCollisions.setDescription('A count of frames for which transmission on a\n                particular interface fails due to excessive\n                collisions.')
dot3StatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsInternalMacTransmitErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsInternalMacTransmitErrors.setDescription('A count of frames for which transmission on a\n                particular interface fails due to an internal MAC\n                sublayer transmit error. A frame is only counted\n                by an instance of this object if it is not counted\n                by the corresponding instance of either the\n                dot3StatsLateCollisions object, the\n                dot3StatsExcessiveCollisions object, the\n                dot3StatsCarrierSenseErrors object, or the\n                dot3StatsExcessiveDeferrals object.\n\n                The precise meaning of the count represented by an\n                instance of this object is implementation-\n                specific.  In particular, an instance of this\n                object may represent a count of transmission\n                errors on a particular interface that are not\n                otherwise counted.')
dot3StatsCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsCarrierSenseErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsCarrierSenseErrors.setDescription('The number of times that the carrier sense\n                condition was lost or never asserted when\n                attempting to transmit a frame on a particular\n                interface.\n\n                The count represented by an instance of this\n                object is incremented at most once per\n                transmission attempt, even if the carrier sense\n                condition fluctuates during a transmission\n                attempt.')
dot3StatsExcessiveDeferrals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsExcessiveDeferrals.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsExcessiveDeferrals.setDescription('A count of frames for which transmission on a\n                particular interface is deferred for an excessive\n                period of time.')
dot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsFrameTooLongs.setDescription('A count of frames received on a particular\n                interface that exceed the maximum permitted frame\n                size.\n\n                The count represented by an instance of this\n                object is incremented when the frameTooLong status\n                is returned by the MAC service to the LLC (or\n                other MAC user). Received frames for which\n                multiple error conditions obtain are, according to\n                the conventions of [9], counted exclusively\n                according to the error status presented to the\n                LLC.')
dot3StatsInRangeLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsInRangeLengthErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsInRangeLengthErrors.setDescription('A count of frames received on a particular\n                interface with a length field value that falls\n                between the minimum unpadded LLC data size and the\n                maximum allowed LLC data size inclusive and that\n                does not match the number of LLC data octets\n                received.\n\n                The count represented by an instance of this\n                object also includes frames for which the length\n                field value is less than the minimum unpadded LLC\n                data size.')
dot3StatsOutOfRangeLengthFields = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsOutOfRangeLengthFields.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsOutOfRangeLengthFields.setDescription('A count of frames received on a particular\n                interface for which the length field value exceeds\n                the maximum allowed LLC data size.\n\n                The count represented by an instance of this\n                object is not incremented in implementations that\n                observe Ethernet encapsulation conventions (by\n                which the IEEE 802.3 length field is interpreted\n                as the Ethernet Type field).')
dot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsInternalMacReceiveErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot3StatsInternalMacReceiveErrors.setDescription('A count of frames for which reception on a\n                particular interface fails due to an internal MAC\n                sublayer receive error. A frame is only counted by\n                an instance of this object if it is not counted by\n                the corresponding instance of either the\n                dot3StatsFrameTooLongs object, the\n                dot3StatsAlignmentErrors object, the\n                dot3StatsFCSErrors object, the\n                dot3StatsInRangeLengthErrors object, or the\n                dot3StatsOutOfRangeLengthFields object.\n\n                The precise meaning of the count represented by an\n                instance of this object is implementation-\n                specific.  In particular, an instance of this\n                object may represent a count of receive errors on\n                a particular interface that are not otherwise\n                counted.')
dot3CollTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 5), )
if mibBuilder.loadTexts: dot3CollTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot3CollTable.setDescription('A collection of collision histograms for a\n                particular set of interfaces.')
dot3CollEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 5, 1), ).setIndexNames((0, "RFC1284-MIB", "dot3CollIndex"), (0, "RFC1284-MIB", "dot3CollCount"))
if mibBuilder.loadTexts: dot3CollEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot3CollEntry.setDescription('A cell in the histogram of per-frame collisions\n                for a particular interface.  An instance of this\n                object represents the frequency of individual MAC\n                frames for which the transmission (successful or\n                otherwise) on a particular interface is\n                accompanied by a particular number of media\n                collisions.')
dot3CollIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3CollIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot3CollIndex.setDescription('The index value that uniquely identifies the\n                interface to which a particular collision\n                histogram cell pertains.  The interface identified\n                by a particular value of this index is the same\n                interface as identified by the same value of\n                ifIndex.')
dot3CollCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3CollCount.setStatus('mandatory')
if mibBuilder.loadTexts: dot3CollCount.setDescription('The number of per-frame media collisions for\n                which a particular collision histogram cell\n                represents the frequency on a particular\n                interface.')
dot3CollFrequencies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3CollFrequencies.setStatus('mandatory')
if mibBuilder.loadTexts: dot3CollFrequencies.setDescription('A count of individual MAC frames for which the\n                transmission (successful or otherwise) on a\n                particular interface is accompanied by a\n                particular number of media collisions.')
dot3Errors = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7))
dot3ErrorInitError = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7, 1))
dot3ErrorLoopbackError = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7, 2))
dot3Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6))
dot3TestTdr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6, 1))
dot3ChipSets = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8))
dot3ChipSetAMD = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1))
dot3ChipSetAMD7990 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1))
dot3ChipSetAMD79900 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2))
dot3ChipSetIntel = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2))
dot3ChipSetIntel82586 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 1))
dot3ChipSetIntel82596 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 2))
dot3ChipSetSeeq = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3))
dot3ChipSetSeeq8003 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 1))
dot3ChipSetNational = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4))
dot3ChipSetNational8390 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 1))
dot3ChipSetNationalSonic = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 2))
dot3ChipSetFujitsu = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5))
dot3ChipSetFujitsu86950 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 1))
mibBuilder.exportSymbols("RFC1284-MIB", dot3StatsIndex=dot3StatsIndex, dot3TestTdr=dot3TestTdr, dot3ChipSetAMD=dot3ChipSetAMD, dot3Entry=dot3Entry, dot3StatsOutOfRangeLengthFields=dot3StatsOutOfRangeLengthFields, dot3ChipSetAMD7990=dot3ChipSetAMD7990, dot3StatsSQETestErrors=dot3StatsSQETestErrors, dot3StatsLateCollisions=dot3StatsLateCollisions, dot3StatsCarrierSenseErrors=dot3StatsCarrierSenseErrors, dot3Errors=dot3Errors, dot3ErrorInitError=dot3ErrorInitError, dot3MulticastReceiveStatus=dot3MulticastReceiveStatus, dot3StatsInRangeLengthErrors=dot3StatsInRangeLengthErrors, dot3TxEnabled=dot3TxEnabled, dot3StatsTable=dot3StatsTable, dot3CollEntry=dot3CollEntry, dot3CollFrequencies=dot3CollFrequencies, dot3=dot3, dot3StatsAlignmentErrors=dot3StatsAlignmentErrors, dot3ErrorLoopbackError=dot3ErrorLoopbackError, dot3ChipSetSeeq=dot3ChipSetSeeq, dot3InitializeMac=dot3InitializeMac, dot3StatsDeferredTransmissions=dot3StatsDeferredTransmissions, dot3StatsMultipleCollisionFrames=dot3StatsMultipleCollisionFrames, dot3ChipSetSeeq8003=dot3ChipSetSeeq8003, dot3Tests=dot3Tests, dot3ChipSetNationalSonic=dot3ChipSetNationalSonic, dot3ChipSetIntel82596=dot3ChipSetIntel82596, dot3StatsInternalMacTransmitErrors=dot3StatsInternalMacTransmitErrors, dot3CollIndex=dot3CollIndex, dot3Index=dot3Index, dot3CollCount=dot3CollCount, dot3StatsExcessiveCollisions=dot3StatsExcessiveCollisions, dot3StatsExcessiveDeferrals=dot3StatsExcessiveDeferrals, dot3CollTable=dot3CollTable, dot3ChipSetAMD79900=dot3ChipSetAMD79900, dot3ChipSetNational8390=dot3ChipSetNational8390, dot3ChipSetFujitsu=dot3ChipSetFujitsu, dot3StatsFrameTooLongs=dot3StatsFrameTooLongs, dot3ChipSetIntel82586=dot3ChipSetIntel82586, dot3MacSubLayerStatus=dot3MacSubLayerStatus, dot3ChipSetFujitsu86950=dot3ChipSetFujitsu86950, dot3StatsInternalMacReceiveErrors=dot3StatsInternalMacReceiveErrors, dot3Table=dot3Table, dot3TestTdrValue=dot3TestTdrValue, dot3ChipSets=dot3ChipSets, dot3ChipSetIntel=dot3ChipSetIntel, dot3StatsEntry=dot3StatsEntry, dot3StatsSingleCollisionFrames=dot3StatsSingleCollisionFrames, dot3StatsFCSErrors=dot3StatsFCSErrors, dot3ChipSetNational=dot3ChipSetNational)
