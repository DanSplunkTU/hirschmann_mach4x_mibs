#
# PySNMP MIB module BEGEMOT-HAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HAST-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:22:37 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, IpAddress, TimeTicks, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Integer32, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "IpAddress", "TimeTicks", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Integer32", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
begemotHast = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 220))
begemotHast.setRevisions(('2013-04-13 00:00', '2013-07-01 00:00', '2013-12-29 00:00',))
if mibBuilder.loadTexts: begemotHast.setLastUpdated('201304130000Z')
if mibBuilder.loadTexts: begemotHast.setOrganization('FreeBSD')
begemotHastObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1))
hastConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1))
hastConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastConfigFile.setStatus('current')
hastResourceTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2), )
if mibBuilder.loadTexts: hastResourceTable.setStatus('current')
hastResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1), ).setIndexNames((0, "BEGEMOT-HAST-MIB", "hastResourceIndex"))
if mibBuilder.loadTexts: hastResourceEntry.setStatus('current')
hastResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceIndex.setStatus('current')
hastResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceName.setStatus('current')
hastResourceRole = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("undef", 0), ("init", 1), ("primary", 2), ("secondary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hastResourceRole.setStatus('current')
hastResourceProvName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceProvName.setStatus('current')
hastResourceLocalPath = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceLocalPath.setStatus('current')
hastResourceExtentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceExtentSize.setStatus('current')
hastResourceKeepDirty = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceKeepDirty.setStatus('current')
hastResourceRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceRemoteAddr.setStatus('current')
hastResourceSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceSourceAddr.setStatus('current')
hastResourceReplication = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("fullsync", 0), ("memsync", 1), ("async", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReplication.setStatus('current')
hastResourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("complete", 0), ("degraded", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceStatus.setStatus('current')
hastResourceDirty = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDirty.setStatus('current')
hastResourceReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReads.setStatus('current')
hastResourceWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWrites.setStatus('current')
hastResourceDeletes = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDeletes.setStatus('current')
hastResourceFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceFlushes.setStatus('current')
hastResourceActivemapUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceActivemapUpdates.setStatus('current')
hastResourceReadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReadErrors.setStatus('current')
hastResourceWriteErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWriteErrors.setStatus('current')
hastResourceDeleteErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDeleteErrors.setStatus('current')
hastResourceFlushErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceFlushErrors.setStatus('current')
hastResourceWorkerPid = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWorkerPid.setStatus('current')
hastResourceLocalQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceLocalQueue.setStatus('current')
hastResourceSendQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceSendQueue.setStatus('current')
hastResourceRecvQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceRecvQueue.setStatus('current')
hastResourceDoneQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDoneQueue.setStatus('current')
hastResourceIdleQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceIdleQueue.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-HAST-MIB", hastResourceSourceAddr=hastResourceSourceAddr, hastResourceEntry=hastResourceEntry, begemotHastObjects=begemotHastObjects, hastResourceKeepDirty=hastResourceKeepDirty, hastResourceStatus=hastResourceStatus, hastResourceDeleteErrors=hastResourceDeleteErrors, hastResourceRole=hastResourceRole, hastResourceReadErrors=hastResourceReadErrors, hastResourceFlushes=hastResourceFlushes, hastResourceWrites=hastResourceWrites, hastResourceSendQueue=hastResourceSendQueue, hastResourceIdleQueue=hastResourceIdleQueue, hastConfig=hastConfig, hastResourceDirty=hastResourceDirty, hastResourceLocalPath=hastResourceLocalPath, hastResourceTable=hastResourceTable, hastResourceExtentSize=hastResourceExtentSize, hastResourceRemoteAddr=hastResourceRemoteAddr, hastConfigFile=hastConfigFile, hastResourceLocalQueue=hastResourceLocalQueue, hastResourceReplication=hastResourceReplication, hastResourceWriteErrors=hastResourceWriteErrors, hastResourceDeletes=hastResourceDeletes, hastResourceProvName=hastResourceProvName, hastResourceReads=hastResourceReads, hastResourceDoneQueue=hastResourceDoneQueue, hastResourceWorkerPid=hastResourceWorkerPid, hastResourceActivemapUpdates=hastResourceActivemapUpdates, PYSNMP_MODULE_ID=begemotHast, hastResourceName=hastResourceName, hastResourceRecvQueue=hastResourceRecvQueue, begemotHast=begemotHast, hastResourceFlushErrors=hastResourceFlushErrors, hastResourceIndex=hastResourceIndex)
