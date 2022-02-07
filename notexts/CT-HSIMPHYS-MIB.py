#
# PySNMP MIB module CT-HSIMPHYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-HSIMPHYS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ctHSIMPhysMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctHSIMPhysMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hsimInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1))
hsimBoardRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimBoardRev.setStatus('mandatory')
hsimBoardId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimBoardId.setStatus('mandatory')
hsimEpldRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimEpldRev.setStatus('mandatory')
hsimEpldId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimEpldId.setStatus('mandatory')
hsimFsbRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimFsbRev.setStatus('mandatory')
hsimSsbRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimSsbRev.setStatus('mandatory')
hsimFwRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimFwRev.setStatus('mandatory')
hsimPeripheralMBusInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8))
mBusNumberBoardsInstalled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusNumberBoardsInstalled.setStatus('mandatory')
mBusBoardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2), )
if mibBuilder.loadTexts: mBusBoardTable.setStatus('mandatory')
mBusBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "mBusBoardID"))
if mibBuilder.loadTexts: mBusBoardEntry.setStatus('mandatory')
mBusBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardID.setStatus('mandatory')
mBusBoardEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("cmm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardEntryType.setStatus('mandatory')
mBusBoardOIDPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardOIDPointer.setStatus('mandatory')
hsimPeripheralWpimInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9))
wpimNumberBoardsInstalled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimNumberBoardsInstalled.setStatus('mandatory')
wpimBoardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2), )
if mibBuilder.loadTexts: wpimBoardTable.setStatus('mandatory')
wpimBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "wpimBoardID"))
if mibBuilder.loadTexts: wpimBoardEntry.setStatus('mandatory')
wpimBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardID.setStatus('mandatory')
wpimBoardEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardEntryType.setStatus('mandatory')
wpimBoardOIDPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardOIDPointer.setStatus('mandatory')
hsimLocalHwDevicesInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10))
localHwDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1), )
if mibBuilder.loadTexts: localHwDevicesTable.setStatus('mandatory')
localHwDevicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "localHwDeviceID"))
if mibBuilder.loadTexts: localHwDevicesEntry.setStatus('mandatory')
localHwDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceID.setStatus('mandatory')
localHwDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("siemensMunich32", 2), ("mitelMT8985", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceType.setStatus('mandatory')
localHwDeviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceOperStatus.setStatus('mandatory')
localHwDeviceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: localHwDeviceAdminStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CT-HSIMPHYS-MIB", hsimPeripheralWpimInfo=hsimPeripheralWpimInfo, mBusBoardOIDPointer=mBusBoardOIDPointer, hsimBoardRev=hsimBoardRev, wpimBoardEntry=wpimBoardEntry, mBusNumberBoardsInstalled=mBusNumberBoardsInstalled, hsimLocalHwDevicesInfo=hsimLocalHwDevicesInfo, hsimBoardId=hsimBoardId, mBusBoardEntryType=mBusBoardEntryType, mBusBoardID=mBusBoardID, hsimEpldRev=hsimEpldRev, mBusBoardTable=mBusBoardTable, hsimFwRev=hsimFwRev, localHwDeviceType=localHwDeviceType, wpimBoardID=wpimBoardID, mBusBoardEntry=mBusBoardEntry, wpimBoardOIDPointer=wpimBoardOIDPointer, localHwDeviceID=localHwDeviceID, localHwDeviceAdminStatus=localHwDeviceAdminStatus, wpimNumberBoardsInstalled=wpimNumberBoardsInstalled, hsimEpldId=hsimEpldId, wpimBoardTable=wpimBoardTable, hsimSsbRev=hsimSsbRev, hsimFsbRev=hsimFsbRev, localHwDevicesTable=localHwDevicesTable, localHwDeviceOperStatus=localHwDeviceOperStatus, localHwDevicesEntry=localHwDevicesEntry, hsimInfo=hsimInfo, hsimPeripheralMBusInfo=hsimPeripheralMBusInfo, wpimBoardEntryType=wpimBoardEntryType)
