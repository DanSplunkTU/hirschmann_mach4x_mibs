#
# PySNMP MIB module ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ATM-DXI-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Unsigned32, TimeTicks, enterprises, Counter32, NotificationType, ModuleIdentity, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "TimeTicks", "enterprises", "Counter32", "NotificationType", "ModuleIdentity", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmUniDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3))
class Dfa(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

atmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3, 2))
atmDxiConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 2), )
if mibBuilder.loadTexts: atmDxiConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfTable.setDescription('This table contains\n\tATM DXI configuration information\n\tincluding information on the mode supported\n\tacross the DXI.')
atmDxiConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiConfIfIndex"))
if mibBuilder.loadTexts: atmDxiConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfEntry.setDescription('This list contains ATM DXI configuration information.')
atmDxiConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI\n\tinterface for which this entry contains management information.\n\tThis is the same value as used to identify the IfEntry describing\n\tthe DCE interface.  Management uses and expects this value.  In\n\tthe proxy mode of operation, the DCE always treats this as 0, but\n\tpreserves it in its response to the DTE.  0, the DXI value, means\n\tthe interface over which the DXI LMI request was received.')
atmDxiConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiConfMode.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfMode.setDescription('This object identifies the dxi mode being\n\tused at the atm dxi port.')
atmDxiDFAConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 3), )
if mibBuilder.loadTexts: atmDxiDFAConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfTable.setDescription('This table contains configuration information about\n\ta particular DFA.')
atmDxiDFAConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"), (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"))
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setDescription('This list contains ATM DXI DFA configuration\n\tinformation.')
atmDxiDFAConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI\n\tinterface for which this entry contains management information.\n\tThis is the same value as used to identify the IfEntry describing\n\tthe DCE interface.  Management uses and expects this value.  In\n\tthe proxy mode of operation, the DCE always treats this as 0, but\n\tpreserves it in its response to the DTE.  0, the DXI value, means\n\tthe interface over which the DXI LMI request was received.')
atmDxiDFAConfDfaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2), Dfa()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setDescription('This object identifies the DFA instance on the DXI\n\tidentified by atmDxiDFAConfIfIndex.')
atmDxiDFAConfAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("aal34", 3), ("aal5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setDescription('This object identifies the AAL type supported at this DFA.\n\tNote, if mode 2 is supported on the DXI identified by the\n\tcorresponding instance of atmDxiDFAConfIfIndex and that\n\tinstance of atmDxiDFAConfIfIndex identifies the DCE side\n\tof the DXI, then this object contains the AAL Type being\n\trun on the corresponding VPI/VCI on the corresponding ATM UNI\n\tinterface.')
atmDxiEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 353, 3, 2, 4), ObjectIdentifier())
if mibBuilder.loadTexts: atmDxiEnterprise.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiEnterprise.setDescription("This object is included as the first ID-Value pair\n\tin a Trap PDU for which the Generic Trap Type field\n\thas the value 'enterpriseSpecific'.  The value of the\n\tobject identifies the enterprise under whose authority\n\tthe value of the Enterprise Trap Type field is defined.")
mibBuilder.exportSymbols("ATM-DXI-MIB", atmDxiDFAConfTable=atmDxiDFAConfTable, atmDxiConfMode=atmDxiConfMode, atmDxiConfIfIndex=atmDxiConfIfIndex, atmForum=atmForum, Dfa=Dfa, atmDxiConfEntry=atmDxiConfEntry, atmDxiDFAConfEntry=atmDxiDFAConfEntry, atmDxiDFAConfAALType=atmDxiDFAConfAALType, atmDxi=atmDxi, atmUniDxi=atmUniDxi, atmDxiConfTable=atmDxiConfTable, atmDxiDFAConfIfIndex=atmDxiDFAConfIfIndex, atmDxiDFAConfDfaIndex=atmDxiDFAConfDfaIndex, atmDxiEnterprise=atmDxiEnterprise)
