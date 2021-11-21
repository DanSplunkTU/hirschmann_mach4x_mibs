#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:27 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, Gauge32, enterprises, Integer32, Counter32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "enterprises", "Integer32", "Counter32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
freeBSD = ModuleIdentity((1, 3, 6, 1, 4, 1, 2238))
freeBSD.setRevisions(('2006-10-31 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: freeBSD.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: freeBSD.setLastUpdated('200610311000Z')
if mibBuilder.loadTexts: freeBSD.setOrganization('The FreeBSD Project.')
if mibBuilder.loadTexts: freeBSD.setContactInfo('phk@FreeBSD.org is contact person for this file.\n\t\t core@FreeBSD.org is the final authority.')
if mibBuilder.loadTexts: freeBSD.setDescription('The Structure of Management Information for the\n\t\tFreeBSD Project enterprise MIB subtree.')
freeBSDsrc = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 1))
if mibBuilder.loadTexts: freeBSDsrc.setStatus('current')
if mibBuilder.loadTexts: freeBSDsrc.setDescription('Subtree for things which lives in the src tree.')
freeBSDports = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 2))
if mibBuilder.loadTexts: freeBSDports.setStatus('current')
if mibBuilder.loadTexts: freeBSDports.setDescription('Subtree for things which lives in the ports tree.')
freeBSDpeople = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3))
if mibBuilder.loadTexts: freeBSDpeople.setStatus('current')
if mibBuilder.loadTexts: freeBSDpeople.setDescription('Subtree for FreeBSD people.\n\t\t Under this branch any FreeBSD committer may claim\n\t\t a subtree.  Grab the next sequential oid in the list.\n\t\t These assignments are not revoked when committers leave\n\t\t the FreeBSD project.\n\t\t')
freeBSDpeoplePhk = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3, 1))
if mibBuilder.loadTexts: freeBSDpeoplePhk.setStatus('current')
if mibBuilder.loadTexts: freeBSDpeoplePhk.setDescription('Subtree for phk@FreeBSD.org')
freeBSDVersion = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 4))
if mibBuilder.loadTexts: freeBSDVersion.setStatus('current')
if mibBuilder.loadTexts: freeBSDVersion.setDescription('Subtree to register FreeBSD versions. The OID for a FreeBSD\n\t\t version is formed by appending the dot delimited numbers\n\t\t from the release number to this base OID. Examples:\n\n\t\t  5.2.1-STABLE:\tfreeBSDVersion.5.2.1\n\t\t  6.1-STABLE:\tfreeBSDVersion.6.1\n\t\t  7.0-CURRENT:\tfreeBSDVersion.7.0\n\n\t\t There is no indication whether this is STABLE or CURRENT.\n\n\t\t The sysObjectId is automatically set to the value indicated\n\t\t by the uname(3) release field by bsnmpd(1). This initial\n\t\t value can be overwritten in the configuration file.')
mibBuilder.exportSymbols("FREEBSD-MIB", PYSNMP_MODULE_ID=freeBSD, freeBSD=freeBSD, freeBSDsrc=freeBSDsrc, freeBSDVersion=freeBSDVersion, freeBSDports=freeBSDports, freeBSDpeople=freeBSDpeople, freeBSDpeoplePhk=freeBSDpeoplePhk)
