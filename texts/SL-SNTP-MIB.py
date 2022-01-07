#
# PySNMP MIB module SL-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-SNTP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:50 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, iso, Counter64, Integer32, ModuleIdentity, Bits, Unsigned32, MibIdentifier, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Counter64", "Integer32", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks")
TextualConvention, DisplayString, TimeStamp, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "RowStatus", "TruthValue")
slSntp = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21))
if mibBuilder.loadTexts: slSntp.setLastUpdated('200007240000Z')
if mibBuilder.loadTexts: slSntp.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slSntp.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slSntp.setDescription('This MIB module describes the SNTP Client')
slSntpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1))
slSntpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2))
slSntpConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("unicast", 2), ("broadcast", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigMode.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigMode.setDescription('Current operational mode of SNTP client')
slSntpConfigPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigPollInterval.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigPollInterval.setDescription('Period of time (in seconds) between succesive attempts to \n                  perform an update via SNTP')
slSntpConfigRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 3), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigRetryCount.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigRetryCount.setDescription('The number of query attempts the SNTP client should perform before reporting\n    that the SNTP client cannot communicate with the peer.')
slSntpConfigTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigTimeZone.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigTimeZone.setDescription('The time zone this node is currently located in, expressed as\n    as an hours offset to the GMT (-12..+12).\n    Note:  Daylight savings time is not automatically calculated.')
slSntpConfigDayLightSaving = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigDayLightSaving.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigDayLightSaving.setDescription('It specifies if daylight saving time is applicable.')
slSntpConfigFractTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigFractTimeZone.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigFractTimeZone.setDescription('The fractional part of the timezone specified in minutes (-60..+60).')
slSntpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10), )
if mibBuilder.loadTexts: slSntpConfigTable.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigTable.setDescription('A table containing trusted SNTP servers to be queried in \n                  unicast mode')
slSntpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1), ).setIndexNames((0, "SL-SNTP-MIB", "slSntpConfigAddress"))
if mibBuilder.loadTexts: slSntpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigEntry.setDescription('A trusted server and its expected version number')
slSntpConfigAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigAddress.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigAddress.setDescription('Ip Address of a trusted SNTP server.')
slSntpConfigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigVersion.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigVersion.setDescription('Protocol version used by this SNTP server')
slSntpConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigPriority.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigPriority.setDescription('Priority given to this server.')
slSntpConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigRowStatus.setDescription('The Status of this SNTP server information.')
slSntpConfigMaxVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7200000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigMaxVariance.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigMaxVariance.setDescription('The variance expressed as the number of milliseconds between client and \n    peer which will trigger an alarm.  This is useful in determining if the \n    historical data recorded in NOVRAM for statistics trending or timestamps \n    used for traps is outside the configured variance parameter.')
slSntpConfigVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSntpConfigVariance.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigVariance.setDescription('The amount of time expressed as the number of milliseconds delta between \n    client and peer.')
slSntpConfigVarianceDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigVarianceDetectEnable.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigVarianceDetectEnable.setDescription('Used to enable or disable variance threshold alarms.')
slSntpConfigServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("disconnected", 1), ("connected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSntpConfigServerStatus.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigServerStatus.setDescription('The status of this srever.')
slSntpPeerFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 1)).setObjects(("SL-SNTP-MIB", "slSntpConfigAddress"))
if mibBuilder.loadTexts: slSntpPeerFailureTrap.setStatus('current')
if mibBuilder.loadTexts: slSntpPeerFailureTrap.setDescription('The SNTP Client is unable to communicate with the NTP Server which \n    has been configured.')
slSntpConfigVarianceTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 2)).setObjects(("SL-SNTP-MIB", "slSntpConfigAddress"), ("SL-SNTP-MIB", "slSntpConfigMaxVariance"), ("SL-SNTP-MIB", "slSntpConfigVariance"))
if mibBuilder.loadTexts: slSntpConfigVarianceTrap.setStatus('current')
if mibBuilder.loadTexts: slSntpConfigVarianceTrap.setDescription('The difference in time between client and peer exceeds the configured\n    variance.')
mibBuilder.exportSymbols("SL-SNTP-MIB", slSntpConfigPriority=slSntpConfigPriority, slSntpConfigVariance=slSntpConfigVariance, slSntpConfigVarianceDetectEnable=slSntpConfigVarianceDetectEnable, slSntpConfigRetryCount=slSntpConfigRetryCount, slSntpConfigDayLightSaving=slSntpConfigDayLightSaving, PYSNMP_MODULE_ID=slSntp, slSntpConfigTable=slSntpConfigTable, slSntpConfigServerStatus=slSntpConfigServerStatus, slSntpConfigPollInterval=slSntpConfigPollInterval, slSntpConfigVarianceTrap=slSntpConfigVarianceTrap, slSntpConfigFractTimeZone=slSntpConfigFractTimeZone, slSntpConfigMaxVariance=slSntpConfigMaxVariance, slSntpConfig=slSntpConfig, slSntpConfigTimeZone=slSntpConfigTimeZone, slSntpPeerFailureTrap=slSntpPeerFailureTrap, slSntpConfigMode=slSntpConfigMode, slSntpConfigEntry=slSntpConfigEntry, slSntpConfigAddress=slSntpConfigAddress, slSntp=slSntp, slSntpConfigVersion=slSntpConfigVersion, slSntpTraps=slSntpTraps, slSntpConfigRowStatus=slSntpConfigRowStatus)
