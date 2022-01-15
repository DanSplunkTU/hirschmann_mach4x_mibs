#
# PySNMP MIB module AT-PLUGGABLE-DIAGNOSTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-PLUGGABLE-DIAGNOSTICS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:51:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, Gauge32, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atPluggableDiag = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28))
atPluggableDiag.setRevisions(('2015-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atPluggableDiag.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: atPluggableDiag.setLastUpdated('201507170000Z')
if mibBuilder.loadTexts: atPluggableDiag.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atPluggableDiag.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atPluggableDiag.setDescription('The AT Pluggbale Diagnostics MIB contains objects to retrieve the standard\n        diagnostic information from installed SFP modules.')
atPluggableDiagTable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1))
atPluggableDiagTempTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1), )
if mibBuilder.loadTexts: atPluggableDiagTempTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempTable.setDescription('A table of information regarding the various temperature parameters observed\n           as a part of Digital diagnostics monitoring, for all the optical pluggables\n           installed in the devices.')
atPluggableDiagTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempChannel"))
if mibBuilder.loadTexts: atPluggableDiagTempEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempEntry.setDescription('The information about various temperature parameters of pluggables\n        such as current status reading, current alarm status, higher and lower\n        alarm threshold, current warning, higher and lower warning threshold.')
atPluggableDiagTempIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTempIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagTempChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTempChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagTempStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 3), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempStatusReading.setDescription('The current temperature status reading.')
atPluggableDiagTempCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempCurrentAlarm.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempCurrentAlarm.setDescription('The current temperature alarm reading.')
atPluggableDiagTempAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 5), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMax.setDescription('The maximum temperature alarm threshold value.')
atPluggableDiagTempAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 6), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMin.setDescription('The minimum temperature alarm threshold value.')
atPluggableDiagTempCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempCurrentWarning.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempCurrentWarning.setDescription('The current temperature warnings.')
atPluggableDiagTempWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 8), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempWarningMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempWarningMax.setDescription('The maximum temperature warning threshold value.')
atPluggableDiagTempWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 9), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempWarningMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTempWarningMin.setDescription('The minimum temperature warning threshold value.')
atPluggableDiagVccTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2), )
if mibBuilder.loadTexts: atPluggableDiagVccTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccTable.setDescription('A table of information regarding the various Voltage (Vcc) parameters observed\n        as a part of Digital diagnostics monitoring, for all the optical pluggables\n        installed in the devices.')
atPluggableDiagVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccChannel"))
if mibBuilder.loadTexts: atPluggableDiagVccEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccEntry.setDescription('The information about various Voltage (Vcc) parameters of pluggables\n        such as current status reading, current alarm status, higher and lower\n        alarm threshold, current warning, higher and lower warning threshold.')
atPluggableDiagVccIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagVccIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagVccChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagVccChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagVccStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 3), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccStatusReading.setDescription('The current Voltage (Vcc) status reading.')
atPluggableDiagVccCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccCurrentAlarm.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccCurrentAlarm.setDescription('The current Voltage (Vcc) alarm reading.')
atPluggableDiagVccAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 5), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMax.setDescription('The maximum Voltage (Vcc) alarm threshold value.')
atPluggableDiagVccAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 6), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMin.setDescription('The minimum Voltage (Vcc) alarm threshold value.')
atPluggableDiagVccCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccCurrentWarning.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccCurrentWarning.setDescription('The current Voltage (Vcc) warnings.')
atPluggableDiagVccWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 8), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccWarningMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccWarningMax.setDescription('The maximum Voltage (Vcc) warning threshold value.')
atPluggableDiagVccWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 9), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccWarningMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagVccWarningMin.setDescription('The minimum Voltage (Vcc) warning threshold value.')
atPluggableDiagTxBiasTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3), )
if mibBuilder.loadTexts: atPluggableDiagTxBiasTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasTable.setDescription('A table of information regarding the various Tx Bias Current (mA)\n        parameters observed as a part of Digital diagnostics monitoring,\n        for all the optical pluggables installed in the devices.')
atPluggableDiagTxBiasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasChannel"))
if mibBuilder.loadTexts: atPluggableDiagTxBiasEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasEntry.setDescription('The information about various Tx Bias Current (mA)\n        parameters of pluggables such as current status reading,\n        current alarm status, higher and lower alarm threshold,\n        current warning, higher and lower warning threshold.')
atPluggableDiagTxBiasIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTxBiasIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagTxBiasChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTxBiasChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagTxBiasStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 3), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasStatusReading.setDescription('The current Tx Bias (mA) status reading.')
atPluggableDiagTxBiasCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentAlarm.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentAlarm.setDescription('The current Tx Bias (mA) alarm reading.')
atPluggableDiagTxBiasAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 5), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMax.setDescription('The maximum Tx Bias (mA) alarm threshold value.')
atPluggableDiagTxBiasAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 6), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMin.setDescription('The minimum Tx Bias (mA) alarm threshold value.')
atPluggableDiagTxBiasCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentWarning.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentWarning.setDescription('The current Tx Bias (mA) warnings.')
atPluggableDiagTxBiasWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 8), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMax.setDescription('The maximum Tx Bias (mA) warning threshold value.')
atPluggableDiagTxBiasWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 9), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMin.setDescription('The minimum Tx Bias (mA) warning threshold value.')
atPluggableDiagTxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4), )
if mibBuilder.loadTexts: atPluggableDiagTxPowerTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerTable.setDescription('A table of information regarding the various Tx Power (mW)\n        parameters observed as a part of Digital diagnostics monitoring,\n        for all the optical pluggables installed in the devices.')
atPluggableDiagTxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerChannel"))
if mibBuilder.loadTexts: atPluggableDiagTxPowerEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerEntry.setDescription('The information about various Tx Power (mW)\n        parameters of pluggables such as current status reading,\n        current alarm status, higher and lower alarm threshold,\n        current warning, higher and lower warning threshold.')
atPluggableDiagTxPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTxPowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagTxPowerChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTxPowerChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagTxPowerStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 3), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerStatusReading.setDescription('The current Tx Power (mW) status reading.')
atPluggableDiagTxPowerCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentAlarm.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentAlarm.setDescription('The current Tx Power (mW) alarm reading.')
atPluggableDiagTxPowerAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 5), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMax.setDescription('The maximum Tx Power (mW) alarm threshold value.')
atPluggableDiagTxPowerAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 6), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMin.setDescription('The minimum Tx Power (mW) alarm threshold value.')
atPluggableDiagTxPowerCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentWarning.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentWarning.setDescription('The current Tx Power (mW) warnings.')
atPluggableDiagTxPowerWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 8), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMax.setDescription('The maximum Tx Power (mW) warning threshold value.')
atPluggableDiagTxPowerWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 9), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMin.setDescription('The minimum Tx Power (mW) warning threshold value.')
atPluggableDiagRxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5), )
if mibBuilder.loadTexts: atPluggableDiagRxPowerTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerTable.setDescription('A table of information regarding the various Rx Power (mW)\n        parameters observed as a part of Digital diagnostics monitoring,\n        for all the optical pluggables installed in the devices.')
atPluggableDiagRxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerChannel"))
if mibBuilder.loadTexts: atPluggableDiagRxPowerEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerEntry.setDescription('The information about various Rx Power (mW)\n        parameters of pluggables such as current status reading,\n        current alarm status, higher and lower alarm threshold,\n        current warning, higher and lower warning threshold.')
atPluggableDiagRxPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagRxPowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagRxPowerChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagRxPowerChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagRxPowerStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 3), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerStatusReading.setDescription('The current Rx Power (mW) status reading.')
atPluggableDiagRxPowerCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentAlarm.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentAlarm.setDescription('The current Rx Power (mW) alarm reading.')
atPluggableDiagRxPowerAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 5), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMax.setDescription('The maximum Rx Power (mW) alarm threshold value.')
atPluggableDiagRxPowerAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 6), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMin.setDescription('The minimum Rx Power (mW) alarm threshold value.')
atPluggableDiagRxPowerCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentWarning.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentWarning.setDescription('The current Rx Power (mW) warnings.')
atPluggableDiagRxPowerWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 8), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMax.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMax.setDescription('The maximum Rx Power (mW) warning threshold value.')
atPluggableDiagRxPowerWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 9), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMin.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMin.setDescription('The minimum Rx Power (mW) warning threshold value.')
atPluggableDiagRxLosTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6), )
if mibBuilder.loadTexts: atPluggableDiagRxLosTable.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxLosTable.setDescription('A table of information regarding the Rx Loss of Singal (Los)\n        parameters observed as a part of Digital diagnostics monitoring,\n        for all the optical pluggables installed in the devices.')
atPluggableDiagRxLosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosChannel"))
if mibBuilder.loadTexts: atPluggableDiagRxLosEntry.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxLosEntry.setDescription('The information about various Rx Loss of Singal (Los) parameters\n        of pluggables such as current status reading.')
atPluggableDiagRxLosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagRxLosIfIndex.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxLosIfIndex.setDescription('The ifindex of the pluggable.')
atPluggableDiagRxLosChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagRxLosChannel.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxLosChannel.setDescription('The channel number of the pluggable.')
atPluggableDiagRxLosStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxLosStatusReading.setStatus('current')
if mibBuilder.loadTexts: atPluggableDiagRxLosStatusReading.setDescription('The current Rx Los status reading.')
mibBuilder.exportSymbols("AT-PLUGGABLE-DIAGNOSTICS-MIB", atPluggableDiagTxBiasCurrentWarning=atPluggableDiagTxBiasCurrentWarning, atPluggableDiagRxPowerEntry=atPluggableDiagRxPowerEntry, atPluggableDiagRxPowerWarningMin=atPluggableDiagRxPowerWarningMin, atPluggableDiagTxPowerIfIndex=atPluggableDiagTxPowerIfIndex, atPluggableDiagVccAlarmMin=atPluggableDiagVccAlarmMin, atPluggableDiagRxPowerCurrentWarning=atPluggableDiagRxPowerCurrentWarning, atPluggableDiagRxLosStatusReading=atPluggableDiagRxLosStatusReading, atPluggableDiagTempStatusReading=atPluggableDiagTempStatusReading, atPluggableDiagTempCurrentAlarm=atPluggableDiagTempCurrentAlarm, atPluggableDiagVccStatusReading=atPluggableDiagVccStatusReading, atPluggableDiagTempEntry=atPluggableDiagTempEntry, atPluggableDiagRxPowerStatusReading=atPluggableDiagRxPowerStatusReading, atPluggableDiagTxBiasCurrentAlarm=atPluggableDiagTxBiasCurrentAlarm, atPluggableDiagRxLosTable=atPluggableDiagRxLosTable, atPluggableDiagRxPowerCurrentAlarm=atPluggableDiagRxPowerCurrentAlarm, atPluggableDiagTempWarningMin=atPluggableDiagTempWarningMin, atPluggableDiagTxPowerTable=atPluggableDiagTxPowerTable, atPluggableDiagVccAlarmMax=atPluggableDiagVccAlarmMax, atPluggableDiagTxBiasWarningMax=atPluggableDiagTxBiasWarningMax, atPluggableDiagTxPowerAlarmMax=atPluggableDiagTxPowerAlarmMax, atPluggableDiagTable=atPluggableDiagTable, atPluggableDiagRxPowerTable=atPluggableDiagRxPowerTable, atPluggableDiagRxPowerIfIndex=atPluggableDiagRxPowerIfIndex, atPluggableDiagTempAlarmMax=atPluggableDiagTempAlarmMax, atPluggableDiagRxPowerAlarmMax=atPluggableDiagRxPowerAlarmMax, atPluggableDiagTxPowerCurrentWarning=atPluggableDiagTxPowerCurrentWarning, atPluggableDiagTxPowerAlarmMin=atPluggableDiagTxPowerAlarmMin, atPluggableDiagVccEntry=atPluggableDiagVccEntry, atPluggableDiagTxBiasEntry=atPluggableDiagTxBiasEntry, atPluggableDiagTxPowerWarningMin=atPluggableDiagTxPowerWarningMin, atPluggableDiagTempWarningMax=atPluggableDiagTempWarningMax, atPluggableDiagTempTable=atPluggableDiagTempTable, atPluggableDiagVccCurrentWarning=atPluggableDiagVccCurrentWarning, atPluggableDiagTxBiasChannel=atPluggableDiagTxBiasChannel, atPluggableDiagRxPowerChannel=atPluggableDiagRxPowerChannel, atPluggableDiagTempChannel=atPluggableDiagTempChannel, atPluggableDiagTxPowerChannel=atPluggableDiagTxPowerChannel, atPluggableDiagTempAlarmMin=atPluggableDiagTempAlarmMin, atPluggableDiagTempCurrentWarning=atPluggableDiagTempCurrentWarning, atPluggableDiagTxPowerStatusReading=atPluggableDiagTxPowerStatusReading, atPluggableDiagTxBiasAlarmMin=atPluggableDiagTxBiasAlarmMin, atPluggableDiagVccTable=atPluggableDiagVccTable, atPluggableDiagRxLosIfIndex=atPluggableDiagRxLosIfIndex, atPluggableDiagRxLosEntry=atPluggableDiagRxLosEntry, atPluggableDiagTxPowerCurrentAlarm=atPluggableDiagTxPowerCurrentAlarm, atPluggableDiagTxBiasStatusReading=atPluggableDiagTxBiasStatusReading, atPluggableDiagTempIfIndex=atPluggableDiagTempIfIndex, PYSNMP_MODULE_ID=atPluggableDiag, atPluggableDiagVccIfIndex=atPluggableDiagVccIfIndex, atPluggableDiagTxPowerEntry=atPluggableDiagTxPowerEntry, atPluggableDiagTxBiasWarningMin=atPluggableDiagTxBiasWarningMin, atPluggableDiagRxPowerAlarmMin=atPluggableDiagRxPowerAlarmMin, atPluggableDiagRxLosChannel=atPluggableDiagRxLosChannel, atPluggableDiagTxBiasAlarmMax=atPluggableDiagTxBiasAlarmMax, atPluggableDiag=atPluggableDiag, atPluggableDiagVccChannel=atPluggableDiagVccChannel, atPluggableDiagTxBiasTable=atPluggableDiagTxBiasTable, atPluggableDiagVccCurrentAlarm=atPluggableDiagVccCurrentAlarm, atPluggableDiagTxPowerWarningMax=atPluggableDiagTxPowerWarningMax, atPluggableDiagRxPowerWarningMax=atPluggableDiagRxPowerWarningMax, atPluggableDiagTxBiasIfIndex=atPluggableDiagTxBiasIfIndex, atPluggableDiagVccWarningMax=atPluggableDiagVccWarningMax, atPluggableDiagVccWarningMin=atPluggableDiagVccWarningMin)
