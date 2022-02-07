#
# PySNMP MIB module NBS-OSA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OSA-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:16:28 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ifAlias, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "InterfaceIndex")
NbsCmmcChannelBand, = mibBuilder.importSymbols("NBS-CMMCENUM-MIB", "NbsCmmcChannelBand")
NbsTcMHz, nbs = mibBuilder.importSymbols("NBS-MIB", "NbsTcMHz", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, TimeTicks, IpAddress, Counter64, NotificationType, ObjectIdentity, Unsigned32, iso, Bits, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "TimeTicks", "IpAddress", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "iso", "Bits", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsOsaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 207))
if mibBuilder.loadTexts: nbsOsaMib.setLastUpdated('201503190000Z')
if mibBuilder.loadTexts: nbsOsaMib.setOrganization('NBS')
nbsOsaPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 1))
if mibBuilder.loadTexts: nbsOsaPortGrp.setStatus('current')
nbsOsaSpectrumGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 2))
if mibBuilder.loadTexts: nbsOsaSpectrumGrp.setStatus('current')
nbsOsaChannelGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 3))
if mibBuilder.loadTexts: nbsOsaChannelGrp.setStatus('current')
nbsOsaTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 4))
if mibBuilder.loadTexts: nbsOsaTraps.setStatus('current')
nbsOsaPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaPortTableSize.setStatus('current')
nbsOsaPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 1, 2), )
if mibBuilder.loadTexts: nbsOsaPortTable.setStatus('current')
nbsOsaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaPortIfIndex"))
if mibBuilder.loadTexts: nbsOsaPortEntry.setStatus('current')
nbsOsaPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaPortIfIndex.setStatus('current')
nbsOsaPortAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaPortAttenuation.setStatus('current')
nbsOsaPortChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaPortChannels.setStatus('current')
nbsOsaSpectrumTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumTableSize.setStatus('current')
nbsOsaSpectrumTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 2, 2), )
if mibBuilder.loadTexts: nbsOsaSpectrumTable.setStatus('current')
nbsOsaSpectrumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaSpectrumIfIndex"), (0, "NBS-OSA-MIB", "nbsOsaSpectrumWavelength"))
if mibBuilder.loadTexts: nbsOsaSpectrumEntry.setStatus('current')
nbsOsaSpectrumIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumIfIndex.setStatus('current')
nbsOsaSpectrumWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 3), Integer32())
if mibBuilder.loadTexts: nbsOsaSpectrumWavelength.setStatus('current')
nbsOsaSpectrumTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumTimestamp.setStatus('current')
nbsOsaSpectrumRxPowerOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumRxPowerOper.setStatus('current')
nbsOsaChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelTableSize.setStatus('current')
nbsOsaChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 3, 2), )
if mibBuilder.loadTexts: nbsOsaChannelTable.setStatus('current')
nbsOsaChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaChannelIfIndex"), (0, "NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaChannelEntry.setStatus('current')
nbsOsaChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelIfIndex.setStatus('current')
nbsOsaChannelFrequencyNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelFrequencyNominal.setStatus('current')
nbsOsaChannelBand = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 3), NbsCmmcChannelBand()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelBand.setStatus('current')
nbsOsaChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelNumber.setStatus('current')
nbsOsaChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelStatus.setStatus('current')
nbsOsaChannelTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelTimestamp.setStatus('current')
nbsOsaChannelFrequencyOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 7), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelFrequencyOper.setStatus('current')
nbsOsaChannelRxPowerOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 8), Integer32().clone(-100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerOper.setStatus('current')
nbsOsaChannelRxPowerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerMin.setStatus('current')
nbsOsaChannelRxPowerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerMax.setStatus('current')
nbsOsaChannelOSNROper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelOSNROper.setStatus('current')
nbsOsaChannelOSNRMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 12), Integer32().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelOSNRMin.setStatus('current')
nbsOsaChannelOSNRMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 13), Integer32().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelOSNRMax.setStatus('current')
nbsOsaTrapPortChannelAdded = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 1)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaTrapPortChannelAdded.setStatus('current')
nbsOsaTrapPortChannelDropped = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 2)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaTrapPortChannelDropped.setStatus('current')
nbsOsaTrapPortRxPowerTooLow = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 3)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMin"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerTooLow.setStatus('current')
nbsOsaTrapPortRxPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 4)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerOK.setStatus('current')
nbsOsaTrapPortRxPowerTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 5)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMax"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerTooHigh.setStatus('current')
nbsOsaTrapPortOSNRTooLow = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 6)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNRMin"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNRTooLow.setStatus('current')
nbsOsaTrapPortOSNROk = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 7)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNROk.setStatus('current')
nbsOsaTrapPortOSNRTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 8)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNRMax"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNRTooHigh.setStatus('current')
mibBuilder.exportSymbols("NBS-OSA-MIB", nbsOsaPortGrp=nbsOsaPortGrp, nbsOsaTrapPortRxPowerTooLow=nbsOsaTrapPortRxPowerTooLow, PYSNMP_MODULE_ID=nbsOsaMib, nbsOsaTraps=nbsOsaTraps, nbsOsaChannelNumber=nbsOsaChannelNumber, nbsOsaPortIfIndex=nbsOsaPortIfIndex, nbsOsaChannelOSNROper=nbsOsaChannelOSNROper, nbsOsaPortTableSize=nbsOsaPortTableSize, nbsOsaChannelOSNRMax=nbsOsaChannelOSNRMax, nbsOsaPortAttenuation=nbsOsaPortAttenuation, nbsOsaMib=nbsOsaMib, nbsOsaTrapPortChannelDropped=nbsOsaTrapPortChannelDropped, nbsOsaTrapPortOSNRTooHigh=nbsOsaTrapPortOSNRTooHigh, nbsOsaChannelRxPowerOper=nbsOsaChannelRxPowerOper, nbsOsaTrapPortOSNROk=nbsOsaTrapPortOSNROk, nbsOsaTrapPortChannelAdded=nbsOsaTrapPortChannelAdded, nbsOsaChannelBand=nbsOsaChannelBand, nbsOsaSpectrumTable=nbsOsaSpectrumTable, nbsOsaChannelOSNRMin=nbsOsaChannelOSNRMin, nbsOsaChannelEntry=nbsOsaChannelEntry, nbsOsaChannelIfIndex=nbsOsaChannelIfIndex, nbsOsaPortTable=nbsOsaPortTable, nbsOsaSpectrumGrp=nbsOsaSpectrumGrp, nbsOsaSpectrumRxPowerOper=nbsOsaSpectrumRxPowerOper, nbsOsaPortEntry=nbsOsaPortEntry, nbsOsaChannelTimestamp=nbsOsaChannelTimestamp, nbsOsaChannelTable=nbsOsaChannelTable, nbsOsaSpectrumIfIndex=nbsOsaSpectrumIfIndex, nbsOsaSpectrumWavelength=nbsOsaSpectrumWavelength, nbsOsaSpectrumTableSize=nbsOsaSpectrumTableSize, nbsOsaChannelFrequencyNominal=nbsOsaChannelFrequencyNominal, nbsOsaChannelFrequencyOper=nbsOsaChannelFrequencyOper, nbsOsaChannelRxPowerMin=nbsOsaChannelRxPowerMin, nbsOsaSpectrumTimestamp=nbsOsaSpectrumTimestamp, nbsOsaChannelRxPowerMax=nbsOsaChannelRxPowerMax, nbsOsaTrapPortRxPowerTooHigh=nbsOsaTrapPortRxPowerTooHigh, nbsOsaTrapPortOSNRTooLow=nbsOsaTrapPortOSNRTooLow, nbsOsaChannelGrp=nbsOsaChannelGrp, nbsOsaSpectrumEntry=nbsOsaSpectrumEntry, nbsOsaChannelTableSize=nbsOsaChannelTableSize, nbsOsaChannelStatus=nbsOsaChannelStatus, nbsOsaPortChannels=nbsOsaPortChannels, nbsOsaTrapPortRxPowerOK=nbsOsaTrapPortRxPowerOK)
