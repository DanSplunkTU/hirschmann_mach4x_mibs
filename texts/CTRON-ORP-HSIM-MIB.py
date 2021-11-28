#
# PySNMP MIB module CTRON-ORP-HSIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:22 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctOrpHSIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctOrpHSIM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Integer32, Bits, IpAddress, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Integer32", "Bits", "IpAddress", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ctOrpHSIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1), )
if mibBuilder.loadTexts: ctOrpHSIMTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMTable.setDescription('This table defines orp HSIMs.')
ctOrpHSIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1), ).setIndexNames((0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMSlot"), (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMIndex"))
if mibBuilder.loadTexts: ctOrpHSIMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMEntry.setDescription('Describes a particular entry.')
ctOrpHSIMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMSlot.setDescription('In a chassis environment, this object indicates the slot in which \n     the module, which contains the HSIM resides. In the case of a \n     stand-alone device the slot will always be 1.')
ctOrpHSIMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMIndex.setDescription('This object is a unique index referring to a given HSIM on a module \n     or stand-alone device.')
ctOrpHSIMIfRef = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIfRef.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMIfRef.setDescription('This object contains an OID which associates this HSIM with a unique \n     interface.  This OID must be an existing and accessible ifIndex leaf \n     from ifTable in RFC1213 or RFC1573.')
ctOrpHSIMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMMACAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMMACAddress.setDescription('Provides the base Ethernet MAC Address of the installed HSIM.')
ctOrpHSIMIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMIPAddress.setDescription('Provides the base IP address of the installed HSIM.')
ctOrpHSIMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMSubnetMask.setDescription('Provides the subnet mask of the base IP address of the installed \n     HSIM.')
ctOrpHSIMROCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMROCommName.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMROCommName.setDescription('Provides the Read-Only Community name associated with the base IP \n     Address of the installed HSIM.')
ctOrpHSIMRWCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMRWCommName.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMRWCommName.setDescription('Provides the Read-Write Community name associated with the base IP \n     Address of the installed HSIM.')
ctOrpHSIMSUCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSUCommName.setStatus('mandatory')
if mibBuilder.loadTexts: ctOrpHSIMSUCommName.setDescription('Provides the Super-User Community name associated with the base IP \n     Address of the installed HSIM.')
mibBuilder.exportSymbols("CTRON-ORP-HSIM-MIB", MacAddress=MacAddress, ctOrpHSIMSlot=ctOrpHSIMSlot, ctOrpHSIMRWCommName=ctOrpHSIMRWCommName, ctOrpHSIMIPAddress=ctOrpHSIMIPAddress, ctOrpHSIMIndex=ctOrpHSIMIndex, ctOrpHSIMROCommName=ctOrpHSIMROCommName, ctOrpHSIMEntry=ctOrpHSIMEntry, ctOrpHSIMMACAddress=ctOrpHSIMMACAddress, ctOrpHSIMIfRef=ctOrpHSIMIfRef, ctOrpHSIMSUCommName=ctOrpHSIMSUCommName, ctOrpHSIMTable=ctOrpHSIMTable, ctOrpHSIMSubnetMask=ctOrpHSIMSubnetMask)
