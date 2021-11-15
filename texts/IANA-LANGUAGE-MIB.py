#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:28 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Gauge32, Unsigned32, mib_2, iso, Integer32, IpAddress, Counter32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Unsigned32", "mib-2", "iso", "Integer32", "IpAddress", "Counter32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaLanguages = ModuleIdentity((1, 3, 6, 1, 2, 1, 73))
ianaLanguages.setRevisions(('2014-05-22 00:00', '2000-05-10 00:00', '1999-09-09 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaLanguages.setRevisionsDescriptions(('Updated contact info.', 'Import mib-2 instead of experimental, so that\n                 this module compiles', 'Initial version as published at time of\n                 publication of RFC 2591.',))
if mibBuilder.loadTexts: ianaLanguages.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaLanguages.setOrganization('IANA')
if mibBuilder.loadTexts: ianaLanguages.setContactInfo('Internet Assigned Numbers Authority (IANA)\n\n         Postal: ICANN\n                 12025 Waterfront Drive, Suite 300\n                 Los Angeles, CA 90094-2536\n\n         Tel:    +1 310-301-5800\n         E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaLanguages.setDescription("The MIB module registers object identifier values for\n         well-known programming and scripting languages. Every\n         language registration MUST describe the format used\n         when transferring scripts written in this language.\n\n         Any additions or changes to the contents of this MIB\n         module require Designated Expert Review as defined in\n         the Guidelines for Writing IANA Considerations Section\n         document. The Designated Expert will be selected by\n         the IESG Area Director of the OPS Area.\n\n         Note, this module does not have to register all possible\n         languages since languages are identified by object\n         identifier values. It is therefore possible to registered\n         languages in private OID trees. The references given below are not\n         normative with regard to the language version. Other\n         references might be better suited to describe some newer\n         versions of this language. The references are only\n         provided as `a pointer into the right direction'.")
ianaLangJavaByteCode = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 1))
if mibBuilder.loadTexts: ianaLangJavaByteCode.setStatus('current')
if mibBuilder.loadTexts: ianaLangJavaByteCode.setDescription('Java byte code to be processed by a Java virtual machine.\n         A script written in Java byte code is transferred by using\n         the Java archive file format (JAR).')
if mibBuilder.loadTexts: ianaLangJavaByteCode.setReference('The Java Virtual Machine Specification.\n         ISBN 0-201-63452-X')
ianaLangTcl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 2))
if mibBuilder.loadTexts: ianaLangTcl.setStatus('current')
if mibBuilder.loadTexts: ianaLangTcl.setDescription('The Tool Command Language (Tcl). A script written in the\n         Tcl language is transferred in Tcl source code format.')
if mibBuilder.loadTexts: ianaLangTcl.setReference('Tcl and the Tk Toolkit.\n         ISBN 0-201-63337-X')
ianaLangPerl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 3))
if mibBuilder.loadTexts: ianaLangPerl.setStatus('current')
if mibBuilder.loadTexts: ianaLangPerl.setDescription('The Perl language. A script written in the Perl language\n         is transferred in Perl source code format.')
if mibBuilder.loadTexts: ianaLangPerl.setReference('Programming Perl.\n         ISBN 1-56592-149-6')
ianaLangScheme = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 4))
if mibBuilder.loadTexts: ianaLangScheme.setStatus('current')
if mibBuilder.loadTexts: ianaLangScheme.setDescription('The Scheme language. A script written in the Scheme\n         language is transferred in Scheme source code format.')
if mibBuilder.loadTexts: ianaLangScheme.setReference('The Revised^4 Report on the Algorithmic Language Scheme.\n         MIT Press')
ianaLangSRSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 5))
if mibBuilder.loadTexts: ianaLangSRSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangSRSL.setDescription('The SNMP Script Language defined by SNMP Research. A\n         script written in the SNMP Script Language is transferred\n         in the SNMP Script Language source code format.')
ianaLangPSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 6))
if mibBuilder.loadTexts: ianaLangPSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangPSL.setDescription('The Patrol Script Language defined by BMC Software. A script\n         written in the Patrol Script Language is transferred in the\n         Patrol Script Language source code format.')
if mibBuilder.loadTexts: ianaLangPSL.setReference('PATROL Script Language Reference Manual, Version 3.0,\n         November 30, 1995. BMC Software, Inc. 2101 City West Blvd.,\n         Houston, Texas 77042.')
ianaLangSMSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 7))
if mibBuilder.loadTexts: ianaLangSMSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangSMSL.setDescription('The Systems Management Scripting Language. A script written\n         in the SMSL language is transferred in the SMSL source code\n         format.')
if mibBuilder.loadTexts: ianaLangSMSL.setReference('ISO/ITU Command Sequencer.\n         ISO 10164-21 or ITU X.753')
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLangTcl=ianaLangTcl, ianaLanguages=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLangSMSL=ianaLangSMSL, ianaLangPSL=ianaLangPSL, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangSRSL=ianaLangSRSL, ianaLangPerl=ianaLangPerl, PYSNMP_MODULE_ID=ianaLanguages)
