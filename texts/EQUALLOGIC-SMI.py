#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:35 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, NotificationType, MibIdentifier, ModuleIdentity, iso, Bits, Gauge32, Counter32, ObjectIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso", "Bits", "Gauge32", "Counter32", "ObjectIdentity", "Integer32", "Unsigned32")
TextualConvention, TruthValue, RowStatus, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "RowPointer", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: equalLogic.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: equalLogic.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762\n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: equalLogic.setDescription('Equallogic Inc. group information\n\n        Copyright (c) 2002-2009 by Dell, Inc. \n        \n        All rights reserved.  This software may not be copied, disclosed, \n        transferred, or used except in accordance with a license granted \n        by Dell, Inc.  This software embodies proprietary information \n        and trade secrets of Dell, Inc. \n        ')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", equalLogic=equalLogic, eqlPSSeries=eqlPSSeries, PYSNMP_MODULE_ID=equalLogic, products=products)
