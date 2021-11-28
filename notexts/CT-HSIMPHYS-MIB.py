#
# PySNMP MIB module CT-HSIMPHYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-HSIMPHYS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctHSIMPhysMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctHSIMPhysMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CT-HSIMPHYS-MIB", hsimFsbRev=hsimFsbRev, mBusBoardOIDPointer=mBusBoardOIDPointer, mBusBoardTable=mBusBoardTable, hsimPeripheralWpimInfo=hsimPeripheralWpimInfo, wpimBoardTable=wpimBoardTable, wpimBoardEntryType=wpimBoardEntryType, wpimBoardID=wpimBoardID, hsimSsbRev=hsimSsbRev, localHwDevicesEntry=localHwDevicesEntry, localHwDevicesTable=localHwDevicesTable, wpimNumberBoardsInstalled=wpimNumberBoardsInstalled, hsimEpldId=hsimEpldId, mBusBoardEntry=mBusBoardEntry, hsimLocalHwDevicesInfo=hsimLocalHwDevicesInfo, mBusBoardEntryType=mBusBoardEntryType, hsimBoardId=hsimBoardId, localHwDeviceID=localHwDeviceID, localHwDeviceOperStatus=localHwDeviceOperStatus, hsimPeripheralMBusInfo=hsimPeripheralMBusInfo, hsimInfo=hsimInfo, mBusNumberBoardsInstalled=mBusNumberBoardsInstalled, localHwDeviceType=localHwDeviceType, hsimEpldRev=hsimEpldRev, wpimBoardEntry=wpimBoardEntry, mBusBoardID=mBusBoardID, wpimBoardOIDPointer=wpimBoardOIDPointer, hsimBoardRev=hsimBoardRev, localHwDeviceAdminStatus=localHwDeviceAdminStatus, hsimFwRev=hsimFwRev)
