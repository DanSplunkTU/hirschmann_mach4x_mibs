#
# PySNMP MIB module DMTF-SERVICE-LAYER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DMTF-SERVICE-LAYER-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dmiEventStateKey, dmiEventDateTime, dmiCompId, dmiEventSystem, dmiEventSubSystem, dmiEventSeverity, DmiString, DmiDate, dmiEventAssociatedGroup = mibBuilder.importSymbols("DMTF-DMI-MIB", "dmiEventStateKey", "dmiEventDateTime", "dmiCompId", "dmiEventSystem", "dmiEventSubSystem", "dmiEventSeverity", "DmiString", "DmiDate", "dmiEventAssociatedGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DmiCounter(Counter32):
    pass

class DmiCounter64(Counter64):
    pass

class DmiGauge(Gauge32):
    pass

class DmiInteger(Integer32):
    pass

class DmiOctetstring(OctetString):
    pass

class DmiCompId(Integer32):
    pass

class DmiGroupId(Integer32):
    pass

dmtf = MibIdentifier((1, 3, 6, 1, 4, 1, 412))
dmtfStdMifs = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 2))
dmtfDynOids = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 3))
dmtfServiceLayerMIF = ModuleIdentity((1, 3, 6, 1, 4, 1, 412, 2, 1))
if mibBuilder.loadTexts: dmtfServiceLayerMIF.setLastUpdated('9710221800Z')
if mibBuilder.loadTexts: dmtfServiceLayerMIF.setOrganization('Desktop Management Task Force')
dmtfComponentIDTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 1, 1), )
if mibBuilder.loadTexts: dmtfComponentIDTable.setStatus('current')
dmtfComponentIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1), ).setIndexNames((0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"), (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dmtfComponentIDEntry.setStatus('current')
manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 1), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturer.setStatus('current')
product = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 2), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: product.setStatus('current')
version = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 3), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
serialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 4), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
installation = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 5), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installation.setStatus('current')
verify = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("anErrorOccurredCheckStatusCode", 0), ("thisComponentDoesNotExist", 1), ("verificationIsNotSupported", 2), ("reserved", 3), ("thisComponentExistsButTheFunctionalityIsUntested", 4), ("thisComponentExistsButTheFunctionalityIsUnknown", 5), ("thisComponentExistsAndIsNotFunctioningCorrectly", 6), ("thisComponentExistsAndIsFunctioningCorrectly", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: verify.setStatus('current')
dmtfSPIndicationSubscriptionTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 1, 3), )
if mibBuilder.loadTexts: dmtfSPIndicationSubscriptionTable.setStatus('current')
dmtfSPIndicationSubscriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1), ).setIndexNames((0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"), (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberRPCType"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberTransportType"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberAddressing"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberID"))
if mibBuilder.loadTexts: dmtfSPIndicationSubscriptionEntry.setStatus('current')
dmtfSPIndicationSubscriptionState = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtfSPIndicationSubscriptionState.setStatus('current')
subscriberRPCType = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 1), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberRPCType.setStatus('current')
subscriberTransportType = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 2), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberTransportType.setStatus('current')
subscriberAddressing = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 3), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberAddressing.setStatus('current')
subscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberID.setStatus('current')
subscriptionExpirationWarningDateStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 5), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriptionExpirationWarningDateStamp.setStatus('current')
subscriptionExpirationDateStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 6), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriptionExpirationDateStamp.setStatus('current')
indicationFailureThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: indicationFailureThreshold.setStatus('current')
dmtfSPFilterInformationTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 1, 4), )
if mibBuilder.loadTexts: dmtfSPFilterInformationTable.setStatus('current')
dmtfSPFilterInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1), ).setIndexNames((0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"), (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberRPCType"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberTransportType"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberAddressing"), (0, "DMTF-SERVICE-LAYER-MIB", "subscriberID"), (0, "DMTF-SERVICE-LAYER-MIB", "componentID"), (0, "DMTF-SERVICE-LAYER-MIB", "groupClassString"))
if mibBuilder.loadTexts: dmtfSPFilterInformationEntry.setStatus('current')
dmtfSPFilterInformationState = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtfSPFilterInformationState.setStatus('current')
subscriberRPCType2 = MibScalar((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 1), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberRPCType2.setStatus('current')
subscriberTransportType2 = MibScalar((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 2), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberTransportType2.setStatus('current')
subscriberAddressing2 = MibScalar((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 3), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberAddressing2.setStatus('current')
subscriberID2 = MibScalar((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberID2.setStatus('current')
componentID = MibScalar((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentID.setStatus('current')
groupClassString = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 6), DmiString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupClassString.setStatus('current')
eventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("monitor", 1), ("information", 2), ("oK", 4), ("nonCritical-1", 8), ("critical", 16), ("nonRecoverable", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
mibBuilder.exportSymbols("DMTF-SERVICE-LAYER-MIB", dmtf=dmtf, DmiOctetstring=DmiOctetstring, DmiGroupId=DmiGroupId, installation=installation, manufacturer=manufacturer, subscriberRPCType=subscriberRPCType, subscriberAddressing=subscriberAddressing, dmtfSPIndicationSubscriptionTable=dmtfSPIndicationSubscriptionTable, eventSeverity=eventSeverity, DmiGauge=DmiGauge, verify=verify, product=product, dmtfSPFilterInformationState=dmtfSPFilterInformationState, DmiCounter=DmiCounter, subscriberAddressing2=subscriberAddressing2, subscriptionExpirationDateStamp=subscriptionExpirationDateStamp, serialNumber=serialNumber, subscriberTransportType2=subscriberTransportType2, subscriberID2=subscriberID2, dmtfSPFilterInformationTable=dmtfSPFilterInformationTable, indicationFailureThreshold=indicationFailureThreshold, dmtfServiceLayerMIF=dmtfServiceLayerMIF, subscriberID=subscriberID, subscriberRPCType2=subscriberRPCType2, dmtfSPIndicationSubscriptionState=dmtfSPIndicationSubscriptionState, dmtfSPIndicationSubscriptionEntry=dmtfSPIndicationSubscriptionEntry, dmtfStdMifs=dmtfStdMifs, dmtfComponentIDTable=dmtfComponentIDTable, DmiCounter64=DmiCounter64, subscriberTransportType=subscriberTransportType, componentID=componentID, dmtfSPFilterInformationEntry=dmtfSPFilterInformationEntry, DmiCompId=DmiCompId, version=version, dmtfDynOids=dmtfDynOids, groupClassString=groupClassString, DmiInteger=DmiInteger, dmtfComponentIDEntry=dmtfComponentIDEntry, subscriptionExpirationWarningDateStamp=subscriptionExpirationWarningDateStamp, PYSNMP_MODULE_ID=dmtfServiceLayerMIF)
