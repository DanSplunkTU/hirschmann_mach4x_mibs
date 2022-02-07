#
# PySNMP MIB module NIMBLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nimble/NIMBLE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:16:48 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits, MibIdentifier, NotificationType, ObjectIdentity, Gauge32, enterprises, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity", "Gauge32", "enterprises", "Integer32", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
nimble = ModuleIdentity((1, 3, 6, 1, 4, 1, 37447))
nimble.setRevisions(('2012-08-31 00:00', '2012-06-12 00:00', '2011-02-28 00:00',))
if mibBuilder.loadTexts: nimble.setLastUpdated('201208310000Z')
if mibBuilder.loadTexts: nimble.setOrganization('Nimble Storage, Inc.')
variables = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 1))
volNumberOfVolumes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volNumberOfVolumes.setStatus('obsolete')
volTable = MibTable((1, 3, 6, 1, 4, 1, 37447, 1, 2), )
if mibBuilder.loadTexts: volTable.setStatus('current')
volEntry = MibTableRow((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1), ).setIndexNames((0, "NIMBLE-MIB", "volIndex"))
if mibBuilder.loadTexts: volEntry.setStatus('current')
volIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: volIndex.setStatus('current')
volID = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volID.setStatus('current')
volName = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volName.setStatus('current')
volSizeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volSizeLow.setStatus('current')
volSizeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volSizeHigh.setStatus('current')
volUsageLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volUsageLow.setStatus('current')
volUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volUsageHigh.setStatus('current')
volReserveLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volReserveLow.setStatus('current')
volReserveHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volReserveHigh.setStatus('current')
volOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volOnline.setStatus('current')
volNumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volNumConnections.setStatus('current')
volStatTimeEpochSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volStatTimeEpochSeconds.setStatus('current')
volIoReads = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReads.setStatus('current')
volIoReadTimeMicrosec = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadTimeMicrosec.setStatus('current')
volIoReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadBytes.setStatus('current')
volIoSeqReads = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqReads.setStatus('current')
volIoSeqReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqReadBytes.setStatus('current')
volIoNonseqReadTotalHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadTotalHits.setStatus('current')
volIoNonseqReadMemHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadMemHits.setStatus('current')
volIoNonseqReadSSDHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadSSDHits.setStatus('current')
volIoReadLatency0uTo100u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency0uTo100u.setStatus('current')
volIoReadLatency100uTo200u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency100uTo200u.setStatus('current')
volIoReadLatency200uTo500u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency200uTo500u.setStatus('current')
volIoReadLatency500uTo1m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency500uTo1m.setStatus('current')
volIoReadLatency1mTo2m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency1mTo2m.setStatus('current')
volIoReadLatency2mTo5m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency2mTo5m.setStatus('current')
volIoReadLatency5mTo10m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency5mTo10m.setStatus('current')
volIoReadLatency10mTo20m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency10mTo20m.setStatus('current')
volIoReadLatency20mTo50m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency20mTo50m.setStatus('current')
volIoReadLatency50mTo100m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency50mTo100m.setStatus('current')
volIoReadLatency100mTo200m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency100mTo200m.setStatus('current')
volIoReadLatency200mTo500m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency200mTo500m.setStatus('current')
volIoReadLatency500mTomax = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency500mTomax.setStatus('current')
volIoWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWrites.setStatus('current')
volIoWriteTimeMicrosec = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteTimeMicrosec.setStatus('current')
volIoWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteBytes.setStatus('current')
volIoSeqWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqWrites.setStatus('current')
volIoSeqWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqWriteBytes.setStatus('current')
volIoWriteLatency0uTo100u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency0uTo100u.setStatus('current')
volIoWriteLatency100uTo200u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency100uTo200u.setStatus('current')
volIoWriteLatency200uTo500u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency200uTo500u.setStatus('current')
volIoWriteLatency500uTo1m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency500uTo1m.setStatus('current')
volIoWriteLatency1mTo2m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency1mTo2m.setStatus('current')
volIoWriteLatency2mTo5m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency2mTo5m.setStatus('current')
volIoWriteLatency5mTo10m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency5mTo10m.setStatus('current')
volIoWriteLatency10mTo20m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency10mTo20m.setStatus('current')
volIoWriteLatency20mTo50m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency20mTo50m.setStatus('current')
volIoWriteLatency50mTo100m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency50mTo100m.setStatus('current')
volIoWriteLatency100mTo200m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency100mTo200m.setStatus('current')
volIoWriteLatency200mTo500m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency200mTo500m.setStatus('current')
volIoWriteLatency500mTomax = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency500mTomax.setStatus('current')
volDiskVolBytesUsedLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 52), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskVolBytesUsedLow.setStatus('current')
volDiskVolBytesUsedHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 53), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskVolBytesUsedHigh.setStatus('current')
volDiskSnapBytesUsedLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskSnapBytesUsedLow.setStatus('current')
volDiskSnapBytesUsedHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 55), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskSnapBytesUsedHigh.setStatus('current')
globalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 1, 3))
statTimeEpochSeconds = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statTimeEpochSeconds.setStatus('current')
ioReads = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReads.setStatus('current')
ioSeqReads = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqReads.setStatus('current')
ioWrites = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWrites.setStatus('current')
ioSeqWrites = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqWrites.setStatus('current')
ioReadTimeMicrosec = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReadTimeMicrosec.setStatus('current')
ioWriteTimeMicrosec = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWriteTimeMicrosec.setStatus('current')
ioReadBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReadBytes.setStatus('current')
ioSeqReadBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqReadBytes.setStatus('current')
ioWriteBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWriteBytes.setStatus('current')
ioSeqWriteBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqWriteBytes.setStatus('current')
diskVolBytesUsedLow = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVolBytesUsedLow.setStatus('current')
diskVolBytesUsedHigh = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVolBytesUsedHigh.setStatus('current')
diskSnapBytesUsedLow = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSnapBytesUsedLow.setStatus('current')
diskSnapBytesUsedHigh = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSnapBytesUsedHigh.setStatus('current')
ioNonseqReadHits = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioNonseqReadHits.setStatus('current')
arrays = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 3))
arrayEntry = MibScalar((1, 3, 6, 1, 4, 1, 37447, 3, 1), DisplayString())
if mibBuilder.loadTexts: arrayEntry.setStatus('current')
mibBuilder.exportSymbols("NIMBLE-MIB", volIoWriteLatency5mTo10m=volIoWriteLatency5mTo10m, ioReadBytes=ioReadBytes, globalStats=globalStats, volIoReads=volIoReads, volIoReadLatency5mTo10m=volIoReadLatency5mTo10m, volIoReadLatency200mTo500m=volIoReadLatency200mTo500m, volIoReadTimeMicrosec=volIoReadTimeMicrosec, volDiskVolBytesUsedLow=volDiskVolBytesUsedLow, volIoWriteLatency100uTo200u=volIoWriteLatency100uTo200u, volIoWriteLatency100mTo200m=volIoWriteLatency100mTo200m, volSizeLow=volSizeLow, diskSnapBytesUsedLow=diskSnapBytesUsedLow, volIoReadLatency500uTo1m=volIoReadLatency500uTo1m, volIoWriteLatency1mTo2m=volIoWriteLatency1mTo2m, volIndex=volIndex, volIoNonseqReadMemHits=volIoNonseqReadMemHits, volIoWriteBytes=volIoWriteBytes, volIoReadLatency100uTo200u=volIoReadLatency100uTo200u, volSizeHigh=volSizeHigh, volNumberOfVolumes=volNumberOfVolumes, arrayEntry=arrayEntry, ioReads=ioReads, ioWriteTimeMicrosec=ioWriteTimeMicrosec, volIoWriteTimeMicrosec=volIoWriteTimeMicrosec, diskVolBytesUsedLow=diskVolBytesUsedLow, volDiskVolBytesUsedHigh=volDiskVolBytesUsedHigh, statTimeEpochSeconds=statTimeEpochSeconds, volIoWriteLatency500uTo1m=volIoWriteLatency500uTo1m, ioSeqReads=ioSeqReads, diskSnapBytesUsedHigh=diskSnapBytesUsedHigh, volIoReadLatency2mTo5m=volIoReadLatency2mTo5m, volDiskSnapBytesUsedLow=volDiskSnapBytesUsedLow, volReserveHigh=volReserveHigh, volIoReadLatency1mTo2m=volIoReadLatency1mTo2m, ioReadTimeMicrosec=ioReadTimeMicrosec, volIoSeqReadBytes=volIoSeqReadBytes, volTable=volTable, volIoWriteLatency200uTo500u=volIoWriteLatency200uTo500u, volStatTimeEpochSeconds=volStatTimeEpochSeconds, volNumConnections=volNumConnections, volIoReadLatency0uTo100u=volIoReadLatency0uTo100u, volIoWrites=volIoWrites, volIoWriteLatency200mTo500m=volIoWriteLatency200mTo500m, ioNonseqReadHits=ioNonseqReadHits, volIoSeqWriteBytes=volIoSeqWriteBytes, ioWriteBytes=ioWriteBytes, PYSNMP_MODULE_ID=nimble, volReserveLow=volReserveLow, volIoWriteLatency50mTo100m=volIoWriteLatency50mTo100m, volIoWriteLatency500mTomax=volIoWriteLatency500mTomax, volEntry=volEntry, volIoSeqWrites=volIoSeqWrites, volIoWriteLatency10mTo20m=volIoWriteLatency10mTo20m, volIoWriteLatency2mTo5m=volIoWriteLatency2mTo5m, volIoReadLatency100mTo200m=volIoReadLatency100mTo200m, arrays=arrays, volIoReadLatency20mTo50m=volIoReadLatency20mTo50m, volID=volID, variables=variables, volOnline=volOnline, volIoSeqReads=volIoSeqReads, diskVolBytesUsedHigh=diskVolBytesUsedHigh, volIoWriteLatency0uTo100u=volIoWriteLatency0uTo100u, nimble=nimble, volIoReadLatency10mTo20m=volIoReadLatency10mTo20m, volUsageHigh=volUsageHigh, ioSeqWriteBytes=ioSeqWriteBytes, ioSeqReadBytes=ioSeqReadBytes, volName=volName, volDiskSnapBytesUsedHigh=volDiskSnapBytesUsedHigh, volIoNonseqReadSSDHits=volIoNonseqReadSSDHits, volIoReadBytes=volIoReadBytes, volIoReadLatency200uTo500u=volIoReadLatency200uTo500u, volIoNonseqReadTotalHits=volIoNonseqReadTotalHits, volUsageLow=volUsageLow, volIoReadLatency500mTomax=volIoReadLatency500mTomax, volIoWriteLatency20mTo50m=volIoWriteLatency20mTo50m, ioSeqWrites=ioSeqWrites, ioWrites=ioWrites, volIoReadLatency50mTo100m=volIoReadLatency50mTo100m)
