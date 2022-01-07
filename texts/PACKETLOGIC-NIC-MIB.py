#
# PySNMP MIB module PACKETLOGIC-NIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-NIC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:23:06 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Unsigned32, Counter32, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, TimeTicks, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "TimeTicks", "Integer32", "Counter64")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
nic = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2))
nic.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nic.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: nic.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: nic.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: nic.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: nic.setDescription('MIB for PacketLogic2 Network Interface Modules')
slots = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1), )
if mibBuilder.loadTexts: slots.setStatus('current')
if mibBuilder.loadTexts: slots.setDescription('Conceptual Table')
slotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1), ).setIndexNames((0, "PACKETLOGIC-NIC-MIB", "slotEntryIndex"))
if mibBuilder.loadTexts: slotEntry.setStatus('current')
if mibBuilder.loadTexts: slotEntry.setDescription('Conceptual Table')
slotEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slotEntryIndex.setStatus('current')
if mibBuilder.loadTexts: slotEntryIndex.setDescription('Unique Row Index for Conceptual Table')
channels = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2), )
if mibBuilder.loadTexts: channels.setStatus('current')
if mibBuilder.loadTexts: channels.setDescription('Conceptual Table')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1), ).setIndexNames((0, "PACKETLOGIC-NIC-MIB", "channelEntryIndex"))
if mibBuilder.loadTexts: channelEntry.setStatus('current')
if mibBuilder.loadTexts: channelEntry.setDescription('Conceptual Table')
channelEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: channelEntryIndex.setStatus('current')
if mibBuilder.loadTexts: channelEntryIndex.setDescription('Unique Row Index for Conceptual Table')
slotLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLabel.setStatus('current')
if mibBuilder.loadTexts: slotLabel.setDescription('Slot Label')
slotState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotState.setStatus('current')
if mibBuilder.loadTexts: slotState.setDescription('Slot State')
slotBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotBypass.setStatus('current')
if mibBuilder.loadTexts: slotBypass.setDescription('Slot Bypass Support')
slotChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotChannels.setStatus('current')
if mibBuilder.loadTexts: slotChannels.setDescription('Slot Channels')
slotInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotInterface.setStatus('current')
if mibBuilder.loadTexts: slotInterface.setDescription('Slot Interface Type')
slotPartNo = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotPartNo.setStatus('current')
if mibBuilder.loadTexts: slotPartNo.setDescription('Slot Part Number')
slotPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotPorts.setStatus('current')
if mibBuilder.loadTexts: slotPorts.setDescription('Slot Ports')
slotSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotSpeed.setStatus('current')
if mibBuilder.loadTexts: slotSpeed.setDescription('Slot Speed')
channelLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelLocation.setStatus('current')
if mibBuilder.loadTexts: channelLocation.setDescription('Channel Location')
channelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelLabel.setStatus('current')
if mibBuilder.loadTexts: channelLabel.setDescription('Channel Label')
channelSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelSlot.setStatus('current')
if mibBuilder.loadTexts: channelSlot.setDescription('Slot Label')
totalThroughput = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalThroughput.setStatus('current')
if mibBuilder.loadTexts: totalThroughput.setDescription('Total potential throughput based on capacity of installed NICs (Gb/s)')
mibBuilder.exportSymbols("PACKETLOGIC-NIC-MIB", slots=slots, slotChannels=slotChannels, channelLocation=channelLocation, channelLabel=channelLabel, slotPartNo=slotPartNo, channelEntry=channelEntry, channelSlot=channelSlot, channelEntryIndex=channelEntryIndex, slotInterface=slotInterface, slotEntryIndex=slotEntryIndex, totalThroughput=totalThroughput, slotEntry=slotEntry, slotPorts=slotPorts, PYSNMP_MODULE_ID=nic, slotBypass=slotBypass, slotLabel=slotLabel, slotState=slotState, slotSpeed=slotSpeed, channels=channels, nic=nic)
