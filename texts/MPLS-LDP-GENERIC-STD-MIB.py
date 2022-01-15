#
# PySNMP MIB module MPLS-LDP-GENERIC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-LDP-GENERIC-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityIndex, mplsLdpEntityLdpId = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityIndex", "mplsLdpEntityLdpId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, IpAddress, Gauge32, Bits, Unsigned32, Counter32, NotificationType, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "Bits", "Unsigned32", "Counter32", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, StorageType, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "DisplayString", "RowStatus")
mplsLdpGenericStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 7))
mplsLdpGenericStdMIB.setRevisions(('2004-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setRevisionsDescriptions(('Initial version published as part of RFC 3815.',))
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setOrganization('Multiprotocol Label Switching (mpls)\n                     Working Group')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setContactInfo('Joan Cucchiara (jcucchiara@mindspring.com)\n            Marconi Communications, Inc.\n\n            Hans Sjostrand (hans@ipunplugged.com)\n            ipUnplugged\n\n\n            James V. Luciani (james_luciani@mindspring.com)\n            Marconi Communications, Inc.\n\n            Working Group Chairs:\n            George Swallow,   email: swallow@cisco.com\n            Loa Andersson,    email: loa@pi.se\n\n            MPLS Working Group, email: mpls@uu.net\n       ')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setDescription('Copyright (C) The Internet Society (year). The\n           initial version of this MIB module was published\n           in RFC 3815. For full legal notices see the RFC\n           itself or see:\n           http://www.ietf.org/copyrights/ianamib.html\n\n           This MIB contains managed object definitions for\n           configuring and monitoring the Multiprotocol Label\n           Switching (MPLS), Label Distribution Protocol (LDP),\n           utilizing ethernet as the Layer 2 media.')
mplsLdpGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1))
mplsLdpGenericConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2))
mplsLdpEntityGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1))
mplsLdpEntityGenericLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityGenericLRTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLRTable.setDescription("The MPLS LDP Entity Generic Label Range (LR)\n           Table.\n\n           The purpose of this table is to provide a mechanism\n           for configurating a contiguous range of generic labels,\n           or a 'label range' for LDP Entities.\n\n           LDP Entities which use Generic Labels must have at least\n           one entry in this table.  In other words, this table\n           'extends' the mpldLdpEntityTable for Generic Labels.")
mplsLdpEntityGenericLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMin"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMax"))
if mibBuilder.loadTexts: mplsLdpEntityGenericLREntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLREntry.setDescription("A row in the LDP Entity Generic Label\n           Range (LR) Table.  One entry in this table contains\n           information on a single range of labels\n           represented by the configured Upper and Lower\n           Bounds pairs.  NOTE: there is NO corresponding\n           LDP message which relates to the information\n           in this table, however, this table does provide\n           a way for a user to 'reserve' a generic label\n           range.\n\n           NOTE:  The ranges for a specific LDP Entity\n           are UNIQUE and non-overlapping.\n\n           A row will not be created unless a unique and\n           non-overlapping range is specified.")
mplsLdpEntityGenericLRMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMin.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMin.setDescription('The minimum label configured for this range.')
mplsLdpEntityGenericLRMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMax.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMax.setDescription('The maximum label configured for this range.')
mplsLdpEntityGenericLabelSpace = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("perPlatform", 1), ("perInterface", 2))).clone('perPlatform')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLabelSpace.setReference('RFC3036, LDP Specification, Section 2.2.1,\n           Label Spaces.')
if mibBuilder.loadTexts: mplsLdpEntityGenericLabelSpace.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLabelSpace.setDescription('This value of this object is perPlatform(1), then\n          this means that the label space type is\n          per platform.\n\n          If this object is perInterface(2), then this\n          means that the label space type is per Interface.')
mplsLdpEntityGenericIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericIfIndexOrZero.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericIfIndexOrZero.setDescription("This value represents either the InterfaceIndex of\n          the 'ifLayer' where these Generic Label would be created,\n\n\n          or 0 (zero).  The value of zero means that the\n          InterfaceIndex is not known.\n\n          However, if the InterfaceIndex is known,\n          then it must be represented by this value.\n\n          If an InterfaceIndex becomes known, then the\n          network management entity (e.g., SNMP agent) responsible\n          for this object MUST change the value from 0 (zero) to the\n          value of the InterfaceIndex.")
mplsLdpEntityGenericLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRStorageType.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLRStorageType.setDescription("The storage type for this conceptual row.\n           Conceptual rows having the value 'permanent(4)'\n           need not allow write-access to any columnar\n           objects in the row.")
mplsLdpEntityGenericLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityGenericLRRowStatus.setDescription("The status of this conceptual row.  All writable\n            objects in this row may be modified at any time,\n            however, as described in  detail in the section\n            entitled, 'Changing Values After Session\n            Establishment', and again described in the\n            DESCRIPTION clause of the mplsLdpEntityAdminStatus object,\n            if a session has been initiated with a Peer,\n            changing objects in this table will\n            wreak havoc with the session and interrupt traffic.\n            To repeat again:  the recommended procedure is\n            to set the mplsLdpEntityAdminStatus to\n            down, thereby explicitly causing a\n            session to be torn down. Then, change objects\n            in this entry, then set the mplsLdpEntityAdminStatus\n            to enable which enables a new session to be initiated.\n\n            There must exist at least one entry in this\n            table for every LDP Entity that has a\n            generic label configured.")
mplsLdpGenericGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1))
mplsLdpGenericCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2))
mplsLdpGenericModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleFullCompliance = mplsLdpGenericModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsLdpGenericModuleFullCompliance.setDescription('The Module is implemented with support for\n           read-create and read-write.  In other words,\n           both monitoring and configuration\n           are available when using this MODULE-COMPLIANCE.')
mplsLdpGenericModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 2)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleReadOnlyCompliance = mplsLdpGenericModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsLdpGenericModuleReadOnlyCompliance.setDescription('The Module is implemented with support for\n           read-only.  In other words, only monitoring\n           is available by implementing this MODULE-COMPLIANCE.')
mplsLdpGenericGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLabelSpace"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericIfIndexOrZero"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRStorageType"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericGroup = mplsLdpGenericGroup.setStatus('current')
if mibBuilder.loadTexts: mplsLdpGenericGroup.setDescription('Objects that apply to all MPLS LDP implementations\n           using Generic Labels as the Layer 2.')
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-STD-MIB", mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects, mplsLdpEntityGenericLabelSpace=mplsLdpEntityGenericLabelSpace, mplsLdpGenericModuleFullCompliance=mplsLdpGenericModuleFullCompliance, mplsLdpGenericCompliances=mplsLdpGenericCompliances, mplsLdpGenericModuleReadOnlyCompliance=mplsLdpGenericModuleReadOnlyCompliance, mplsLdpGenericObjects=mplsLdpGenericObjects, PYSNMP_MODULE_ID=mplsLdpGenericStdMIB, mplsLdpEntityGenericLRMax=mplsLdpEntityGenericLRMax, mplsLdpGenericConformance=mplsLdpGenericConformance, mplsLdpEntityGenericLRRowStatus=mplsLdpEntityGenericLRRowStatus, mplsLdpGenericStdMIB=mplsLdpGenericStdMIB, mplsLdpEntityGenericLREntry=mplsLdpEntityGenericLREntry, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpEntityGenericIfIndexOrZero=mplsLdpEntityGenericIfIndexOrZero, mplsLdpEntityGenericLRMin=mplsLdpEntityGenericLRMin, mplsLdpEntityGenericLRStorageType=mplsLdpEntityGenericLRStorageType, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpEntityGenericLRTable=mplsLdpEntityGenericLRTable)
