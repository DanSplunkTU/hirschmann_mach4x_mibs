#
# PySNMP MIB module AT-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-NTP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:44:42 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Integer32, Counter64, Counter32, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "ObjectIdentity", "IpAddress")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
atNtp = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502))
atNtp.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2008-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atNtp.setRevisionsDescriptions(('Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Initial revision. ',))
if mibBuilder.loadTexts: atNtp.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: atNtp.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atNtp.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atNtp.setDescription('This MIB file contains definitions of managed objects\n                for the Allied Telesis Network Time Protocol configuration. ')
atNtpPeerIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpPeerIndexNext.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerIndexNext.setDescription("This object represents the next available value for\n                the object 'atNtpPeerIndex'.\n\n                For creation of a new entry in the 'atNtpPeerTable',\n                a management application should read this object,\n                get the value and use the same.")
atNtpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7), )
if mibBuilder.loadTexts: atNtpPeerTable.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerTable.setDescription("This table contains information on the Network Time\n                Protocol (NTP) peers' configurations in the system.")
atNtpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1), ).setIndexNames((0, "AT-NTP-MIB", "atNtpPeerIndex"))
if mibBuilder.loadTexts: atNtpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerEntry.setDescription('A conceptual entry in atNtpPeerTable.')
atNtpPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atNtpPeerIndex.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerIndex.setDescription("This object represents the index corresponding to\n                a particular NTP server or peer configuration in\n                the system.\n\n                For creation of a new entry, the value of this object\n                should be same as that of the value of\n                'atNtpPeerIndexNext' object. If this is not\n                the case, then the entry creation will fail.")
atNtpPeerNameAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 2), DisplayString().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerNameAddr.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerNameAddr.setDescription("This object represents host name, or the IP address,\n                of the NTP peer.\n\n                This object is a current object for row creation.\n\n                When a new row is created, this object is set with\n                a default value '0.0.0.0', and the management\n                application should change it to a desired value by\n                a SET operation.")
atNtpPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("server", 1), ("peer", 2))).clone('peer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerMode.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerMode.setDescription("This object represents the mode of the peer.\n                It's value is coded as follows:\n                server(1),\n                peer(2)")
atNtpPeerPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerPreference.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerPreference.setDescription("This object specifies whether this peer is the\n                preferred one over the others.\n\n                It's value is encoded as follows:\n                0 - unknown\n                1 - not preferred\n                2 - preferred\n\n                When the value of this object is 'not preferred',\n                NTP chooses the peer with which to synchronize the\n                time on the local system. If this object is set to\n                'preferred', NTP will choose the corresponding peer to\n                synchronize the time with.\n                ")
atNtpPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerVersion.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerVersion.setDescription("This object represents the NTP version the peer\n                supports. It's value is encoded as follows:\n                0 - unknown\n                1 - version 1\n                2 - version 2\n                3 - version 3\n                4 - version 4\n                ")
atNtpPeerKeyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerKeyNumber.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerKeyNumber.setDescription('This object represents the authentication key number.')
atNtpPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 7), RowStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atNtpPeerRowStatus.setStatus('current')
if mibBuilder.loadTexts: atNtpPeerRowStatus.setDescription("The status of this row.\n\n                The reading of this object should have a value of\n                'active(1)'.\n\n                For creation of new entry, a management application\n                should set this object with value 'createAndGo(4)',\n                and using the same value as that got from reading\n                object 'atNtpPeerIndexNext', as the index for\n                the new entry.\n\n                When an entry is created, the object 'atNtpPeerNameAddr'\n                in the entry is set with a default value '0.0.0.0'.\n                The management application should change it to\n                a desired value with a SET operation.\n\n                The management application may need to take\n                additional SET operations to set values for other\n                objects, to ensure they have desired values.\n\n                For deletion of entry, a management application\n                should set this object with value 'destroy(6)'.\n\n                Once an entry is deleted, other entries in the table\n                which have bigger index than the deleted one, will\n                be indexed again. Therefore a management\n                application can effectively delete multiple entries\n                by repeating the SET operation using the same index.")
atNtpAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10), )
if mibBuilder.loadTexts: atNtpAssociationTable.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationTable.setDescription('This table contains NTP association information.')
atNtpAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1), ).setIndexNames((0, "AT-NTP-MIB", "atNtpAssociationIndex"))
if mibBuilder.loadTexts: atNtpAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationEntry.setDescription('An conceptual entry in atNtpAssociationTable.')
atNtpAssociationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: atNtpAssociationIndex.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationIndex.setDescription('This object represents the index corresponding to\n                a particular NTP association.')
atNtpAssociationPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationPeerAddr.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationPeerAddr.setDescription("This object represents the peer's IP address or host\n                name.")
atNtpAssocaitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssocaitionStatus.setStatus('current')
if mibBuilder.loadTexts: atNtpAssocaitionStatus.setDescription("This object indicates the association's status.\n                It's value is defined as follows:\n                master(synced),\n                master(unsynced),\n                selected,\n                candidate,\n                configured,\n                unknown.\n                ")
atNtpAssociationConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationConfigured.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationConfigured.setDescription("This object indicates whether the association\n                is from configuration or not. It's value can be\n                either 'configured' or 'dynamic'.\n                ")
atNtpAssociationRefClkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationRefClkAddr.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationRefClkAddr.setDescription('This object indicates the IP address for the\n                reference clock.')
atNtpAssociationStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationStratum.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationStratum.setDescription('This object indicates the stratum of the peer clock.')
atNtpAssociationPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 7), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationPoll.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationPoll.setDescription('This object indicates the time between NTP requests\n                from the device to the server.')
atNtpAssociationReach = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationReach.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationReach.setDescription('This object indicates the reachability status of\n                the peer.')
atNtpAssociationDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationDelay.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationDelay.setDescription('This object indicates the round trip delay between\n                the device and the server.')
atNtpAssociationOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationOffset.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationOffset.setDescription('This object indicates the difference between\n                the device clock and the server clock.')
atNtpAssociationDisp = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationDisp.setStatus('current')
if mibBuilder.loadTexts: atNtpAssociationDisp.setDescription('This object indicates the lowest measure of\n                error associated with peer offset based on delay,\n                in seconds.')
atNtpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11))
atNtpSysClockSync = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysClockSync.setStatus('current')
if mibBuilder.loadTexts: atNtpSysClockSync.setDescription('This object indicates whether the system clock\n                is synchronized.')
atNtpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysStratum.setStatus('current')
if mibBuilder.loadTexts: atNtpSysStratum.setDescription('This object represents the stratum of the local clock.')
atNtpSysReference = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysReference.setStatus('current')
if mibBuilder.loadTexts: atNtpSysReference.setDescription('This object represents the current synchronization\n                source.')
atNtpSysFrequency = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 4), Integer32()).setUnits('Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysFrequency.setStatus('current')
if mibBuilder.loadTexts: atNtpSysFrequency.setDescription('This object represents the actual clock frequency.\n                source.')
atNtpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysPrecision.setStatus('current')
if mibBuilder.loadTexts: atNtpSysPrecision.setDescription('Signed integer indicating the precision of the system clock,\n                in seconds to the nearest power of two. The value is rounded\n                to the next larger power of two; for instance, a 50-Hz(20 ms)\n                or 60-Hz (16.67 ms) power-frequency clock would be assigned\n                the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled\n                clock would be assigned the value -9 (1.95 ms).')
atNtpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRefTime.setStatus('current')
if mibBuilder.loadTexts: atNtpSysRefTime.setDescription('This object indicates the local time when the\n                local clock was last updated. If the local clock\n                has never been synchronized, the value is zero')
atNtpSysClkOffset = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 7), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysClkOffset.setStatus('current')
if mibBuilder.loadTexts: atNtpSysClkOffset.setDescription('This object indicates the offset of the local clock\n                relative to the server clock, in milliseconds.')
atNtpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 8), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRootDelay.setStatus('current')
if mibBuilder.loadTexts: atNtpSysRootDelay.setDescription('This object indicats the total round-trip delay\n                in milliseconds, to the primary reference source\n                at the root of the synchronization subnet.')
atNtpSysRootDisp = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 9), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRootDisp.setStatus('current')
if mibBuilder.loadTexts: atNtpSysRootDisp.setDescription('This object indicates the maximum error in\n                milliseconds, relative to the primary reference\n                source at the root of the synchronization\n                subnet.')
mibBuilder.exportSymbols("AT-NTP-MIB", atNtpSysClkOffset=atNtpSysClkOffset, atNtpAssociationPoll=atNtpAssociationPoll, atNtpAssociationPeerAddr=atNtpAssociationPeerAddr, atNtpStatus=atNtpStatus, atNtpAssociationEntry=atNtpAssociationEntry, atNtpPeerNameAddr=atNtpPeerNameAddr, atNtpAssociationConfigured=atNtpAssociationConfigured, atNtpAssociationDisp=atNtpAssociationDisp, atNtpPeerKeyNumber=atNtpPeerKeyNumber, atNtp=atNtp, atNtpSysRootDisp=atNtpSysRootDisp, atNtpPeerIndex=atNtpPeerIndex, atNtpPeerTable=atNtpPeerTable, atNtpPeerRowStatus=atNtpPeerRowStatus, atNtpPeerIndexNext=atNtpPeerIndexNext, atNtpAssociationOffset=atNtpAssociationOffset, atNtpSysFrequency=atNtpSysFrequency, atNtpSysReference=atNtpSysReference, atNtpAssociationDelay=atNtpAssociationDelay, PYSNMP_MODULE_ID=atNtp, atNtpAssociationIndex=atNtpAssociationIndex, atNtpSysRefTime=atNtpSysRefTime, atNtpAssociationReach=atNtpAssociationReach, atNtpPeerPreference=atNtpPeerPreference, atNtpSysPrecision=atNtpSysPrecision, atNtpSysRootDelay=atNtpSysRootDelay, atNtpAssociationTable=atNtpAssociationTable, atNtpSysStratum=atNtpSysStratum, atNtpSysClockSync=atNtpSysClockSync, atNtpPeerVersion=atNtpPeerVersion, atNtpAssociationStratum=atNtpAssociationStratum, atNtpAssocaitionStatus=atNtpAssocaitionStatus, atNtpPeerEntry=atNtpPeerEntry, atNtpAssociationRefClkAddr=atNtpAssociationRefClkAddr, atNtpPeerMode=atNtpPeerMode)
