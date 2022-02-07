#
# PySNMP MIB module CTRON-SFPS-SOFTLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-SOFTLINK-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
sfpsCentersFacility, sfpsMcastFacility, sfpsVNSFacility, sfpsBetaFacility, sfpsLiteFacility, sfpsRAFacility, sfpsCallTapFacility, sfpsFpcFacility, sfpsVLANFacility, sfpsUpLinkFacility, sfpsDiagFacility, sfpsFabricFacility = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsCentersFacility", "sfpsMcastFacility", "sfpsVNSFacility", "sfpsBetaFacility", "sfpsLiteFacility", "sfpsRAFacility", "sfpsCallTapFacility", "sfpsFpcFacility", "sfpsVLANFacility", "sfpsUpLinkFacility", "sfpsDiagFacility", "sfpsFabricFacility")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class HexInteger(Integer32):
    pass

sfpsCentersFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1), )
if mibBuilder.loadTexts: sfpsCentersFacilityTable.setStatus('mandatory')
sfpsCentersFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsCentersFacilityAddress"))
if mibBuilder.loadTexts: sfpsCentersFacilityEntry.setStatus('mandatory')
sfpsCentersFacilityAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityAddress.setStatus('mandatory')
sfpsCentersFacilityMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityMetric.setStatus('mandatory')
sfpsCentersFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityElementName.setStatus('mandatory')
sfpsCentersFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityOperStatus.setStatus('mandatory')
sfpsCentersFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCentersFacilityAdminStatus.setStatus('mandatory')
sfpsCentersFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityStatusTime.setStatus('mandatory')
sfpsCentersFacilityRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityRequests.setStatus('mandatory')
sfpsCentersFacilityResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCentersFacilityResponses.setStatus('mandatory')
sfpsBetaFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1), )
if mibBuilder.loadTexts: sfpsBetaFacilityTable.setStatus('mandatory')
sfpsBetaFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsBetaFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsBetaFacilityEntry.setStatus('mandatory')
sfpsBetaFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsBetaFacilityHashIndex.setStatus('mandatory')
sfpsBetaFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsBetaFacilityElementName.setStatus('mandatory')
sfpsBetaFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsBetaFacilityAdminStatus.setStatus('mandatory')
sfpsBetaFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsBetaFacilityOperStatus.setStatus('mandatory')
sfpsBetaFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsBetaFacilityStatusTime.setStatus('mandatory')
sfpsCallTapFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1), )
if mibBuilder.loadTexts: sfpsCallTapFacilityTable.setStatus('mandatory')
sfpsCallTapFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsCallTapFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsCallTapFacilityEntry.setStatus('mandatory')
sfpsCallTapFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTapFacilityHashIndex.setStatus('mandatory')
sfpsCallTapFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTapFacilityElementName.setStatus('mandatory')
sfpsCallTapFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapFacilityAdminStatus.setStatus('mandatory')
sfpsCallTapFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTapFacilityOperStatus.setStatus('mandatory')
sfpsCallTapFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTapFacilityStatusTime.setStatus('mandatory')
sfpsDiagFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1), )
if mibBuilder.loadTexts: sfpsDiagFacilityTable.setStatus('mandatory')
sfpsDiagFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsDiagFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsDiagFacilityEntry.setStatus('mandatory')
sfpsDiagFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagFacilityHashIndex.setStatus('mandatory')
sfpsDiagFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagFacilityElementName.setStatus('mandatory')
sfpsDiagFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagFacilityAdminStatus.setStatus('mandatory')
sfpsDiagFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagFacilityOperStatus.setStatus('mandatory')
sfpsDiagFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagFacilityStatusTime.setStatus('mandatory')
sfpsFabricFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1), )
if mibBuilder.loadTexts: sfpsFabricFacilityTable.setStatus('mandatory')
sfpsFabricFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsFabricFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsFabricFacilityEntry.setStatus('mandatory')
sfpsFabricFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFabricFacilityHashIndex.setStatus('mandatory')
sfpsFabricFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFabricFacilityElementName.setStatus('mandatory')
sfpsFabricFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsFabricFacilityAdminStatus.setStatus('mandatory')
sfpsFabricFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFabricFacilityOperStatus.setStatus('mandatory')
sfpsFabricFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFabricFacilityStatusTime.setStatus('mandatory')
sfpsLiteFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1), )
if mibBuilder.loadTexts: sfpsLiteFacilityTable.setStatus('mandatory')
sfpsLiteFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsLiteFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsLiteFacilityEntry.setStatus('mandatory')
sfpsLiteFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsLiteFacilityHashIndex.setStatus('mandatory')
sfpsLiteFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsLiteFacilityElementName.setStatus('mandatory')
sfpsLiteFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsLiteFacilityAdminStatus.setStatus('mandatory')
sfpsLiteFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsLiteFacilityOperStatus.setStatus('mandatory')
sfpsLiteFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsLiteFacilityStatusTime.setStatus('mandatory')
sfpsFpcFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1), )
if mibBuilder.loadTexts: sfpsFpcFacilityTable.setStatus('mandatory')
sfpsFpcFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsFpcFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsFpcFacilityEntry.setStatus('mandatory')
sfpsFpcFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFpcFacilityHashIndex.setStatus('mandatory')
sfpsFpcFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFpcFacilityElementName.setStatus('mandatory')
sfpsFpcFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsFpcFacilityAdminStatus.setStatus('mandatory')
sfpsFpcFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFpcFacilityOperStatus.setStatus('mandatory')
sfpsFpcFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFpcFacilityStatusTime.setStatus('mandatory')
sfpsMcastFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1), )
if mibBuilder.loadTexts: sfpsMcastFacilityTable.setStatus('mandatory')
sfpsMcastFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsMcastFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsMcastFacilityEntry.setStatus('mandatory')
sfpsMcastFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMcastFacilityHashIndex.setStatus('mandatory')
sfpsMcastFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMcastFacilityElementName.setStatus('mandatory')
sfpsMcastFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMcastFacilityAdminStatus.setStatus('mandatory')
sfpsMcastFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMcastFacilityOperStatus.setStatus('mandatory')
sfpsMcastFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMcastFacilityStatusTime.setStatus('mandatory')
sfpsVLANFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1), )
if mibBuilder.loadTexts: sfpsVLANFacilityTable.setStatus('mandatory')
sfpsVLANFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsVLANFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsVLANFacilityEntry.setStatus('mandatory')
sfpsVLANFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVLANFacilityHashIndex.setStatus('mandatory')
sfpsVLANFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVLANFacilityElementName.setStatus('mandatory')
sfpsVLANFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVLANFacilityAdminStatus.setStatus('mandatory')
sfpsVLANFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVLANFacilityOperStatus.setStatus('mandatory')
sfpsVLANFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVLANFacilityStatusTime.setStatus('mandatory')
sfpsVNSFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1), )
if mibBuilder.loadTexts: sfpsVNSFacilityTable.setStatus('mandatory')
sfpsVNSFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsVNSFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsVNSFacilityEntry.setStatus('mandatory')
sfpsVNSFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVNSFacilityHashIndex.setStatus('mandatory')
sfpsVNSFacilityElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVNSFacilityElementName.setStatus('mandatory')
sfpsVNSFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kControlOther", 1), ("kControlDisable", 2), ("kControlEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVNSFacilityAdminStatus.setStatus('mandatory')
sfpsVNSFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVNSFacilityOperStatus.setStatus('mandatory')
sfpsVNSFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsVNSFacilityStatusTime.setStatus('mandatory')
sfpsRAFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1), )
if mibBuilder.loadTexts: sfpsRAFacilityTable.setStatus('mandatory')
sfpsRAFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsRAFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsRAFacilityEntry.setStatus('mandatory')
sfpsRAFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsRAFacilityHashIndex.setStatus('mandatory')
sfpsRAFacilityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsRAFacilityName.setStatus('mandatory')
sfpsRAFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsRAFacilityAdminStatus.setStatus('mandatory')
sfpsRAFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("halted", 2), ("pending", 3), ("faulted", 4), ("notStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsRAFacilityOperStatus.setStatus('mandatory')
sfpsRAFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsRAFacilityStatusTime.setStatus('mandatory')
sfpsUplinkFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1), )
if mibBuilder.loadTexts: sfpsUplinkFacilityTable.setStatus('mandatory')
sfpsUplinkFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsUplinkFacilityHashIndex"))
if mibBuilder.loadTexts: sfpsUplinkFacilityEntry.setStatus('mandatory')
sfpsUplinkFacilityHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsUplinkFacilityHashIndex.setStatus('mandatory')
sfpsUplinkFacilityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsUplinkFacilityName.setStatus('mandatory')
sfpsUplinkFacilityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsUplinkFacilityAdminStatus.setStatus('mandatory')
sfpsUplinkFacilityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("halted", 2), ("pending", 3), ("faulted", 4), ("notStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsUplinkFacilityOperStatus.setStatus('mandatory')
sfpsUplinkFacilityStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsUplinkFacilityStatusTime.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-SOFTLINK-MIB", sfpsCentersFacilityMetric=sfpsCentersFacilityMetric, sfpsVLANFacilityOperStatus=sfpsVLANFacilityOperStatus, sfpsCentersFacilityStatusTime=sfpsCentersFacilityStatusTime, sfpsFabricFacilityTable=sfpsFabricFacilityTable, sfpsFpcFacilityOperStatus=sfpsFpcFacilityOperStatus, sfpsVNSFacilityAdminStatus=sfpsVNSFacilityAdminStatus, sfpsFpcFacilityTable=sfpsFpcFacilityTable, sfpsLiteFacilityElementName=sfpsLiteFacilityElementName, sfpsRAFacilityName=sfpsRAFacilityName, sfpsCallTapFacilityTable=sfpsCallTapFacilityTable, sfpsDiagFacilityTable=sfpsDiagFacilityTable, sfpsFabricFacilityStatusTime=sfpsFabricFacilityStatusTime, sfpsBetaFacilityAdminStatus=sfpsBetaFacilityAdminStatus, sfpsRAFacilityOperStatus=sfpsRAFacilityOperStatus, sfpsCentersFacilityElementName=sfpsCentersFacilityElementName, sfpsBetaFacilityOperStatus=sfpsBetaFacilityOperStatus, sfpsBetaFacilityElementName=sfpsBetaFacilityElementName, sfpsVNSFacilityStatusTime=sfpsVNSFacilityStatusTime, sfpsBetaFacilityHashIndex=sfpsBetaFacilityHashIndex, sfpsCentersFacilityTable=sfpsCentersFacilityTable, sfpsFabricFacilityAdminStatus=sfpsFabricFacilityAdminStatus, sfpsFabricFacilityOperStatus=sfpsFabricFacilityOperStatus, sfpsUplinkFacilityStatusTime=sfpsUplinkFacilityStatusTime, sfpsUplinkFacilityAdminStatus=sfpsUplinkFacilityAdminStatus, sfpsFpcFacilityHashIndex=sfpsFpcFacilityHashIndex, sfpsUplinkFacilityHashIndex=sfpsUplinkFacilityHashIndex, sfpsCentersFacilityAdminStatus=sfpsCentersFacilityAdminStatus, sfpsDiagFacilityStatusTime=sfpsDiagFacilityStatusTime, sfpsCallTapFacilityStatusTime=sfpsCallTapFacilityStatusTime, sfpsBetaFacilityStatusTime=sfpsBetaFacilityStatusTime, sfpsLiteFacilityEntry=sfpsLiteFacilityEntry, sfpsDiagFacilityAdminStatus=sfpsDiagFacilityAdminStatus, sfpsRAFacilityStatusTime=sfpsRAFacilityStatusTime, sfpsUplinkFacilityEntry=sfpsUplinkFacilityEntry, sfpsCallTapFacilityElementName=sfpsCallTapFacilityElementName, sfpsDiagFacilityEntry=sfpsDiagFacilityEntry, sfpsRAFacilityHashIndex=sfpsRAFacilityHashIndex, sfpsUplinkFacilityName=sfpsUplinkFacilityName, sfpsUplinkFacilityTable=sfpsUplinkFacilityTable, HexInteger=HexInteger, sfpsRAFacilityTable=sfpsRAFacilityTable, sfpsFpcFacilityAdminStatus=sfpsFpcFacilityAdminStatus, sfpsFpcFacilityEntry=sfpsFpcFacilityEntry, sfpsCentersFacilityOperStatus=sfpsCentersFacilityOperStatus, sfpsRAFacilityAdminStatus=sfpsRAFacilityAdminStatus, sfpsFabricFacilityEntry=sfpsFabricFacilityEntry, sfpsLiteFacilityStatusTime=sfpsLiteFacilityStatusTime, sfpsDiagFacilityOperStatus=sfpsDiagFacilityOperStatus, sfpsFabricFacilityHashIndex=sfpsFabricFacilityHashIndex, sfpsVLANFacilityHashIndex=sfpsVLANFacilityHashIndex, sfpsVNSFacilityEntry=sfpsVNSFacilityEntry, sfpsMcastFacilityElementName=sfpsMcastFacilityElementName, sfpsVNSFacilityHashIndex=sfpsVNSFacilityHashIndex, sfpsLiteFacilityTable=sfpsLiteFacilityTable, sfpsMcastFacilityEntry=sfpsMcastFacilityEntry, sfpsFpcFacilityStatusTime=sfpsFpcFacilityStatusTime, sfpsVLANFacilityEntry=sfpsVLANFacilityEntry, sfpsMcastFacilityOperStatus=sfpsMcastFacilityOperStatus, sfpsMcastFacilityStatusTime=sfpsMcastFacilityStatusTime, sfpsCallTapFacilityAdminStatus=sfpsCallTapFacilityAdminStatus, sfpsVLANFacilityStatusTime=sfpsVLANFacilityStatusTime, sfpsCallTapFacilityEntry=sfpsCallTapFacilityEntry, sfpsMcastFacilityTable=sfpsMcastFacilityTable, sfpsVNSFacilityElementName=sfpsVNSFacilityElementName, sfpsVLANFacilityTable=sfpsVLANFacilityTable, sfpsDiagFacilityHashIndex=sfpsDiagFacilityHashIndex, sfpsCallTapFacilityHashIndex=sfpsCallTapFacilityHashIndex, sfpsLiteFacilityHashIndex=sfpsLiteFacilityHashIndex, sfpsCentersFacilityResponses=sfpsCentersFacilityResponses, sfpsLiteFacilityAdminStatus=sfpsLiteFacilityAdminStatus, sfpsCentersFacilityEntry=sfpsCentersFacilityEntry, sfpsCallTapFacilityOperStatus=sfpsCallTapFacilityOperStatus, sfpsVNSFacilityTable=sfpsVNSFacilityTable, sfpsLiteFacilityOperStatus=sfpsLiteFacilityOperStatus, sfpsMcastFacilityAdminStatus=sfpsMcastFacilityAdminStatus, sfpsFpcFacilityElementName=sfpsFpcFacilityElementName, sfpsDiagFacilityElementName=sfpsDiagFacilityElementName, sfpsBetaFacilityTable=sfpsBetaFacilityTable, sfpsRAFacilityEntry=sfpsRAFacilityEntry, sfpsFabricFacilityElementName=sfpsFabricFacilityElementName, sfpsVLANFacilityElementName=sfpsVLANFacilityElementName, sfpsUplinkFacilityOperStatus=sfpsUplinkFacilityOperStatus, sfpsVNSFacilityOperStatus=sfpsVNSFacilityOperStatus, sfpsMcastFacilityHashIndex=sfpsMcastFacilityHashIndex, sfpsCentersFacilityRequests=sfpsCentersFacilityRequests, sfpsCentersFacilityAddress=sfpsCentersFacilityAddress, sfpsVLANFacilityAdminStatus=sfpsVLANFacilityAdminStatus, sfpsBetaFacilityEntry=sfpsBetaFacilityEntry)
