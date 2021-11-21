#
# PySNMP MIB module ACD-SMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-SMAP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:33:09 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter32, Unsigned32, iso, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Gauge32, Integer32, MibIdentifier, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Unsigned32", "iso", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier", "Bits", "Counter64")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
acdSmap = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 8))
acdSmap.setRevisions(('2008-10-01 01:00', '2008-06-15 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdSmap.setRevisionsDescriptions(('Definition revision.', 'Initial version of MIB module ACD-SMAP-MIB.',))
if mibBuilder.loadTexts: acdSmap.setLastUpdated('200810010100Z')
if mibBuilder.loadTexts: acdSmap.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdSmap.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             4878 Levy, suite 202\n             Saint-Laurent, Quebec Canada H4R 2P1\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdSmap.setDescription('The Service mapping database for this Accedian Networks device.')
acdSmapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 0))
acdSmapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1))
acdSmapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2))
acdSmapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1))
acdSmapCoSProfTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: acdSmapCoSProfTable.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfTable.setDescription('The CoS profile table. Each row in the table represents a CoS Profile.\n         A CoS profile is used to map an input packet to an L2 class of service.\n         This traffic mapping (classification) is accomplished using one of\n         the following fields in the incoming packet:\n\n         p-bits in 802.1Q / 802.1Q-in-Q tags\n         IP precedence bits in IPv4 TOS byte\n         DSCP bits in IPv4 DSCP byte\n\n         The class of service value (0-7) assigned to the outgoing traffic is\n         selected based on the conformance level (Green/Yellow) of the incoming\n         traffic. The following sections describe the general configuration\n         parameters and the mapping table of a CoS profile.')
acdSmapCoSProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"))
if mibBuilder.loadTexts: acdSmapCoSProfEntry.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfEntry.setDescription('An entry consisting of all settings to manage a CoS profile.')
acdSmapCoSProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapCoSProfID.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfID.setDescription('Unique value for each CoS Profile instance.')
acdSmapCoSProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfRowStatus.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfRowStatus.setDescription('All columns must have a valid value before a row can be activated. To\n        create a new CoS Profile you shall provide the a unique name and the\n        type for an empty row with the RowStatus set to Create and Go. To\n        delete the CoS Profile you need to set the RowStatus to destroy.')
acdSmapCoSProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfName.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfName.setDescription('This is a string to uniquely identify the CoS profile.')
acdSmapCoSProfType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfType.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfType.setDescription('Indicates the type of CoS profile. Possible values are:  PCP, IP\n         precedence or DSCP.')
acdSmapCoSProfDecodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfDecodeDropBit.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfDecodeDropBit.setDescription('This field is only valid for PCP CoS profiles. If this field is set,\n         the pre-marking color is decoded from the DEI bit (Drop Eligible\n         Indication). Otherwise, the user defined pre-color is used.')
acdSmapCoSProfEncodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfEncodeDropBit.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfEncodeDropBit.setDescription('This field controls the DEI bit in an S-VLAN tag. If this field is set\n         and the outgoing packet is marked yellow then the DEI bit is set to 1.\n         Otherwise, the DEI is set to 0.')
acdSmapCoSProfCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: acdSmapCoSProfCodePointTable.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointTable.setDescription('The Configuration table of all code point entries. Each row in the\n         table represents a Code point. the number of code points depend of the\n         acdSmapCoSProfType value.\n\n         p-bits in 802.1Q / 802.1Q-in-Q tags\n         IP precedence bits in IPv4 TOS byte\n         DSCP bits in IPv4 DSCP byte\n\n         The class of service value (0-7) assigned to the outgoing traffic is\n         selected based on the conformance level (Green/Yellow) of the incoming\n         traffic.')
acdSmapCoSProfCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"), (0, "ACD-SMAP-MIB", "acdSmapCoSProfCodePointID"))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointEntry.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointEntry.setDescription('An entry consisting of all settings for a code point.')
acdSmapCoSProfCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointID.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointID.setDescription('Unique value for each row. Base on Code Point, 0 to 63 for DSCP or 0\n         to 7 for PCP or IP precedence.')
acdSmapCoSProfCodePointPreMarkingColor = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2))).clone('green')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointPreMarkingColor.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointPreMarkingColor.setDescription('This is the user pre-color to mark the incoming traffic. This field\n         is only valid if acdSmapCoSProfDecodeDropBit is not set.')
acdSmapCoSProfCodePointGreenOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointGreenOut.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointGreenOut.setDescription('The class of service value that will be used in the outgoing green\n         packets. This value is selected if the result of the bandwidth\n         regulator assigned to this entry is green or if the pre-marking\n         color is green and no bandwidth regulator is assigned to this entry.')
acdSmapCoSProfCodePointYellowOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointYellowOut.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointYellowOut.setDescription('The class of service value that will be used in the outgoing yellow\n         packets. This value is selected if the result of the bandwidth\n         regulator assigned to this entry is yellow or if the pre-marking\n         color is yellow and no bandwidth regulator is assigned to this entry.')
acdSmapRegSetTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3), )
if mibBuilder.loadTexts: acdSmapRegSetTable.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetTable.setDescription('The Regulator Set profile table. Each row in the table represents a\n         Regulator Set. A bandwidth regulator set allows the user to regulate\n         traffic based on the following information:\n\n         p-bits in 802.1Q / 802.1Q-in-Q tags\n         IP precedence bits in IPv4 TOS byte\n         DSCP bits in IPv4 DSCP byte.\n        ')
acdSmapRegSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"))
if mibBuilder.loadTexts: acdSmapRegSetEntry.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetEntry.setDescription('An entry consisting of all settings to manage a Regulator set.')
acdSmapRegSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapRegSetID.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetID.setDescription('Unique value for each Regulator set instance.')
acdSmapRegSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetRowStatus.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetRowStatus.setDescription('All columns must have a valid value before a row can be activated. To\n        create a new Regulator set you shall provide the a unique name and the\n        type for an empty row with the RowStatus set to Create and Go. To\n        delete the CoS Profile you need to set the RowStatus to destroy.')
acdSmapRegSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetName.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetName.setDescription('This is a string to uniquely identify the Regulator set.')
acdSmapRegSetType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetType.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetType.setDescription('Indicates the type of Regulator Set. Possible values are:  PCP, IP\n         precedence or DSCP.')
acdSmapRegSetCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4), )
if mibBuilder.loadTexts: acdSmapRegSetCodePointTable.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointTable.setDescription('The Configuration table of all code point entries. Each row in the\n         table represents a Code point. the number of code points depend of the\n         acdSmapCoSProfType value.\n\n         p-bits in 802.1Q / 802.1Q-in-Q tags;\n         IP precedence bits in IPv4 TOS byte;\n         DSCP bits in IPv4 DSCP byte.\n         ')
acdSmapRegSetCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"), (0, "ACD-SMAP-MIB", "acdSmapRegSetCodePointID"))
if mibBuilder.loadTexts: acdSmapRegSetCodePointEntry.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointEntry.setDescription('An entry consisting of all settings for a code point.')
acdSmapRegSetCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapRegSetCodePointID.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointID.setDescription('Unique value for each row. Base on Code Point, 0 to 64 for DSCP or 0\n         to 7 for PCP or IP precedence.')
acdSmapRegSetCodePointRegulatorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorID.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorID.setDescription('The bandwidth regulator that will be used to regulate the traffic flow\n         that has this PCP/IP precendence/DSCP value. Refer to acdRegulatorTable \n         to find the exact identifier (same as acdRegulatorID).')
acdSmapRegSetCodePointRegulatorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorEnable.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorEnable.setDescription('Enable or disable traffic regulation for this  PCP, IP precedence or\n         DSCP value.')
acdSmapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1))
acdSmapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2))
acdSmapCoSProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfRowStatus"), ("ACD-SMAP-MIB", "acdSmapCoSProfName"), ("ACD-SMAP-MIB", "acdSmapCoSProfType"), ("ACD-SMAP-MIB", "acdSmapCoSProfDecodeDropBit"), ("ACD-SMAP-MIB", "acdSmapCoSProfEncodeDropBit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfGroup = acdSmapCoSProfGroup.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfGroup.setDescription('Objects for the CoS profile Group.')
acdSmapCoSProfCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 2)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfCodePointPreMarkingColor"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGreenOut"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointYellowOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfCodePointGroup = acdSmapCoSProfCodePointGroup.setStatus('current')
if mibBuilder.loadTexts: acdSmapCoSProfCodePointGroup.setDescription('Objects for the CoS profile CodePoint Group.')
acdSmapRegSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 3)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetRowStatus"), ("ACD-SMAP-MIB", "acdSmapRegSetName"), ("ACD-SMAP-MIB", "acdSmapRegSetType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetGroup = acdSmapRegSetGroup.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetGroup.setDescription('Objects for the Regulator Set Group.')
acdSmapRegSetCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 4)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorID"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetCodePointGroup = acdSmapRegSetCodePointGroup.setStatus('current')
if mibBuilder.loadTexts: acdSmapRegSetCodePointGroup.setDescription('Objects for the Regulator Set CodePoint Group.')
acdSmapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfGroup"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCompliance = acdSmapCompliance.setStatus('current')
if mibBuilder.loadTexts: acdSmapCompliance.setDescription('The compliance statement for support of the ACD-SMAP-MIB module.')
mibBuilder.exportSymbols("ACD-SMAP-MIB", acdSmapCoSProfCodePointTable=acdSmapCoSProfCodePointTable, acdSmapCoSProfEncodeDropBit=acdSmapCoSProfEncodeDropBit, acdSmapRegSetCodePointID=acdSmapRegSetCodePointID, acdSmapCoSProfID=acdSmapCoSProfID, acdSmapRegSetType=acdSmapRegSetType, acdSmapCoSProfCodePointID=acdSmapCoSProfCodePointID, acdSmapCoSProfCodePointPreMarkingColor=acdSmapCoSProfCodePointPreMarkingColor, acdSmapCoSProfGroup=acdSmapCoSProfGroup, acdSmapCoSProfEntry=acdSmapCoSProfEntry, acdSmapMIBObjects=acdSmapMIBObjects, acdSmapCoSProfCodePointYellowOut=acdSmapCoSProfCodePointYellowOut, acdSmapGroups=acdSmapGroups, acdSmapRegSetCodePointEntry=acdSmapRegSetCodePointEntry, acdSmapCoSProfRowStatus=acdSmapCoSProfRowStatus, acdSmapNotifications=acdSmapNotifications, acdSmapRegSetID=acdSmapRegSetID, acdSmapRegSetCodePointGroup=acdSmapRegSetCodePointGroup, PYSNMP_MODULE_ID=acdSmap, acdSmap=acdSmap, acdSmapCoSProfType=acdSmapCoSProfType, acdSmapRegSetCodePointRegulatorID=acdSmapRegSetCodePointRegulatorID, acdSmapConformance=acdSmapConformance, acdSmapConfig=acdSmapConfig, acdSmapCoSProfCodePointGroup=acdSmapCoSProfCodePointGroup, acdSmapCompliance=acdSmapCompliance, acdSmapRegSetCodePointTable=acdSmapRegSetCodePointTable, acdSmapCoSProfName=acdSmapCoSProfName, acdSmapRegSetEntry=acdSmapRegSetEntry, acdSmapRegSetRowStatus=acdSmapRegSetRowStatus, acdSmapCoSProfCodePointEntry=acdSmapCoSProfCodePointEntry, acdSmapRegSetName=acdSmapRegSetName, acdSmapCoSProfCodePointGreenOut=acdSmapCoSProfCodePointGreenOut, acdSmapCompliances=acdSmapCompliances, acdSmapCoSProfDecodeDropBit=acdSmapCoSProfDecodeDropBit, acdSmapRegSetCodePointRegulatorEnable=acdSmapRegSetCodePointRegulatorEnable, acdSmapRegSetTable=acdSmapRegSetTable, acdSmapRegSetGroup=acdSmapRegSetGroup, acdSmapCoSProfTable=acdSmapCoSProfTable)
