#
# PySNMP MIB module PHION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/PHION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:11:07 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, ModuleIdentity, Bits, Unsigned32, Integer32, Counter64, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, MibIdentifier, IpAddress, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "Unsigned32", "Integer32", "Counter64", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "Counter32", "enterprises")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
phion = ModuleIdentity((1, 3, 6, 1, 4, 1, 10704))
phion.setRevisions(('2014-01-08 00:00', '2014-01-07 00:00', '2013-12-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: phion.setRevisionsDescriptions(('insert OBJECT-GROUPS', 'Removed syntax errors', 'Removed errors and warnings',))
if mibBuilder.loadTexts: phion.setLastUpdated('201401080000Z')
if mibBuilder.loadTexts: phion.setOrganization('Barracuda Networks')
if mibBuilder.loadTexts: phion.setContactInfo('http://www.barracuda.com')
if mibBuilder.loadTexts: phion.setDescription('.')
event = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 10))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 1))
fwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 20))
fwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21))
fwCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10704, 20, 1)).setObjects(("PHION-MIB", "boxGroup"), ("PHION-MIB", "serverGroup"), ("PHION-MIB", "releaseGroup"), ("PHION-MIB", "hotfixGroup"), ("PHION-MIB", "hwGroup"), ("PHION-MIB", "raidGroup"), ("PHION-MIB", "vpnGroup"), ("PHION-MIB", "bgpGroup"), ("PHION-MIB", "ospfGroup"), ("PHION-MIB", "ripGroup"), ("PHION-MIB", "fwstatsGroup"), ("PHION-MIB", "vpnusersGroup"), ("PHION-MIB", "trafficshapeGroup"), ("PHION-MIB", "diskspaceGroup"), ("PHION-MIB", "eventGroup"), ("PHION-MIB", "notificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fwCompliance = fwCompliance.setStatus('current')
if mibBuilder.loadTexts: fwCompliance.setDescription('Firewall Info Groups')
serviceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 1))
firmwareGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 2))
hwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 3))
netGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 4))
eventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 5))
class ServiceState(TextualConvention, Integer32):
    description = 'The state a box service be in.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 4))
    namedValues = NamedValues(("unknown", -1), ("stopped", 0), ("started", 1), ("blocked", 2), ("removed", 4))

class SensorType(TextualConvention, Integer32):
    description = 'The types of sensors.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3))
    namedValues = NamedValues(("unknown", -1), ("voltage", 0), ("fan", 1), ("temperature", 2), ("psu-status", 3))

class RaidEventSeverity(TextualConvention, Integer32):
    description = 'The values of raid event severity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("error", 1), ("warning", 2), ("information", 3), ("debug", 4))

class VpnStates(TextualConvention, Integer32):
    description = 'The states of the VPN tunnel'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1))
    namedValues = NamedValues(("down", -1), ("down-disabled", 0), ("active", 1))

