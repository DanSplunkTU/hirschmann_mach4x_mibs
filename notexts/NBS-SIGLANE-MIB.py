#
# PySNMP MIB module NBS-SIGLANE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SIGLANE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:30:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsCmmcChannelBand, = mibBuilder.importSymbols("NBS-CMMCENUM-MIB", "NbsCmmcChannelBand")
NbsTcMHz, NbsTcTemperature, NbsTcMilliDb, nbs, NbsTcMicroAmp = mibBuilder.importSymbols("NBS-MIB", "NbsTcMHz", "NbsTcTemperature", "NbsTcMilliDb", "nbs", "NbsTcMicroAmp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ModuleIdentity, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, IpAddress, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSigLaneMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 236))
if mibBuilder.loadTexts: nbsSigLaneMib.setLastUpdated('201710180000Z')
if mibBuilder.loadTexts: nbsSigLaneMib.setOrganization('NBS')
nbsSigLanePortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 10))
if mibBuilder.loadTexts: nbsSigLanePortGrp.setStatus('current')
nbsSigLaneLaneGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 20))
if mibBuilder.loadTexts: nbsSigLaneLaneGrp.setStatus('current')
nbsSigLaneTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 100))
if mibBuilder.loadTexts: nbsSigLaneTraps.setStatus('current')
nbsSigLaneTraps0 = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 100, 0))
if mibBuilder.loadTexts: nbsSigLaneTraps0.setStatus('current')
nbsSigLanePortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 236, 10, 1), )
if mibBuilder.loadTexts: nbsSigLanePortTable.setStatus('current')
nbsSigLanePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1), ).setIndexNames((0, "NBS-SIGLANE-MIB", "nbsSigLanePortIfIndex"))
if mibBuilder.loadTexts: nbsSigLanePortEntry.setStatus('current')
nbsSigLanePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortIfIndex.setStatus('current')
nbsSigLanePortFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fiber", 2), ("lambda", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortFacility.setStatus('current')
nbsSigLanePortLanes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortLanes.setStatus('current')
nbsSigLaneLaneTable = MibTable((1, 3, 6, 1, 4, 1, 629, 236, 20, 1), )
if mibBuilder.loadTexts: nbsSigLaneLaneTable.setStatus('current')
nbsSigLaneLaneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1), ).setIndexNames((0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIfIndex"), (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIndex"))
if mibBuilder.loadTexts: nbsSigLaneLaneEntry.setStatus('current')
nbsSigLaneLaneIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneIfIndex.setStatus('current')
nbsSigLaneLaneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneIndex.setStatus('current')
nbsSigLaneLaneFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 10), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFrequency.setStatus('current')
nbsSigLaneLaneWavelengthX = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneWavelengthX.setStatus('current')
nbsSigLaneLaneChannelBand = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 12), NbsCmmcChannelBand()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneChannelBand.setStatus('current')
nbsSigLaneLaneChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneChannelNumber.setStatus('current')
nbsSigLaneLaneTxDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("no", 2), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigLaneLaneTxDisable.setStatus('current')
nbsSigLaneLaneFaultsCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFaultsCaps.setStatus('current')
nbsSigLaneLaneFaultsOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFaultsOper.setStatus('current')
nbsSigLaneLaneTxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPowerLevel.setStatus('current')
nbsSigLaneLaneTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 21), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPower.setStatus('current')
nbsSigLaneLaneTxPowerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 22), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPowerAdmin.setStatus('current')
nbsSigLaneLaneRxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneRxPowerLevel.setStatus('current')
nbsSigLaneLaneRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 31), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneRxPower.setStatus('current')
nbsSigLaneLaneBiasAmpsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneBiasAmpsLevel.setStatus('current')
nbsSigLaneLaneBiasAmps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 41), NbsTcMicroAmp().clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneBiasAmps.setStatus('current')
nbsSigLaneLaneLaserTempLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneLaserTempLevel.setStatus('current')
nbsSigLaneLaneLaserTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 51), NbsTcTemperature().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneLaserTemp.setStatus('current')
nbsSigLaneLaneEthTxAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 60), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthTxAllOctets.setStatus('current')
nbsSigLaneLaneEthTxAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 61), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthTxAllFrames.setStatus('current')
nbsSigLaneLaneEthRxAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 70), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthRxAllOctets.setStatus('current')
nbsSigLaneLaneEthRxAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 71), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthRxAllFrames.setStatus('current')
mibBuilder.exportSymbols("NBS-SIGLANE-MIB", nbsSigLaneLaneBiasAmps=nbsSigLaneLaneBiasAmps, nbsSigLanePortGrp=nbsSigLanePortGrp, nbsSigLaneLaneChannelBand=nbsSigLaneLaneChannelBand, nbsSigLaneTraps0=nbsSigLaneTraps0, nbsSigLaneLaneTxDisable=nbsSigLaneLaneTxDisable, nbsSigLaneLaneTable=nbsSigLaneLaneTable, nbsSigLaneLaneTxPowerLevel=nbsSigLaneLaneTxPowerLevel, nbsSigLaneLaneTxPowerAdmin=nbsSigLaneLaneTxPowerAdmin, nbsSigLaneLaneLaserTemp=nbsSigLaneLaneLaserTemp, nbsSigLaneLaneFaultsCaps=nbsSigLaneLaneFaultsCaps, nbsSigLaneTraps=nbsSigLaneTraps, nbsSigLaneLaneIndex=nbsSigLaneLaneIndex, nbsSigLaneLaneRxPower=nbsSigLaneLaneRxPower, PYSNMP_MODULE_ID=nbsSigLaneMib, nbsSigLaneLaneEthRxAllFrames=nbsSigLaneLaneEthRxAllFrames, nbsSigLaneLaneChannelNumber=nbsSigLaneLaneChannelNumber, nbsSigLanePortEntry=nbsSigLanePortEntry, nbsSigLaneLaneFrequency=nbsSigLaneLaneFrequency, nbsSigLaneLaneIfIndex=nbsSigLaneLaneIfIndex, nbsSigLaneLaneRxPowerLevel=nbsSigLaneLaneRxPowerLevel, nbsSigLaneLaneWavelengthX=nbsSigLaneLaneWavelengthX, nbsSigLanePortIfIndex=nbsSigLanePortIfIndex, nbsSigLaneLaneEntry=nbsSigLaneLaneEntry, nbsSigLaneLaneBiasAmpsLevel=nbsSigLaneLaneBiasAmpsLevel, nbsSigLanePortTable=nbsSigLanePortTable, nbsSigLanePortLanes=nbsSigLanePortLanes, nbsSigLaneLaneEthRxAllOctets=nbsSigLaneLaneEthRxAllOctets, nbsSigLaneLaneEthTxAllFrames=nbsSigLaneLaneEthTxAllFrames, nbsSigLaneMib=nbsSigLaneMib, nbsSigLaneLaneTxPower=nbsSigLaneLaneTxPower, nbsSigLaneLaneEthTxAllOctets=nbsSigLaneLaneEthTxAllOctets, nbsSigLanePortFacility=nbsSigLanePortFacility, nbsSigLaneLaneGrp=nbsSigLaneLaneGrp, nbsSigLaneLaneFaultsOper=nbsSigLaneLaneFaultsOper, nbsSigLaneLaneLaserTempLevel=nbsSigLaneLaneLaserTempLevel)
