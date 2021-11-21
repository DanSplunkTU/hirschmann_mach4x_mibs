#
# PySNMP MIB module COLUBRIS-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-BANDWIDTH-CONTROL-MIB.my
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:18 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisPriorityQueue, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisPriorityQueue")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, iso, Integer32, TimeTicks, Unsigned32, Bits, NotificationType, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Integer32", "TimeTicks", "Unsigned32", "Bits", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
colubrisBandwidthControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 14))
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setLastUpdated('200408170000Z')
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setDescription('Colubris Networks Bandwidth Control MIB.')
colubrisBandwidthControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1))
coBandwidthControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1))
coBandwidthControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlEnable.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlEnable.setDescription('Indicates if bandwidth control is enabled or disabled on the Internet port.')
coBandwidthControlMaxTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setDescription('Indicates the maximum rate at which data can be transmitted on the \n                 Internet port. If traffic exceeds this rate for short bursts,\n                 it is buffered. Long overages will result in data being dropped.')
coBandwidthControlMaxReceiveRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setDescription('Indicates the maximum rate at which data can be received on the \n                 Internet port. If traffic exceeds this rate for short bursts\n                 it is buffered. Long overages will result in data being dropped.')
coBandwidthControlLevelTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4), )
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setDescription('A table defining the current bandwidth level settings that are\n                 active on the device.')
coBandwidthControlLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1), ).setIndexNames((0, "COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelIndex"))
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setDescription('An entry in the coBandwidthControlLevelTable.\n                 coBandwidthControlLevelIndex - Uniquely access a definition for this\n                                                particular bandwidth control level.')
coBandwidthControlLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 1), ColubrisPriorityQueue())
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setDescription('Specifies the level index. Each index defines a bandwidth level that\n                 traffic can be assigned to. Four indexes are defined (1 to 4) with \n                 the following meanings: 1-Low, 2-Normal, 3- High, 4-Very High.')
coBandwidthControlLevelMinTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setDescription('Specify the minimum transmit rate for the level\n                 as a percentage of coBandwidthControlMaxTransmitRate. This is the \n                 minimum amount of bandwidth that will be assigned to a level as \n                 soon as outgoing traffic is present on the level.')
coBandwidthControlLevelMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setDescription('Specify the maximum transmit rate for the specified level\n                 as a percentage of coBandwidthControlMaxTransmitRate. This is the \n                 maximum amount of outgoing bandwidth that can be consumed by the \n                 level. Traffic in excess will be buffered for short bursts, and \n                 dropped for sustained overages')
coBandwidthControlLevelMinReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setDescription('Specify the minimum receive rate for the specified level \n                 as a percentage of coBandwidthControlMaxReceiveRateRate. This is the \n                 minimum amount of bandwidth that will be assigned to a level as soon \n                 as incoming traffic is present on the level.')
coBandwidthControlLevelMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setDescription('Specify the maximum receive rate for the specified level \n                 as a percentage of coBandwidthControlMaxReceiveRateRate. This is the \n                 maximum amount of incoming bandwidth that can be consumed by the \n                 level. Traffic in excess will be buffered for short bursts, and \n                 dropped for sustained overages.')
colubrisBandwidthControlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2))
colubrisBandwidthControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1))
colubrisBandwidthControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2))
colubrisBandwidthControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1, 1)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "colubrisBandwidthControlMIBGroup"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "colubrisBandwidthControlLevelMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlMIBCompliance = colubrisBandwidthControlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisBandwidthControlMIBCompliance.setDescription('The compliance statement for the Bandwidth Control MIB.')
colubrisBandwidthControlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 1)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlEnable"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlMIBGroup = colubrisBandwidthControlMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisBandwidthControlMIBGroup.setDescription('A collection of objects for use with Bandwidth Controls.')
colubrisBandwidthControlLevelMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 2)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinReceiveRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlLevelMIBGroup = colubrisBandwidthControlLevelMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisBandwidthControlLevelMIBGroup.setDescription('A collection of objects for use with Bandwidth Controls.')
mibBuilder.exportSymbols("COLUBRIS-BANDWIDTH-CONTROL-MIB", PYSNMP_MODULE_ID=colubrisBandwidthControlMIB, coBandwidthControlLevelTable=coBandwidthControlLevelTable, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, coBandwidthControlEnable=coBandwidthControlEnable, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate, colubrisBandwidthControlMIBGroup=colubrisBandwidthControlMIBGroup, colubrisBandwidthControlMIBCompliances=colubrisBandwidthControlMIBCompliances, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, coBandwidthControlConfig=coBandwidthControlConfig, colubrisBandwidthControlMIBCompliance=colubrisBandwidthControlMIBCompliance, colubrisBandwidthControlLevelMIBGroup=colubrisBandwidthControlLevelMIBGroup, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate, colubrisBandwidthControlMIB=colubrisBandwidthControlMIB, colubrisBandwidthControlMIBConformance=colubrisBandwidthControlMIBConformance, colubrisBandwidthControlMIBObjects=colubrisBandwidthControlMIBObjects, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, colubrisBandwidthControlMIBGroups=colubrisBandwidthControlMIBGroups)