boxServices = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 0), )
if mibBuilder.loadTexts: boxServices.setStatus('current')
if mibBuilder.loadTexts: boxServices.setDescription(' ')
boxServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1), ).setIndexNames((0, "PHION-MIB", "boxServiceName"))
if mibBuilder.loadTexts: boxServicesEntry.setStatus('current')
if mibBuilder.loadTexts: boxServicesEntry.setDescription(' ')
boxServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServiceName.setStatus('current')
if mibBuilder.loadTexts: boxServiceName.setDescription(' ')
boxServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 2), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServiceState.setStatus('current')
if mibBuilder.loadTexts: boxServiceState.setDescription(' ')
boxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 1, 1)).setObjects(("PHION-MIB", "boxServiceName"), ("PHION-MIB", "boxServiceState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boxGroup = boxGroup.setStatus('current')
if mibBuilder.loadTexts: boxGroup.setDescription(' ')
serverServices = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 1), )
if mibBuilder.loadTexts: serverServices.setStatus('current')
if mibBuilder.loadTexts: serverServices.setDescription(' ')
serverServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1), ).setIndexNames((0, "PHION-MIB", "serverServiceName"))
if mibBuilder.loadTexts: serverServicesEntry.setStatus('current')
if mibBuilder.loadTexts: serverServicesEntry.setDescription(' ')
serverServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverServiceName.setStatus('current')
if mibBuilder.loadTexts: serverServiceName.setDescription(' ')
serverServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 2), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverServiceState.setStatus('current')
if mibBuilder.loadTexts: serverServiceState.setDescription(' ')
serverGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 1, 2)).setObjects(("PHION-MIB", "serverServiceName"), ("PHION-MIB", "serverServiceState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    serverGroup = serverGroup.setStatus('current')
if mibBuilder.loadTexts: serverGroup.setDescription(' ')
phionRelease = MibScalar((1, 3, 6, 1, 4, 1, 10704, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phionRelease.setStatus('current')
if mibBuilder.loadTexts: phionRelease.setDescription(' ')
releaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 2, 1)).setObjects(("PHION-MIB", "phionRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    releaseGroup = releaseGroup.setStatus('current')
if mibBuilder.loadTexts: releaseGroup.setDescription(' ')
phionHotfixes = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 3), )
if mibBuilder.loadTexts: phionHotfixes.setStatus('current')
if mibBuilder.loadTexts: phionHotfixes.setDescription(' ')
phionHotfixesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1), ).setIndexNames((0, "PHION-MIB", "hotfixName"))
if mibBuilder.loadTexts: phionHotfixesEntry.setStatus('current')
if mibBuilder.loadTexts: phionHotfixesEntry.setDescription(' ')
hotfixName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hotfixName.setStatus('current')
if mibBuilder.loadTexts: hotfixName.setDescription(' ')
hotfixInstallTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hotfixInstallTime.setStatus('current')
if mibBuilder.loadTexts: hotfixInstallTime.setDescription(' ')
hotfixGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 2, 2)).setObjects(("PHION-MIB", "hotfixName"), ("PHION-MIB", "hotfixInstallTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hotfixGroup = hotfixGroup.setStatus('current')
if mibBuilder.loadTexts: hotfixGroup.setDescription(' ')
hwSensors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 4), )
if mibBuilder.loadTexts: hwSensors.setStatus('current')
if mibBuilder.loadTexts: hwSensors.setDescription(' ')
hwSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1), ).setIndexNames((0, "PHION-MIB", "hwSensorName"))
if mibBuilder.loadTexts: hwSensorsEntry.setStatus('current')
if mibBuilder.loadTexts: hwSensorsEntry.setDescription(' ')
hwSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorName.setStatus('current')
if mibBuilder.loadTexts: hwSensorName.setDescription(' ')
hwSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 2), SensorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorType.setStatus('current')
if mibBuilder.loadTexts: hwSensorType.setDescription(' ')
hwSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorValue.setStatus('current')
if mibBuilder.loadTexts: hwSensorValue.setDescription(' ')
hwGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 1)).setObjects(("PHION-MIB", "hwSensorName"), ("PHION-MIB", "hwSensorType"), ("PHION-MIB", "hwSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGroup = hwGroup.setStatus('current')
if mibBuilder.loadTexts: hwGroup.setDescription(' ')
raidEvents = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 5), )
if mibBuilder.loadTexts: raidEvents.setStatus('current')
if mibBuilder.loadTexts: raidEvents.setDescription(' ')
raidEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1), ).setIndexNames((0, "PHION-MIB", "raidEventIndex"))
if mibBuilder.loadTexts: raidEventsEntry.setStatus('current')
if mibBuilder.loadTexts: raidEventsEntry.setDescription(' ')
raidEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventIndex.setStatus('current')
if mibBuilder.loadTexts: raidEventIndex.setDescription(' ')
raidEventSev = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 2), RaidEventSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventSev.setStatus('current')
if mibBuilder.loadTexts: raidEventSev.setDescription(' ')
raidEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventTime.setStatus('current')
if mibBuilder.loadTexts: raidEventTime.setDescription(' ')
raidEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventText.setStatus('current')
if mibBuilder.loadTexts: raidEventText.setDescription(' ')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 2)).setObjects(("PHION-MIB", "raidEventIndex"), ("PHION-MIB", "raidEventSev"), ("PHION-MIB", "raidEventTime"), ("PHION-MIB", "raidEventText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
if mibBuilder.loadTexts: raidGroup.setDescription(' ')
vpnTunnels = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 6), )
if mibBuilder.loadTexts: vpnTunnels.setStatus('current')
if mibBuilder.loadTexts: vpnTunnels.setDescription(' ')
vpnTunnelsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1), ).setIndexNames((0, "PHION-MIB", "vpnName"))
if mibBuilder.loadTexts: vpnTunnelsEntry.setStatus('current')
if mibBuilder.loadTexts: vpnTunnelsEntry.setDescription(' ')
vpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnName.setStatus('current')
if mibBuilder.loadTexts: vpnName.setDescription(' ')
vpnState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 2), VpnStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnState.setStatus('current')
if mibBuilder.loadTexts: vpnState.setDescription(' ')
vpnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 1)).setObjects(("PHION-MIB", "vpnName"), ("PHION-MIB", "vpnState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnGroup = vpnGroup.setStatus('current')
if mibBuilder.loadTexts: vpnGroup.setDescription(' ')
bgpNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 7), )
if mibBuilder.loadTexts: bgpNeighbors.setStatus('current')
if mibBuilder.loadTexts: bgpNeighbors.setDescription(' ')
bgpNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1), ).setIndexNames((0, "PHION-MIB", "bgpNeighborAddress"))
if mibBuilder.loadTexts: bgpNeighborsEntry.setStatus('current')
if mibBuilder.loadTexts: bgpNeighborsEntry.setDescription(' ')
bgpNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: bgpNeighborAddress.setDescription(' ')
bgpNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpNeighborState.setStatus('current')
if mibBuilder.loadTexts: bgpNeighborState.setDescription(' ')
bgpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 2)).setObjects(("PHION-MIB", "bgpNeighborAddress"), ("PHION-MIB", "bgpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgpGroup = bgpGroup.setStatus('current')
if mibBuilder.loadTexts: bgpGroup.setDescription(' ')
ospfNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 8), )
if mibBuilder.loadTexts: ospfNeighbors.setStatus('current')
if mibBuilder.loadTexts: ospfNeighbors.setDescription(' ')
ospfNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1), ).setIndexNames((0, "PHION-MIB", "ospfNeighborId"))
if mibBuilder.loadTexts: ospfNeighborsEntry.setStatus('current')
if mibBuilder.loadTexts: ospfNeighborsEntry.setDescription(' ')
ospfNeighborId = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborId.setStatus('current')
if mibBuilder.loadTexts: ospfNeighborId.setDescription(' ')
ospfNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: ospfNeighborAddress.setDescription(' ')
ospfNeighborInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborInterface.setStatus('current')
if mibBuilder.loadTexts: ospfNeighborInterface.setDescription(' ')
ospfNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborStatus.setStatus('current')
if mibBuilder.loadTexts: ospfNeighborStatus.setDescription(' ')
ospfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 3)).setObjects(("PHION-MIB", "ospfNeighborId"), ("PHION-MIB", "ospfNeighborAddress"), ("PHION-MIB", "ospfNeighborInterface"), ("PHION-MIB", "ospfNeighborStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfGroup = ospfGroup.setStatus('current')
if mibBuilder.loadTexts: ospfGroup.setDescription(' ')
ripNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 9), )
if mibBuilder.loadTexts: ripNeighbors.setStatus('current')
if mibBuilder.loadTexts: ripNeighbors.setDescription(' ')
ripNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1), ).setIndexNames((0, "PHION-MIB", "ripNeighborAddress"))
if mibBuilder.loadTexts: ripNeighborsEntry.setStatus('current')
if mibBuilder.loadTexts: ripNeighborsEntry.setDescription(' ')
ripNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ripNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: ripNeighborAddress.setDescription(' ')
ripNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ripNeighborState.setStatus('current')
if mibBuilder.loadTexts: ripNeighborState.setDescription(' ')
ripGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 4)).setObjects(("PHION-MIB", "ripNeighborAddress"), ("PHION-MIB", "ripNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ripGroup = ripGroup.setStatus('current')
if mibBuilder.loadTexts: ripGroup.setDescription(' ')
fwStats = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 10), )
if mibBuilder.loadTexts: fwStats.setStatus('current')
if mibBuilder.loadTexts: fwStats.setDescription(' ')
fwStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1), ).setIndexNames((0, "PHION-MIB", "firewallSessions"))
if mibBuilder.loadTexts: fwStatsEntry.setStatus('current')
if mibBuilder.loadTexts: fwStatsEntry.setDescription(' ')
firewallSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallSessions.setStatus('current')
if mibBuilder.loadTexts: firewallSessions.setDescription(' ')
packetThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetThroughput.setStatus('current')
if mibBuilder.loadTexts: packetThroughput.setDescription(' ')
dataThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataThroughput.setStatus('current')
if mibBuilder.loadTexts: dataThroughput.setDescription(' ')
firewallSessions64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallSessions64.setStatus('current')
if mibBuilder.loadTexts: firewallSessions64.setDescription(' ')
packetThroughput64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetThroughput64.setStatus('current')
if mibBuilder.loadTexts: packetThroughput64.setDescription(' ')
dataThroughput64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataThroughput64.setStatus('current')
if mibBuilder.loadTexts: dataThroughput64.setDescription(' ')
fwstatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 3)).setObjects(("PHION-MIB", "firewallSessions"), ("PHION-MIB", "packetThroughput"), ("PHION-MIB", "dataThroughput"), ("PHION-MIB", "firewallSessions64"), ("PHION-MIB", "packetThroughput64"), ("PHION-MIB", "dataThroughput64"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fwstatsGroup = fwstatsGroup.setStatus('current')
if mibBuilder.loadTexts: fwstatsGroup.setDescription(' ')
vpnUsers = MibScalar((1, 3, 6, 1, 4, 1, 10704, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnUsers.setStatus('current')
if mibBuilder.loadTexts: vpnUsers.setDescription(' ')
vpnusersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 5)).setObjects(("PHION-MIB", "vpnUsers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnusersGroup = vpnusersGroup.setStatus('current')
if mibBuilder.loadTexts: vpnusersGroup.setDescription(' ')
trafficShape = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 12), )
if mibBuilder.loadTexts: trafficShape.setStatus('current')
if mibBuilder.loadTexts: trafficShape.setDescription(' ')
trafficShapeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1), ).setIndexNames((0, "PHION-MIB", "connectorName"))
if mibBuilder.loadTexts: trafficShapeEntry.setStatus('current')
if mibBuilder.loadTexts: trafficShapeEntry.setDescription(' ')
connectorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectorName.setStatus('current')
if mibBuilder.loadTexts: connectorName.setDescription('Name of shaping connector. With :IN for inbound and :OUT for outbound')
rate = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rate.setStatus('current')
if mibBuilder.loadTexts: rate.setDescription('Rate in kbit/sec')
sessions = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessions.setStatus('current')
if mibBuilder.loadTexts: sessions.setDescription('Number of sessions')
class1Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Total.setStatus('current')
if mibBuilder.loadTexts: class1Total.setDescription('Total bytes for class1')
class1Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Pakets.setStatus('current')
if mibBuilder.loadTexts: class1Pakets.setDescription('Total packets for class1')
class1Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Drop.setStatus('current')
if mibBuilder.loadTexts: class1Drop.setDescription('Dropped packets for class1')
class2Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Total.setStatus('current')
if mibBuilder.loadTexts: class2Total.setDescription('Total bytes for class2')
class2Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Pakets.setStatus('current')
if mibBuilder.loadTexts: class2Pakets.setDescription('Total packets for class2')
class2Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Drop.setStatus('current')
if mibBuilder.loadTexts: class2Drop.setDescription('Dropped packets for class2')
class3Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Total.setStatus('current')
if mibBuilder.loadTexts: class3Total.setDescription('Total bytes for class3')
class3Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Pakets.setStatus('current')
if mibBuilder.loadTexts: class3Pakets.setDescription('Total packets for class3')
class3Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Drop.setStatus('current')
if mibBuilder.loadTexts: class3Drop.setDescription('Dropped packets for class3')
noDelayTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayTotal.setStatus('current')
if mibBuilder.loadTexts: noDelayTotal.setDescription('Total bytes for no delay')
noDelayPakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayPakets.setStatus('current')
if mibBuilder.loadTexts: noDelayPakets.setDescription('Total packets for no delay')
noDelayDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayDrop.setStatus('current')
if mibBuilder.loadTexts: noDelayDrop.setDescription('Dropped packets for no delay')
trafficshapeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 4)).setObjects(("PHION-MIB", "connectorName"), ("PHION-MIB", "rate"), ("PHION-MIB", "sessions"), ("PHION-MIB", "class1Total"), ("PHION-MIB", "class1Pakets"), ("PHION-MIB", "class1Drop"), ("PHION-MIB", "class2Total"), ("PHION-MIB", "class2Pakets"), ("PHION-MIB", "class2Drop"), ("PHION-MIB", "class3Total"), ("PHION-MIB", "class3Pakets"), ("PHION-MIB", "class3Drop"), ("PHION-MIB", "noDelayTotal"), ("PHION-MIB", "noDelayPakets"), ("PHION-MIB", "noDelayDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trafficshapeGroup = trafficshapeGroup.setStatus('current')
if mibBuilder.loadTexts: trafficshapeGroup.setDescription(' ')
diskSpace = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 13), )
if mibBuilder.loadTexts: diskSpace.setStatus('current')
if mibBuilder.loadTexts: diskSpace.setDescription(' ')
diskSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1), ).setIndexNames((0, "PHION-MIB", "partitionName"))
if mibBuilder.loadTexts: diskSpaceEntry.setStatus('current')
if mibBuilder.loadTexts: diskSpaceEntry.setDescription(' ')
partitionName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionName.setStatus('current')
if mibBuilder.loadTexts: partitionName.setDescription('Name of the partition entry')
partitionMaxSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionMaxSpace.setStatus('current')
if mibBuilder.loadTexts: partitionMaxSpace.setDescription('Maximum space of partition entry in KB')
partitionFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionFreeSpace.setStatus('current')
if mibBuilder.loadTexts: partitionFreeSpace.setDescription('Free space of partition entry in KB')
partitionUsedSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionUsedSpace.setStatus('current')
if mibBuilder.loadTexts: partitionUsedSpace.setDescription('Used space of partition entry in KB')
partitionUsedSpacePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionUsedSpacePercent.setStatus('current')
if mibBuilder.loadTexts: partitionUsedSpacePercent.setDescription('Used space of partition entry in %')
diskspaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 5)).setObjects(("PHION-MIB", "partitionName"), ("PHION-MIB", "partitionMaxSpace"), ("PHION-MIB", "partitionFreeSpace"), ("PHION-MIB", "partitionUsedSpace"), ("PHION-MIB", "partitionUsedSpacePercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskspaceGroup = diskspaceGroup.setStatus('current')
if mibBuilder.loadTexts: diskspaceGroup.setDescription(' ')
eventID = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventID.setStatus('current')
if mibBuilder.loadTexts: eventID.setDescription('Event ID')
eventIDDescription = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIDDescription.setStatus('current')
if mibBuilder.loadTexts: eventIDDescription.setDescription('Event Type-Description')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
if mibBuilder.loadTexts: eventType.setDescription('Event Type')
eventAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmTime.setStatus('current')
if mibBuilder.loadTexts: eventAlarmTime.setDescription('Event Alarm Time')
eventLayerDescription = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLayerDescription.setStatus('current')
if mibBuilder.loadTexts: eventLayerDescription.setDescription('Event Layer Description')
eventClassification = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClassification.setStatus('current')
if mibBuilder.loadTexts: eventClassification.setDescription('Event Classification')
eventRepresentation = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventRepresentation.setStatus('current')
if mibBuilder.loadTexts: eventRepresentation.setDescription('Event Representation')
eventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
if mibBuilder.loadTexts: eventSeverity.setDescription('Event Severity')
eventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 5, 1)).setObjects(("PHION-MIB", "eventID"), ("PHION-MIB", "eventIDDescription"), ("PHION-MIB", "eventType"), ("PHION-MIB", "eventAlarmTime"), ("PHION-MIB", "eventLayerDescription"), ("PHION-MIB", "eventClassification"), ("PHION-MIB", "eventRepresentation"), ("PHION-MIB", "eventSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroup = eventGroup.setStatus('current')
if mibBuilder.loadTexts: eventGroup.setDescription(' ')
eventTrap = NotificationType((1, 3, 6, 1, 4, 1, 10704, 11)).setObjects(("PHION-MIB", "eventID"), ("PHION-MIB", "eventIDDescription"), ("PHION-MIB", "eventType"), ("PHION-MIB", "eventAlarmTime"), ("PHION-MIB", "eventLayerDescription"), ("PHION-MIB", "eventClassification"), ("PHION-MIB", "eventRepresentation"), ("PHION-MIB", "eventSeverity"))
if mibBuilder.loadTexts: eventTrap.setStatus('current')
if mibBuilder.loadTexts: eventTrap.setDescription('Trap')
if mibBuilder.loadTexts: eventTrap.setReference(' ')
notificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10704, 21, 5, 2)).setObjects(("PHION-MIB", "eventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationGroup = notificationGroup.setStatus('current')
if mibBuilder.loadTexts: notificationGroup.setDescription(' ')
mibBuilder.exportSymbols("PHION-MIB", boxServicesEntry=boxServicesEntry, fwstatsGroup=fwstatsGroup, class2Drop=class2Drop, raidEventText=raidEventText, bgpNeighborState=bgpNeighborState, notificationGroup=notificationGroup, RaidEventSeverity=RaidEventSeverity, bgpNeighbors=bgpNeighbors, partitionName=partitionName, ospfNeighborId=ospfNeighborId, phionHotfixesEntry=phionHotfixesEntry, trafficshapeGroup=trafficshapeGroup, boxServices=boxServices, fwCompliance=fwCompliance, raidGroup=raidGroup, hwGroups=hwGroups, class2Pakets=class2Pakets, event=event, ospfNeighbors=ospfNeighbors, vpnTunnelsEntry=vpnTunnelsEntry, partitionUsedSpace=partitionUsedSpace, ripGroup=ripGroup, class3Total=class3Total, eventTrap=eventTrap, firewallSessions64=firewallSessions64, noDelayTotal=noDelayTotal, raidEventsEntry=raidEventsEntry, rate=rate, fwStats=fwStats, partitionFreeSpace=partitionFreeSpace, eventGroups=eventGroups, boxServiceName=boxServiceName, trafficShapeEntry=trafficShapeEntry, firewallSessions=firewallSessions, ospfNeighborsEntry=ospfNeighborsEntry, fwGroups=fwGroups, eventAlarmTime=eventAlarmTime, raidEventTime=raidEventTime, serverServiceName=serverServiceName, fwCompliances=fwCompliances, serverServices=serverServices, vpnTunnels=vpnTunnels, packetThroughput=packetThroughput, ospfNeighborInterface=ospfNeighborInterface, netGroups=netGroups, vpnGroup=vpnGroup, partitionMaxSpace=partitionMaxSpace, bgpNeighborAddress=bgpNeighborAddress, phionRelease=phionRelease, boxGroup=boxGroup, serverServicesEntry=serverServicesEntry, sessions=sessions, raidEventIndex=raidEventIndex, diskSpace=diskSpace, vpnusersGroup=vpnusersGroup, firewall=firewall, hotfixInstallTime=hotfixInstallTime, class3Pakets=class3Pakets, bgpNeighborsEntry=bgpNeighborsEntry, diskSpaceEntry=diskSpaceEntry, noDelayPakets=noDelayPakets, serverGroup=serverGroup, hwSensorName=hwSensorName, releaseGroup=releaseGroup, trafficShape=trafficShape, partitionUsedSpacePercent=partitionUsedSpacePercent, serverServiceState=serverServiceState, ripNeighbors=ripNeighbors, diskspaceGroup=diskspaceGroup, eventIDDescription=eventIDDescription, vpnName=vpnName, hwSensorValue=hwSensorValue, eventRepresentation=eventRepresentation, PYSNMP_MODULE_ID=phion, eventSeverity=eventSeverity, dataThroughput64=dataThroughput64, raidEventSev=raidEventSev, packetThroughput64=packetThroughput64, class3Drop=class3Drop, ripNeighborsEntry=ripNeighborsEntry, vpnUsers=vpnUsers, class2Total=class2Total, hwSensors=hwSensors, ServiceState=ServiceState, connectorName=connectorName, phionHotfixes=phionHotfixes, eventClassification=eventClassification, vpnState=vpnState, hwSensorsEntry=hwSensorsEntry, SensorType=SensorType, dataThroughput=dataThroughput, bgpGroup=bgpGroup, ripNeighborAddress=ripNeighborAddress, hwSensorType=hwSensorType, class1Total=class1Total, eventGroup=eventGroup, hotfixName=hotfixName, ospfNeighborAddress=ospfNeighborAddress, firmwareGroups=firmwareGroups, noDelayDrop=noDelayDrop, hotfixGroup=hotfixGroup, hwGroup=hwGroup, ospfGroup=ospfGroup, VpnStates=VpnStates, eventLayerDescription=eventLayerDescription, class1Drop=class1Drop, ripNeighborState=ripNeighborState, ospfNeighborStatus=ospfNeighborStatus, phion=phion, class1Pakets=class1Pakets, serviceGroups=serviceGroups, eventType=eventType, eventID=eventID, raidEvents=raidEvents, fwStatsEntry=fwStatsEntry, boxServiceState=boxServiceState)
