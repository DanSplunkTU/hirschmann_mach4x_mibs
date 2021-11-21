#
# PySNMP MIB module SUPERMICRO-HEALTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-HEALTH-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:36:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, NotificationType, TimeTicks, Bits, MibIdentifier, Gauge32, Integer32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "NotificationType", "TimeTicks", "Bits", "MibIdentifier", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
smHealth, = mibBuilder.importSymbols("SUPERMICRO-SMI", "smHealth")
smHealthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 2, 1))
if mibBuilder.loadTexts: smHealthMIB.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: smHealthMIB.setOrganization('Super Micro Computer Inc.')
if mibBuilder.loadTexts: smHealthMIB.setContactInfo('\tSoftware Lab\n\n\t\tPostal: 980 Rock Avenue\n\t\t\tSan Jose, CA  95131\n\t\t\tUSA\n\n\t\t   Tel: +1 408 503 8000\n\n\t\tE-mail: SoftLab@supermicro.com')
if mibBuilder.loadTexts: smHealthMIB.setDescription('MIB module for monitoring health information')
class SMHealthInfoTypes(TextualConvention, Integer32):
    description = 'Represents the different types of health information that\n\t\tmay be present in a managed device.  The following health\n\t\tinformation types are currently predefined:\n\t\t\t0:  fan speed\n\t\t\t1:  voltage\n\t\t\t2:  temperature\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

smHealthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1))
smHealthMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1), )
if mibBuilder.loadTexts: smHealthMonitorTable.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorTable.setDescription('A table of health monitoring entries.')
smHealthMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1), ).setIndexNames((0, "SUPERMICRO-HEALTH-MIB", "smHealthMonitorIndex"))
if mibBuilder.loadTexts: smHealthMonitorEntry.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorEntry.setDescription('An entry in the health monitoring table.\n\t\tEntries cannot be created or deleted via SNMP operations.')
smHealthMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: smHealthMonitorIndex.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorIndex.setDescription('The unique value identifies this Monitor device.')
smHealthMonitorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorName.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorName.setDescription('A textual full name assigned to the Monitor device.\n\t\tThis object is suitable for output to a human operator.')
smHealthMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 3), SMHealthInfoTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorType.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorType.setDescription('Identifies this Monitor device type.')
smHealthMonitorReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorReading.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorReading.setDescription('Indicates the reading value for the Monitor device that are currently in use on the managed device.\n\t\tFAN readings are displayed in RPM.\n\t\tVoltage readings are displayed in mV.\n\t\tTemperture readings are displayed in Celsius.')
smHealthMonitorHighLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorHighLimit.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorHighLimit.setDescription('Indicates the the High limit for the Monitor device that are currently in use on the managed device.\n\t\tThis is applied to Temperature and Voltage devices only.\n\t\tVoltage limit is displayed in mV, and Temperture limit is displayed in Celsius.')
smHealthMonitorLowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorLowLimit.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorLowLimit.setDescription('Indicates the value for the Low limitation for the Monitor device that are currently in use on the managed device.\n\t\tFAN limit is displayed in RPM, Voltage limit is displayed in mV, and Temperture limit is displayed in Celsius.')
smHealthMonitorMaxReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMaxReading.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorMaxReading.setDescription('Indicates the value for the possible Maximum reading value for the Monitor device that are currently in use on the managed device.\n\t\tFAN readings are displayed in RPM.\n\t\tVoltage readings are displayed in mV.\n\t\tTemperture readings are in Celsius.')
smHealthMonitorMinReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMinReading.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorMinReading.setDescription('Indicates the value for the possible Minimum reading value for the Monitor device that are currently in use on the managed device.\n\t\tFAN readings are displayed in RPM.\n\t\tVoltage readings are displayed in mV.\n\t\tTemperture readings are displayed in Celsius.')
smHealthMonitorDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorDivisor.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorDivisor.setDescription('Indicates the value for the Divisor for the Fan device that are currently in use on the managed device.\n\t\tThis is applied to Fan devices only.')
smHealthMonitorMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorMonitor.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorMonitor.setDescription('Indicates the monitoring status for the Fan device that are currently in use on the managed device.\n\t\t0 = not monitored, 1 = monitored.')
smHealthMonitorReadingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorReadingUnit.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorReadingUnit.setDescription('Indicates the reading unit of the monitor device.')
smHealthMonitorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorStatus.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorStatus.setDescription('Indicates the status of the monitor device. Values:\n\t\t 0: OK\n\t\t 1: Warning\n\t\t 2: Critical\n\t\t')
smHealthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 2))
smHealthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3))
smHealthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1))
smHealthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2))
smHealthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthCompliance = smHealthCompliance.setStatus('current')
if mibBuilder.loadTexts: smHealthCompliance.setDescription('The compliance statement for entities which implement\n\t\tthe Supermicro Health Monitoring MIB')
smHealthMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorType"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorName"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorHighLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorLowLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMaxReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMinReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMonitor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthMonitorGroup = smHealthMonitorGroup.setStatus('current')
if mibBuilder.loadTexts: smHealthMonitorGroup.setDescription('A collection of objects providing Monitor devices.')
smHealthAllinoneStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthAllinoneStatus.setStatus('current')
if mibBuilder.loadTexts: smHealthAllinoneStatus.setDescription('Indicates the all-in-one status of the monitoring items. Values:\n\t\t 0: OK\n\t\t 1: Warning\n\t\t 2: Critical\n\t\t')
smHealthAllinoneMsg = MibScalar((1, 3, 6, 1, 4, 1, 10876, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthAllinoneMsg.setStatus('current')
if mibBuilder.loadTexts: smHealthAllinoneMsg.setDescription('The all-in-one status message of the monitoring items.')
mibBuilder.exportSymbols("SUPERMICRO-HEALTH-MIB", smHealthConformance=smHealthConformance, smHealthCompliances=smHealthCompliances, SMHealthInfoTypes=SMHealthInfoTypes, smHealthObjects=smHealthObjects, smHealthGroups=smHealthGroups, smHealthAllinoneMsg=smHealthAllinoneMsg, smHealthMonitorType=smHealthMonitorType, smHealthMonitorMonitor=smHealthMonitorMonitor, smHealthCompliance=smHealthCompliance, smHealthMonitorIndex=smHealthMonitorIndex, smHealthMonitorStatus=smHealthMonitorStatus, smHealthMonitorMaxReading=smHealthMonitorMaxReading, smHealthAllinoneStatus=smHealthAllinoneStatus, smHealthMonitorGroup=smHealthMonitorGroup, smHealthMonitorLowLimit=smHealthMonitorLowLimit, smHealthMonitorMinReading=smHealthMonitorMinReading, PYSNMP_MODULE_ID=smHealthMIB, smHealthMonitorName=smHealthMonitorName, smHealthMonitorTable=smHealthMonitorTable, smHealthMonitorDivisor=smHealthMonitorDivisor, smHealthNotifications=smHealthNotifications, smHealthMonitorReading=smHealthMonitorReading, smHealthMIB=smHealthMIB, smHealthMonitorHighLimit=smHealthMonitorHighLimit, smHealthMonitorReadingUnit=smHealthMonitorReadingUnit, smHealthMonitorEntry=smHealthMonitorEntry)
