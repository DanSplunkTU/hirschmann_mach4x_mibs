#
# PySNMP MIB module RAPID-CITY-BAY-STACK (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-CITY-BAY-STACK
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
rcBayStack, = mibBuilder.importSymbols("RAPID-CITY", "rcBayStack")
rcMltId, = mibBuilder.importSymbols("RC-MLT-MIB", "rcMltId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, IpAddress, Integer32, Bits, Counter32, MibIdentifier, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "Counter32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rcBayStackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 40, 1))
rcBayStackMIB.setRevisions(('2004-09-29 00:00', '2004-07-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rcBayStackMIB.setRevisionsDescriptions(('Version 6: Fixed IMPORTS, RAPID-CITY-MIB to RAPID-CITY', 'Version 5: Added version info',))
if mibBuilder.loadTexts: rcBayStackMIB.setLastUpdated('200409290000Z')
if mibBuilder.loadTexts: rcBayStackMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: rcBayStackMIB.setContactInfo('\n                                         \n                         Postal:       Nortel Networks \n                                       4401 Great America Parkway \n                                       Santa Clara, CA 95052-8185 \n\n                            Tel: \n                            Fax:  \n                         E-mail:         \n                        ')
if mibBuilder.loadTexts: rcBayStackMIB.setDescription('BayStack specific portion of RAPID-CITY-MIB.')
rcBayStackObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1))
rcBayStackTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21))
rcBayStackTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0))
rcBayStackTftpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1))
rcBayStackTftpAction = MibScalar((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("downloadSshPublicKeys", 2), ("deleteSshDsaAuthKey", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcBayStackTftpAction.setStatus('current')
if mibBuilder.loadTexts: rcBayStackTftpAction.setDescription('This object may be set to initiate a TFTP download of\n                    SSH public keys.  When retrieved, the value will always\n                    be none(1).')
rcBayStackSshSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2), )
if mibBuilder.loadTexts: rcBayStackSshSessionTable.setStatus('current')
if mibBuilder.loadTexts: rcBayStackSshSessionTable.setDescription('Table describing the SSH sessions')
rcBayStackSshSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1), ).setIndexNames((0, "RAPID-CITY-BAY-STACK", "rcBayStackSshSessionId"))
if mibBuilder.loadTexts: rcBayStackSshSessionEntry.setStatus('current')
if mibBuilder.loadTexts: rcBayStackSshSessionEntry.setDescription('An entry describing an SSH session.')
rcBayStackSshSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: rcBayStackSshSessionId.setStatus('current')
if mibBuilder.loadTexts: rcBayStackSshSessionId.setDescription('Session ID')
rcBayStackSshSessionIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcBayStackSshSessionIp.setStatus('current')
if mibBuilder.loadTexts: rcBayStackSshSessionIp.setDescription('IP address of SSH client that opened the session.')
rcBayStackSshExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3))
rcBayStackSshDsaHostKeyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notGenerated", 1), ("generated", 2), ("generating", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcBayStackSshDsaHostKeyStatus.setStatus('current')
if mibBuilder.loadTexts: rcBayStackSshDsaHostKeyStatus.setDescription('This object indicates the current status of the SSH\n                    DSA host key.  If the DSA host key has not yet been\n                    generated, the value will be notGenerated(1).  If it\n                    has already been generated, the value will be\n                    generated(2).  If it is currently being generated,\n                    the value will be generating(3).')
rcMltConfigError = NotificationType((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0, 1)).setObjects(("RC-MLT-MIB", "rcMltId"))
if mibBuilder.loadTexts: rcMltConfigError.setStatus('current')
if mibBuilder.loadTexts: rcMltConfigError.setDescription('An rcMltConfigError trap indicates that one of the\n                       ports in a multi-link trunk was connected to a remote\n                       port that was not also configured as a trunk.  The\n                       trap indicates that the specified trunk has also been\n                       automatically disabled.')
mibBuilder.exportSymbols("RAPID-CITY-BAY-STACK", rcBayStackSshSessionTable=rcBayStackSshSessionTable, rcBayStackMIB=rcBayStackMIB, rcBayStackSshDsaHostKeyStatus=rcBayStackSshDsaHostKeyStatus, rcBayStackObjects=rcBayStackObjects, rcBayStackSshExt=rcBayStackSshExt, rcBayStackSshSessionEntry=rcBayStackSshSessionEntry, rcBayStackSshSessionId=rcBayStackSshSessionId, rcBayStackTftpAction=rcBayStackTftpAction, PYSNMP_MODULE_ID=rcBayStackMIB, rcMltConfigError=rcMltConfigError, rcBayStackTraps=rcBayStackTraps, rcBayStackTftpExt=rcBayStackTftpExt, rcBayStackSshSessionIp=rcBayStackSshSessionIp, rcBayStackTraps0=rcBayStackTraps0)
