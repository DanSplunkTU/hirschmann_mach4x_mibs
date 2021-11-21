#
# PySNMP MIB module EQLREPLPARTNER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLREPLPARTNER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:36:40 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eqliscsiVolumeReplSiteIndex, SiteIndex = mibBuilder.importSymbols("EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex", "SiteIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Integer32, TimeTicks, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter32, Counter64, enterprises, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter32", "Counter64", "enterprises", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
eqlReplPartnerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 26))
eqlReplPartnerModule.setRevisions(('2013-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlReplPartnerModule.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: eqlReplPartnerModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlReplPartnerModule.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlReplPartnerModule.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762\n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlReplPartnerModule.setDescription('Replication Partner information \n\n        Copyright (c) 2013 by Dell Inc. \n        \n        All rights reserved.  This software may not be copied, disclosed, \n        transferred, or used except in accordance with a license granted \n        by Dell Inc.  This software embodies proprietary information \n        and trade secrets of Dell Inc. \n        ')
eqlReplPartnerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 26, 1))
eqlReplPartnerTestTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1), )
if mibBuilder.loadTexts: eqlReplPartnerTestTable.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestTable.setDescription('EqualLogic-Persistent ReplPartnerTestTable.\n                     This table contains replication partner test information.\n                     TimeoutCreate:60 TimeoutDelete:60')
eqlReplPartnerTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"))
if mibBuilder.loadTexts: eqlReplPartnerTestEntry.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestEntry.setDescription('An entry (row) containing replication partner test info.')
class EqlReplPartnerTestStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("valid", 1), ("invalid", 2), ("remote-partner-not-configured", 3))

eqlReplPartnerTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlReplPartnerTestRowStatus.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestRowStatus.setDescription('The row status.')
eqlReplPartnerTestIPAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 2), EqlReplPartnerTestStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlReplPartnerTestIPAddrStatus.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestIPAddrStatus.setDescription('The replication partner IP address test status.')
eqlReplPartnerTestAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 3), EqlReplPartnerTestStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlReplPartnerTestAuthStatus.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestAuthStatus.setDescription('The replication partner authentication test status.')
eqlReplPartnerTestAction = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("start", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlReplPartnerTestAction.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestAction.setDescription('The replication partner test action.')
eqlReplPartnerTestState = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("in-progress", 1), ("complete", 2), ("error", 3), ("restarted", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlReplPartnerTestState.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestState.setDescription('The replication partner test state.')
eqlReplPartnerTestMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestMajorVersion.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestMajorVersion.setDescription('This field specifies the Major part of \n                     the lowest member software version of the \n                     remote replication site group.')
eqlReplPartnerTestMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestMinorVersion.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestMinorVersion.setDescription('This field specifies the Minor part of \n                     the lowest member software version of the \n                     remote replication site group.')
eqlReplPartnerTestMaintVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestMaintVersion.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestMaintVersion.setDescription('This field specifies the Maintenance part of \n                     the lowest member software version of the \n                     remote replication site group.')
eqlReplPartnerTestDelegatedSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestDelegatedSpace.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestDelegatedSpace.setDescription('This field indicates the total delegated space for the partners.\n                     This is a dynamic value, it is not Administrator setable.')
eqlReplPartnerTestDelegatedSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestDelegatedSpaceUsed.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestDelegatedSpaceUsed.setDescription('This field indicates the total delegated space used by partners.\n                     This is a dynamic value, it is not Administrator setable.')
eqlReplPartnerTestTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlReplPartnerTestTimestamp.setStatus('current')
if mibBuilder.loadTexts: eqlReplPartnerTestTimestamp.setDescription('This field specifies the date/time when replication partner test was started.\n                     Time is represented as the time in seconds since 00:00:00 UTC, 1970-01-01.')
mibBuilder.exportSymbols("EQLREPLPARTNER-MIB", eqlReplPartnerTestEntry=eqlReplPartnerTestEntry, eqlReplPartnerTestIPAddrStatus=eqlReplPartnerTestIPAddrStatus, eqlReplPartnerTestAuthStatus=eqlReplPartnerTestAuthStatus, eqlReplPartnerTestState=eqlReplPartnerTestState, eqlReplPartnerTestMajorVersion=eqlReplPartnerTestMajorVersion, eqlReplPartnerTestDelegatedSpace=eqlReplPartnerTestDelegatedSpace, eqlReplPartnerTestTable=eqlReplPartnerTestTable, eqlReplPartnerTestMaintVersion=eqlReplPartnerTestMaintVersion, eqlReplPartnerObjects=eqlReplPartnerObjects, eqlReplPartnerTestAction=eqlReplPartnerTestAction, PYSNMP_MODULE_ID=eqlReplPartnerModule, eqlReplPartnerModule=eqlReplPartnerModule, eqlReplPartnerTestDelegatedSpaceUsed=eqlReplPartnerTestDelegatedSpaceUsed, eqlReplPartnerTestRowStatus=eqlReplPartnerTestRowStatus, eqlReplPartnerTestTimestamp=eqlReplPartnerTestTimestamp, EqlReplPartnerTestStatus=EqlReplPartnerTestStatus, eqlReplPartnerTestMinorVersion=eqlReplPartnerTestMinorVersion)
