#
# PySNMP MIB module BENU-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-VLAN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:50:41 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Unsigned32, Gauge32, Integer32, ModuleIdentity, ObjectIdentity, IpAddress, NotificationType, Bits, iso, MibIdentifier, Counter64, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "iso", "MibIdentifier", "Counter64", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bVLANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8))
bVLANMIB.setRevisions(('2015-05-07 00:00', '2015-04-14 00:00', '2015-01-06 00:00', '2014-11-17 00:00', '2014-08-04 00:00', '2014-06-24 00:00', '2014-05-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bVLANMIB.setRevisionsDescriptions(('Added bWagVlanTotalBytesRcvd and bWagVlanTotalBytesSent\n                 columns in bWagVlanStatsTable', 'Updated MIB file with change in bVlanCurrentNumber Syntax', 'VLAN object-types and notification-types separated.', 'updated MIB file with change in bVLANNotifObjects', 'updated MIB file with correct revision and descriptions.', 'Added VLAN information per port Table', 'This version introduces support for VLAN',))
if mibBuilder.loadTexts: bVLANMIB.setLastUpdated('201505070000Z')
if mibBuilder.loadTexts: bVLANMIB.setOrganization('Benu Networks')
if mibBuilder.loadTexts: bVLANMIB.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: bVLANMIB.setDescription('This MIB module defines VLAN statistics.\n        Copyright (C) 2014 by Benu Networks, Inc.\n        All rights reserved.')
bVLANMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1))
if mibBuilder.loadTexts: bVLANMIBObjects.setStatus('current')
if mibBuilder.loadTexts: bVLANMIBObjects.setDescription('MIB objects for VLAN utilization statistics are defined in this branch.')
bVLANNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0))
if mibBuilder.loadTexts: bVLANNotifObjects.setStatus('current')
if mibBuilder.loadTexts: bVLANNotifObjects.setDescription('Notifications of VLAN utilization statistics are defined in this branch.')
bVLANNotifVariables = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2))
if mibBuilder.loadTexts: bVLANNotifVariables.setStatus('current')
if mibBuilder.loadTexts: bVLANNotifVariables.setDescription('MIB objects for VLAN notifications are defined in this branch.')
bVlanTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1), )
if mibBuilder.loadTexts: bVlanTable.setStatus('current')
if mibBuilder.loadTexts: bVlanTable.setDescription('The table of VLAN utilization performance metrics\n         of each interface.')
bVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1), ).setIndexNames((0, "BENU-VLAN-MIB", "bVlanPortIndex"), (0, "BENU-VLAN-MIB", "bVlanIndex"))
if mibBuilder.loadTexts: bVlanEntry.setStatus('current')
if mibBuilder.loadTexts: bVlanEntry.setDescription('An entry containing VLAN utilization performance metrics\n         for each interface.')
bVlanPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bVlanPortIndex.setStatus('current')
if mibBuilder.loadTexts: bVlanPortIndex.setDescription("The index value that uniquely identifies the interface to which this\n        entry is applicable. The interface identified by a particular value of this\n        index is the same interface as identified by the same value of the\n        IF-MIB's ifIndex.")
bVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: bVlanIndex.setStatus('current')
if mibBuilder.loadTexts: bVlanIndex.setDescription('VLAN id configued on port.')
bVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanName.setStatus('current')
if mibBuilder.loadTexts: bVlanName.setDescription('VLAN name configured on port')
bVlanMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanMTU.setStatus('current')
if mibBuilder.loadTexts: bVlanMTU.setDescription('VLAN MTU configured on port')
bVlanEncapName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanEncapName.setStatus('current')
if mibBuilder.loadTexts: bVlanEncapName.setDescription('VLAN encapsulation name configured on port')
bVlanAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanAdminStatus.setStatus('current')
if mibBuilder.loadTexts: bVlanAdminStatus.setDescription('The desired state of the interface.  When a\n            managed system initializes, all interfaces start with\n            bVlanAdminStatus in the down(2) state.  As a result of either\n            explicit management action or per configuration information\n            retained by the managed system, bVlanAdminStatus is then\n            changed to up(1) state (or remains\n            in the down(2) state).')
bVlanOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanOperStatus.setStatus('current')
if mibBuilder.loadTexts: bVlanOperStatus.setDescription('The current operational state of the interface.  The\n            testing(3) state indicates that no operational packets can\n            be passed.  If bVlanAdminStatus is down(2) then bVlanOperStatus\n            should be down(2).  If bVlanAdminStatus is changed to up(1)\n            then bVlanOperStatus should change to up(1) if the interface is\n            ready to transmit and receive network traffic; it should\n            change to dormant(5) if the interface is waiting for\n            external actions (such as a serial line waiting for an\n            incoming connection); it should remain in the down(2) state\n            if and only if there is a fault that prevents it from going\n            to the up(1) state; it should remain in the notPresent(6)\n            state if the interface has missing (typically, hardware)\n            components.')
bWagVlanTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2), )
if mibBuilder.loadTexts: bWagVlanTable.setStatus('current')
if mibBuilder.loadTexts: bWagVlanTable.setDescription('The table of VLAN utilization performance metrics\n         of each interface.')
bWagVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1), ).setIndexNames((0, "BENU-VLAN-MIB", "bWagVlanPortIndex"), (0, "BENU-VLAN-MIB", "bWagVlanIndex"))
if mibBuilder.loadTexts: bWagVlanEntry.setStatus('current')
if mibBuilder.loadTexts: bWagVlanEntry.setDescription('A logical row in bWagVlanTable')
bWagVlanPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bWagVlanPortIndex.setStatus('current')
if mibBuilder.loadTexts: bWagVlanPortIndex.setDescription("The index value that uniquely identifies the interface to which this\n       entry is applicable. The interface identified by a particular value of this\n       index is the same interface as identified by the same value of the IF-MIB's\n       ifIndex.")
bWagVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: bWagVlanIndex.setStatus('current')
if mibBuilder.loadTexts: bWagVlanIndex.setDescription('VLAN id of the port.')
bWagVlanSubscriberCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagVlanSubscriberCount.setStatus('current')
if mibBuilder.loadTexts: bWagVlanSubscriberCount.setDescription('Number of subscribers currently using this VLAN tunnel.')
bWagVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3), )
if mibBuilder.loadTexts: bWagVlanStatsTable.setStatus('current')
if mibBuilder.loadTexts: bWagVlanStatsTable.setDescription('The table of VLAN utilization performance metrics\n         of each interface.')
bWagVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1), ).setIndexNames((0, "BENU-VLAN-MIB", "bWagVlanStatsPortIndex"), (0, "BENU-VLAN-MIB", "bWagVlanStatsIndex"))
if mibBuilder.loadTexts: bWagVlanStatsEntry.setStatus('current')
if mibBuilder.loadTexts: bWagVlanStatsEntry.setDescription('An entry containing VLAN utilization performance metrics\n         for each interface.')
bWagVlanStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bWagVlanStatsPortIndex.setStatus('current')
if mibBuilder.loadTexts: bWagVlanStatsPortIndex.setDescription("The index value that uniquely identifies the interface to which this\n       entry is applicable. The interface identified by a particular value of this\n       index is the same interface as identified by the same value of the IF-MIB's\n       ifIndex.")
bWagVlanStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bWagVlanStatsIndex.setStatus('current')
if mibBuilder.loadTexts: bWagVlanStatsIndex.setDescription('VLAN id of the port.')
bWagVlanTotalPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagVlanTotalPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: bWagVlanTotalPktsRcvd.setDescription('Total number of packets received from this port.')
bWagVlanTotalPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagVlanTotalPktsSent.setStatus('current')
if mibBuilder.loadTexts: bWagVlanTotalPktsSent.setDescription('Total number of packets sent from this port.')
bWagVlanTotalBytesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagVlanTotalBytesRcvd.setStatus('current')
if mibBuilder.loadTexts: bWagVlanTotalBytesRcvd.setDescription('Total number of bytes received from this port.')
bWagVlanTotalBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagVlanTotalBytesSent.setStatus('current')
if mibBuilder.loadTexts: bWagVlanTotalBytesSent.setDescription('Total number of bytes sent from this port.')
bVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4), )
if mibBuilder.loadTexts: bVlanPortTable.setStatus('current')
if mibBuilder.loadTexts: bVlanPortTable.setDescription('The table of VLAN information per port.')
bVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1), ).setIndexNames((0, "BENU-VLAN-MIB", "bVlanPerPortIndex"))
if mibBuilder.loadTexts: bVlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: bVlanPortEntry.setDescription('An entry containing VLAN information per port')
bVlanPerPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: bVlanPerPortIndex.setStatus('current')
if mibBuilder.loadTexts: bVlanPerPortIndex.setDescription("The index value that uniquely identifies the interface to which this\n       entry is applicable. The interface identified by a particular value of this\n       index is the same interface as identified by the same value of the IF-MIB's\n       ifIndex.")
bVlanTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanTotal.setStatus('current')
if mibBuilder.loadTexts: bVlanTotal.setDescription("The total number of VLAN's created per port")
bVlanActive = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanActive.setStatus('current')
if mibBuilder.loadTexts: bVlanActive.setDescription('Number of VLANs created and active on this port.')
bVlanCurrentNumber = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanCurrentNumber.setStatus('current')
if mibBuilder.loadTexts: bVlanCurrentNumber.setDescription("Total number of VLAN's created and active at present")
bVlanAssocSub = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bVlanAssocSub.setStatus('current')
if mibBuilder.loadTexts: bVlanAssocSub.setDescription("Total number of VLAN's with associated subscribers")
bVlanPortId = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bVlanPortId.setStatus('current')
if mibBuilder.loadTexts: bVlanPortId.setDescription("The index value that uniquely identifies the interface to which this\n        entry is applicable. The interface identified by a particular value of this\n        index is the same interface as identified by the same value of the IF-MIB's\n        ifIndex.")
bVlanId = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bVlanId.setStatus('current')
if mibBuilder.loadTexts: bVlanId.setDescription('VLAN id configured on port.')
bVlanEncapEnable = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 1)).setObjects(("BENU-VLAN-MIB", "bVlanPortId"))
if mibBuilder.loadTexts: bVlanEncapEnable.setStatus('current')
if mibBuilder.loadTexts: bVlanEncapEnable.setDescription('A bVlanEncapEnable trap signifies that the SNMP entity, acting in\n            an agent role, has detected that encapsulation 802.1q is enabled \n            on the port')
bVlanEncapDisable = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 2)).setObjects(("BENU-VLAN-MIB", "bVlanPortId"))
if mibBuilder.loadTexts: bVlanEncapDisable.setStatus('current')
if mibBuilder.loadTexts: bVlanEncapDisable.setDescription('A bVlanEncapEnable trap signifies that the SNMP entity, acting in\n            an agent role, has detected that encapsulation 802.1q is disabled \n            on the port')
bVlanCreate = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 3)).setObjects(("BENU-VLAN-MIB", "bVlanPortId"), ("BENU-VLAN-MIB", "bVlanId"))
if mibBuilder.loadTexts: bVlanCreate.setStatus('current')
if mibBuilder.loadTexts: bVlanCreate.setDescription('A bVlanCreate trap signifies that the SNMP entity, acting in\n            an agent role, has detected that VLAN is created with \n            bVlanIndex')
bVlanDelete = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 4)).setObjects(("BENU-VLAN-MIB", "bVlanPortId"), ("BENU-VLAN-MIB", "bVlanId"))
if mibBuilder.loadTexts: bVlanDelete.setStatus('current')
if mibBuilder.loadTexts: bVlanDelete.setDescription('A bVlanDelete trap signifies that the SNMP entity, acting in\n            an agent role, has detected that VLAN is deleted with \n            bVlanIndex')
mibBuilder.exportSymbols("BENU-VLAN-MIB", bVlanTable=bVlanTable, bVlanPerPortIndex=bVlanPerPortIndex, bVlanActive=bVlanActive, bVlanId=bVlanId, bVlanEntry=bVlanEntry, bWagVlanIndex=bWagVlanIndex, bWagVlanStatsIndex=bWagVlanStatsIndex, bVlanEncapName=bVlanEncapName, bVlanPortEntry=bVlanPortEntry, bWagVlanEntry=bWagVlanEntry, bVlanMTU=bVlanMTU, bVlanEncapEnable=bVlanEncapEnable, bVlanOperStatus=bVlanOperStatus, bVlanPortId=bVlanPortId, bVLANNotifObjects=bVLANNotifObjects, bVlanIndex=bVlanIndex, bVlanCurrentNumber=bVlanCurrentNumber, bVLANMIB=bVLANMIB, bWagVlanTotalPktsRcvd=bWagVlanTotalPktsRcvd, bWagVlanTable=bWagVlanTable, bVlanPortIndex=bVlanPortIndex, bWagVlanTotalBytesRcvd=bWagVlanTotalBytesRcvd, bVLANNotifVariables=bVLANNotifVariables, bVlanCreate=bVlanCreate, PYSNMP_MODULE_ID=bVLANMIB, bWagVlanTotalBytesSent=bWagVlanTotalBytesSent, bWagVlanStatsPortIndex=bWagVlanStatsPortIndex, bWagVlanSubscriberCount=bWagVlanSubscriberCount, bVlanTotal=bVlanTotal, bVlanDelete=bVlanDelete, bVlanAdminStatus=bVlanAdminStatus, bVLANMIBObjects=bVLANMIBObjects, bVlanEncapDisable=bVlanEncapDisable, bWagVlanStatsTable=bWagVlanStatsTable, bWagVlanPortIndex=bWagVlanPortIndex, bVlanName=bVlanName, bWagVlanTotalPktsSent=bWagVlanTotalPktsSent, bVlanAssocSub=bVlanAssocSub, bVlanPortTable=bVlanPortTable, bWagVlanStatsEntry=bWagVlanStatsEntry)
