#
# PySNMP MIB module MSERIES-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-PORT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:38:17 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
PortStatus, PortType, PortMode = mibBuilder.importSymbols("MSERIES-TC", "PortStatus", "PortType", "PortMode")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Counter32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity, MibIdentifier, ModuleIdentity, Counter64, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Counter64", "Bits", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smartPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 3))
smartPort.setRevisions(('2014-02-12 13:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartPort.setRevisionsDescriptions(('The initial revision of the MSERIES Port MIB.',))
if mibBuilder.loadTexts: smartPort.setLastUpdated('201402121344Z')
if mibBuilder.loadTexts: smartPort.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartPort.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartPort.setDescription('This is the enterprise specific Port MIB for SmartOptics M-Series.')
smartPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1))
smartPortGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 1))
smartPortList = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2))
smartPortMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 2))
smartPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 1))
smartPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 2))
smartPortTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1), )
if mibBuilder.loadTexts: smartPortTable.setStatus('current')
if mibBuilder.loadTexts: smartPortTable.setDescription('A port table.')
smartPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1), ).setIndexNames((0, "MSERIES-PORT-MIB", "smartPortIndex"))
if mibBuilder.loadTexts: smartPortEntry.setStatus('current')
if mibBuilder.loadTexts: smartPortEntry.setDescription('An entry in the port list.')
smartPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartPortIndex.setStatus('current')
if mibBuilder.loadTexts: smartPortIndex.setDescription('A unique index for each port that corresponds to the index in the interface table')
smartPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartPortName.setStatus('current')
if mibBuilder.loadTexts: smartPortName.setDescription('The name of the port.')
smartPortAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartPortAlias.setStatus('current')
if mibBuilder.loadTexts: smartPortAlias.setDescription('User configurable Port Alias for the port.\n\n         Not writeable in SmartOS v2.3')
smartPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 4), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartPortType.setStatus('current')
if mibBuilder.loadTexts: smartPortType.setDescription('The type of port.\n\n         rx(1) - Receiving port.\n\n         tx(2) - Transmitting port.\n\n         biDi(3) - Bidirectional port.')
smartPortPower = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartPortPower.setStatus('current')
if mibBuilder.loadTexts: smartPortPower.setDescription('The power level in units of 0.1 dBm.')
smartPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 6), PortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartPortStatus.setStatus('current')
if mibBuilder.loadTexts: smartPortStatus.setDescription('The operational state for a port.\n\n        idle(1) - The port is not activated\n\n        down(2) - The port traffic is lost.\n\n        up(3) - There is traffic on the port.\n\n        high(4) - The port got to high power.\n\n        low(5) - The port got to low power.\n\n        eyeSafety(6) - The Line Tx port is in Eye Safety Mode.\n        This means that either the connector on the\n        Line Tx port is not inserted or that you have\n        too strong reflection from the line fiber.\n\n        cd(7) - Channel detected.\n\n        ncd(8) - No channel detected.')
smartPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 7), PortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartPortMode.setStatus('current')
if mibBuilder.loadTexts: smartPortMode.setDescription("The Mode of the Port.\n\n         normal (1) - The port is active. No alarms\n         are beeing suppressed.\n\n         service (2) . The port is in service mode\n         and alarms are beeing suppressed. When service\n         is ready smartPortMode  should be set to\n         'normal' again.\n\n         Not writeable in SmartOS v2.3")
smartPortHighPowerAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartPortHighPowerAlarmThreshold.setStatus('current')
if mibBuilder.loadTexts: smartPortHighPowerAlarmThreshold.setDescription('The threshold for the High Power alarm.\n\n         Not writeable in SmartOS v2.3')
smartPortLowPowerAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartPortLowPowerAlarmThreshold.setStatus('current')
if mibBuilder.loadTexts: smartPortLowPowerAlarmThreshold.setDescription('The threshold for the Low Power alarm.\n\n         Not writeable in SmartOS v2.3')
smartPortListGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 1, 1)).setObjects(("MSERIES-PORT-MIB", "smartPortIndex"), ("MSERIES-PORT-MIB", "smartPortName"), ("MSERIES-PORT-MIB", "smartPortAlias"), ("MSERIES-PORT-MIB", "smartPortType"), ("MSERIES-PORT-MIB", "smartPortPower"), ("MSERIES-PORT-MIB", "smartPortStatus"), ("MSERIES-PORT-MIB", "smartPortMode"), ("MSERIES-PORT-MIB", "smartPortHighPowerAlarmThreshold"), ("MSERIES-PORT-MIB", "smartPortLowPowerAlarmThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartPortListGroupV1 = smartPortListGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartPortListGroupV1.setDescription('The Port List MIB objects v1.')
smartPortBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 2, 1)).setObjects(("MSERIES-PORT-MIB", "smartPortListGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartPortBasicComplV1 = smartPortBasicComplV1.setStatus('current')
if mibBuilder.loadTexts: smartPortBasicComplV1.setDescription('Basic implementation requirements for the port MIB V1.')
mibBuilder.exportSymbols("MSERIES-PORT-MIB", smartPortLowPowerAlarmThreshold=smartPortLowPowerAlarmThreshold, smartPortType=smartPortType, smartPortStatus=smartPortStatus, smartPort=smartPort, smartPortAlias=smartPortAlias, smartPortMode=smartPortMode, smartPortIndex=smartPortIndex, smartPortPower=smartPortPower, smartPortTable=smartPortTable, smartPortCompliances=smartPortCompliances, smartPortBasicComplV1=smartPortBasicComplV1, smartPortObjects=smartPortObjects, smartPortEntry=smartPortEntry, smartPortGroups=smartPortGroups, smartPortName=smartPortName, smartPortHighPowerAlarmThreshold=smartPortHighPowerAlarmThreshold, PYSNMP_MODULE_ID=smartPort, smartPortList=smartPortList, smartPortListGroupV1=smartPortListGroupV1, smartPortGeneral=smartPortGeneral, smartPortMIBConformance=smartPortMIBConformance)
