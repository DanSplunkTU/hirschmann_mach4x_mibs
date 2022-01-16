#
# PySNMP MIB module BEGEMOT-NETGRAPH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-NETGRAPH
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:43 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Integer32, iso, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, Bits, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Integer32", "iso", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Bits", "Gauge32", "TimeTicks")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
begemotNg = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 2))
if mibBuilder.loadTexts: begemotNg.setLastUpdated('200311140000Z')
if mibBuilder.loadTexts: begemotNg.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: begemotNg.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotNg.setDescription('The MIB for the NetGraph access module for SNMP.')
begemotNgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1))
class NgTypeName(TextualConvention, OctetString):
    description = 'Name of a netgraph type.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeName(TextualConvention, OctetString):
    description = 'Name of a netgraph node.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeNameOrEmpty(TextualConvention, OctetString):
    description = 'Name of a netgraph node.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class NgHookName(TextualConvention, OctetString):
    description = 'Name of a netgraph hook.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeId(TextualConvention, Unsigned32):
    description = 'Node identifier.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NgNodeIdOrZero(TextualConvention, Unsigned32):
    description = "Node identifier or 0 for 'no-node'."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

begemotNgConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1))
begemotNgControlNodeName = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 1), NgNodeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgControlNodeName.setStatus('current')
if mibBuilder.loadTexts: begemotNgControlNodeName.setDescription('The name of the netgraph node of this daemon. The name is\n\t    writeable during initialisation. If the name is set from\n\t    the empty string to the non-empty string, the netgraph socket\n\t    is created. Once set it cannot be changed.')
begemotNgResBufSiz = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 65536)).clone(20000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgResBufSiz.setStatus('current')
if mibBuilder.loadTexts: begemotNgResBufSiz.setDescription('The size of the receive buffers for netgraph messages.')
begemotNgTimeout = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgTimeout.setStatus('current')
if mibBuilder.loadTexts: begemotNgTimeout.setDescription('The maximum time to wait for a response to a netgraph message.')
begemotNgDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgDebugLevel.setStatus('current')
if mibBuilder.loadTexts: begemotNgDebugLevel.setDescription('The netgraph library debug level. This should be set only\n\t    if the daemon is run with a terminal attached.')
begemotNgStats = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2))
begemotNgNoMems = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNoMems.setStatus('current')
if mibBuilder.loadTexts: begemotNgNoMems.setDescription('Number of times a memory allocation has failed for buffers\n\t    or the message queue.')
begemotNgMsgReadErrs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgMsgReadErrs.setStatus('current')
if mibBuilder.loadTexts: begemotNgMsgReadErrs.setDescription('Number of times reading a netgraph message has failed.')
begemotNgTooLargeMsgs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgTooLargeMsgs.setStatus('current')
if mibBuilder.loadTexts: begemotNgTooLargeMsgs.setDescription('Number of times a netgraph message was too large for\n\t    the buffer. Try increasing begemotNgResBufSiz if\n\t    this happens.')
begemotNgDataReadErrs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgDataReadErrs.setStatus('current')
if mibBuilder.loadTexts: begemotNgDataReadErrs.setDescription('Number of times reading a netgraph data message has failed.')
begemotNgTooLargeDatas = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgTooLargeDatas.setStatus('current')
if mibBuilder.loadTexts: begemotNgTooLargeDatas.setDescription('Number of times a netgraph data message was too large.\n\t    You need to increase begemotNgResBufSiz.')
begemotNgTypeTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3), )
if mibBuilder.loadTexts: begemotNgTypeTable.setStatus('current')
if mibBuilder.loadTexts: begemotNgTypeTable.setDescription('A table containing information about all netgraph node types.')
begemotNgTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgTypeName"))
if mibBuilder.loadTexts: begemotNgTypeEntry.setStatus('current')
if mibBuilder.loadTexts: begemotNgTypeEntry.setDescription('Table entry that describes one netgraph node.')
begemotNgTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 1), NgTypeName())
if mibBuilder.loadTexts: begemotNgTypeName.setStatus('current')
if mibBuilder.loadTexts: begemotNgTypeName.setDescription('The name of the type. Used as index.')
begemotNgTypeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loaded", 1), ("unloaded", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotNgTypeStatus.setStatus('current')
if mibBuilder.loadTexts: begemotNgTypeStatus.setDescription('If loaded then the node type is available. A type can be load\n\t    by setting this field to loaded. It is unload if the field is\n\t    set to unloaded. Note, that a type cannot be unloaded if it\n\t    is compiled into the kernel or has nodes of this type. The name\n\t    of the file containing the type implementation is constructed by\n\t    prepending ng_ to the type name.')
begemotNgNodeTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4), )
if mibBuilder.loadTexts: begemotNgNodeTable.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeTable.setDescription('A table containing information about all netgraph nodes.')
begemotNgNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgNodeId"))
if mibBuilder.loadTexts: begemotNgNodeEntry.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeEntry.setDescription('Table entry that describes one netgraph node.')
begemotNgNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 1), NgNodeId())
if mibBuilder.loadTexts: begemotNgNodeId.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeId.setDescription('The 32bit node id of this node. 0 is an illegal value.')
begemotNgNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeStatus.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeStatus.setDescription('Indicates whether the node exists or not.')
begemotNgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 3), NgNodeNameOrEmpty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeName.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeName.setDescription('Name of the node (if any).')
begemotNgNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 4), NgTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeType.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeType.setDescription('Type name of the node.')
begemotNgNodeHooks = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeHooks.setStatus('current')
if mibBuilder.loadTexts: begemotNgNodeHooks.setDescription('Number of hooks on this node.')
begemotNgHookTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5), )
if mibBuilder.loadTexts: begemotNgHookTable.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookTable.setDescription('A table containing information about all netgraph hooks.')
begemotNgHookEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookNodeId"), (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookHook"))
if mibBuilder.loadTexts: begemotNgHookEntry.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookEntry.setDescription('Table entry that describes one netgraph node.')
begemotNgHookNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 1), NgNodeId())
if mibBuilder.loadTexts: begemotNgHookNodeId.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookNodeId.setDescription('The 32bit node id of this node.')
begemotNgHookHook = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 2), NgHookName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookHook.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookHook.setDescription('Name of the hook.')
begemotNgHookStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookStatus.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookStatus.setDescription('Indicates whether the hook exists or not.')
begemotNgHookPeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 4), NgNodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerNodeId.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookPeerNodeId.setDescription('The 32bit node id of the peer node of this hook.')
begemotNgHookPeerHook = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 5), NgHookName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerHook.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookPeerHook.setDescription('Name of the peer hook.')
begemotNgHookPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 6), NgTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerType.setStatus('current')
if mibBuilder.loadTexts: begemotNgHookPeerType.setDescription('Name of the peer type.')
mibBuilder.exportSymbols("BEGEMOT-NETGRAPH-MIB", begemotNgMsgReadErrs=begemotNgMsgReadErrs, begemotNgHookTable=begemotNgHookTable, begemotNgNoMems=begemotNgNoMems, begemotNgStats=begemotNgStats, begemotNg=begemotNg, begemotNgTooLargeDatas=begemotNgTooLargeDatas, begemotNgHookNodeId=begemotNgHookNodeId, begemotNgConfig=begemotNgConfig, begemotNgNodeEntry=begemotNgNodeEntry, begemotNgNodeType=begemotNgNodeType, PYSNMP_MODULE_ID=begemotNg, begemotNgHookPeerNodeId=begemotNgHookPeerNodeId, begemotNgHookPeerType=begemotNgHookPeerType, begemotNgNodeId=begemotNgNodeId, begemotNgTypeStatus=begemotNgTypeStatus, NgNodeIdOrZero=NgNodeIdOrZero, NgNodeId=NgNodeId, begemotNgTypeEntry=begemotNgTypeEntry, begemotNgTooLargeMsgs=begemotNgTooLargeMsgs, begemotNgDataReadErrs=begemotNgDataReadErrs, begemotNgNodeHooks=begemotNgNodeHooks, begemotNgResBufSiz=begemotNgResBufSiz, begemotNgControlNodeName=begemotNgControlNodeName, NgNodeNameOrEmpty=NgNodeNameOrEmpty, begemotNgHookHook=begemotNgHookHook, begemotNgTypeTable=begemotNgTypeTable, NgNodeName=NgNodeName, begemotNgHookPeerHook=begemotNgHookPeerHook, begemotNgObjects=begemotNgObjects, NgHookName=NgHookName, begemotNgHookStatus=begemotNgHookStatus, begemotNgNodeName=begemotNgNodeName, begemotNgNodeTable=begemotNgNodeTable, begemotNgTypeName=begemotNgTypeName, begemotNgNodeStatus=begemotNgNodeStatus, begemotNgHookEntry=begemotNgHookEntry, begemotNgDebugLevel=begemotNgDebugLevel, begemotNgTimeout=begemotNgTimeout, NgTypeName=NgTypeName)
