#
# PySNMP MIB module ADTRAN-AOS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-VRRP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:20 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSRouter, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSRouter", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter64, ObjectIdentity, iso, MibIdentifier, IpAddress, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "IpAddress", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSVrrpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 2, 3))
adGenAOSVrrpMib.setRevisions(('2014-07-29 00:00', '2014-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSVrrpMib.setRevisionsDescriptions(('Revised text in descriptions.', 'Created the adGenAosVrrp MIB. Revision R11.3',))
if mibBuilder.loadTexts: adGenAOSVrrpMib.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: adGenAOSVrrpMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSVrrpMib.setContactInfo('      Technical Support Dept.\n             Postal: ADTRAN, Inc.\n             901 Explorer Blvd.\n             Huntsville, AL 35806\n\n             Tel: +1 800 726-8663\n             Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSVrrpMib.setDescription('The MIB module defines VRRP V2 and V3 notifications for AdtranOS\n        products and provides information about the virtual router instance.')
adGenAOSVrrp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3))
adGenAOSVrrpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0))
adGenAOSVrrpTrapCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1))
adGenAOSVrrpTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2), )
if mibBuilder.loadTexts: adGenAOSVrrpTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpTable.setDescription('Vrrp Router instances.')
adGenAOSVrrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpVersion"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpId"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddrType"))
if mibBuilder.loadTexts: adGenAOSVrrpEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpEntry.setDescription('The parameters of a particular VRRP Instance.')
adGenAOSVrrpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("v2", 2), ("v3", 3))))
if mibBuilder.loadTexts: adGenAOSVrrpVersion.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpVersion.setDescription('Specifies the version of VRRP used in the current Virtual Router instance.')
adGenAOSVrrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: adGenAOSVrrpId.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpId.setDescription('Identifies a row in the AdGenAOSVrrpTable. The ID is unique to the VRRP \n            instance of VRRP Type (v2 and v3). ')
adGenAOSVrrpInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 3), InetAddressType())
if mibBuilder.loadTexts: adGenAOSVrrpInetAddrType.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpInetAddrType.setDescription('Identifies the primary IP address type.')
adGenAOSVrrpInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpInetAddr.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpInetAddr.setDescription('Identifies the primary IP address.')
adGenAOSVrrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpOperStatus.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpOperStatus.setDescription('Identifies if the router is the master or backup.')
adGenAOSVrrpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpPriority.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpPriority.setDescription('Displays the priority of the virtual router instance.')
adGenAOSVrrpMasterTrapCntl = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrapCntl.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrapCntl.setDescription('This variable indicates whether the system produces\n            the adGenAOSVrrpMaster trap.')
adGenAOSVrrpMasterTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus"))
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrap.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrap.setDescription('A Master Trap signifies that one of the virtual routers has changed \n            its state. Either from Master to Backup or Backup to Master')
adGenAOSVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20))
adGenAOSVrrpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1))
adGenAOSVrrpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2))
adGenAOSVrrpFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpObjectGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpTrapCfgGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpTrapGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpFullCompliance = adGenAOSVrrpFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        VRRP V2 and V3 in adGenAosVrrp MIB. When this MIB is implemented\n        with support for read-write, then such an implementation can claim\n        full compliance.')
adGenAOSVrrpReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 2)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpReadOnlyCompliance = adGenAOSVrrpReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpReadOnlyCompliance.setDescription('The compliance statement for SNMP entities which implement\n            VRRP V2 and V3 in adGenAOSVrrp MIB. When this MIB is implemented\n            without support for read-create (i.e. in read-only mode),\n            then such an implementation can claim read-only compliance.\n      \t\tA virtual router can be defined but cannot be modified using \n      \t\tthis MIB.')
adGenAOSVrrpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddr"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpObjectGroup = adGenAOSVrrpObjectGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpObjectGroup.setDescription('The objects that define VRRP table.')
adGenAOSVrrpTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 2)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrapCntl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpTrapCfgGroup = adGenAOSVrrpTrapCfgGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpTrapCfgGroup.setDescription('This group contains the objects necessary to enable/disable\n            VRRP traps.')
adGenAOSVrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 3)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpTrapGroup = adGenAOSVrrpTrapGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpTrapGroup.setDescription('The objects necessary to control VRRP state notification messages.')
adGenAOSVrrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 4)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpNotificationGroup = adGenAOSVrrpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSVrrpNotificationGroup.setDescription('Traps which may be used to detect the change of state\n          in any of the virtual router instances.')
mibBuilder.exportSymbols("ADTRAN-AOS-VRRP-MIB", adGenAOSVrrpId=adGenAOSVrrpId, adGenAOSVrrpGroups=adGenAOSVrrpGroups, adGenAOSVrrpConformance=adGenAOSVrrpConformance, adGenAOSVrrpVersion=adGenAOSVrrpVersion, adGenAOSVrrpNotificationGroup=adGenAOSVrrpNotificationGroup, PYSNMP_MODULE_ID=adGenAOSVrrpMib, adGenAOSVrrpMasterTrapCntl=adGenAOSVrrpMasterTrapCntl, adGenAOSVrrpCompliances=adGenAOSVrrpCompliances, adGenAOSVrrp=adGenAOSVrrp, adGenAOSVrrpMib=adGenAOSVrrpMib, adGenAOSVrrpTrapGroup=adGenAOSVrrpTrapGroup, adGenAOSVrrpTable=adGenAOSVrrpTable, adGenAOSVrrpOperStatus=adGenAOSVrrpOperStatus, adGenAOSVrrpReadOnlyCompliance=adGenAOSVrrpReadOnlyCompliance, adGenAOSVrrpFullCompliance=adGenAOSVrrpFullCompliance, adGenAOSVrrpObjectGroup=adGenAOSVrrpObjectGroup, adGenAOSVrrpInetAddrType=adGenAOSVrrpInetAddrType, adGenAOSVrrpInetAddr=adGenAOSVrrpInetAddr, adGenAOSVrrpEntry=adGenAOSVrrpEntry, adGenAOSVrrpPriority=adGenAOSVrrpPriority, adGenAOSVrrpMasterTrap=adGenAOSVrrpMasterTrap, adGenAOSVrrpTrap=adGenAOSVrrpTrap, adGenAOSVrrpTrapCfgGroup=adGenAOSVrrpTrapCfgGroup, adGenAOSVrrpTrapCntl=adGenAOSVrrpTrapCntl)
