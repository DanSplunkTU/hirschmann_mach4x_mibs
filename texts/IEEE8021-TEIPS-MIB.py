#
# PySNMP MIB module IEEE8021-TEIPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-TEIPS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:30:43 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ieee8021BridgeBaseComponentId, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId")
IEEE8021PbbTeTSidId, ieee802dot1mibs, IEEE8021BridgePortNumber, IEEE8021TeipsIpgid, IEEE8021TeipsIpgConfigAdmin, IEEE8021TeipsIpgConfigActiveRequests = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PbbTeTSidId", "ieee802dot1mibs", "IEEE8021BridgePortNumber", "IEEE8021TeipsIpgid", "IEEE8021TeipsIpgConfigAdmin", "IEEE8021TeipsIpgConfigActiveRequests")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Unsigned32, TimeTicks, iso, ObjectIdentity, Bits, NotificationType, Integer32, Counter32, Counter64, IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity", "Bits", "NotificationType", "Integer32", "Counter32", "Counter64", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, DisplayString, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention", "StorageType")
ieee8021TeipsMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 24))
ieee8021TeipsMib.setRevisions(('2011-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021TeipsMib.setRevisionsDescriptions(('Version 1 of the TEIPS MIB module based upon IEEE 802.1Qbf',))
if mibBuilder.loadTexts: ieee8021TeipsMib.setLastUpdated('201108170000Z')
if mibBuilder.loadTexts: ieee8021TeipsMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021TeipsMib.setContactInfo('WG-URL:   http://grouper.ieee.org/groups/802/1/index.html\n        WG-EMail: stds-802-1@ieee.org \n        Contact:  Bob Sultan\n                  c/o Tony Jeffree, IEEE 802.1 Working Group Chair\n        Postal:   IEEE Standards Board\n                  445 Hoes Lane\n                  P.O. Box 1331\n                  Piscataway, NJ 08855-1331\n                  USA\n        E-mail:   tony@jeffree.co.uk\n       ')
if mibBuilder.loadTexts: ieee8021TeipsMib.setDescription('Copyright (C) IEEE.  All Rights Reserved\n        This MIB module is part of IEEE 802.1Q;\n        See the IEEE 802.1Q standard for full legal notices.\n\n        Unless otherwise indicated, the references in this\n        MIB module are to IEEE 802.1Q-2011 as amended by\n        the following standards:\n              IEEE 802.1az\n              IEEE 802.1bb\n              IEEE 802.1bc\n              IEEE 802.1be')
ieee8021TeipsNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 0))
ieee8021TeipsObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 1))
ieee8021TeipsConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2))
ieee8021TeipsIpgTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 1), )
if mibBuilder.loadTexts: ieee8021TeipsIpgTable.setReference('12.20.1')
if mibBuilder.loadTexts: ieee8021TeipsIpgTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgTable.setDescription('The IPG table.  Each entry in this table corresponds to an\n        Infrastructure Protection Group (IPG) associated with a PBB\n        supporting Infrastructure Protection Switching (IPS).')
ieee8021TeipsIpgEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"))
if mibBuilder.loadTexts: ieee8021TeipsIpgEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgEntry.setDescription('The IPG table entry.')
ieee8021TeipsIpgid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 1), IEEE8021TeipsIpgid())
if mibBuilder.loadTexts: ieee8021TeipsIpgid.setReference('12.20.1.1.3 a')
if mibBuilder.loadTexts: ieee8021TeipsIpgid.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgid.setDescription('Uniquely identifies an IPG within the PBB.')
ieee8021TeipsIpgWorkingMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingMA.setReference('12.20.1.1.3 b)')
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingMA.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingMA.setDescription("Identifies the Segment MA that corresponds to\n        the IPG's working entity.  The MA index in\n        this column must hold a value that is the\n        value of dot1agCfmStackMaIndex column for\n        some entry in the dot1agCfmStackTable before\n        the RowStatus for this row can be set to\n        Active.  Furthermore, this column may not be\n        modified when the RowStatus for this row is\n        Active.")
ieee8021TeipsIpgProtectionMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionMA.setReference('12.20.1.1.3 c)')
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionMA.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionMA.setDescription("Identifies the Segment MA that corresponds to the\n        IPG's protection entity.  The MA index in this\n        column must hold a value that is the value of\n        dot1agCfmStackMaIndex column for some entry in\n        the dot1agCfmStackTable before the RowStatus\n        for this row can be set to Active.  Furthermore,\n        this column may not be modified when the\n        RowStatus for this row is Active.")
ieee8021TeipsIpgWorkingPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 4), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingPortNumber.setReference('12.20.2.1.3 b)')
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingPortNumber.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingPortNumber.setDescription('Identifies the local Port associated with the\n        IPG Working Segment.')
ieee8021TeipsIpgProtectionPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 5), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionPortNumber.setReference('12.20.2.1.3 c)')
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionPortNumber.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionPortNumber.setDescription('Identifies the local Port associated with the\n        IPG Protection Segment.')
ieee8021TeipsIpgStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgStorageType.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgStorageType.setDescription('This object indicates the persistence of this\n        entry. All read-create columns must be\n        writable if this column is set to permanent.')
ieee8021TeipsIpgRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgRowStatus.setReference('12.20.1.2')
if mibBuilder.loadTexts: ieee8021TeipsIpgRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgRowStatus.setDescription('The status of this row.\n        The writable columns in a row cannot be\n        changed if the row is active.  The\n        TeipsIpgWorkingMA and TeipsIpgProtectionMA\n        columns must be specified before the row\n        can be activated.')
ieee8021TeipsTesiTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 2), )
if mibBuilder.loadTexts: ieee8021TeipsTesiTable.setReference('12.20.2.1.3 e)')
if mibBuilder.loadTexts: ieee8021TeipsTesiTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiTable.setDescription('The IPG TE-SID table contains identifies\n         the TE service instances associated with\n         an IPG.')
ieee8021TeipsTesiEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1), ).setIndexNames((0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiIndex"))
if mibBuilder.loadTexts: ieee8021TeipsTesiEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiEntry.setDescription('The TE-IPS TESI entry.  Each entry identifies\n         a TESI associated with an IPG.')
ieee8021TeipsTesiIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021TeipsTesiIndex.setReference('12.20.2.1.3 e')
if mibBuilder.loadTexts: ieee8021TeipsTesiIndex.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiIndex.setDescription('This is an identifier, of local signifigance to a\n         particular PBB-TE TE-SID associated with an IPG.')
ieee8021TeipsTesiId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 2), IEEE8021PbbTeTSidId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiId.setReference('12.20.2.1.3 e')
if mibBuilder.loadTexts: ieee8021TeipsTesiId.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiId.setDescription('This column holds the TESI identifier corresponding\n         to a TE service instance associated with an IPG.')
ieee8021TeipsTesiStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiStorageType.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiStorageType.setDescription('This object indicates the persistence of this\n        entry. All read-create columns must be\n        writable for permanent rows.')
ieee8021TeipsTesiRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsTesiRowStatus.setDescription('This column holds the status for this row.\n         When the status is active, no columns of\n         this table may be modified.  All columns\n         must have a valid value before the row\n         can be activated.')
ieee8021TeipsCandidatePsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 3), )
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsTable.setReference('12.20.2.1.3 d)')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsTable.setDescription('The Candidate PS table lists, in priority order,\n         from highest priority to lowest priority, the\n         Maintenance Associations corresponding to\n         candidate Protection Segments associated with\n         an IPG.')
ieee8021TeipsCandidatePsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1), ).setIndexNames((0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsIndex"))
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsEntry.setDescription('A Candidate PS entry.  Each entry identifies a\n         candidate Protection Segment associated with an IPG.')
ieee8021TeipsCandidatePsIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsIndex.setReference('12.20.2.1.3 d)')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsIndex.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsIndex.setDescription('This is an identifier, of local signifigance\n         to a particular candidate Protection Segment\n         associated with an IPG.')
ieee8021TeipsCandidatePsMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsMA.setReference('12.20.2.1.3 d)')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsMA.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsMA.setDescription('This column holds the candidate Protection\n         Segment MA corresponding to a candidate\n         Protection Segment associated with an IPG.')
ieee8021TeipsCandidatePsPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 3), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsPort.setReference('12.20.2.1.3 d)')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsPort.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsPort.setDescription('This column holds the Port Number\n         corresponding to the candidate Protection\n         Segment associated with an IPG.')
ieee8021TeipsCandidatePsOper = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsOper.setReference('12.20.2.1.3 d)')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsOper.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsOper.setDescription('This column indicates whether or not\n         the candidate Protection Segment is\n         operational.')
ieee8021TeipsCandidatePsStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsStorageType.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsStorageType.setDescription('This object indicates the persistence\n        of this entry. All read-create\n        columns must be writable for permanent rows.')
ieee8021TeipsCandidatePsRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsRowStatus.setDescription('This column holds the status for this row.\n         When the status is active, no columns\n         of this table may be modified.  All\n         columns must have a valid value before the row\n         can be activated.')
ieee8021TeipsIpgConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 4), )
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigTable.setReference('12.20.2.1.3 f,g,h,i,j,k)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigTable.setDescription('The PBB-TE IPS IPG config table contains\n         configuration and status information for\n         each IPG configured in the system.\n         Entries in this table are created implicitly\n         by the creation of entries in the\n         ieee8021TeipsIpgTable.')
ieee8021TeipsIpgConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"))
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigEntry.setDescription('The IPG confguration table entry.  Rows are\n         created in this table implicitly when a row\n         is added to the ieee8021TeipsIpgTable.')
ieee8021TeipsIpgConfigState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("workingSegment", 1), ("protectionSegment", 2), ("waitToRestore", 3), ("protAdmin", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigState.setReference('12.20.2.1.3 f)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigState.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigState.setDescription('This column indicates the current state of the\n         protection switching state machine for an IPG. \n         The value can be one of the following:\n\n        workingSegment(1)    The protection switching state machine\n                             is in the WORKING_PATH state.\n        protectionSegment(2) The protection switching state machine\n                             is in the PROTECTION_PATH state.\n        waitToRestore(3)     The protection switching state machine\n                             is in the WTR state.\n        protAdmin(4)         The protection switching state machine\n                             is in the PROT_ADMIN state.')
ieee8021TeipsIpgConfigCommandStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 2), IEEE8021TeipsIpgConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandStatus.setReference('12.20.2.1.3 f)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandStatus.setDescription('This column indicates the status of\n         administrative commands within the\n         protection group.  It reflects the current\n         operational administrative command being\n         acted upon by the IPG.')
ieee8021TeipsIpgConfigCommandLast = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 3), IEEE8021TeipsIpgConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandLast.setReference('12.20.2.1.3 f)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandLast.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandLast.setDescription('This column indicates the last attempted administrative\n         command applied to the IPG.  It is changed\n         whenever a write is made to the CommandAdmin column of\n         this table and is essentially record of the last attempted\n         administrative operation.')
ieee8021TeipsIpgConfigCommandAdmin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 4), IEEE8021TeipsIpgConfigAdmin().clone('clear')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandAdmin.setReference('12.20.2.1.3 f')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandAdmin.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandAdmin.setDescription('This column is used by the operator to request\n        that the IPG state machine perform some\n        administrative operation.  The operator requests\n        a command by writing the command value to this\n        column.  The state machine indicates the command\n        that it is performing by setting the value of the\n        CommandStatus column of this table.  This column\n        always reads back as clear(1).')
ieee8021TeipsIpgConfigActiveRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 5), IEEE8021TeipsIpgConfigActiveRequests()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigActiveRequests.setReference('12.20.2.1.3 f)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigActiveRequests.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigActiveRequests.setDescription('This column shows the status of active requests\n         associated with the IPG.')
ieee8021TeipsIpgConfigWTR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigWTR.setReference('12.20.2.1.3 h)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigWTR.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigWTR.setDescription('This column is used to configure the\n         wait-to-restore timer for the IPG operation.\n         The timer may be configured in steps of 1 minute\n         between 5 and 12 minutes, the default being 5.\n         Additionally, the value 0 is used to indicate\n         that the IPG is to operate non-revertively.  The\n         value 0 is not permitted if the IPG is configured\n         for M:1 IPS operation.')
ieee8021TeipsIpgConfigHoldOff = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('deciseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigHoldOff.setReference('12.20.2.1.3 i)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigHoldOff.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigHoldOff.setDescription('This column is used to configure the hold off\n        timer.  The purpose is to allow IPS to fix the problem\n        before a higher-layer mechanism, such as PBB-TE TESI\n        protection, is invoked or to allow an inner IPG to fix \n        the problem before IPS is invoked by the outer IPG when \n        IPGs are nested.  The hold off timer has a period of\n        from 0 to 10 seconds, the default being 0, with a 100ms\n        granularity.')
ieee8021TeipsIpgM1ConfigState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("psAssigned", 1), ("segmentOk", 2), ("segmentFailed", 3), ("assignNewPs", 4), ("revertToBetterPs", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgM1ConfigState.setReference('12.20.2.1.3 j)')
if mibBuilder.loadTexts: ieee8021TeipsIpgM1ConfigState.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgM1ConfigState.setDescription('This column indicates the current state of the M:1 protection\n         switching state machine for an IPG if M:1 IPS is supported.\n         The value can be one of the following:\n\n        psAssigned(1)        The protection switching state machine\n                             is in the PS_ASSIGNED state.\n        segmentOk(2)         The protection switching state machine\n                             is in the SEGMENT_OK state.\n        segmentFailed(3)     The protection switching state machine\n                             is in the SEGMENT_FAILED state.\n        assignNewPs(4)       The protection switching state machine\n                             is in the ASSIGN_NEW_PS state. \n        revertToBetterPs(5)  The protection switching state machine\n                             is in the REVERT_T0_BETTER_PS state.')
ieee8021TeipsIpgConfigMWTR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 9), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigMWTR.setReference('12.20.2.1.3 k)')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigMWTR.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigMWTR.setDescription('This column is used to configure the M:1 wait-to-restore\n         timer for the IPG operation if M:1 protection is\n         supported.  The timer may be configured in steps of\n         1 minute between 5 and 12 minutes, the default being 5.\n         Additionally, the value 0 is used to indicate that the\n         IPG is to operate non-revertively.')
ieee8021TeipsIpgConfigNotifyEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigNotifyEnable.setDescription('This column is used to enable or disable transmission\n         of ieee8021TeipsIpgAdminFailure notifications.\n         These notifications are generated whenever an\n         administrative command cannot be performed by the IPG.')
ieee8021TeipsIpgConfigStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigStorageType.setDescription('This object indicates the persistence of this entry. For\n        permanent objects the ieee8021TeipsIpgConfigCommandAdmin\n        column must be writable.')
ieee8021TeipsIpgAdminFailure = NotificationType((1, 3, 111, 2, 802, 1, 1, 24, 0, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"))
if mibBuilder.loadTexts: ieee8021TeipsIpgAdminFailure.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgAdminFailure.setDescription('An IPG generates this notification whenever\n         an adminisistrative command cannot be\n         executed by the IPS state machine.  For\n         example, when a requested  manual switch\n         cannot be performed because of a signal\n         failure condition.\n\n         The management entity receiving the\n         notification can identify\n         the system from the network source\n         address of the notification and can\n         identify the IPG by the indices of \n         the OID of the ieee8021TeipsIpgConfigState\n         variable in the notification:\n               \n         ieee8021BridgeBaseComponentId - Identifies\n         the  component on the bridge where the\n         protection group is configured.\n\n         ieee8021TeipsIpgid - The ID of the protection group.\n        ')
ieee8021TeipsCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2, 1))
ieee8021TeipsGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2, 2))
ieee8021TeipsIpgGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingPortNumber"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionPortNumber"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgGroup = ieee8021TeipsIpgGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgGroup.setDescription('Objects for the IPG group.')
ieee8021TeipsCandidatePsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 2)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsPort"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsOper"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsCandidatePsGroup = ieee8021TeipsCandidatePsGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsGroup.setDescription('Objects for the Candidate PS group.')
ieee8021TeipsIpgTesiGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 3)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiId"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgTesiGroup = ieee8021TeipsIpgTesiGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgTesiGroup.setDescription('Objects for the IPG Tuple group.')
ieee8021TeipsIpgConfigManGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 4)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandAdmin"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigActiveRequests"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigNotifyEnable"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgConfigManGroup = ieee8021TeipsIpgConfigManGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigManGroup.setDescription('Mandatory objects for the TeipsConfiguration group.')
ieee8021TeipsIpgConfigOptGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 5)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigWTR"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigMWTR"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgM1ConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigHoldOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgConfigOptGroup = ieee8021TeipsIpgConfigOptGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigOptGroup.setDescription('Optional 0bjects for the TeipsConfiguration group.')
ieee8021TeipsNotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 6)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgAdminFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsNotificationsGroup = ieee8021TeipsNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsNotificationsGroup.setDescription('Objects for the notifications group.')
ieee8021TeipsCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgTesiGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigManGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsNotificationsGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigOptGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsCompliance = ieee8021TeipsCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021TeipsCompliance.setDescription('The compliance statement for support\n         of the TEIPS MIB module.')
mibBuilder.exportSymbols("IEEE8021-TEIPS-MIB", ieee8021TeipsCandidatePsIndex=ieee8021TeipsCandidatePsIndex, ieee8021TeipsTesiTable=ieee8021TeipsTesiTable, ieee8021TeipsIpgConfigWTR=ieee8021TeipsIpgConfigWTR, ieee8021TeipsIpgConfigActiveRequests=ieee8021TeipsIpgConfigActiveRequests, ieee8021TeipsTesiEntry=ieee8021TeipsTesiEntry, ieee8021TeipsIpgWorkingPortNumber=ieee8021TeipsIpgWorkingPortNumber, ieee8021TeipsCandidatePsStorageType=ieee8021TeipsCandidatePsStorageType, ieee8021TeipsIpgTesiGroup=ieee8021TeipsIpgTesiGroup, ieee8021TeipsCandidatePsRowStatus=ieee8021TeipsCandidatePsRowStatus, ieee8021TeipsIpgConfigCommandStatus=ieee8021TeipsIpgConfigCommandStatus, ieee8021TeipsCompliances=ieee8021TeipsCompliances, ieee8021TeipsIpgConfigCommandLast=ieee8021TeipsIpgConfigCommandLast, ieee8021TeipsIpgConfigOptGroup=ieee8021TeipsIpgConfigOptGroup, ieee8021TeipsCandidatePsPort=ieee8021TeipsCandidatePsPort, ieee8021TeipsMib=ieee8021TeipsMib, ieee8021TeipsIpgProtectionMA=ieee8021TeipsIpgProtectionMA, ieee8021TeipsNotificationsGroup=ieee8021TeipsNotificationsGroup, ieee8021TeipsIpgConfigManGroup=ieee8021TeipsIpgConfigManGroup, ieee8021TeipsObjects=ieee8021TeipsObjects, ieee8021TeipsCandidatePsOper=ieee8021TeipsCandidatePsOper, ieee8021TeipsCandidatePsEntry=ieee8021TeipsCandidatePsEntry, ieee8021TeipsConformance=ieee8021TeipsConformance, ieee8021TeipsIpgStorageType=ieee8021TeipsIpgStorageType, ieee8021TeipsIpgWorkingMA=ieee8021TeipsIpgWorkingMA, ieee8021TeipsIpgEntry=ieee8021TeipsIpgEntry, ieee8021TeipsIpgConfigState=ieee8021TeipsIpgConfigState, ieee8021TeipsIpgConfigNotifyEnable=ieee8021TeipsIpgConfigNotifyEnable, ieee8021TeipsGroups=ieee8021TeipsGroups, ieee8021TeipsCandidatePsTable=ieee8021TeipsCandidatePsTable, ieee8021TeipsIpgid=ieee8021TeipsIpgid, ieee8021TeipsIpgGroup=ieee8021TeipsIpgGroup, ieee8021TeipsIpgM1ConfigState=ieee8021TeipsIpgM1ConfigState, ieee8021TeipsIpgAdminFailure=ieee8021TeipsIpgAdminFailure, ieee8021TeipsIpgConfigMWTR=ieee8021TeipsIpgConfigMWTR, ieee8021TeipsTesiRowStatus=ieee8021TeipsTesiRowStatus, ieee8021TeipsCandidatePsMA=ieee8021TeipsCandidatePsMA, ieee8021TeipsIpgProtectionPortNumber=ieee8021TeipsIpgProtectionPortNumber, ieee8021TeipsTesiId=ieee8021TeipsTesiId, ieee8021TeipsIpgConfigEntry=ieee8021TeipsIpgConfigEntry, ieee8021TeipsIpgConfigCommandAdmin=ieee8021TeipsIpgConfigCommandAdmin, ieee8021TeipsIpgConfigStorageType=ieee8021TeipsIpgConfigStorageType, ieee8021TeipsCandidatePsGroup=ieee8021TeipsCandidatePsGroup, ieee8021TeipsIpgConfigHoldOff=ieee8021TeipsIpgConfigHoldOff, ieee8021TeipsCompliance=ieee8021TeipsCompliance, ieee8021TeipsTesiIndex=ieee8021TeipsTesiIndex, ieee8021TeipsTesiStorageType=ieee8021TeipsTesiStorageType, ieee8021TeipsIpgConfigTable=ieee8021TeipsIpgConfigTable, ieee8021TeipsIpgTable=ieee8021TeipsIpgTable, ieee8021TeipsNotifications=ieee8021TeipsNotifications, PYSNMP_MODULE_ID=ieee8021TeipsMib, ieee8021TeipsIpgRowStatus=ieee8021TeipsIpgRowStatus)
