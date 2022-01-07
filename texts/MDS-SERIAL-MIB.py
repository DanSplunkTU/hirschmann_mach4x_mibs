#
# PySNMP MIB module MDS-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERIAL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:22:31 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, MibIdentifier, NotificationType, ModuleIdentity, iso, IpAddress, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity", "iso", "IpAddress", "Counter64", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
mdsSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2))
mdsSerialMIB.setRevisions(('2018-05-16 00:00', '2014-05-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsSerialMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Initial version.',))
if mibBuilder.loadTexts: mdsSerialMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsSerialMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsSerialMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsSerialMIB.setDescription('The MIB module to describe the system.')
mSerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1))
mSerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 1))
mSerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2))
mSerTermServerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1), )
if mibBuilder.loadTexts: mSerTermServerStatusTable.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerStatusTable.setDescription('This table contains status of terminal servers.')
mSerTermServerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1), ).setIndexNames((0, "MDS-SERIAL-MIB", "mSerTermServerSerialPort"))
if mibBuilder.loadTexts: mSerTermServerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerStatusEntry.setDescription('Each entry contains status of a terminal server.')
mSerTermServerSerialPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerSerialPort.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerSerialPort.setDescription('The serial port on which this terminal server is configured.')
mSerTermServerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerDescription.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerDescription.setDescription('The serial port on which this terminal server is configured.')
mSerTermServerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerEnabled.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerEnabled.setDescription('The serial port on which this terminal server is configured.')
mSerTermServerIpTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerIpTxPackets.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerIpTxPackets.setDescription('Number of packets transmitted on IP interface.')
mSerTermServerIpTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerIpTxBytes.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerIpTxBytes.setDescription('Number of bytes transmitted on IP interface.')
mSerTermServerIpRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerIpRxPackets.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerIpRxPackets.setDescription('Number of packets received on IP interface.')
mSerTermServerIpRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerIpRxBytes.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerIpRxBytes.setDescription('Number of bytes received on IP interface.')
mSerTermServerSerialTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerSerialTxPackets.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerSerialTxPackets.setDescription('Number of packets transmitted on serial interface.')
mSerTermServerSerialTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerSerialTxBytes.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerSerialTxBytes.setDescription('Number of bytes transmitted on serial interface.')
mSerTermServerSerialRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerSerialRxPackets.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerSerialRxPackets.setDescription('Number of packets received on serial interface.')
mSerTermServerSerialRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSerTermServerSerialRxBytes.setStatus('current')
if mibBuilder.loadTexts: mSerTermServerSerialRxBytes.setDescription('Number of bytes received on serial interface.')
mdsSerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3))
mdsSerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 1))
mdsSerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 2))
mSerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 1, 1)).setObjects(("MDS-SERIAL-MIB", "mSerStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSerCompliance = mSerCompliance.setStatus('current')
if mibBuilder.loadTexts: mSerCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-SERIAL-MIB.')
mSerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 2, 1)).setObjects(("MDS-SERIAL-MIB", "mSerTermServerSerialPort"), ("MDS-SERIAL-MIB", "mSerTermServerDescription"), ("MDS-SERIAL-MIB", "mSerTermServerEnabled"), ("MDS-SERIAL-MIB", "mSerTermServerIpTxPackets"), ("MDS-SERIAL-MIB", "mSerTermServerIpTxBytes"), ("MDS-SERIAL-MIB", "mSerTermServerIpRxPackets"), ("MDS-SERIAL-MIB", "mSerTermServerIpRxBytes"), ("MDS-SERIAL-MIB", "mSerTermServerSerialTxPackets"), ("MDS-SERIAL-MIB", "mSerTermServerSerialTxBytes"), ("MDS-SERIAL-MIB", "mSerTermServerSerialRxPackets"), ("MDS-SERIAL-MIB", "mSerTermServerSerialRxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSerStatusGroup = mSerStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mSerStatusGroup.setDescription('A collection of objects providing information about\n        orbit system status.')
mibBuilder.exportSymbols("MDS-SERIAL-MIB", mdsSerMIBGroups=mdsSerMIBGroups, mSerTermServerIpRxBytes=mSerTermServerIpRxBytes, mdsSerMIBConformance=mdsSerMIBConformance, mSerConfig=mSerConfig, mSerTermServerSerialTxBytes=mSerTermServerSerialTxBytes, mSerMIBObjects=mSerMIBObjects, mSerTermServerDescription=mSerTermServerDescription, mSerStatusGroup=mSerStatusGroup, mSerTermServerIpRxPackets=mSerTermServerIpRxPackets, mSerTermServerSerialRxPackets=mSerTermServerSerialRxPackets, mdsSerialMIB=mdsSerialMIB, mSerCompliance=mSerCompliance, mSerTermServerIpTxBytes=mSerTermServerIpTxBytes, mSerTermServerStatusEntry=mSerTermServerStatusEntry, mSerTermServerIpTxPackets=mSerTermServerIpTxPackets, mSerTermServerEnabled=mSerTermServerEnabled, mSerTermServerStatusTable=mSerTermServerStatusTable, mSerTermServerSerialPort=mSerTermServerSerialPort, mSerStatus=mSerStatus, PYSNMP_MODULE_ID=mdsSerialMIB, mSerTermServerSerialRxBytes=mSerTermServerSerialRxBytes, mSerTermServerSerialTxPackets=mSerTermServerSerialTxPackets, mdsSerMIBCompliances=mdsSerMIBCompliances)
