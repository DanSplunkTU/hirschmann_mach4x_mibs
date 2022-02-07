#
# PySNMP MIB module EQLAGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLAGENT-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:02 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, enterprises, Counter32, IpAddress, MibIdentifier, ModuleIdentity, Bits, TimeTicks, Gauge32, iso, ObjectIdentity, Unsigned32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "enterprises", "Counter32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Bits", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
eqlAgentModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 12))
eqlAgentModule.setRevisions(('2002-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlAgentModule.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: eqlAgentModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlAgentModule.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlAgentModule.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762             \n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlAgentModule.setDescription('Equallogic Inc. Storage Array extended error mib\n\n         Copyright (c) 2003-2009 by Dell, Inc.\n\n         All rights reserved.  This software may not be copied, disclosed,\n         transferred, or used except in accordance with a license granted\n         by Dell, Inc.  This software embodies proprietary information\n         and trade secrets of Dell, Inc.\n        ')
eqlAgentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 1))
eqlAgentNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 2))
eqlAgentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 3))
eqlAgentInetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12, 4))
eqlExtErrorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1), )
if mibBuilder.loadTexts: eqlExtErrorTable.setStatus('current')
if mibBuilder.loadTexts: eqlExtErrorTable.setDescription('A conceptual table which associates extended error information with each \n\t\t\t\t\t\tSNMP operation that produced an error where such information is available')
eqlExtErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1), ).setIndexNames((0, "EQLAGENT-MIB", "eqlEntIpAddr"), (0, "EQLAGENT-MIB", "eqlSNMPrid"))
if mibBuilder.loadTexts: eqlExtErrorEntry.setStatus('current')
if mibBuilder.loadTexts: eqlExtErrorEntry.setDescription(' A sequence of extended error information for each SNMP operation producing \n\t\t\t\t\t\tan extended error')
eqlEntIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: eqlEntIpAddr.setStatus('current')
if mibBuilder.loadTexts: eqlEntIpAddr.setDescription('The IP address of the entity making the SNMP request')
eqlSNMPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPrid.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPrid.setDescription('The value of the request id of the SNMP PDU which resulted in the \n                      associated error.')
eqlSNMPExtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPExtErrCode.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPExtErrCode.setDescription('The value of the extended error code resulting from the SNMP PDU with the\n                     associated request id and source address')
eqlSNMPExtErrMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPExtErrMsg.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPExtErrMsg.setDescription('The human-readable, meaningful error message that is associated with the\n                  extended error code. In most cases, this will be identical to the string \n                  that appeared on the management console after the error occurred')
eqlExtInetErrorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4), )
if mibBuilder.loadTexts: eqlExtInetErrorTable.setStatus('current')
if mibBuilder.loadTexts: eqlExtInetErrorTable.setDescription('A conceptual table which associates extended error information with each \n\t\t\t\t\t\tSNMP operation that produced an error where such information is available')
eqlExtInetErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1), ).setIndexNames((0, "EQLAGENT-MIB", "eqlEntInetAddrType"), (0, "EQLAGENT-MIB", "eqlEntInetAddr"), (0, "EQLAGENT-MIB", "eqlSNMPInetrid"))
if mibBuilder.loadTexts: eqlExtInetErrorEntry.setStatus('current')
if mibBuilder.loadTexts: eqlExtInetErrorEntry.setDescription('A sequence of extended error information for each SNMP operation producing \n\t\t\t\t\t\tan extended error')
eqlEntInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: eqlEntInetAddrType.setStatus('current')
if mibBuilder.loadTexts: eqlEntInetAddrType.setDescription('The IP address of the entity making the SNMP request')
eqlEntInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: eqlEntInetAddr.setStatus('current')
if mibBuilder.loadTexts: eqlEntInetAddr.setDescription('The IP address of the entity making the SNMP request')
eqlSNMPInetrid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetrid.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPInetrid.setDescription('The value of the request id of the SNMP PDU which resulted in the \n\t\t\t\t\t\tassociated error.')
eqlSNMPInetExtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetExtErrCode.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPInetExtErrCode.setDescription('The value of the extended error code resulting from the SNMP PDU with the\n\t\t\t\t\t\tassociated request id and source address.')
eqlSNMPInetExtErrMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSNMPInetExtErrMsg.setStatus('current')
if mibBuilder.loadTexts: eqlSNMPInetExtErrMsg.setDescription('The human-readable, meaningful error message that is associated with the\n\t\t\t\t\t\textended error code. In most cases, this will be identical to the string \n\t\t\t\t\t\tthat appeared on the management console after the error occurred.')
mibBuilder.exportSymbols("EQLAGENT-MIB", eqlAgentConformance=eqlAgentConformance, eqlExtInetErrorEntry=eqlExtInetErrorEntry, eqlExtInetErrorTable=eqlExtInetErrorTable, eqlEntInetAddr=eqlEntInetAddr, eqlSNMPInetrid=eqlSNMPInetrid, eqlSNMPExtErrCode=eqlSNMPExtErrCode, eqlAgentInetObjects=eqlAgentInetObjects, eqlAgentNotifications=eqlAgentNotifications, eqlExtErrorEntry=eqlExtErrorEntry, eqlSNMPInetExtErrCode=eqlSNMPInetExtErrCode, eqlSNMPrid=eqlSNMPrid, eqlAgentModule=eqlAgentModule, eqlSNMPInetExtErrMsg=eqlSNMPInetExtErrMsg, eqlSNMPExtErrMsg=eqlSNMPExtErrMsg, eqlEntIpAddr=eqlEntIpAddr, PYSNMP_MODULE_ID=eqlAgentModule, eqlExtErrorTable=eqlExtErrorTable, eqlEntInetAddrType=eqlEntInetAddrType, eqlAgentObjects=eqlAgentObjects)
