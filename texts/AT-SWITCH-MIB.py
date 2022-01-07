#
# PySNMP MIB module AT-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-SWITCH-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:58 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, TimeTicks, Bits, Integer32, Counter32, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Bits", "Integer32", "Counter32", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swi = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87))
swi.setRevisions(('2006-06-12 12:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: swi.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: swi.setLastUpdated('200606121222Z')
if mibBuilder.loadTexts: swi.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: swi.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: swi.setDescription('This MIB file contains definitions of managed objects for the\n\t    SWITCH module. ')
swiPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1), )
if mibBuilder.loadTexts: swiPortTable.setStatus('current')
if mibBuilder.loadTexts: swiPortTable.setDescription('Table of port properties.')
swiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swiPortNumber"))
if mibBuilder.loadTexts: swiPortEntry.setStatus('current')
if mibBuilder.loadTexts: swiPortEntry.setDescription('An entry in the port information table.')
swiPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortNumber.setStatus('current')
if mibBuilder.loadTexts: swiPortNumber.setDescription('This object identifies the port of the switch.')
swiPortIngressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortIngressLimit.setStatus('current')
if mibBuilder.loadTexts: swiPortIngressLimit.setDescription('The Ingress Bandwidth Limit applied to the port. A value of\n            zero indicates that no limit is set.')
swiPortEgressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortEgressLimit.setStatus('current')
if mibBuilder.loadTexts: swiPortEgressLimit.setDescription('The Egress Bandwidth Limit applied to the port. A value of\n            zero indicates that no limit is set.')
swiPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4), )
if mibBuilder.loadTexts: swiPortVlanTable.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanTable.setDescription('Table of port vlan properties.')
swiPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swiPortVlanPortNumber"), (0, "AT-SWITCH-MIB", "swiPortVlanVlanId"))
if mibBuilder.loadTexts: swiPortVlanEntry.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanEntry.setDescription('An entry of vlan  in the port information table.')
swiPortVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortVlanPortNumber.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanPortNumber.setDescription('This object identifies the port of the switch.')
swiPortVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortVlanVlanId.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanVlanId.setDescription('This object identifies the vlans that a port attached to ')
swiPortVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortVlanControl.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanControl.setDescription('The writting to this object enables or disable the port in a vlan.\n              The reading  of this object indicates the port state in a vlan. ')
swiPortVlanStateNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 9)).setObjects(("AT-SWITCH-MIB", "swiPortVlanPortNumber"), ("AT-SWITCH-MIB", "swiPortVlanVlanId"), ("AT-SWITCH-MIB", "swiPortVlanControl"))
if mibBuilder.loadTexts: swiPortVlanStateNotify.setStatus('current')
if mibBuilder.loadTexts: swiPortVlanStateNotify.setDescription('This objects informs a state change of a port in vlan.')
swi56xxPortCounterTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2), )
if mibBuilder.loadTexts: swi56xxPortCounterTable.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortCounterTable.setDescription('Table of swi56xx port counter properties.')
swi56xxPortCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swi56xxPortNumber"))
if mibBuilder.loadTexts: swi56xxPortCounterEntry.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortCounterEntry.setDescription('An entry in the port information table.')
swi56xxPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortNumber.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortNumber.setDescription('This object identifies the port of the switch.')
swi56xxRxTx64kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx64kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx64kPkts.setDescription('The number of 64kB packets received and transmitted.')
swi56xxRxTx65To127kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx65To127kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx65To127kPkts.setDescription('The number of 65kB To 127kB packets received and transmitted.')
swi56xxRxTx128To255kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx128To255kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx128To255kPkts.setDescription('The number of 128kB To 255kB packets received and transmitted.')
swi56xxRxTx256To511kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx256To511kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx256To511kPkts.setDescription('The number of 256kB To 511kB packets received and transmitted.')
swi56xxRxTx512To1023kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx512To1023kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx512To1023kPkts.setDescription('The number of 512kB To 1023kB packets received and transmitted.')
swi56xxRxTx1024ToMaxPktSzPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx1024ToMaxPktSzPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx1024ToMaxPktSzPkts.setDescription('The number of 1024kB To MaxPktSz packets received and transmitted.')
swi56xxRxTx519To1522kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx519To1522kPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxRxTx519To1522kPkts.setDescription('The number of 519kB To 1522kB packets received and transmitted.')
swi56xxPortRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOctets.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxOctets.setDescription('The number of octets received.')
swi56xxPortRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxPkts.setDescription('The number of packets received.')
swi56xxPortRxFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxFCSErrors.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxFCSErrors.setDescription('The number of frames received containing a Frame Check Sequence\n             error.')
swi56xxPortRxMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxMulticastPkts.setDescription('The number of multicast packets received.')
swi56xxPortRxBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxBroadcastPkts.setDescription('The number of broadcast packets received.')
swi56xxPortRxPauseMACCtlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxPauseMACCtlFrms.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxPauseMACCtlFrms.setDescription('The number of valid PAUSE MAC Control frames received.')
swi56xxPortRxOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOversizePkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxOversizePkts.setDescription('The number of oversize packets received.')
swi56xxPortRxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxFragments.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxFragments.setDescription('The number of fragments received.')
swi56xxPortRxJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxJabbers.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxJabbers.setDescription('The number of jabber frames received.')
swi56xxPortRxMACControlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxMACControlFrms.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxMACControlFrms.setDescription('The number of MAC Control frames (Pause and\n             Unsupported) received.')
swi56xxPortRxUnsupportOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxUnsupportOpcode.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxUnsupportOpcode.setDescription('The number of MAC Control frames with unsupported\n             opcode (i.e. not Pause) received.')
swi56xxPortRxAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxAlignmentErrors.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxAlignmentErrors.setDescription('The number of frames with alignment errors received.')
swi56xxPortRxOutOfRngeLenFld = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOutOfRngeLenFld.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxOutOfRngeLenFld.setDescription('The number of packets with length out of range received.')
swi56xxPortRxSymErDurCarrier = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxSymErDurCarrier.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxSymErDurCarrier.setDescription('The number of frames with invalid data symbols received.')
swi56xxPortRxCarrierSenseErr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxCarrierSenseErr.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxCarrierSenseErr.setDescription('The number of false carrier conditions between frames received.')
swi56xxPortRxUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxUndersizePkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxUndersizePkts.setDescription('The number of undersized packets received.')
swi56xxPortRxIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxIpInHdrErrors.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortRxIpInHdrErrors.setDescription('swiPortRxIpInHdrErrors')
swi56xxPortTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxOctets.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxOctets.setDescription('The number of octets transmitted.')
swi56xxPortTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxPkts.setDescription('The number of packets transmitted.')
swi56xxPortTxFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFCSErrors.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxFCSErrors.setDescription('The number of frames containing a Frame Check Sequence\n             error transmitted.')
swi56xxPortTxMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxMulticastPkts.setDescription('The number of multicast packets transmitted.')
swi56xxPortTxBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxBroadcastPkts.setDescription('The number of broadcast packets transmitted.')
swi56xxPortTxPauseMACCtlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPauseMACCtlFrms.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxPauseMACCtlFrms.setDescription('The number of valid PAUSE MAC Control frames transmitted.')
swi56xxPortTxOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxOversizePkts.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxOversizePkts.setDescription('The number of oversize packets transmitted.')
swi56xxPortTxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFragments.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxFragments.setDescription('The number of fragments transmitted.')
swi56xxPortTxJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxJabbers.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxJabbers.setDescription('The number of jabber frames transmitted.')
swi56xxPortTxPauseCtrlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPauseCtrlFrms.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxPauseCtrlFrms.setDescription('The number of Pause control frames transmitted.')
swi56xxPortTxFrameWDeferrdTx = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFrameWDeferrdTx.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxFrameWDeferrdTx.setDescription('The number of frames deferred once before successful\n             transmission.')
swi56xxPortTxFrmWExcesDefer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFrmWExcesDefer.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxFrmWExcesDefer.setDescription('The number of frame aborted after too many deferrals.')
swi56xxPortTxSingleCollsnFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxSingleCollsnFrm.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxSingleCollsnFrm.setDescription('The number of frames which experienced exactly one\n             collision.')
swi56xxPortTxMultCollsnFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxMultCollsnFrm.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxMultCollsnFrm.setDescription('The number of frames which experienced 2 to 15 collisions\n             (including late collisions).')
swi56xxPortTxLateCollsns = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxLateCollsns.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxLateCollsns.setDescription('The number of frames which experienced late collisions.')
swi56xxPortTxExcessivCollsns = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxExcessivCollsns.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxExcessivCollsns.setDescription('The number of frames aborted before transmission after 16\n             collisions.')
swi56xxPortTxCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxCollisionFrames.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortTxCollisionFrames.setDescription('The total number of collisions.')
swi56xxPortMiscDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscDropEvents.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortMiscDropEvents.setDescription('The number of packets discarded at ingress port.')
swi56xxPortMiscTaggedPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscTaggedPktTx.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortMiscTaggedPktTx.setDescription('The number of VLAN tagged packets transmitted.')
swi56xxPortMiscTotalPktTxAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscTotalPktTxAbort.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortMiscTotalPktTxAbort.setDescription('The number of Layer 2 and 3 packets aborted during\n             transmission.')
swi56xxPortHWMultiTTLexpired = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiTTLexpired.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortHWMultiTTLexpired.setDescription('Number of multicast TTL expired frames.')
swi56xxPortHWMultiBridgedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiBridgedFrames.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortHWMultiBridgedFrames.setDescription('Number of multicast bridged frames')
swi56xxPortHWMultiRxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiRxDrops.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortHWMultiRxDrops.setDescription('Number of multicast frames dropped at reception')
swi56xxPortHWMultiTxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiTxDrops.setStatus('current')
if mibBuilder.loadTexts: swi56xxPortHWMultiTxDrops.setDescription('NNumber of multicast frames dropped at transmission')
swiDebugVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3))
swiTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0))
swiDebugMemoryParityErrors = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiDebugMemoryParityErrors.setStatus('current')
if mibBuilder.loadTexts: swiDebugMemoryParityErrors.setDescription('For switches based on certain switch chips, the number of parity errors\n            that have been detected in packet memory associated with the switch. If the\n            device does not include the counting of memory parity errors, this variable\n            will return 0.')
swiIntrusionDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0, 6)).setObjects(("AT-SWITCH-MIB", "swiPortNumber"))
if mibBuilder.loadTexts: swiIntrusionDetectionTrap.setStatus('current')
if mibBuilder.loadTexts: swiIntrusionDetectionTrap.setDescription('An intrusion detection trap is generated when a port has intrusion\n                detection enabled, and the action taken when intrusion is detected is\n                to generate a trap. Intrusion is detected when the number of MAC\n                addresses learned on the port exceeds the configured learn limit.\n                The ifIndex of the port is included in the trap.')
mibBuilder.exportSymbols("AT-SWITCH-MIB", swiPortVlanEntry=swiPortVlanEntry, swi56xxPortRxOctets=swi56xxPortRxOctets, swi56xxPortTxLateCollsns=swi56xxPortTxLateCollsns, swi56xxPortRxBroadcastPkts=swi56xxPortRxBroadcastPkts, swi56xxPortTxFragments=swi56xxPortTxFragments, swi56xxPortTxPkts=swi56xxPortTxPkts, swi56xxPortHWMultiTxDrops=swi56xxPortHWMultiTxDrops, swi56xxPortRxFragments=swi56xxPortRxFragments, swi56xxRxTx65To127kPkts=swi56xxRxTx65To127kPkts, swi56xxPortNumber=swi56xxPortNumber, swi56xxPortHWMultiTTLexpired=swi56xxPortHWMultiTTLexpired, swi56xxRxTx256To511kPkts=swi56xxRxTx256To511kPkts, swiDebugMemoryParityErrors=swiDebugMemoryParityErrors, swi56xxPortRxJabbers=swi56xxPortRxJabbers, swi56xxPortTxFrameWDeferrdTx=swi56xxPortTxFrameWDeferrdTx, swi56xxPortTxMultCollsnFrm=swi56xxPortTxMultCollsnFrm, swi56xxPortRxFCSErrors=swi56xxPortRxFCSErrors, swiPortVlanVlanId=swiPortVlanVlanId, swiPortVlanTable=swiPortVlanTable, swi56xxRxTx519To1522kPkts=swi56xxRxTx519To1522kPkts, swi56xxPortMiscTaggedPktTx=swi56xxPortMiscTaggedPktTx, swiTrap=swiTrap, swi56xxPortTxFCSErrors=swi56xxPortTxFCSErrors, swi=swi, swiPortEntry=swiPortEntry, swi56xxPortTxPauseCtrlFrms=swi56xxPortTxPauseCtrlFrms, swi56xxPortHWMultiBridgedFrames=swi56xxPortHWMultiBridgedFrames, swiIntrusionDetectionTrap=swiIntrusionDetectionTrap, swi56xxRxTx512To1023kPkts=swi56xxRxTx512To1023kPkts, swi56xxPortTxOversizePkts=swi56xxPortTxOversizePkts, swi56xxPortRxPkts=swi56xxPortRxPkts, swiPortVlanControl=swiPortVlanControl, swi56xxPortTxPauseMACCtlFrms=swi56xxPortTxPauseMACCtlFrms, swi56xxPortTxJabbers=swi56xxPortTxJabbers, swi56xxRxTx64kPkts=swi56xxRxTx64kPkts, swiPortIngressLimit=swiPortIngressLimit, swi56xxPortTxOctets=swi56xxPortTxOctets, swiPortVlanStateNotify=swiPortVlanStateNotify, PYSNMP_MODULE_ID=swi, swi56xxPortCounterEntry=swi56xxPortCounterEntry, swi56xxPortRxPauseMACCtlFrms=swi56xxPortRxPauseMACCtlFrms, swi56xxPortRxMACControlFrms=swi56xxPortRxMACControlFrms, swi56xxPortRxOutOfRngeLenFld=swi56xxPortRxOutOfRngeLenFld, swiDebugVariables=swiDebugVariables, swi56xxPortRxMulticastPkts=swi56xxPortRxMulticastPkts, swi56xxPortTxBroadcastPkts=swi56xxPortTxBroadcastPkts, swi56xxRxTx1024ToMaxPktSzPkts=swi56xxRxTx1024ToMaxPktSzPkts, swi56xxPortRxSymErDurCarrier=swi56xxPortRxSymErDurCarrier, swi56xxPortRxUnsupportOpcode=swi56xxPortRxUnsupportOpcode, swi56xxPortCounterTable=swi56xxPortCounterTable, swiPortTable=swiPortTable, swiPortNumber=swiPortNumber, swi56xxPortRxOversizePkts=swi56xxPortRxOversizePkts, swi56xxPortTxExcessivCollsns=swi56xxPortTxExcessivCollsns, swi56xxPortTxFrmWExcesDefer=swi56xxPortTxFrmWExcesDefer, swi56xxRxTx128To255kPkts=swi56xxRxTx128To255kPkts, swi56xxPortTxCollisionFrames=swi56xxPortTxCollisionFrames, swi56xxPortRxIpInHdrErrors=swi56xxPortRxIpInHdrErrors, swi56xxPortRxAlignmentErrors=swi56xxPortRxAlignmentErrors, swi56xxPortTxSingleCollsnFrm=swi56xxPortTxSingleCollsnFrm, swi56xxPortRxCarrierSenseErr=swi56xxPortRxCarrierSenseErr, swi56xxPortMiscTotalPktTxAbort=swi56xxPortMiscTotalPktTxAbort, swi56xxPortMiscDropEvents=swi56xxPortMiscDropEvents, swi56xxPortHWMultiRxDrops=swi56xxPortHWMultiRxDrops, swi56xxPortTxMulticastPkts=swi56xxPortTxMulticastPkts, swi56xxPortRxUndersizePkts=swi56xxPortRxUndersizePkts, swiPortVlanPortNumber=swiPortVlanPortNumber, swiPortEgressLimit=swiPortEgressLimit)
