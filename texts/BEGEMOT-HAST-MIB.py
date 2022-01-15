#
# PySNMP MIB module BEGEMOT-HAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HAST-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:16:22 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, MibIdentifier, Unsigned32, Gauge32, NotificationType, Integer32, Counter64, ObjectIdentity, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "MibIdentifier", "Unsigned32", "Gauge32", "NotificationType", "Integer32", "Counter64", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
begemotHast = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 220))
begemotHast.setRevisions(('2013-04-13 00:00', '2013-07-01 00:00', '2013-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: begemotHast.setRevisionsDescriptions(('Initial revision.', 'Added hastResourceWorkerPid.', 'Added hastResourceLocalQueue, hastResourceSendQueue,\n\t    hastResourceRecvQueue, hastResourceDoneQueue,\n\t    hastResourceIdleQueue.',))
if mibBuilder.loadTexts: begemotHast.setLastUpdated('201304130000Z')
if mibBuilder.loadTexts: begemotHast.setOrganization('FreeBSD')
if mibBuilder.loadTexts: begemotHast.setContactInfo('\t\tMikolaj Golub\n\n\t     Postal:\tBluhera 27v 11\n\t\t\t61146 Kharkiv\n\t\t\tUkraine\n\n\t     Fax:\tN/A\n\n\t     E-Mail:\ttrociny@FreeBSD.org')
if mibBuilder.loadTexts: begemotHast.setDescription('The Begemot MIB for managing HAST.')
begemotHastObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1))
hastConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1))
hastConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastConfigFile.setStatus('current')
if mibBuilder.loadTexts: hastConfigFile.setDescription('HAST configuration file location.')
hastResourceTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2), )
if mibBuilder.loadTexts: hastResourceTable.setStatus('current')
if mibBuilder.loadTexts: hastResourceTable.setDescription('A table containing information about all HAST resources.')
hastResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1), ).setIndexNames((0, "BEGEMOT-HAST-MIB", "hastResourceIndex"))
if mibBuilder.loadTexts: hastResourceEntry.setStatus('current')
if mibBuilder.loadTexts: hastResourceEntry.setDescription('Table entry that describes one HAST resource.')
hastResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceIndex.setStatus('current')
if mibBuilder.loadTexts: hastResourceIndex.setDescription('Resource index.')
hastResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceName.setStatus('current')
if mibBuilder.loadTexts: hastResourceName.setDescription('Resource name.')
hastResourceRole = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("undef", 0), ("init", 1), ("primary", 2), ("secondary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hastResourceRole.setStatus('current')
if mibBuilder.loadTexts: hastResourceRole.setDescription('Resource role.')
hastResourceProvName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceProvName.setStatus('current')
if mibBuilder.loadTexts: hastResourceProvName.setDescription('Resource GEOM provider name that appears as /dev/hast/<name>.')
hastResourceLocalPath = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceLocalPath.setStatus('current')
if mibBuilder.loadTexts: hastResourceLocalPath.setDescription('Path to the local component which is used as a backend\n\tprovider for the resource.')
hastResourceExtentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceExtentSize.setStatus('current')
if mibBuilder.loadTexts: hastResourceExtentSize.setDescription('Size of an extent.  Extent is a block which is\n\tused for synchronization.  hastd(8) maintains a\n\tmap of dirty extents and extent is the smallest\n\tregion that can be marked as dirty.  If any part\n\tof an extent is modified, entire extent will be\n\tsynchronized when nodes connect.')
hastResourceKeepDirty = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceKeepDirty.setStatus('current')
if mibBuilder.loadTexts: hastResourceKeepDirty.setDescription('Maximum number of dirty extents to keep dirty all\n\tthe time.  Most recently used extents are kept\n\tdirty to reduce number of metadata updates.')
hastResourceRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceRemoteAddr.setStatus('current')
if mibBuilder.loadTexts: hastResourceRemoteAddr.setDescription('Address of the remote hastd(8) daemon for the resource.')
hastResourceSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceSourceAddr.setStatus('current')
if mibBuilder.loadTexts: hastResourceSourceAddr.setDescription('Local address the resource is bound to.')
hastResourceReplication = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("fullsync", 0), ("memsync", 1), ("async", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReplication.setStatus('current')
if mibBuilder.loadTexts: hastResourceReplication.setDescription('Resource replication mode.')
hastResourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("complete", 0), ("degraded", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceStatus.setStatus('current')
if mibBuilder.loadTexts: hastResourceStatus.setDescription('Resource replication status.')
hastResourceDirty = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDirty.setStatus('current')
if mibBuilder.loadTexts: hastResourceDirty.setDescription('Current number of dirty extents for the resource.')
hastResourceReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReads.setStatus('current')
if mibBuilder.loadTexts: hastResourceReads.setDescription('Count of resource local read operations.')
hastResourceWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWrites.setStatus('current')
if mibBuilder.loadTexts: hastResourceWrites.setDescription('Count of resource local write operations.')
hastResourceDeletes = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDeletes.setStatus('current')
if mibBuilder.loadTexts: hastResourceDeletes.setDescription('Count of resource local delete operations.')
hastResourceFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceFlushes.setStatus('current')
if mibBuilder.loadTexts: hastResourceFlushes.setDescription('Count of resource local flush operations.')
hastResourceActivemapUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceActivemapUpdates.setStatus('current')
if mibBuilder.loadTexts: hastResourceActivemapUpdates.setDescription('Count of resource local activemap updates.')
hastResourceReadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceReadErrors.setStatus('current')
if mibBuilder.loadTexts: hastResourceReadErrors.setDescription('Count of resource local read operations that failed.')
hastResourceWriteErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWriteErrors.setStatus('current')
if mibBuilder.loadTexts: hastResourceWriteErrors.setDescription('Count of resource local write operations that failed.')
hastResourceDeleteErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDeleteErrors.setStatus('current')
if mibBuilder.loadTexts: hastResourceDeleteErrors.setDescription('Count of resource local delete operations that failed.')
hastResourceFlushErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceFlushErrors.setStatus('current')
if mibBuilder.loadTexts: hastResourceFlushErrors.setDescription('Count of resource local flush operations that failed.')
hastResourceWorkerPid = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceWorkerPid.setStatus('current')
if mibBuilder.loadTexts: hastResourceWorkerPid.setDescription('Worker process ID.')
hastResourceLocalQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceLocalQueue.setStatus('current')
if mibBuilder.loadTexts: hastResourceLocalQueue.setDescription('Number of outstanding I/O requests to the local component.')
hastResourceSendQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceSendQueue.setStatus('current')
if mibBuilder.loadTexts: hastResourceSendQueue.setDescription('Number of outstanding I/O requests to send to the remote\n\tcomponent.')
hastResourceRecvQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceRecvQueue.setStatus('current')
if mibBuilder.loadTexts: hastResourceRecvQueue.setDescription('Number of outstanding I/O requests waiting for response\n\tfrom the remote component.')
hastResourceDoneQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceDoneQueue.setStatus('current')
if mibBuilder.loadTexts: hastResourceDoneQueue.setDescription('Number of processed I/O requests to return to the kernel.')
hastResourceIdleQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hastResourceIdleQueue.setStatus('current')
if mibBuilder.loadTexts: hastResourceIdleQueue.setDescription('Number of request objects in the free bucket.')
mibBuilder.exportSymbols("BEGEMOT-HAST-MIB", hastResourceTable=hastResourceTable, hastResourceRemoteAddr=hastResourceRemoteAddr, hastResourceDeletes=hastResourceDeletes, hastResourceSendQueue=hastResourceSendQueue, hastResourceKeepDirty=hastResourceKeepDirty, hastResourceStatus=hastResourceStatus, hastResourceSourceAddr=hastResourceSourceAddr, hastResourceExtentSize=hastResourceExtentSize, hastResourceReplication=hastResourceReplication, hastConfig=hastConfig, hastResourceDeleteErrors=hastResourceDeleteErrors, hastResourceName=hastResourceName, hastResourceLocalPath=hastResourceLocalPath, hastConfigFile=hastConfigFile, hastResourceFlushErrors=hastResourceFlushErrors, hastResourceWrites=hastResourceWrites, hastResourceDoneQueue=hastResourceDoneQueue, hastResourceWriteErrors=hastResourceWriteErrors, hastResourceDirty=hastResourceDirty, hastResourceActivemapUpdates=hastResourceActivemapUpdates, PYSNMP_MODULE_ID=begemotHast, hastResourceFlushes=hastResourceFlushes, hastResourceProvName=hastResourceProvName, hastResourceIdleQueue=hastResourceIdleQueue, begemotHast=begemotHast, hastResourceReads=hastResourceReads, begemotHastObjects=begemotHastObjects, hastResourceEntry=hastResourceEntry, hastResourceWorkerPid=hastResourceWorkerPid, hastResourceRecvQueue=hastResourceRecvQueue, hastResourceIndex=hastResourceIndex, hastResourceLocalQueue=hastResourceLocalQueue, hastResourceReadErrors=hastResourceReadErrors, hastResourceRole=hastResourceRole)
