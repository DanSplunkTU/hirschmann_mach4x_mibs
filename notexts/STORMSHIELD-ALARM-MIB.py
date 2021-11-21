#
# PySNMP MIB module STORMSHIELD-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ALARM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:29 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, ModuleIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, Unsigned32, iso, Gauge32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ModuleIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "Unsigned32", "iso", "Gauge32", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stormshieldMIB, snsNotifications = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB", "snsNotifications")
snsAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 5))
snsAlarm.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsAlarm.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsAlarm.setOrganization('Stormshield')
snsATable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0), )
if mibBuilder.loadTexts: snsATable.setStatus('current')
snsAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAIndex"))
if mibBuilder.loadTexts: snsAEntry.setStatus('current')
snsAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAIndex.setStatus('current')
snsATime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsATime.setStatus('current')
snsASif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASif.setStatus('current')
snsADif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADif.setStatus('current')
snsAProto = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAProto.setStatus('current')
snsASaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASaddr.setStatus('current')
snsADaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADaddr.setStatus('current')
snsASport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASport.setStatus('current')
snsADport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADport.setStatus('current')
snsASname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASname.setStatus('current')
snsADname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADname.setStatus('current')
snsAMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAMessage.setStatus('current')
snsAicmpTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1), )
if mibBuilder.loadTexts: snsAicmpTable.setStatus('current')
snsAicmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAicmpIndex"))
if mibBuilder.loadTexts: snsAicmpEntry.setStatus('current')
snsAicmpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAicmpIndex.setStatus('current')
snsAicmpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpTime.setStatus('current')
snsAicmpSif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSif.setStatus('current')
snsAicmpDif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDif.setStatus('current')
snsAicmpSaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSaddr.setStatus('current')
snsAicmpDaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDaddr.setStatus('current')
snsAicmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpType.setStatus('current')
snsAicmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpCode.setStatus('current')
snsAicmpSname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSname.setStatus('current')
snsAicmpDname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDname.setStatus('current')
snsAicmpMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpMessage.setStatus('current')
snsNotification = NotificationType((1, 3, 6, 1, 4, 1, 11256, 1, 6, 1)).setObjects(("STORMSHIELD-ALARM-MIB", "snsATime"), ("STORMSHIELD-ALARM-MIB", "snsASif"), ("STORMSHIELD-ALARM-MIB", "snsASaddr"), ("STORMSHIELD-ALARM-MIB", "snsADaddr"), ("STORMSHIELD-ALARM-MIB", "snsAMessage"))
if mibBuilder.loadTexts: snsNotification.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-ALARM-MIB", snsAlarm=snsAlarm, snsAicmpIndex=snsAicmpIndex, snsAicmpDaddr=snsAicmpDaddr, snsAIndex=snsAIndex, snsADport=snsADport, PYSNMP_MODULE_ID=snsAlarm, snsAicmpDname=snsAicmpDname, snsAicmpTime=snsAicmpTime, snsAProto=snsAProto, snsAicmpTable=snsAicmpTable, snsNotification=snsNotification, snsAicmpEntry=snsAicmpEntry, snsADif=snsADif, snsASport=snsASport, snsATime=snsATime, snsAicmpSif=snsAicmpSif, snsAicmpMessage=snsAicmpMessage, snsAicmpSaddr=snsAicmpSaddr, snsAEntry=snsAEntry, snsASif=snsASif, snsASname=snsASname, snsATable=snsATable, snsADname=snsADname, snsAicmpSname=snsAicmpSname, snsADaddr=snsADaddr, snsAMessage=snsAMessage, snsAicmpCode=snsAicmpCode, snsASaddr=snsASaddr, snsAicmpType=snsAicmpType, snsAicmpDif=snsAicmpDif)
