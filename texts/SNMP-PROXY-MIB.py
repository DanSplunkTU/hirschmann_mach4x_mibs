#
# PySNMP MIB module SNMP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-PROXY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
SnmpAdminString, SnmpEngineID = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID")
SnmpTagValue, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Integer32, Counter64, snmpModules, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Counter32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "snmpModules", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
StorageType, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "DisplayString")
snmpProxyMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 14))
snmpProxyMIB.setRevisions(('2002-10-14 00:00', '1998-08-04 00:00', '1997-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpProxyMIB.setRevisionsDescriptions(('Clarifications, published as\n                 RFC 3413.', 'Clarifications, published as\n                 RFC 2573.', 'The initial revision, published as RFC2273.',))
if mibBuilder.loadTexts: snmpProxyMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpProxyMIB.setOrganization('IETF SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpProxyMIB.setContactInfo('WG-email:   snmpv3@lists.tislabs.com\n         Subscribe:  majordomo@lists.tislabs.com\n                     In message body:  subscribe snmpv3\n\n         Co-Chair:   Russ Mundy\n                     Network Associates Laboratories\n         Postal:     15204 Omega Drive, Suite 300\n                     Rockville, MD 20850-4601\n                     USA\n         EMail:      mundy@tislabs.com\n         Phone:      +1 301-947-7107\n\n         Co-Chair:   David Harrington\n                     Enterasys Networks\n         Postal:     35 Industrial Way\n                     P. O. Box 5004\n                     Rochester, New Hampshire 03866-5005\n                     USA\n         EMail:      dbh@enterasys.com\n         Phone:      +1 603-337-2614\n\n         Co-editor:  David B. Levi\n                     Nortel Networks\n         Postal:     3505 Kesterwood Drive\n                     Knoxville, Tennessee 37918\n         EMail:      dlevi@nortelnetworks.com\n         Phone:      +1 865 686 0432\n\n         Co-editor:  Paul Meyer\n                     Secure Computing Corporation\n         Postal:     2675 Long Lake Road\n                     Roseville, Minnesota 55113\n         EMail:      paul_meyer@securecomputing.com\n         Phone:      +1 651 628 1592\n\n         Co-editor:  Bob Stewart\n                     Retired')
if mibBuilder.loadTexts: snmpProxyMIB.setDescription('This MIB module defines MIB objects which provide\n         mechanisms to remotely configure the parameters\n         used by a proxy forwarding application.\n\n         Copyright (C) The Internet Society (2002). This\n         version of this MIB module is part of RFC 3413;\n         see the RFC itself for full legal notices.\n        ')
snmpProxyObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 1))
snmpProxyConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3))
snmpProxyTable = MibTable((1, 3, 6, 1, 6, 3, 14, 1, 2), )
if mibBuilder.loadTexts: snmpProxyTable.setStatus('current')
if mibBuilder.loadTexts: snmpProxyTable.setDescription('The table of translation parameters used by proxy forwarder\n         applications for forwarding SNMP messages.')
snmpProxyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 14, 1, 2, 1), ).setIndexNames((1, "SNMP-PROXY-MIB", "snmpProxyName"))
if mibBuilder.loadTexts: snmpProxyEntry.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntry.setDescription('A set of translation parameters used by a proxy forwarder\n         application for forwarding SNMP messages.\n\n         Entries in the snmpProxyTable are created and deleted\n         using the snmpProxyRowStatus object.')
snmpProxyName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: snmpProxyName.setStatus('current')
if mibBuilder.loadTexts: snmpProxyName.setDescription('The locally arbitrary, but unique identifier associated\n         with this snmpProxyEntry.')
snmpProxyType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("trap", 3), ("inform", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyType.setStatus('current')
if mibBuilder.loadTexts: snmpProxyType.setDescription('The type of message that may be forwarded using\n         the translation parameters defined by this entry.')
snmpProxyContextEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 3), SnmpEngineID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextEngineID.setStatus('current')
if mibBuilder.loadTexts: snmpProxyContextEngineID.setDescription('The contextEngineID contained in messages that\n         may be forwarded using the translation parameters\n         defined by this entry.')
snmpProxyContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextName.setStatus('current')
if mibBuilder.loadTexts: snmpProxyContextName.setDescription('The contextName contained in messages that may be\n         forwarded using the translation parameters defined\n         by this entry.\n\n         This object is optional, and if not supported, the\n         contextName contained in a message is ignored when\n         selecting an entry in the snmpProxyTable.')
snmpProxyTargetParamsIn = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyTargetParamsIn.setStatus('current')
if mibBuilder.loadTexts: snmpProxyTargetParamsIn.setDescription('This object selects an entry in the snmpTargetParamsTable.\n         The selected entry is used to determine which row of the\n         snmpProxyTable to use for forwarding received messages.')
snmpProxySingleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxySingleTargetOut.setStatus('current')
if mibBuilder.loadTexts: snmpProxySingleTargetOut.setDescription('This object selects a management target defined in the\n         snmpTargetAddrTable (in the SNMP-TARGET-MIB).  The\n         selected target is defined by an entry in the\n         snmpTargetAddrTable whose index value (snmpTargetAddrName)\n         is equal to this object.\n\n         This object is only used when selection of a single\n         target is required (i.e. when forwarding an incoming\n         read or write request).')
snmpProxyMultipleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 7), SnmpTagValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyMultipleTargetOut.setStatus('current')
if mibBuilder.loadTexts: snmpProxyMultipleTargetOut.setDescription('This object selects a set of management targets defined\n         in the snmpTargetAddrTable (in the SNMP-TARGET-MIB).\n\n         This object is only used when selection of multiple\n         targets is required (i.e. when forwarding an incoming\n         notification).')
snmpProxyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyStorageType.setStatus('current')
if mibBuilder.loadTexts: snmpProxyStorageType.setDescription("The storage type of this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
snmpProxyRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyRowStatus.setStatus('current')
if mibBuilder.loadTexts: snmpProxyRowStatus.setDescription('The status of this conceptual row.\n\n         To create a row in this table, a manager must\n\n         set this object to either createAndGo(4) or\n         createAndWait(5).\n\n         The following objects may not be modified while the\n         value of this object is active(1):\n             - snmpProxyType\n             - snmpProxyContextEngineID\n             - snmpProxyContextName\n             - snmpProxyTargetParamsIn\n             - snmpProxySingleTargetOut\n             - snmpProxyMultipleTargetOut')
snmpProxyCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 1))
snmpProxyGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 2))
snmpProxyCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 14, 3, 1, 1)).setObjects(("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"), ("SNMP-PROXY-MIB", "snmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyCompliance = snmpProxyCompliance.setStatus('current')
if mibBuilder.loadTexts: snmpProxyCompliance.setDescription('The compliance statement for SNMP entities which include\n         a proxy forwarding application.')
snmpProxyGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 14, 3, 2, 3)).setObjects(("SNMP-PROXY-MIB", "snmpProxyType"), ("SNMP-PROXY-MIB", "snmpProxyContextEngineID"), ("SNMP-PROXY-MIB", "snmpProxyContextName"), ("SNMP-PROXY-MIB", "snmpProxyTargetParamsIn"), ("SNMP-PROXY-MIB", "snmpProxySingleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyMultipleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyStorageType"), ("SNMP-PROXY-MIB", "snmpProxyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyGroup = snmpProxyGroup.setStatus('current')
if mibBuilder.loadTexts: snmpProxyGroup.setDescription('A collection of objects providing remote configuration of\n         management target translation parameters for use by\n         proxy forwarder applications.')
mibBuilder.exportSymbols("SNMP-PROXY-MIB", snmpProxyCompliance=snmpProxyCompliance, snmpProxyGroup=snmpProxyGroup, snmpProxySingleTargetOut=snmpProxySingleTargetOut, snmpProxyType=snmpProxyType, snmpProxyMultipleTargetOut=snmpProxyMultipleTargetOut, snmpProxyGroups=snmpProxyGroups, snmpProxyTable=snmpProxyTable, snmpProxyTargetParamsIn=snmpProxyTargetParamsIn, snmpProxyCompliances=snmpProxyCompliances, snmpProxyConformance=snmpProxyConformance, snmpProxyMIB=snmpProxyMIB, snmpProxyEntry=snmpProxyEntry, snmpProxyObjects=snmpProxyObjects, PYSNMP_MODULE_ID=snmpProxyMIB, snmpProxyRowStatus=snmpProxyRowStatus, snmpProxyName=snmpProxyName, snmpProxyStorageType=snmpProxyStorageType, snmpProxyContextName=snmpProxyContextName, snmpProxyContextEngineID=snmpProxyContextEngineID)
