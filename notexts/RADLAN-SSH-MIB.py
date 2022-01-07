#
# PySNMP MIB module RADLAN-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SSH-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:24:45 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, MibIdentifier, Bits, IpAddress, Counter32, TimeTicks, Unsigned32, Gauge32, ModuleIdentity, ObjectIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "MibIdentifier", "Bits", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 78))
rlSsh.setRevisions(('2003-01-03 00:24', '2003-09-21 00:24',))
if mibBuilder.loadTexts: rlSsh.setLastUpdated('200209300024Z')
if mibBuilder.loadTexts: rlSsh.setOrganization('Radlan Computer Communication Ltd.')
class RlSshPublicKeyAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 999))
    namedValues = NamedValues(("rsa1", 0), ("rsa", 1), ("dsa", 2), ("none", 999))

class RlSshPublicKeyDigestFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("hex", 0), ("bubbleBabble", 1))

rlSshMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshMibVersion.setStatus('current')
rlSshServer = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 78, 2))
rlSshServerHostPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 1), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTable.setStatus('current')
rlSshServerHostPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTableEntry.setStatus('current')
rlSshServerHostPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyAlgorithm.setStatus('current')
rlSshServerHostPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentId.setStatus('current')
rlSshServerHostPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentText.setStatus('current')
rlSshServerHostPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 2), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTable.setStatus('current')
rlSshServerHostPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFingerprintAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTableEntry.setStatus('current')
rlSshServerHostPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshServerHostPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshServerHostPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprint.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 3), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTable.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserName"), (0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTableEntry.setStatus('current')
rlSshServerAuthorizedUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserName.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentId.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentText.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentStatus.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 5), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTable.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserFingerprintName"), (0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setStatus('current')
rlSshServerAuthorizedUserFingerprintName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserFingerprintName.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 3), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprint.setStatus('current')
rlSshServerSessionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 6), )
if mibBuilder.loadTexts: rlSshServerSessionTable.setStatus('current')
rlSshServerSessionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerSessionIdentifier"))
if mibBuilder.loadTexts: rlSshServerSessionTableEntry.setStatus('current')
rlSshServerSessionIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionIdentifier.setStatus('current')
rlSshServerSessionPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerAddress.setStatus('current')
rlSshServerSessionPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerPort.setStatus('current')
rlSshServerSessionPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerVersion.setStatus('current')
rlSshServerSessionUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionUsername.setStatus('current')
rlSshServerSessionCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionCipher.setStatus('current')
rlSshServerSessionHMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionHMAC.setStatus('current')
rlSshServerPort = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 101), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerPort.setStatus('current')
rlSshServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 102), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnable.setStatus('current')
rlSshServerEnablePublicKeyAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnablePublicKeyAuthentication.setStatus('current')
rlSshServerRegenerateHostKey = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 104), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerRegenerateHostKey.setStatus('current')
rlSshClient = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 78, 3))
rlSshClientUserName = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 3, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientUserName.setStatus('current')
rlSshClientRegenerateSelfKey = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 3, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientRegenerateSelfKey.setStatus('current')
rlSshClientSelfPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 3, 3), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTable.setStatus('current')
rlSshClientSelfPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTableEntry.setStatus('current')
rlSshClientSelfPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentId.setStatus('current')
rlSshClientSelfPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyAlgorithm.setStatus('current')
rlSshClientSelfPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentText.setStatus('current')
rlSshClientSelfPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 3, 4), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTable.setStatus('current')
rlSshClientSelfPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTableEntry.setStatus('current')
rlSshClientSelfPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshClientSelfPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshClientSelfPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprint.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SSH-MIB", rlSshServerSessionIdentifier=rlSshServerSessionIdentifier, rlSshClient=rlSshClient, rlSshServerAuthorizedUsersPublicKeyTable=rlSshServerAuthorizedUsersPublicKeyTable, rlSshServerSessionTableEntry=rlSshServerSessionTableEntry, rlSshServerAuthorizedUserFingerprintName=rlSshServerAuthorizedUserFingerprintName, rlSshClientSelfPublicKeyFingerprintTableEntry=rlSshClientSelfPublicKeyFingerprintTableEntry, rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm=rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm, rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry=rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry, rlSshServerHostPublicKeyFingerprintTable=rlSshServerHostPublicKeyFingerprintTable, rlSshServerHostPublicKeyTableEntry=rlSshServerHostPublicKeyTableEntry, rlSshServerAuthorizedUsersPublicKeyFingerprintTable=rlSshServerAuthorizedUsersPublicKeyFingerprintTable, RlSshPublicKeyAlgorithm=RlSshPublicKeyAlgorithm, rlSshServerHostPublicKeyFragmentText=rlSshServerHostPublicKeyFragmentText, rlSshServerHostPublicKeyFingerprint=rlSshServerHostPublicKeyFingerprint, rlSshServerSessionHMAC=rlSshServerSessionHMAC, PYSNMP_MODULE_ID=rlSsh, rlSshServerHostPublicKeyFingerprintTableEntry=rlSshServerHostPublicKeyFingerprintTableEntry, rlSshServerAuthorizedUsersPublicKeyTableEntry=rlSshServerAuthorizedUsersPublicKeyTableEntry, rlSshServerAuthorizedUserName=rlSshServerAuthorizedUserName, rlSshServerAuthorizedUserPublicKeyFragmentStatus=rlSshServerAuthorizedUserPublicKeyFragmentStatus, rlSshServerSessionUsername=rlSshServerSessionUsername, rlSshServerSessionCipher=rlSshServerSessionCipher, rlSshClientSelfPublicKeyFragmentId=rlSshClientSelfPublicKeyFragmentId, rlSshServerHostPublicKeyAlgorithm=rlSshServerHostPublicKeyAlgorithm, rlSshServerEnable=rlSshServerEnable, rlSshClientSelfPublicKeyTable=rlSshClientSelfPublicKeyTable, rlSshClientSelfPublicKeyFingerprintAlgorithm=rlSshClientSelfPublicKeyFingerprintAlgorithm, rlSshServerSessionTable=rlSshServerSessionTable, rlSshClientUserName=rlSshClientUserName, rlSshServerAuthorizedUserPublicKeyFragmentText=rlSshServerAuthorizedUserPublicKeyFragmentText, rlSshServer=rlSshServer, rlSshClientSelfPublicKeyTableEntry=rlSshClientSelfPublicKeyTableEntry, rlSshClientSelfPublicKeyFingerprint=rlSshClientSelfPublicKeyFingerprint, rlSshServerSessionPeerPort=rlSshServerSessionPeerPort, rlSshServerAuthorizedUserPublicKeyFingerprint=rlSshServerAuthorizedUserPublicKeyFingerprint, rlSshServerEnablePublicKeyAuthentication=rlSshServerEnablePublicKeyAuthentication, rlSshClientSelfPublicKeyAlgorithm=rlSshClientSelfPublicKeyAlgorithm, rlSshMibVersion=rlSshMibVersion, rlSshServerHostPublicKeyFingerprintAlgorithm=rlSshServerHostPublicKeyFingerprintAlgorithm, rlSshServerAuthorizedUserPublicKeyFragmentId=rlSshServerAuthorizedUserPublicKeyFragmentId, rlSshServerRegenerateHostKey=rlSshServerRegenerateHostKey, RlSshPublicKeyDigestFormat=RlSshPublicKeyDigestFormat, rlSsh=rlSsh, rlSshClientRegenerateSelfKey=rlSshClientRegenerateSelfKey, rlSshServerSessionPeerAddress=rlSshServerSessionPeerAddress, rlSshClientSelfPublicKeyFingerprintTable=rlSshClientSelfPublicKeyFingerprintTable, rlSshClientSelfPublicKeyFingerprintDigestFormat=rlSshClientSelfPublicKeyFingerprintDigestFormat, rlSshServerSessionPeerVersion=rlSshServerSessionPeerVersion, rlSshClientSelfPublicKeyFragmentText=rlSshClientSelfPublicKeyFragmentText, rlSshServerHostPublicKeyFragmentId=rlSshServerHostPublicKeyFragmentId, rlSshServerHostPublicKeyTable=rlSshServerHostPublicKeyTable, rlSshServerPort=rlSshServerPort, rlSshServerHostPublicKeyFingerprintDigestFormat=rlSshServerHostPublicKeyFingerprintDigestFormat, rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat=rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat)
