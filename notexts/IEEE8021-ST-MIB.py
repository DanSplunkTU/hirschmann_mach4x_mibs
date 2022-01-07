#
# PySNMP MIB module IEEE8021-ST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-ST-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:04 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ieee8021BridgeBasePort, ieee8021BridgeBaseComponentId = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBaseComponentId")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, NotificationType, Unsigned32, Gauge32, ObjectIdentity, Counter32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "IpAddress", "iso", "Integer32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ieee8021STMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 30))
ieee8021STMib.setRevisions(('2018-06-21 00:00', '2016-08-15 00:00', '2016-02-19 00:00',))
if mibBuilder.loadTexts: ieee8021STMib.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: ieee8021STMib.setOrganization('IEEE 802.1 Working Group')
class IEEE8021STTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.29.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021STPTPtimeValue(TextualConvention, OctetString):
    reference = '8.6.8.4, 8.6.9.4, 12.29.1'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

ieee8021STNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 0))
ieee8021STObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1))
ieee8021STConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2))
ieee8021STMaxSDUSubtree = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1, 1))
ieee8021STParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1, 2))
ieee8021STMaxSDUTable = MibTable((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021STMaxSDUTable.setStatus('current')
ieee8021STMaxSDUEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-ST-MIB", "ieee8021STTrafficClass"))
if mibBuilder.loadTexts: ieee8021STMaxSDUEntry.setStatus('current')
ieee8021STTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 1), IEEE8021STTrafficClassValue())
if mibBuilder.loadTexts: ieee8021STTrafficClass.setStatus('current')
ieee8021STMaxSDU = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 2), Unsigned32()).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STMaxSDU.setStatus('current')
ieee8021TransmissionOverrun = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TransmissionOverrun.setStatus('current')
ieee8021STParametersTable = MibTable((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021STParametersTable.setStatus('current')
ieee8021STParametersEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021STParametersEntry.setStatus('current')
ieee8021STGateEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STGateEnabled.setStatus('current')
ieee8021STAdminGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminGateStates.setStatus('current')
ieee8021STOperGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperGateStates.setStatus('current')
ieee8021STAdminControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminControlListLength.setStatus('current')
ieee8021STOperControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperControlListLength.setStatus('current')
ieee8021STAdminControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminControlList.setStatus('current')
ieee8021STOperControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperControlList.setStatus('current')
ieee8021STAdminCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeNumerator.setStatus('current')
ieee8021STAdminCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeDenominator.setStatus('current')
ieee8021STOperCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeNumerator.setStatus('current')
ieee8021STOperCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeDenominator.setStatus('current')
ieee8021STAdminCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 12), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeExtension.setStatus('current')
ieee8021STOperCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 13), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeExtension.setStatus('current')
ieee8021STAdminBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 14), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminBaseTime.setStatus('current')
ieee8021STOperBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 15), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperBaseTime.setStatus('current')
ieee8021STConfigChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STConfigChange.setStatus('current')
ieee8021STConfigChangeTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 17), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigChangeTime.setStatus('current')
ieee8021STTickGranularity = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STTickGranularity.setStatus('current')
ieee8021STCurrentTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 19), IEEE8021STPTPtimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STCurrentTime.setStatus('current')
ieee8021STConfigPending = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigPending.setStatus('current')
ieee8021STConfigChangeError = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigChangeError.setStatus('current')
ieee8021STSupportedListMax = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STSupportedListMax.setStatus('current')
ieee8021STCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2, 1))
ieee8021STGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2, 2))
ieee8021STObjectsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 30, 2, 2, 1)).setObjects(("IEEE8021-ST-MIB", "ieee8021STMaxSDU"), ("IEEE8021-ST-MIB", "ieee8021TransmissionOverrun"), ("IEEE8021-ST-MIB", "ieee8021STGateEnabled"), ("IEEE8021-ST-MIB", "ieee8021STAdminGateStates"), ("IEEE8021-ST-MIB", "ieee8021STOperGateStates"), ("IEEE8021-ST-MIB", "ieee8021STAdminControlListLength"), ("IEEE8021-ST-MIB", "ieee8021STOperControlListLength"), ("IEEE8021-ST-MIB", "ieee8021STAdminControlList"), ("IEEE8021-ST-MIB", "ieee8021STOperControlList"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeNumerator"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeDenominator"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeNumerator"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeDenominator"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeExtension"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeExtension"), ("IEEE8021-ST-MIB", "ieee8021STAdminBaseTime"), ("IEEE8021-ST-MIB", "ieee8021STOperBaseTime"), ("IEEE8021-ST-MIB", "ieee8021STConfigChange"), ("IEEE8021-ST-MIB", "ieee8021STConfigChangeTime"), ("IEEE8021-ST-MIB", "ieee8021STTickGranularity"), ("IEEE8021-ST-MIB", "ieee8021STCurrentTime"), ("IEEE8021-ST-MIB", "ieee8021STConfigPending"), ("IEEE8021-ST-MIB", "ieee8021STConfigChangeError"), ("IEEE8021-ST-MIB", "ieee8021STSupportedListMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021STObjectsGroup = ieee8021STObjectsGroup.setStatus('current')
ieee8021STCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 30, 2, 1, 1)).setObjects(("IEEE8021-ST-MIB", "ieee8021STObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021STCompliance = ieee8021STCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-ST-MIB", ieee8021STParametersTable=ieee8021STParametersTable, ieee8021STConfigChangeError=ieee8021STConfigChangeError, ieee8021STCompliances=ieee8021STCompliances, ieee8021TransmissionOverrun=ieee8021TransmissionOverrun, IEEE8021STTrafficClassValue=IEEE8021STTrafficClassValue, ieee8021STParameters=ieee8021STParameters, ieee8021STTrafficClass=ieee8021STTrafficClass, ieee8021STObjects=ieee8021STObjects, ieee8021STMaxSDUTable=ieee8021STMaxSDUTable, ieee8021STAdminGateStates=ieee8021STAdminGateStates, ieee8021STTickGranularity=ieee8021STTickGranularity, ieee8021STOperBaseTime=ieee8021STOperBaseTime, ieee8021STOperCycleTimeNumerator=ieee8021STOperCycleTimeNumerator, ieee8021STConformance=ieee8021STConformance, ieee8021STOperControlList=ieee8021STOperControlList, ieee8021STOperCycleTimeDenominator=ieee8021STOperCycleTimeDenominator, ieee8021STAdminControlListLength=ieee8021STAdminControlListLength, ieee8021STAdminCycleTimeDenominator=ieee8021STAdminCycleTimeDenominator, ieee8021STMaxSDU=ieee8021STMaxSDU, ieee8021STConfigChangeTime=ieee8021STConfigChangeTime, ieee8021STAdminBaseTime=ieee8021STAdminBaseTime, ieee8021STConfigPending=ieee8021STConfigPending, ieee8021STCompliance=ieee8021STCompliance, ieee8021STMaxSDUSubtree=ieee8021STMaxSDUSubtree, ieee8021STOperCycleTimeExtension=ieee8021STOperCycleTimeExtension, ieee8021STAdminCycleTimeNumerator=ieee8021STAdminCycleTimeNumerator, ieee8021STOperControlListLength=ieee8021STOperControlListLength, ieee8021STCurrentTime=ieee8021STCurrentTime, ieee8021STConfigChange=ieee8021STConfigChange, ieee8021STMaxSDUEntry=ieee8021STMaxSDUEntry, ieee8021STObjectsGroup=ieee8021STObjectsGroup, ieee8021STMib=ieee8021STMib, ieee8021STNotifications=ieee8021STNotifications, ieee8021STOperGateStates=ieee8021STOperGateStates, PYSNMP_MODULE_ID=ieee8021STMib, ieee8021STSupportedListMax=ieee8021STSupportedListMax, ieee8021STParametersEntry=ieee8021STParametersEntry, ieee8021STGateEnabled=ieee8021STGateEnabled, ieee8021STAdminCycleTimeExtension=ieee8021STAdminCycleTimeExtension, ieee8021STGroups=ieee8021STGroups, IEEE8021STPTPtimeValue=IEEE8021STPTPtimeValue, ieee8021STAdminControlList=ieee8021STAdminControlList)
