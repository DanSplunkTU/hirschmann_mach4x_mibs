#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.8 at Sat Jan 15 18:02:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanStatusT, VlanGroupT = mibBuilder.importSymbols("ExaltComm", "VlanStatusT", "VlanGroupT")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Integer32, MibIdentifier, ModuleIdentity, TimeTicks, Bits, Gauge32, Unsigned32, ObjectIdentity, Counter64, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vlan = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3))
if mibBuilder.loadTexts: vlan.setStatus('current')
if mibBuilder.loadTexts: vlan.setDescription('VLAN interfaces.')
vlanStatus = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1), VlanStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanStatus.setStatus('current')
if mibBuilder.loadTexts: vlanStatus.setDescription('This setting enables or disables VLAN support.')
vlanDefaultMgmtId = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultMgmtId.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultMgmtId.setDescription('This is the Default management VLAN ID for all Ethernet\n                            Interface.')
vlanInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6), )
if mibBuilder.loadTexts: vlanInterfaces.setStatus('current')
if mibBuilder.loadTexts: vlanInterfaces.setDescription('This is a table of Vlan interface configurations.')
vlanInterfacesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1), ).setIndexNames((0, "VLAN", "vlanDefaultId"))
if mibBuilder.loadTexts: vlanInterfacesEntry.setStatus('current')
if mibBuilder.loadTexts: vlanInterfacesEntry.setDescription('This is a Vlan table entry.')
vlanDefaultId = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultId.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultId.setDescription('This is the default VLAN ID for the ETH2 Ethernet\n                            Interface.')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanID.setStatus('current')
if mibBuilder.loadTexts: vlanID.setDescription('This is the list of Vlan ID in comma seperated format. For\n                             example, 2,10-20,2000.')
commitVlanSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitVlanSettings.setStatus('current')
if mibBuilder.loadTexts: commitVlanSettings.setDescription('This command allows saving, or resetting Vlan\n                            parameters to factory original. Options are:\n                            save, clear, reset; where clear will abandon\n                            unsaved changes.')
mibBuilder.exportSymbols("VLAN", vlanDefaultId=vlanDefaultId, vlanID=vlanID, commitVlanSettings=commitVlanSettings, vlanDefaultMgmtId=vlanDefaultMgmtId, vlanInterfaces=vlanInterfaces, vlan=vlan, vlanInterfacesEntry=vlanInterfacesEntry, vlanStatus=vlanStatus)
