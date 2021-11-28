#
# PySNMP MIB module BEGEMOT-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-ATM
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, ModuleIdentity, Integer32, NotificationType, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, Bits, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "NotificationType", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotAtm = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 101))
if mibBuilder.loadTexts: begemotAtm.setLastUpdated('200407190000Z')
if mibBuilder.loadTexts: begemotAtm.setOrganization('German Aerospace Centre')
begemotAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1))
class AtmESI(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

begemotAtmIfTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1), )
if mibBuilder.loadTexts: begemotAtmIfTable.setStatus('current')
begemotAtmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: begemotAtmIfEntry.setStatus('current')
begemotAtmIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfName.setStatus('current')
begemotAtmIfPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfPcr.setStatus('current')
begemotAtmIfMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("other", 1), ("unknown", 3), ("utp25", 4), ("taxi100", 5), ("taxi140", 6), ("mm155", 7), ("sm155", 8), ("utp155", 9), ("mm622", 10), ("sm622", 11), ("virtual", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMedia.setStatus('current')
begemotAtmIfVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfVpiBits.setStatus('current')
begemotAtmIfVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfVciBits.setStatus('current')
begemotAtmIfMaxVpcs = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMaxVpcs.setStatus('current')
begemotAtmIfMaxVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777216))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMaxVccs.setStatus('current')
begemotAtmIfEsi = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 8), AtmESI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfEsi.setStatus('current')
begemotAtmIfCarrierStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("carrierOn", 1), ("carrierOff", 2), ("unknown", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfCarrierStatus.setStatus('current')
begemotAtmIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotAtmIfMode.setStatus('current')
begemotAtmIfTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfTableLastChange.setStatus('current')
begemotAtmHWTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3), )
if mibBuilder.loadTexts: begemotAtmHWTable.setStatus('current')
begemotAtmHWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1), )
begemotAtmIfEntry.registerAugmentions(("BEGEMOT-ATM-MIB", "begemotAtmHWEntry"))
begemotAtmHWEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
if mibBuilder.loadTexts: begemotAtmHWEntry.setStatus('current')
begemotAtmHWVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWVendor.setStatus('current')
begemotAtmHWDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWDevice.setStatus('current')
begemotAtmHWSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWSerial.setStatus('current')
begemotAtmHWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWVersion.setStatus('current')
begemotAtmHWSoftVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWSoftVersion.setStatus('current')
begemotAtmSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4))
mibBuilder.exportSymbols("BEGEMOT-ATM-MIB", begemotAtmIfCarrierStatus=begemotAtmIfCarrierStatus, begemotAtmIfMode=begemotAtmIfMode, begemotAtmHWTable=begemotAtmHWTable, begemotAtmIfVciBits=begemotAtmIfVciBits, AtmESI=AtmESI, begemotAtmIfEsi=begemotAtmIfEsi, begemotAtmIfEntry=begemotAtmIfEntry, begemotAtmIfMedia=begemotAtmIfMedia, begemotAtm=begemotAtm, begemotAtmHWEntry=begemotAtmHWEntry, begemotAtmIfTable=begemotAtmIfTable, begemotAtmHWDevice=begemotAtmHWDevice, begemotAtmHWVendor=begemotAtmHWVendor, begemotAtmSysGroup=begemotAtmSysGroup, begemotAtmIfVpiBits=begemotAtmIfVpiBits, PYSNMP_MODULE_ID=begemotAtm, begemotAtmObjects=begemotAtmObjects, begemotAtmIfName=begemotAtmIfName, begemotAtmIfMaxVccs=begemotAtmIfMaxVccs, begemotAtmIfMaxVpcs=begemotAtmIfMaxVpcs, begemotAtmHWVersion=begemotAtmHWVersion, begemotAtmHWSoftVersion=begemotAtmHWSoftVersion, begemotAtmIfTableLastChange=begemotAtmIfTableLastChange, begemotAtmHWSerial=begemotAtmHWSerial, begemotAtmIfPcr=begemotAtmIfPcr)
