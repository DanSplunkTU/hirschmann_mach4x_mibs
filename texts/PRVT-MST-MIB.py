#
# PySNMP MIB module PRVT-MST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-MST-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Timeout, dot1dBasePort, BridgeId, dot1dStpPortEntry = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "dot1dBasePort", "BridgeId", "dot1dStpPortEntry")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, Counter32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "TimeStamp")
prvtMSTMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 107))
prvtMSTMib.setRevisions(('2005-02-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtMSTMib.setRevisionsDescriptions(('Fixed spelling errors and changed the contact info.',))
if mibBuilder.loadTexts: prvtMSTMib.setLastUpdated('200502160000Z')
if mibBuilder.loadTexts: prvtMSTMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtMSTMib.setContactInfo(' BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtMSTMib.setDescription('The MIB module for managing 802.1s\nMultiple Spanning Tree Protocol (MSTP).')
prvtMSTNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0))
prvtMSTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1))
mSTRegion = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1))
mSTBridgeParams = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2))
mSTTimers = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3))
mSTPort = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4))
mSTRegionEditControl = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1))
mSTRegionParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2))
mSTRegionEditBufferStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("released", 1), ("acquiredBySnmp", 2), ("acquiredByNonSnmp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionEditBufferStatus.setStatus('current')
if mibBuilder.loadTexts: mSTRegionEditBufferStatus.setDescription('Indicates the current ownership status of the unique\nRegion Config Edit Buffer.\n\nreleased -- the Edit Buffer can be acquired by any of\nthe SNMP management stations.\n\nacquiredBySnmp -- the Edit Buffer is acquired by\nany of the SNMP management stations.\n\nacquiredByNonSnmp -- the Edit Buffer is acquired by the\nnon-SNMP users managing the device.')
mSTRegionEditBufferOperation = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("acquire", 2), ("releaseWithForce", 3), ("commit", 4), ("rollBack", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditBufferOperation.setStatus('current')
if mibBuilder.loadTexts: mSTRegionEditBufferOperation.setDescription('Indicates the operation that is performed on the Region\nConfig Edit Buffer.\n\nother -- none of the following operations.\n\nacquire -- acquire the Edit Buffer. This operation can\nonly be performed when the mSTRegionEditBufferStatus\nobject has the value of\nreleased(1). After the successful execution of\nthis action, the mSTRegionEditBufferStatus object\nwill be changed to acquiredBySnmp(2).\n\nreleaseWithForce -- release the Edit Buffer acquired by\nnon-SNMP users with force and discard the changes\nin the Edit Buffer. This operation can only be\nperformed when the mSTRegionEditBufferStatus object\nhas the value of acquiredByNonSnmp(2).\n\ncommit -- commit the changes in the Edit Buffer\nand release the Edit Buffer. The successful\nexecution of this action will make the changes\nin the Edit Buffer effective on the device.\nThis operation can only be performed when the\nmSTRegionEditBufferStatus object has the\nvalue of acquiredBySnmp(3).\n\nrollBack -- discard the changes in the Edit Buffer\nand release the Edit Buffer. This operation can\nonly be performed when the mSTRegionEditBufferStatus\nobject has the value of acquiredBySnmp(3).\n\nThis object always returns other(1) when it is read.')
mSTRegionName = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionName.setStatus('current')
if mibBuilder.loadTexts: mSTRegionName.setDescription('The operational MST region name.')
mSTRegionEditName = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditName.setStatus('current')
if mibBuilder.loadTexts: mSTRegionEditName.setDescription('The MST region name in the Edit Buffer.\n\nThis object is only instantiated when the\nmSTRegionEditBufferStatus object has the value of\nacquiredBySnmp(2).')
mSTRegionRevision = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionRevision.setStatus('current')
if mibBuilder.loadTexts: mSTRegionRevision.setDescription('The operational MST region version.')
mSTRegionEditRevision = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditRevision.setStatus('current')
if mibBuilder.loadTexts: mSTRegionEditRevision.setDescription('The MST region version in the Edit Buffer. This object is\nonly instantiated when the mSTRegionEditBufferStatus object\nhas the value of acquiredBySnmp(2).')
mSTInstanceVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5), )
if mibBuilder.loadTexts: mSTInstanceVlanTable.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlanTable.setDescription('This table contains MST instance information with\none entry for each MST instance numbered from 0\nto mSTMaxInstanceNumber.')
mSTInstanceVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceVlanEntry.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlanEntry.setDescription('A conceptual row containing the MST instance\ninformation.')
mSTInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mSTInstanceIndex.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceIndex.setDescription('An integer that uniquely identifies an MST instance\nfrom 0 to the object value of mSTMaxInstanceNumber.')
mSTInstanceVlansMapped = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlansMapped.setDescription("A string of octets containing one bit per VLAN. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 0 through 7; the second octet to VLANs 8 through\n15; etc. The least significant bit of each octet\ncorresponds to the lowest value VlanIndex in that octet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to '1'.")
mSTInstanceVlansMapped2k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped2k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlansMapped2k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 1024 through 2047. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 1024 through 1031; the second octet to VLANs 1032\nthrough 1039; etc. The least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to '1'.")
mSTInstanceVlansMapped3k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped3k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlansMapped3k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 2048 through 3071. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 2048 through 2055; the second octet to VLANs 2056\nthrough 2063; etc. The least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to '1'.")
mSTInstanceVlansMapped4k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped4k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlansMapped4k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 3072 through 4095. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 3072 through 3079; the second octet to VLANs 3080\nthrough 3087; etc. The least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to '1'.")
mSTInstanceVlanEditTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6), )
if mibBuilder.loadTexts: mSTInstanceVlanEditTable.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlanEditTable.setDescription('This table contains MST instance information in the\nEdit Buffer with one entry for each MST\ninstance numbered from 0 to mSTMaxInstanceNumber.\n\nThis table is only instantiated when the\nmSTRegionEditBufferStatus object has the value of\nacquiredBySnmp(2).')
mSTInstanceVlanEditEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceVlanEditEntry.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceVlanEditEntry.setDescription('A conceptual row containing MST instance information\nin the Edit Buffer.')
mSTInstanceEditVlansMap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceEditVlansMap.setDescription("A string of octets containing one bit per VLAN. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 0 through 7; the second octet to VLANs 8 through\n15; etc. The least significant bit of each octet\ncorresponds to the lowest value VlanIndex in that octet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to\n'1'. Each VLAN can only be mapped to one unique MST\ninstance in the range from 1 to mSTMaxInstanceNumber.\nIf the bit corresponding to a VLAN is changed from '1'\nto '0', then that VLAN will be automatically mapped to\nMST instance 0 by the device.")
mSTInstanceEditVlansMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap2k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceEditVlansMap2k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 1024 through 2047.\nThe first octet corresponds to VLANs with VlanIndex values\nof 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.\nThe least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to\n'1'. Each VLAN can only be mapped to one unique MST\ninstance in the range from 1 to mSTMaxInstanceNumber.\nIf the bit corresponding to a VLAN is changed from '1'\nto '0', then that VLAN will be automatically mapped to\nMST instance 0 by the device.")
mSTInstanceEditVlansMap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap3k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceEditVlansMap3k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 2048 through 3071. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 2048 through 2055; the second octet to VLANs 2056\nthrough 2063; etc. The least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to\n'1'. Each VLAN can only be mapped to one unique MST\ninstance in the range from 1 to mSTMaxInstanceNumber.\nIf the bit corresponding to a VLAN is changed from '1'\nto '0', then that VLAN will be automatically mapped to\nMST instance 0 by the device.")
mSTInstanceEditVlansMap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap4k.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceEditVlansMap4k.setDescription("A string of octets containing one bit per VLAN for\nVLANs with VlanIndex values of 3072 through 4095. The\nfirst octet corresponds to VLANs with VlanIndex values\nof 3072 through 3079; the second octet to VLANs 3080\nthrough 3087; etc. The least significant bit of each\noctet corresponds to the lowest value VlanIndex in that\noctet.\n\nFor each VLAN, if it is mapped to this MST instance,\nthen the bit corresponding to that VLAN is set to\n'1'. Each VLAN can only be mapped to one unique MST\ninstance in the range from 1 to mSTMaxInstanceNumber.\nIf the bit corresponding to a VLAN is changed from '1'\nto '0', then that VLAN will be automatically mapped to\nMST instance 0 by the device.")
mSTMaxHopCount = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTMaxHopCount.setStatus('current')
if mibBuilder.loadTexts: mSTMaxHopCount.setDescription('The maximum number of hops for the MST region.')
mSTMaxInstanceNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTMaxInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: mSTMaxInstanceNumber.setDescription('The maximum MST (Multiple Spanning Tree) instance IDs\nthat are supported by the device for the MST Protocol.')
mSTInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3), )
if mibBuilder.loadTexts: mSTInstanceTable.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceTable.setDescription('This table contains MST instance information with\none entry for each MST instance numbered from 0\nto mSTMaxInstanceNumber.')
mSTInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceEntry.setDescription('A conceptual row containing the MST instance\ninformation.')
mSTInstanceDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 1), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceDesignatedRoot.setReference('IEEE 802.1D-1990: Section 4.5.5.4')
if mibBuilder.loadTexts: mSTInstanceDesignatedRoot.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceDesignatedRoot.setDescription('The unique MST Bridge Identifier of the Bridge\nrecorded as the Root in the Configuration BPDUs\ntransmitted by the Designated Bridge for the\nsegment to which the port is attached.')
mSTInstanceRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootCost.setReference('IEEE 802.1D-1990: Section 4.5.5.5')
if mibBuilder.loadTexts: mSTInstanceRootCost.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceRootCost.setDescription('The path cost of the root Port of this MST. This value is\ncompared to the Root Path Cost field in received\nbridge PDUs.')
mSTInstanceRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootPort.setReference('IEEE 802.1D-1990: Section 4.5.5.6')
if mibBuilder.loadTexts: mSTInstanceRootPort.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceRootPort.setDescription('The root port of this MST.')
mSTInstanceDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceDesignatedBridge.setReference('IEEE 802.1D-1990: Section 4.5.5.4')
if mibBuilder.loadTexts: mSTInstanceDesignatedBridge.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceDesignatedBridge.setDescription('The unique MST Designated Bridge Identifier. ')
mSTInstanceRootPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootPriority.setReference('IEEE 802.1D-1990: Section 4.5.5.5')
if mibBuilder.loadTexts: mSTInstanceRootPriority.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceRootPriority.setDescription('The MST root priority.')
mSTInstanceRemainingHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRemainingHopCount.setStatus('current')
if mibBuilder.loadTexts: mSTInstanceRemainingHopCount.setDescription('The remaining hop count for this MST instance.')
mSTInstancePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440)).clone(32768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstancePriority.setStatus('current')
if mibBuilder.loadTexts: mSTInstancePriority.setDescription('MSTI priority, in steps of 4096.')
mSTMigrationTimer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTMigrationTimer.setStatus('current')
if mibBuilder.loadTexts: mSTMigrationTimer.setDescription('MST (Multiple Spanning Tree) migration timer .\nDetermines timeout migration in seconds')
mSTTxHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTTxHoldCount.setStatus('current')
if mibBuilder.loadTexts: mSTTxHoldCount.setDescription('MST (Multiple Spanning Tree) Tx Hold Counter')
mSTMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 3), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTMaxAge.setReference('IEEE 802.1D-1990: Section 4.5.3.4')
if mibBuilder.loadTexts: mSTMaxAge.setStatus('current')
if mibBuilder.loadTexts: mSTMaxAge.setDescription('The maximum age of Multiple Spanning Tree Protocol\ninformation learned from the network on any port\nbefore it is discarded, in units of hundredths of\na second. This is the actual value that this\nbridge is currently using.')
mSTHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 4), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTHelloTime.setReference('IEEE 802.1D-1990: Section 4.5.3.5')
if mibBuilder.loadTexts: mSTHelloTime.setStatus('current')
if mibBuilder.loadTexts: mSTHelloTime.setDescription('The time between the transmissions of\nConfiguration bridge PDUs by this node on any port\nwhen the port is the root of the spanning tree or trying\nto become so, in units of hundredths of a second.\nThis is the actual value that this bridge is\ncurrently using.')
mSTForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 5), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTForwardDelay.setReference('IEEE 802.1D-1990: Section 4.5.3.6')
if mibBuilder.loadTexts: mSTForwardDelay.setStatus('current')
if mibBuilder.loadTexts: mSTForwardDelay.setDescription('This time value, measured in units of hundredths\nof a second, controls how fast a port changes its\nspanning state when moving toward the Forwarding\nstate. The value determines how long the port\nstays in each of the Listening and Learning\nstates, which precede the Forwarding state. This\nvalue is also used, when a topology change has\nbeen detected and is underway, to age all dynamic\nentries in the Forwarding Database. Note that\nthis value is the one that this bridge is\ncurrently using, in contrast to\nmSTBridgeForwardDelay which is the value that\nthis bridge and all others would start using\nif/when this bridge were to become the root.')
mSTBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 6), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeMaxAge.setReference('IEEE 802.1D-1990: Section 4.5.3.8')
if mibBuilder.loadTexts: mSTBridgeMaxAge.setStatus('current')
if mibBuilder.loadTexts: mSTBridgeMaxAge.setDescription('The value that all bridges use for MaxAge when\nthis bridge is acting as the root. Note that\n802.1D-1990 specifies that the range for this\nparameter is related to the value of\nmSTBridgeHelloTime. The granularity of this\ntimer is specified by 802.1D-1990 to be 1 second.\nAn agent may return a badValue error if a set operation is\nattempted with a value that is not a whole number\nof seconds.')
mSTBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 7), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeHelloTime.setReference('IEEE 802.1D-1990: Section 4.5.3.9')
if mibBuilder.loadTexts: mSTBridgeHelloTime.setStatus('current')
if mibBuilder.loadTexts: mSTBridgeHelloTime.setDescription('The value that all bridges use for HelloTime when\nthis bridge is acting as the root. The\ngranularity of this timer is specified by 802.1D-\n1990 to be 1 second. An agent may return a badValue error if a set operation is\nattempted with a value that is not a whole number\nof seconds.')
mSTBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 8), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeForwardDelay.setReference('IEEE 802.1D-1990: Section 4.5.3.10')
if mibBuilder.loadTexts: mSTBridgeForwardDelay.setStatus('current')
if mibBuilder.loadTexts: mSTBridgeForwardDelay.setDescription('The value that all bridges use for ForwardDelay\nwhen this bridge is acting as the root. Note that\n802.1D-1990 specifies that the range for this\nparameter is related to the value of\nmSTBridgeMaxAge. The granularity of this\ntimer is specified by 802.1D-1990 to be 1 second.\nAn agent may return a badValue error if a set operation is\nattempted with a value that is not a whole number\nof seconds.')
mSTPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1), )
if mibBuilder.loadTexts: mSTPortTable.setStatus('current')
if mibBuilder.loadTexts: mSTPortTable.setDescription('A table containing port information for the MST\nProtocol on all the bridge ports existing on the\nsystem.')
mSTPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: mSTPortEntry.setStatus('current')
if mibBuilder.loadTexts: mSTPortEntry.setDescription('An entry with port information for the MST Protocol\non a bridge port.')
mSTPortAdminLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pointToPoint", 1), ("shared", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortAdminLinkType.setStatus('current')
if mibBuilder.loadTexts: mSTPortAdminLinkType.setDescription("Indicates the administrative link type configuration of\na bridge port for the MST protocol.\n\npointToPoint -- the port is administratively configured to\nbe connected to a point-to-point link.\n\nshared -- the port is administratively configured to be\nconnected to a shared medium.\n\nauto -- the administrative configuration of the port's\nlink type depends on the duplex mode of the port's link.\nIf the port's link is full-duplex, the administrative\nlink type configuration on this port will be taken\nas pointTopoint(1). If the port link is half-duplex,\nthe administrative link type configuration on this\nport will be taken as shared(2).\n\nThis configuration of this object only takes effect when the\nstpxSpanningTreeType is mst(4).")
mSTPortOperLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pointToPoint", 1), ("shared", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortOperLinkType.setStatus('current')
if mibBuilder.loadTexts: mSTPortOperLinkType.setDescription('Indicates the operational link type of a bridge port\nfor the MST protocol.\n\npointToPoint -- the port is operationally connected to\na point-to-point link.\n\nshared -- the port is operationally connected to\na shared medium.\n\nother -- none of the above.\n\nThis object is only instantiated when the value of the\nstpxSpanningTreeType object is mst(4).')
mSTPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortProtocolMigration.setReference('IEEE 802.1w clause 14.8.2.4, 17.26.')
if mibBuilder.loadTexts: mSTPortProtocolMigration.setStatus('current')
if mibBuilder.loadTexts: mSTPortProtocolMigration.setDescription('The protocol migration control on this port. When the\nvalue of thw stpxSpanningTreeType object is mst(4), setting\ntrue(1) to this object forces the device to try using\nversion 2 BPDUs on this port. When the value of\nthe stpxSpanningTreeType object is not mst(4), setting true(1) to\nthis object has no effect. Setting false(2) to this object\nhas no effect. This object always returns false(2) when read.')
mSTPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 4), Bits().clone(namedValues=NamedValues(("edge", 0), ("boundary", 1), ("pvst", 2), ("stp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortStatus.setStatus('current')
if mibBuilder.loadTexts: mSTPortStatus.setDescription('Indicates the operational status of the port for the\nMST protocol.\n\nedge -- this port is an edge port for the MST region.\n\nboundary -- this port is a boundary port for the\nMST region.\n\npvst -- this port is connected to a PVST/PVST+ bridge.\n\nstp -- this port is connected to a Single Spanning\nTree bridge.\n\nThis object is only instantiated when the object value\nof stpxSpanningTreeType is mst(4).')
mSTPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortAdminEdgePort.setReference('IEEE 802.1t clause 14.8.2, 18.3.3')
if mibBuilder.loadTexts: mSTPortAdminEdgePort.setStatus('current')
if mibBuilder.loadTexts: mSTPortAdminEdgePort.setDescription('The administrative value of the Edge Port parameter. A\nvalue of true(1) indicates that this port should be\nassumed as an edge-port and a value of FALSE(2) indicates\nthat this port should be assumed as a non-edge-port.')
mSTPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortOperEdgePort.setReference('IEEE 802.1t clause 14.8.2, 18.3.4')
if mibBuilder.loadTexts: mSTPortOperEdgePort.setStatus('current')
if mibBuilder.loadTexts: mSTPortOperEdgePort.setDescription('The operational value of the Edge Port parameter. The\nobject is initialized to the value of\ndot1dStpPortAdminEdgePort and is set false(2) on reception of\na BPDU.')
mSTPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortEnable.setReference('IEEE 802.1D-1990: Section 4.5.5.2')
if mibBuilder.loadTexts: mSTPortEnable.setStatus('current')
if mibBuilder.loadTexts: mSTPortEnable.setDescription('The enabled/disabled status of the port.')
mSTPortPerMstTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2), )
if mibBuilder.loadTexts: mSTPortPerMstTable.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstTable.setDescription('A table containing a list of the bridge ports for a\nparticular MST instance. This table holds the\nsettings.')
mSTPortPerMstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: mSTPortPerMstEntry.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstEntry.setDescription('An entry containing the port information for the MST\nprotocol on a port for a particular MST instance.')
mSTPortPerMstRoleValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("root", 2), ("designated", 3), ("alternate", 4), ("backUp", 5), ("boundary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstRoleValue.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstRoleValue.setDescription('Indicates the port role on a particular MST instance\nfor the MST protocol.\n\ndisabled -- this port has no role on this MST instance.\n\nroot -- this port has the role of root port on this MST\ninstance.\n\ndesignated -- this port has the role of designated\nport on this MST instance.\n\nalternate -- this port has the role of alternate port\non this MST instance.\n\nbackUp -- this port has the role of backup port on this\nMST instance.\n\nboundary -- this port has the role of boundary port on\nthis MST instance.')
mSTPortPerMstPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortPerMstPriority.setReference('IEEE 802.1D-1990: Section 4.5.5.1')
if mibBuilder.loadTexts: mSTPortPerMstPriority.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstPriority.setDescription('The value of the priority field which is\ncontained in the first (in network byte order)\noctet of the (2 octet long) Port ID. The other\noctet of the Port ID is given by the value of\nmSTPort.')
mSTPortPerMstState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstState.setReference('IEEE 802.1D-1990: Section 4.5.5.2')
if mibBuilder.loadTexts: mSTPortPerMstState.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstState.setDescription("The port's current state as defined by\napplication of the Spanning Tree Protocol. This\nstate controls what action a port takes on\nreception of a frame. If the bridge has detected\na port that is malfunctioning it will place that\nport into the broken(6) state. For ports that\nare disabled (see mSTPortEnable), this object\nwill have a value of disabled(1).")
mSTPortPerMstPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortPerMstPathCost.setReference('IEEE 802.1D-1990: Section 4.5.5.3')
if mibBuilder.loadTexts: mSTPortPerMstPathCost.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstPathCost.setDescription('The contribution of this port to the path cost of\npaths toward the spanning tree root that include\nthis port. 802.1D-1990 recommends that the\ndefault value of this parameter be in inverse\nproportion to the speed of the attached LAN.')
mSTPortPerMstDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedCost.setReference('')
if mibBuilder.loadTexts: mSTPortPerMstDesignatedCost.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstDesignatedCost.setDescription('')
mSTPortPerMstDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedBridge.setReference('')
if mibBuilder.loadTexts: mSTPortPerMstDesignatedBridge.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstDesignatedBridge.setDescription('')
mSTPortPerMstDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedPort.setStatus('current')
if mibBuilder.loadTexts: mSTPortPerMstDesignatedPort.setDescription("The Port Identifier of the port on the MST Instance Designated Bridge for this port's segment.")
mstpNewRoot = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 1)).setObjects(("PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mstpNewRoot.setStatus('current')
if mibBuilder.loadTexts: mstpNewRoot.setDescription('This notification is the MSTP equivalent of the standard STP newRoot notification.')
mstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 2)).setObjects(("PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mstpTopologyChange.setStatus('current')
if mibBuilder.loadTexts: mstpTopologyChange.setDescription('This notification is the MSTP equivalent of the standard STP topologyChange notification.')
mibBuilder.exportSymbols("PRVT-MST-MIB", mSTPort=mSTPort, mSTRegionName=mSTRegionName, mSTMaxAge=mSTMaxAge, mSTPortStatus=mSTPortStatus, mSTInstanceVlanTable=mSTInstanceVlanTable, mstpTopologyChange=mstpTopologyChange, mSTBridgeForwardDelay=mSTBridgeForwardDelay, mSTInstanceDesignatedBridge=mSTInstanceDesignatedBridge, prvtMSTObjects=prvtMSTObjects, mSTPortPerMstRoleValue=mSTPortPerMstRoleValue, mSTInstanceEditVlansMap=mSTInstanceEditVlansMap, mSTInstanceIndex=mSTInstanceIndex, mSTRegionEditRevision=mSTRegionEditRevision, mSTInstanceRootPort=mSTInstanceRootPort, mSTPortPerMstDesignatedBridge=mSTPortPerMstDesignatedBridge, mSTInstanceVlansMapped3k=mSTInstanceVlansMapped3k, mstpNewRoot=mstpNewRoot, mSTInstanceVlansMapped4k=mSTInstanceVlansMapped4k, mSTInstanceRemainingHopCount=mSTInstanceRemainingHopCount, mSTHelloTime=mSTHelloTime, mSTInstanceEditVlansMap3k=mSTInstanceEditVlansMap3k, mSTBridgeHelloTime=mSTBridgeHelloTime, mSTRegionEditBufferStatus=mSTRegionEditBufferStatus, mSTMaxInstanceNumber=mSTMaxInstanceNumber, mSTPortPerMstPriority=mSTPortPerMstPriority, mSTTxHoldCount=mSTTxHoldCount, mSTPortTable=mSTPortTable, mSTInstanceVlanEntry=mSTInstanceVlanEntry, mSTPortAdminLinkType=mSTPortAdminLinkType, mSTRegion=mSTRegion, mSTPortProtocolMigration=mSTPortProtocolMigration, mSTPortPerMstEntry=mSTPortPerMstEntry, mSTTimers=mSTTimers, mSTInstanceEditVlansMap2k=mSTInstanceEditVlansMap2k, mSTInstanceDesignatedRoot=mSTInstanceDesignatedRoot, mSTForwardDelay=mSTForwardDelay, mSTBridgeParams=mSTBridgeParams, mSTPortEnable=mSTPortEnable, mSTInstanceTable=mSTInstanceTable, mSTInstancePriority=mSTInstancePriority, mSTPortOperLinkType=mSTPortOperLinkType, mSTInstanceEntry=mSTInstanceEntry, mSTPortPerMstDesignatedPort=mSTPortPerMstDesignatedPort, prvtMSTNotifications=prvtMSTNotifications, mSTPortPerMstTable=mSTPortPerMstTable, mSTPortEntry=mSTPortEntry, mSTRegionRevision=mSTRegionRevision, mSTInstanceRootCost=mSTInstanceRootCost, mSTPortPerMstState=mSTPortPerMstState, mSTInstanceRootPriority=mSTInstanceRootPriority, mSTMigrationTimer=mSTMigrationTimer, mSTInstanceVlansMapped=mSTInstanceVlansMapped, mSTInstanceEditVlansMap4k=mSTInstanceEditVlansMap4k, prvtMSTMib=prvtMSTMib, mSTRegionEditControl=mSTRegionEditControl, mSTPortAdminEdgePort=mSTPortAdminEdgePort, mSTInstanceVlanEditTable=mSTInstanceVlanEditTable, mSTMaxHopCount=mSTMaxHopCount, mSTPortPerMstPathCost=mSTPortPerMstPathCost, mSTRegionParameters=mSTRegionParameters, mSTInstanceVlanEditEntry=mSTInstanceVlanEditEntry, mSTPortPerMstDesignatedCost=mSTPortPerMstDesignatedCost, mSTBridgeMaxAge=mSTBridgeMaxAge, mSTInstanceVlansMapped2k=mSTInstanceVlansMapped2k, PYSNMP_MODULE_ID=prvtMSTMib, mSTPortOperEdgePort=mSTPortOperEdgePort, mSTRegionEditBufferOperation=mSTRegionEditBufferOperation, mSTRegionEditName=mSTRegionEditName)
