#
# PySNMP MIB module T11-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, Gauge32, Bits, Unsigned32, Counter32, NotificationType, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "Bits", "Unsigned32", "Counter32", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
t11TcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 136))
t11TcMIB.setRevisions(('2006-03-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11TcMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 4439.',))
if mibBuilder.loadTexts: t11TcMIB.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: t11TcMIB.setOrganization('T11')
if mibBuilder.loadTexts: t11TcMIB.setContactInfo('     Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  Phone: +1 408 853-9172\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA USA 95134\n                  Phone: +1 408-526-5260\n                  EMail: kzm@cisco.com')
if mibBuilder.loadTexts: t11TcMIB.setDescription('This module defines textual conventions used in T11 MIBs.\n\n           Copyright (C) The Internet Society (2006).  This version\n           of this MIB module is part of RFC 4439;  see the RFC\n           itself for full legal notices.')
class T11FabricIndex(TextualConvention, Unsigned32):
    reference = 'Fibre Channel - Switch Fabric - 4 (FC-SW-4),\n                 ANSI INCITS 418-2006, section 6.1.27.2.4.'
    description = "A Fabric Index that is used as a unique\n           index value to identify a particular Fabric within\n           one (or more) physical infrastructures.\n\n           In an environment that is conformant to FC-SW-3, where\n\n\n\n           there is always exactly one Fabric in a single physical\n           infrastructure, the value of this Fabric Index will\n           always be 1.\n\n           However, the current standard, FC-SW-4, defines\n           how multiple Fabrics, each with its own management\n           instrumentation, could operate within one (or more)\n           physical infrastructures.  When such multiple Fabrics\n           are in use, this index value is used to uniquely\n           identify a particular Fabric within a physical\n           infrastructure.\n\n           Note that the value of this textual convention has a\n           range of (0..4095) so as to be consistent with FC-SW-4,\n           which says that a 'VF_ID Bitmap' is 512 bytes long, with\n           the high-order bit representing VF_ID zero, and the\n           low-order bit representing 4095."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

mibBuilder.exportSymbols("T11-TC-MIB", T11FabricIndex=T11FabricIndex, t11TcMIB=t11TcMIB, PYSNMP_MODULE_ID=t11TcMIB)
